__author__ = 'Robert'
from images2gif import writeGif
from PIL import Image
import os

imagestoshow=21

#file_names =  sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')], key=os.path.getctime, reverse=True)
file_names =  sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')], key=os.path.getctime)

goback=738
if len(file_names)-goback>imagestoshow:
	file_names=file_names[len(file_names)-goback-imagestoshow:len(file_names)-goback]
print file_names

images = [Image.open(fn) for fn in file_names]

filename = "my_gif.GIF"
print filename
writeGif(filename, images, duration=0.45)
