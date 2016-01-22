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
#file_names=[ 'w530.jpg', 'w540.jpg', 'w550.jpg', 'w60.jpg', 'w610.jpg', 'w620.jpg', 'w630.jpg', 'w640.jpg', 'w650.jpg','w70.jpg', 'w710.jpg', 'w720.jpg', 'w730.jpg', 'w740.jpg', 'w750.jpg', 'w80.jpg', 'w810.jpg', 'w820.jpg', 'w830.jpg', 'w840.jpg', 'w850.jpg', 'w90.jpg', 'w910.jpg', 'w920.jpg', 'w930.jpg', 'w940.jpg', 'w950.jpg', 'w100.jpg', 'w1010.jpg', 'w1020.jpg', 'w1030.jpg', 'w1040.jpg', 'w1050.jpg']

file_names=['w530.jpg', 'w540.jpg', 'w550.jpg', 'w60.jpg', 'w610.jpg', 'w620.jpg', 'w630.jpg', 'w640.jpg', 'w650.jpg','w70.jpg', 'w710.jpg', 'w720.jpg', 'w730.jpg', 'w740.jpg', 'w750.jpg', 'w80.jpg', 'w810.jpg', 'w820.jpg', 'w830.jpg', 'w840.jpg', 'w850.jpg', 'w90.jpg', 'w910.jpg', 'w920.jpg', 'w930.jpg']


#file_names=['w90.jpg', 'w910.jpg', 'w920.jpg', 'w930.jpg', 'w940.jpg', 'w950.jpg', 'w100.jpg', 'w1010.jpg', 'w1020.jpg', 'w1030.jpg', 'w1040.jpg', 'w1050.jpg']
#file_names=['w110.jpg', 'w1110.jpg', 'w1120.jpg', 'w1130.jpg', 'w1140.jpg', 'w1150.jpg', 'w120.jpg', 'w1210.jpg', 'w1220.jpg', 'w1230.jpg', 'w1240.jpg', 'w1250.jpg', 'w130.jpg', 'w1310.jpg', 'w1320.jpg', 'w1330.jpg', 'w1340.jpg', 'w1350.jpg', 'w140.jpg', 'w1410.jpg', 'w1420.jpg', 'w1430.jpg', 'w1440.jpg', 'w1450.jpg']

#file_names=['w160.jpg', 'w1610.jpg', 'w1620.jpg', 'w1630.jpg', 'w1640.jpg', 'w1650.jpg',  'w170.jpg', 'w1710.jpg', 'w1720.jpg', 'w1730.jpg', 'w1740.jpg', 'w1750.jpg',  'w180.jpg', 'w1810.jpg', 'w1820.jpg', 'w1830.jpg', 'w1840.jpg', 'w1850.jpg']

images = [Image.open(fn) for fn in file_names]

filename = "my_gif.GIF"
print filename
writeGif(filename, images, duration=0.5)
