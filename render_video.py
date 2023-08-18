from math import ceil, floor
import time
import random
import os
from moviepy.editor import *
from mutagen.mp3 import MP3
import math
from PIL import Image
import moviepy.video.fx.all as vfx
from moviepy.video.fx.resize import resize
from natsort import natsorted 
import random
from scripts import *
from customtitle import get_title_img_kam, get_title_img_prime


def render_video(voice: str, video_path: str, title_text: str, script: list[str], fps: int, threads: int, output_file: str, top_left: tuple, bottom_right: tuple):
    audio_clips = []
    text_clips = []

    if len(os.listdir('audio')) == 0:
        audio_folder = '0'
    else:
        audio_folder = str(int(list(reversed(natsorted(os.listdir('audio'))))[0])+1)
    os.mkdir(os.path.join('audio', audio_folder))

    for i, sentence in enumerate([title_text]+script):
        if len(os.listdir(os.path.join('audio',audio_folder))) == 0:
            title = '0.mp3'
        else:
            title = str(int(list(reversed(natsorted(os.listdir(os.path.join('audio',audio_folder)))))[0].split('.')[0])+1)+'.mp3'
        get_voice_file(voice,sentence,f'audio/{audio_folder}/{title}')
        print(f'{i+1}/{len([title_text]+script)} audio clips done...')

    get_title_img_prime(title_text)

    for a in natsorted(os.listdir(os.path.join('audio',audio_folder))):
        audio_clips.append(AudioFileClip(os.path.join('audio',audio_folder,a)))
    for n, sentence in enumerate([title_text]+script):
        if n == 0:
            title_clip = ImageClip('title.png')
            title_clip = title_clip.set_duration(MP3(os.path.join('audio', audio_folder, f'{n}.mp3')).info.length)
        else:
            clip = TextClip(sentence, color='white', font='Coolvetica',size=(600,400),method='caption')
            clip = clip.set_duration(MP3(os.path.join('audio', audio_folder, f'{n}.mp3')).info.length)
            text_clips.append(clip)

    audio = concatenate_audioclips(audio_clips)
    subtitles = concatenate_videoclips([title_clip]+text_clips)
    subtitles = subtitles.set_position(('center', 'center'))
    bg = VideoFileClip(video_path)
    bg = bg.fx( vfx.crop, x1=top_left[0], y1=top_left[1], x2=bottom_right[0], y2=bottom_right[1])

    start = random.randint(0, int(bg.duration)-600)
    bg = bg.subclip(start, start+audio.duration)

    final = CompositeVideoClip([bg, subtitles])
    final = final.set_audio(audio)

    final.write_videofile(output_file, fps=fps, threads=threads)

def render_video2(voice, video_path: str, script: list[str], fps: int, threads: int, output_file: str, top_left: tuple, bottom_right: tuple):
    audio_clips = []
    text_clips = []
    text_clips2 = []
    audio_folder = str(int(list(reversed(natsorted(os.listdir('audio'))))[0]))

    for a in os.listdir(os.path.join('audio',audio_folder)):
        audio_clips.append(AudioFileClip(os.path.join('audio',audio_folder,a)))
    for n, sentence in enumerate(script[1:]):
        clip = TextClip(sentence, color='white', font='Coolvetica',size=(600,400),method='caption')
        clip2 = TextClip(sentence, color='white', font='Coolvetica',size=(600,400),method='caption',stroke_color='black',stroke_width=3)
        clip2 = clip2.set_duration(MP3(os.path.join('audio', audio_folder, f'{n+1}.mp3')).info.length)
        clip = clip.set_duration(MP3(os.path.join('audio', audio_folder, f'{n+1}.mp3')).info.length)
        text_clips.append(clip)
        text_clips2.append(clip2)

    audio = concatenate_audioclips(audio_clips)
    subtitles = concatenate_videoclips(text_clips)
    subtitles2 = concatenate_videoclips(text_clips2)
    subtitles2 = subtitles2.set_position(('center', 'center'))
    subtitles = subtitles.set_position(('center', 'center'))
    bg = VideoFileClip(video_path)
    bg = bg.fx( vfx.crop, x1=top_left[0], y1=top_left[1], x2=bottom_right[0], y2=bottom_right[1])

    start = random.randint(0, int(bg.duration)-600)
    bg = bg.subclip(start, start+audio.duration)

    final = CompositeVideoClip([bg, subtitles2, subtitles])
    final = final.set_audio(audio)

    final.write_videofile(output_file, fps=fps, threads=threads)