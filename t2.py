__author__ = 'Robert'
from images2gif import writeGif
from PIL import Image
import os

#ile_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg))
#['animationframa.png', 'animationframb.png', ...] "
file_names=['weather11.jpg', 'weather12.jpg', 'weather20.jpg', 'weather19.jpg', 'weather29.jpg', 'weather7.jpg', 'weather7.jpg', 'weather8.jpg', 'weather9.jpg'] 
#file_names=['yt1.jpg', 'yt2.jpg', 'yt3.jpg', 'yt4.jpg', 'yt5.jpg', 'yt6.jpg', 'yt7.jpg', 'yt8.jpg', 'yt9.jpg'] 

images = [Image.open(fn) for fn in file_names]

filename = "my_gif.GIF"
print filename
writeGif(filename, images, duration=0.5)
