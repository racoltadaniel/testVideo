import os
import json

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

def fix_json(json_str):
    # Replace typographical apostrophes with straight quotes
    json_str = json_str.replace("’", "'")
    # Replace any incorrect quotes (e.g., mixed single and double quotes)
    json_str = (
        json_str.replace("“", '"').replace("”", '"').replace("‘", '"').replace("’", '"')
    )
    # Add escaping for quotes within the strings
    json_str = json_str.replace('"you didn"t"', '"you didn\'t"')
    return json_str


if __name__ == "__main__":

    captions_timed = [
        ((0, 0.92), "Script Colin"),
        ((0.92, 2.44), "I 36M met"),
        ((2.44, 3.12), "my now ex"),
        ((3.12, 4.52), "34F a little"),
        ((4.52, 4.78), "over two"),
        ((4.78, 5.24), "years ago"),
        ((5.24, 6.74), "During that"),
        ((6.74, 7.22), "time the"),
        ((7.22, 8.06), "idea of her"),
        ((8.06, 8.4), "getting a"),
        ((8.4, 8.8), "boob job"),
        ((8.8, 9.24), "has come"),
        ((9.24, 9.6), "up a few"),
        ((9.6, 10.22), "times She'd"),
        ((10.22, 11.84), "asked me"),
        ((11.84, 12.42), "I ever dated"),
        ((12.42, 13.14), "anyone with"),
        ((13.14, 13.62), "them and"),
        ((13.62, 14.28), "what I thought"),
        ((14.28, 14.46), "of them"),
        ((14.46, 15.94), "I told her"),
        ((15.94, 16.12), "I had I"),
        ((16.12, 16.74), "am not a"),
        ((16.74, 17.34), "fan at all"),
        ((17.34, 17.74), "and they"),
        ((17.74, 18.2), "are a deal"),
        ((18.2, 18.76), "breaker for"),
        ((18.76, 18.98), "me About"),
        ((18.98, 20.34), "this time"),
        ((20.34, 20.8), "last year"),
        ((20.8, 21.34), "she asked"),
        ((21.34, 21.86), "me what I"),
        ((21.86, 22.34), "thought of"),
        ((22.34, 22.88), "her getting"),
        ((22.88, 23.06), "a boob job"),
        ((23.06, 24.9), "She was feeling"),
        ((24.9, 25.28), "a bit"),
        ((25.28, 26.26), "self-conscious"),
        ((26.26, 26.26), "and wanted"),
        ((26.26, 26.9), "something"),
        ((26.9, 27.28), "bigger than"),
        ((27.28, 27.96), "I told her"),
        ((27.96, 28.38), "she can do"),
        ((28.38, 28.76), "what she"),
        ((28.76, 29.3), "wants with"),
        ((29.3, 29.72), "her body"),
        ((29.72, 30.04), "I am not"),
        ((30.04, 31.34), "going to"),
        ((31.34, 31.76), "tell her"),
        ((31.76, 32.3), "no because"),
        ((32.3, 32.9), "it's not"),
        ((32.9, 33.18), "my place"),
        ((33.18, 33.8), "If getting"),
        ((33.8, 35.26), "the boob"),
        ((35.26, 35.72), "job would"),
        ((35.72, 36.12), "help her"),
        ((36.12, 37.18), "self-confidence"),
        ((37.18, 37.46), "and self-image"),
        ((37.46, 38.02), "then it's"),
        ((38.02, 38.5), "something she"),
        ((38.5, 38.98), "might want"),
        ((38.98, 39.4), "to consider"),
        ((39.4, 39.86), "Just that"),
        ((39.86, 41.34), "choices have"),
        ((41.34, 41.96), "consequences"),
        ((41.96, 42.44), "and if she"),
        ((42.44, 43.08), "did get the"),
        ((43.08, 43.44), "boob job"),
        ((43.44, 44.06), "I would leave"),
        ((44.06, 44.6), "She laughed"),
        ((44.6, 46.12), "and thought"),
        ((46.12, 46.58), "I was kidding"),
        ((46.58, 47.16), "The idea"),
        ((47.16, 48.38), "came up a"),
        ((48.38, 48.9), "few more"),
        ((48.9, 49.42), "times and"),
        ((49.42, 49.88), "the answer"),
        ((49.88, 50.52), "was the same"),
        ((50.52, 50.94), "each timeat"),
        ((50.94, 52.1), "the end of"),
        ((52.1, 52.36), "July her"),
        ((52.36, 52.98), "sister came"),
        ((52.98, 53.6), "for a visit"),
        ((53.6, 54.24), "her and was"),
        ((54.24, 54.7), "going to"),
        ((54.7, 55.02), "stay for"),
        ((55.02, 55.38), "a while"),
        ((55.38, 55.88), "This isn't"),
        ((55.88, 56.06), "unusual"),
        ((56.06, 58.14), "especially when"),
        ((58.14, 58.86), "I have a"),
        ((58.86, 59.42), "long-ish work"),
        ((59.42, 59.84), "trip coming"),
        ((59.84, 60.26), "up A week"),
        ((60.26, 60.74), "later I left"),
        ((60.74, 62.36), "for a work"),
        ((62.36, 63.08), "trip that"),
        ((63.08, 63.62), "last about"),
        ((63.62, 63.8), "25 weeks"),
        ((63.8, 64.34), "I get home"),
        ((64.34, 65.74), "in the next"),
        ((65.74, 66.14), "day her"),
        ((66.14, 66.81), "and her sister"),
        ((66.81, 67.34), "come over"),
        ((67.34, 67.68), "to my place"),
        ((67.68, 68.52), "It was obvious"),
        ((68.52, 68.78), "what she"),
        ((68.78, 70.5), "did while"),
        ((70.5, 70.92), "I was gone"),
        ((70.92, 71.34), "as she was"),
        ((71.34, 71.86), "at least"),
        ((71.86, 72.28), "two cup sizes"),
        ((72.28, 72.6), "bigger We"),
        ((72.6, 73.38), "hang out"),
        ((73.38, 73.72), "for a bit"),
        ((73.72, 75.28), "then I tell"),
        ((75.28, 75.66), "them I am"),
        ((75.66, 75.96), "tired and"),
        ((75.96, 76.34), "it was a"),
        ((76.34, 76.94), "long trip"),
        ((76.94, 77.34), "She tells"),
        ((77.34, 77.6), "me she'll"),
        ((77.6, 79.08), "come over"),
        ((79.08, 79.76), "tomorrow to"),
        ((79.76, 79.94), "check in"),
        ((79.94, 80.48), "on me after"),
        ((80.48, 81.12), "they go out"),
        ((81.12, 81.6), "to lunch"),
        ((81.6, 81.8), "and do a"),
        ((81.8, 82.46), "bit of shopping"),
        ((82.46, 83.24), "after thinking"),
        ((83.24, 83.54), "about it"),
        ((83.54, 84.32), "for the evening"),
        ((84.32, 84.8), "I decided"),
        ((84.8, 85.34), "it was a"),
        ((85.34, 86.02), "deal breaker"),
        ((86.02, 86.44), "for me I"),
        ((86.44, 87.04), "went over"),
        ((87.04, 87.26), "to a place"),
        ((87.26, 88.74), "with a box"),
        ((88.74, 89.5), "of her stuff"),
        ((89.5, 90.04), "grabbed my"),
        ((90.04, 90.38), "stuff and"),
        ((90.38, 91.06), "left my copy"),
        ((91.06, 91.8), "of her keys"),
        ((91.8, 92.54), "on the table"),
        ((92.54, 92.86), "As I was"),
        ((92.86, 93.72), "leaving they"),
        ((93.72, 95.02), "rolled him"),
        ((95.02, 95.82), "We went inside"),
        ((95.82, 96.28), "and I told"),
        ((96.28, 97.66), "her I was"),
        ((97.66, 98.42), "leaving That"),
        ((98.42, 98.98), "the surgery"),
        ((98.98, 99.4), "was a deal"),
        ((99.4, 101.16), "breaker for"),
        ((101.16, 101.6), "me and it's"),
        ((101.6, 102.08), "not something"),
        ((102.08, 102.64), "I can come"),
        ((102.64, 103.32), "to live with"),
        ((103.32, 103.68), "It turned"),
        ((103.68, 104.2), "into a big"),
        ((104.2, 105.54), "argument and"),
        ((105.54, 106.0), "I wished"),
        ((106.0, 106.7), "her all the"),
        ((106.7, 106.94), "best and"),
        ((106.94, 107.46), "left after"),
        ((107.46, 107.76), "about 15"),
        ((107.76, 108.48), "minutes for"),
        ((108.48, 108.82), "the last"),
        ((108.82, 109.8), "week she's"),
        ((109.8, 109.97), "blowing up"),
        ((109.97, 110.32), "my phone"),
        ((110.32, 111.1), "switching"),
        ((111.1, 111.7), "between baby"),
        ((111.7, 112.3), "I miss you"),
        ((112.3, 113.06), "and you fucking"),
        ((113.06, 113.48), "loser Her"),
        ((113.48, 114.14), "sister has"),
        ((114.14, 114.74), "been calling"),
        ((114.74, 116.28), "me everything"),
        ((116.28, 116.64), "under the"),
        ((116.64, 117.14), "sun except"),
        ((117.14, 117.54), "my namemy"),
        ((117.54, 118.18), "said I left"),
        ((118.18, 118.74), "Yeah I did"),
        ((118.74, 119.34), "like her"),
        ((119.34, 119.92), "a lot But"),
        ((119.92, 121.52), "fake boobs"),
        ((121.52, 122.16), "are a serious"),
        ((122.16, 123.5), "turn off"),
        ((123.5, 124.04), "for me and"),
        ((124.04, 124.66), "I don't think"),
        ((124.66, 125.3), "I would have"),
        ((125.3, 125.98), "been happy"),
        ((125.98, 126.18), "nor do I"),
        ((126.18, 126.64), "think it's"),
        ((126.64, 127.08), "something I"),
        ((127.08, 127.8), "could have"),
        ((127.8, 128.48), "come to like"),
        ((128.48, 128.68), "I hope she"),
        ((128.68, 128.94), "is happy"),
        ((128.94, 129.28), "and they"),
        ((129.28, 130.86), "help with"),
        ((130.86, 131.24), "herself a"),
        ((131.24, 131.62), "stain but"),
        ((131.62, 131.94), "I couldn't"),
        ((131.94, 132.44), "be a part"),
        ((132.44, 132.9), "of that"),
    ]
    print(split_text('Am fost sa aduc mere de la mama'))
    end = captions_timed[-1][0][1]
    try:
        out = [[[0, 0], ""]]
        content = '```json [ [[0, 2], ["script text"]], [[2, 4], ["met ex"]], [[4, 6], ["2 years ago"]], [[6, 8], ["boob job idea"]], [[8, 10], ["dating question"]], [[10, 12], ["dated with implants"]], [[12, 14], ["not a fan"]], [[14, 16], ["deal breaker"]], [[16, 18], ["last year"]], [[18, 20], ["asked again"]], [[20, 22], ["getting a job"]], [[22, 24], ["feeling self-conscious"]], [[24, 26], ["wanted bigger"]], [[26, 28], ["her choice"]], [[28, 30], ["body decision"]], [[30, 32], ["not my place"]], [[32, 34], ["boob job help"]], [[34, 36], ["self-confidence"]], [[36, 38], ["self-image"]], [[38, 40], ["choices consequences"]], [[40, 42], ["would leave"]], [[42, 44], ["thought joking"]], [[44, 46], ["idea repeated"]], [[46, 48], ["sister visit"]], [[48, 50], ["long work trip"]], [[50, 52], ["2.5 weeks"]], [[52, 54], ["home return"]], [[54, 56], ["visit her"]], [[56, 58], ["obvious surgery"]], [[58, 60], ["two cup sizes"]], [[60, 62], ["tired from trip"]], [[62, 64], ["visit tomorrow"]], [[64, 66], ["shopping"]], [[66, 68], ["decided deal breaker"]], [[68, 70], ["packing stuff"]], [[70, 72], ["leaving keys"]], [[72, 74], ["leaving notice"]], [[74, 76], ["big argument"]], [[76, 78], ["left"]], [[78, 80], ["text messages"]], [[80, 82], ["miss you"]], [[82, 84], ["fucking loser"]], [[84, 86], ["sister angry"]], [[86, 88], ["left sad"]], [[88, 90], ["liked her"]], [[90, 92], ["fake boobs turn off"]], [[92, 94], ["wouldn\'t be happy"]], [[94, 96], ["hope happy"]], [[96, 98], ["self-esteem"]], [[98, 100], ["not part"]] ] ```'
        try:
            out = json.loads(content)
        except Exception as e:
            print(e)
            content = fix_json(content.replace("```json", "").replace("```", ""))
            print("!!!!!!Content after styling ", content)
            out = json.loads(content)
            print("!!!!!!Out ", out)
    except Exception as e:
        print("error in response", e)
