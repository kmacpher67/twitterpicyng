__author__ = 'Robert'
from images2gif import writeGif
from PIL import Image
import os

#ile_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg))
#['animationframa.png', 'animationframb.png', ...] "
#file_names=['w1900.jpg', 'w2323.jpg', 'w2340.jpg', 'w2359.jpg', 'w041.jpg', '', '', '', ''] 
#file_names=['w30.jpg', 'w310.jpg', 'w340.jpg', 'w340.jpg', 'w350.jpg', 'w40.jpg', 'w410.jpg', 'w420.jpg', 'w430.jpg', 'w440.jpg', 'w450.jpg']
#file_names=['w50.jpg', 'w510.jpg', 'w520.jpg', 'w530.jpg', 'w540.jpg', 'w550.jpg', 'w60.jpg', 'w610.jpg', 'w620.jpg', 'w630.jpg', 'w640.jpg', 'w650.jpg']
#file_names=['yt1.jpg', 'yt2.jpg', 'yt3.jpg', 'yt4.jpg', 'yt5.jpg', 'yt6.jpg', 'yt7.jpg', 'yt8.jpg', 'yt9.jpg'] 
file_names=['w70.jpg', 'w710.jpg', 'w720.jpg', 'w730.jpg', 'w740.jpg', 'w750.jpg', 'w80.jpg', 'w810.jpg', 'w820.jpg', 'w830.jpg', 'w840.jpg', 'w850.jpg']

images = [Image.open(fn) for fn in file_names]

filename = "my_gif.GIF"
print filename
writeGif(filename, images, duration=0.5)
