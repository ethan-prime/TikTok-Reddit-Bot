import requests
from natsort import natsorted
import os
import re
from mutagen.mp3 import MP3
from config import XIAPIKEY

voice_id_dict = {

}

with open('voices.txt', 'r') as f:
    for line in f.readlines():
        voice_id_dict[line.split(': ')[0]] = line.split(': ')[1].replace('\n','')

headers = {
    'xi-api-key': XIAPIKEY
}

def translate(text):
    dict = {

    }
    for key, value in dict.items():
        text = text.replace(key, value)
    return text

def convert_script(script):
    script = translate(script)
    title = script.split('\n')[0]
    script = '\n'.join(script.split('\n')[1:])
    script = script.replace('\n','').replace('?','').replace('!','')
    res = re.sub("[^A-Za-z0-9\s.!?,;']+", '', script)
    res = res.split('.')
    for i, s  in enumerate(res):
        new = s.strip()
        if new != '':
            res[i] = new
    return title, res

def get_voice_file(voice: str, text: str, output_path: str, stability: float=0.75, similarity_boost: float=1.0):
    json = {
        "text": text,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity_boost
        }
    }
    r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id_dict[voice]}", headers=headers, json=json)
    with open(output_path, 'wb') as f:
        f.write(r.content)
    try:
        length = MP3(output_path).info.length
    except Exception:
        get_voice_file(voice=voice,text=text,output_path=output_path,stability=stability,similarity_boost=similarity_boost)        
    return r.status_code