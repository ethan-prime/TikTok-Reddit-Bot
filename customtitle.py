from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def get_title_img_kam(title):
    title2 = title.split(' ')
    top = ""
    middle = ""
    middle2 = ""
    bottom = ""
    i = 0
    while len(top) < 30 and i < len(title2):
        top += f'{title2[i]} '
        i += 1
    while len(middle) < 30 and i < len(title2):
        middle += f'{title2[i]} '
        i += 1
    while len(middle2) < 30 and i < len(title2):
        middle2 += f'{title2[i]} '
        i += 1
    bottom = ' '.join(title2[i:])
    title = f'{top}\n{middle}\n{middle2}\n{bottom}'
    img = Image.open('kamreddittitle.png')
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('fonts/coolvetica.otf', 40)
    I1.text((68, 175), title, font=myFont, fill=(0, 0, 0))
    img.save('title.png')

def get_title_img_prime(title):
    title2 = title.split(' ')
    top = ""
    middle = ""
    middle2 = ""
    bottom = ""
    i = 0
    while len(top) < 30 and i < len(title2):
        top += f'{title2[i]} '
        i += 1
    while len(middle) < 30 and i < len(title2):
        middle += f'{title2[i]} '
        i += 1
    while len(middle2) < 30 and i < len(title2):
        middle2 += f'{title2[i]} '
        i += 1
    bottom = ' '.join(title2[i:])
    title = f'{top}\n{middle}\n{middle2}\n{bottom}'
    img = Image.open('primereddittitle.png')
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('fonts/coolvetica.otf', 40)
    I1.text((70, 155), title, font=myFont, fill=(0, 0, 0))
    img.save('title.png')