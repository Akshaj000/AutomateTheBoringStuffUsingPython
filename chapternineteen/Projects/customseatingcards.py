#! python3

import os

from PIL import Image,ImageDraw,ImageFont

os.makedirs('Invitations',exist_ok=True)
file=open('guests.txt')
names=file.readlines()

flower = Image.open('flowers.png').convert('RGBA')

os.chdir('Invitations')

for i in names:
    im = Image.new('RGBA', (360, 290), 'black')
    flower=flower.resize((360,288))
    im.paste(flower, (0, 0), flower)
    drawObj = ImageDraw.Draw(im)
    fontFolder = 'usr/share/fonts'
    font = ImageFont.truetype(os.path.join(fontFolder,'AmaticSC-Regular.ttf'), 40)
    drawObj.text((90, 3),'Welcome'+i, fill='green', font=font)
    drawObj.rectangle((5, 5, 350, 285), outline='green')

    im.save('invite_{}.png'.format(i))