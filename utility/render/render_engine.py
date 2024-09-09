import time
import os
import tempfile
import zipfile
import platform
import subprocess
from moviepy.editor import (AudioFileClip, ColorClip, CompositeVideoClip, CompositeAudioClip, ImageClip,
                            TextClip, VideoFileClip)
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
import requests


generateFolder = ''
def read_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('generate_folder='):
                    return line.split('=', 1)[1].strip()
    except FileNotFoundError:
        print(f"Properties file not found: {file_path}")
    except Exception as e:
        print(f"Error reading properties file: {e}")
    return None

generateFolder = read_api_key('/etc/properties/videogen.properties')

def download_file(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)

def search_program(program_name):
    try: 
        search_cmd = "where" if platform.system() == "Windows" else "which"
        return subprocess.check_output([search_cmd, program_name]).decode().strip()
    except subprocess.CalledProcessError:
        return None

def get_program_path(program_name):
    program_path = search_program(program_name)
    return program_path

def split_text(text, max_length=20):
    """Split text into two lines without cutting words."""
    # If text is short enough, no need to split
    if len(text) <= max_length:
        return text, ''
    
    # Find the last space before the max_length
    split_index = text.rfind(' ', 0, max_length)
    
    # If no space is found, split at the max_length
    if split_index == -1:
        split_index = max_length
    
    # Check if the split point is at the start or end of the text
    if split_index == 0:
        split_index = text.find(' ', max_length)
        if split_index == -1:
            split_index = len(text)
    
    # Ensure that we don't split at the very end of the text
    line1 = text[:split_index].strip()
    line2 = text[split_index:].strip()
    
    return line1, line2



def get_output_media(audio_file_path, timed_captions, background_video_data, video_server, job_id):
    OUTPUT_FILE_NAME = generateFolder + "/rendered_video"+ str(job_id) +".mp4"
    magick_path = get_program_path("magick")
    print(magick_path)
    if magick_path:
        os.environ['IMAGEMAGICK_BINARY'] = magick_path
    else:
        os.environ['IMAGEMAGICK_BINARY'] = '/usr/bin/convert'
    
    visual_clips = []
    for (t1, t2), video_url in background_video_data:
        # Download the video file
        video_filename = tempfile.NamedTemporaryFile(delete=False).name
        download_file(video_url, video_filename)
        
        # Create VideoFileClip from the downloaded file
        video_clip = VideoFileClip(video_filename)
        video_clip = video_clip.set_start(t1)
        video_clip = video_clip.set_end(t2)
        visual_clips.append(video_clip)
    
    audio_clips = []
    audio_file_clip = AudioFileClip(audio_file_path)
    audio_clips.append(audio_file_clip)

    for (t1, t2), text in timed_captions:
        line1, line2 = split_text(text)
        splitText = f"{line1}\n{line2}"
        text_clip = TextClip(txt=splitText, fontsize=100, color="white", stroke_width=4, stroke_color="black", method="label")
        text_clip = text_clip.set_start(t1)
        text_clip = text_clip.set_end(t2)
        text_clip = text_clip.set_position(["center", 800])

        background_clip = ColorClip(size=(text_clip.w + 20, text_clip.h + 20), color=(0, 0, 0))
        background_clip = background_clip.set_opacity(0.5)
        background_clip = background_clip.set_start(t1).set_end(t2).set_position(["center", 800])

        # combined_clip = CompositeVideoClip([background_clip, text_clip])
        visual_clips.append(text_clip)

    video = CompositeVideoClip(visual_clips)
    
    if audio_clips:
        audio = CompositeAudioClip(audio_clips)
        video.duration = audio.duration
        video.audio = audio

    video.write_videofile(OUTPUT_FILE_NAME, codec='libx264', audio_codec='aac', fps=25, preset='veryfast')
    
    # Clean up downloaded files
    for (t1, t2), video_url in background_video_data:
        video_filename = tempfile.NamedTemporaryFile(delete=False).name
        os.remove(video_filename)

    return OUTPUT_FILE_NAME
