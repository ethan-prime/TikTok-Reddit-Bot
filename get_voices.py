import requests
from config import XIAPIKEY

headers = {
    'xi-api-key':XIAPIKEY
}
r = requests.get('https://api.elevenlabs.io/v1/voices', headers=headers)
voices = {

}
for voice in r.json()['voices']:
    voices[voice['name']] = voice['voice_id']

with open('voices.txt', 'w') as f:
    for key, value in voices.items():
        f.write(f'{key}: {value}\n')

print(voices)