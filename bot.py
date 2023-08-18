import requests
from scripts import *
from render_video import *

with open('script.txt','r') as f:
    s = f.read()

title, script = convert_script(s)
print(title, script)
voice = input('What voice would you like to use?')
render_video(voice,'video1.webm',title,script,60,8,'result.mp4',(875,0),(1685,1440))
