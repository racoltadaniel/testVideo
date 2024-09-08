from openai import OpenAI
import os
import edge_tts
import json
import asyncio
import whisper_timestamped as whisper
from utility.script.script_generator import generate_script
from utility.audio.audio_generator import generate_audio
from utility.captions.timed_captions_generator import generate_timed_captions
from utility.video.background_video_generator import generate_video_url
from utility.render.render_engine import get_output_media
from utility.video.video_search_query_generator import getVideoSearchQueriesTimed, merge_empty_intervals
import argparse

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Generate a video from a topic.")
    # parser.add_argument("topic", type=str, help="The topic for the video")

    # args = parser.parse_args()
    # SAMPLE_TOPIC = args.topic
    SAMPLE_FILE_NAME = "audio_tts.wav"
    VIDEO_SERVER = "pexel"

    # response = generate_script(SAMPLE_TOPIC)
    response = '{"script":"I (36M) met my now ex (34F) a little over 2 years ago. During that time, the idea of her getting a boob job has come up a few times. She\'d asked me I ever dated anyone with them and what I thought of them. I told her I had, I am not a fan at all and they are a deal breaker for me. About this time last year, she asked me what I thought of her getting a boob job. She was feeling a bit self consciencous and wanted something bigger.I told her she can do what she wants with her body. I am not going to tell her no, because its not my place. If getting the boob job would help her self confidence and self image then its something she might want to consider. Just that choices have consquences and if she did get the boob job I would leave. She laughed and thought I was kidding. The idea came up a few more times and the answer was the same each time.At the end of July, her sister came for a visit her and was going to stay for awhile. This isn\'t unusual, especially when I have a longish work trip coming up. A week later, I left for a work trip that last about 2.5 weeks.I get home and the next day, her and her sister come over to my place. It was obvious what she did while I was gone as she was at least 2 cup sizes bigger. We hang out for a bit then I tell them I am tired and it was a long trip. She tells me she\'ll come over tomorrow to check in on me after they go out to lunch and do a bit of shopping.After thinking about it for the evening, I decided it was a deal breaker for me. I went over to her place with a box of her stuff, grabbed my stuff and left my copy of her keys on the table. As I was leaving, they rolled him. We went inside and I told her I was leaving. That the surgery was a deal breaker for me and its not something I can come to live with. It turned into a big argument and I wished her all the best and left after about 15 min.For the last week, she\'s blowing up my phone switching between "Baby I miss you" and "You fucking loser". Her sister has been calling me everything under the sun exept my name.Am I sad I left? Yeah, I did like her a lot. But fake boobs are a serious turn off for me and I don\'t think I would have been happy, nor do I think its something I could have come to like. I hope she is happy and they help with her self esteem, but I couldn\'t be a part of that."}'
    print("script: {}".format(response))

    asyncio.run(generate_audio(response, SAMPLE_FILE_NAME))

    timed_captions = generate_timed_captions(SAMPLE_FILE_NAME)
    print("\n1. Timed captions:",  timed_captions)

    # search_terms = getVideoSearchQueriesTimed(response, timed_captions)
    search_terms = [[[0, 2.82], ['meeting ex', 'relationship start', 'two years']], [[2.82, 5.24], ['ex-girlfriend', 'couple years', 'time together']], [[5.24, 7.54], ['boob job', 'surgery discussion', 'breast enhancement']], [[7.54, 9.24], ['previous partners', 'dating history', 'opinion on surgery']], [[9.24, 11.84], ['personal preference', 'dislikes surgery', 'deal breaker']], [[11.84, 13.62], ['body autonomy', 'personal choice', 'health decisions']], [[13.62, 14.58], ['self-confidence', 'body image', 'consider options']], [[14.58, 17.34], ['choices matters', 'consequences', 'surgery impact']], [[17.34, 18.76], ['final decision', 'leaving relationship', 'seriousness']], [[18.76, 20.8], ['request opinion', 'discussion', 'last year']], [[20.8, 22.34], ['self-conscious', 'personal growth', 'surgery thoughts']], [[22.34, 23.68], ['self-esteem', 'surgery reaction', 'personal feelings']], [[23.68, 26.26], ['sister visit', 'family interaction', 'supportive family']], [[26.26, 27.62], ['shopping together', 'casual outing', 'family time']], [[27.62, 29.14], ['back from work', 'homecoming', 'reunion']], [[29.14, 31.34], ['surgery results', 'appearance change', 'cup sizes']], [[31.34, 32.9], ['initial reactions', 'surprise visit', 'reconnect']], [[32.9, 35.26], ['long work trip', 'exhaustion', 'quick visit']], [[35.26, 37.18], ['disagreement', 'serious talk', 'relationship conflict']], [[37.18, 38.5], ['surgery argument', 'left conflict', 'communication issues']], [[38.5, 39.54], ['separation', 'packing up', 'moving out']], [[39.54, 41.96], ['end of relationship', 'final conversation', 'bitterness']], [[41.96, 43.44], ["ex-girlfriend's reaction", 'phone calls', 'communication breakdown']], [[43.44, 44.6], ['emotional turmoil', 'messages exchanged', 'conflicting feelings']], [[44.6, 47.16], ['dealing with emotions', 'closure', 'sadness']], [[47.16, 49.6], ['regret after breakup', 'self-reflection', 'thoughts']], [[49.6, 50.94], ['fake boobs', 'personal turn off', 'relationship discontent']], [[50.94, 52.98], ["ex's response", 'family opinions', 'names exchanged']], [[52.98, 54.7], ['last week conversations', 'emotional responses', 'ongoing conflict']], [[54.7, 56.06], ['personal feelings', 'speak up', 'last messages']], [[56.06, 59.14], ['self-esteem', 'personal happiness', 'trying to cope']], [[59.14, 60.56], ['final decision', 'moving on', 'new chapter']], [[60.56, 63.18], ['long trip', 'work obligations', 'personal time']], [[63.18, 65.12], ['return home', 'emptiness', 'reflection']], [[65.12, 66.81], ['packing boxes', 'leaving behind', 'confrontation']], [[66.81, 68.52], ['surprise visit', 'embracing change', 'new experience']], [[68.52, 70.92], ['breast surgery', 'unexpected results', 'appearance change']], [[70.92, 72.28], ['discussing feelings', 'definition of beauty', 'standards']], [[72.28, 74.96], ['finding closure', 'closure struggle', 'serious discussions']], [[74.96, 76.34], ['post-breakup feelings', 'self-reflection', 'new perspectives']], [[76.34, 77.6], ['plan future', 'next steps', 'self-discovery']], [[77.6, 79.94], ['family support', 'checking in', 'caring sister']], [[79.94, 81.6], ['shopping experience', 'quality time', 'bonding moments']], [[81.6, 82.86], ['end of chapter', 'saying goodbye', 'bittersweet']], [[82.86, 84.32], ['breakup aftermath', 'living with decisions', 'emotional growth']], [[84.32, 86.02], ['memories linger', 'final thoughts', 'finding peace']], [[86.02, 87.26], ['moving on', 'new beginnings', 'emotional journey']], [[87.26, 89.72], ['final actions', 'leaving relationship', 'self-assertion']], [[89.72, 91.58], ['symbolic gestures', 'closure rituals', 'parting ways']], [[91.58, 93.28], ['clearing space', 'ending relationship', 'nostalgic moments']], [[93.28, 95.82], ['goodbyes', 'finality', 'emotional weight']], [[95.82, 98.42], ['arguments', 'impact on feelings', 'relationship tension']], [[98.42, 100.84], ['conflict resolution', 'final goodbye', 'moving forward']], [[100.84, 102.34], ['emotional struggles', 'inner turmoil', 'heartfelt conflict']], [[102.34, 103.68], ['reflecting on choices', 'self-awareness', 'personal growth']], [[103.68, 106.0], ['final resolution', 'accepted choices', 'bittersweet conclusion']], [[106.0, 107.46], ['communication breakdown', 'last attempts', 'completing chapter']], [[107.46, 109.08], ['blowing up phone', 'mixed messages', 'emotional rollercoaster']], [[109.08, 111.1], ['turning emotions', 'self-reflection', 'relationship cleanup']], [[111.1, 112.7], ['conflicted feelings', 'mixed emotions', 'processing breakup']], [[112.7, 114.4], ['name-calling', 'hurtful words', 'loss of respect']], [[114.4, 116.64], ['impact on identity', 'feeling lost', 'self-worth questioned']], [[116.64, 118.18], ['moving on', 'emotional journey', 'new perspectives']], [[118.18, 119.92], ['residual feelings', 'self-awareness', 'uncertain future']], [[119.92, 123.5], ['fake image', 'personal reflection', 'outer beauty']], [[123.5, 125.16], ['serious turn off', 'self-discovery', 'value in authenticity']], [[125.16, 126.47], ['unhappiness reminder', 'self-exploration', 'deeper insight']], [[126.47, 128.0], ['loving someone', 'being a part', 'deep emotional connection']], [[128.0, 129.1], ['hopeful words', 'surviving breakup', 'caring sentiment']], [[129.1, 131.46], ['parting words', 'wishes for happiness', 'moving forward']], [[131.46, 132.9], ['inner conflict', 'complex feelings', 'growing experience']]]
    print("\n2. Search terms:",search_terms)

    background_video_urls = None
    if search_terms is not None:
        background_video_urls = generate_video_url(search_terms, VIDEO_SERVER)
        print("\n3. Background videos:", background_video_urls)
    else:
        print("No background video")

    background_video_urls = merge_empty_intervals(background_video_urls)

    if background_video_urls is not None:
        video = get_output_media(SAMPLE_FILE_NAME, timed_captions, background_video_urls, VIDEO_SERVER)
        print(video)
    else:
        print("No video")
