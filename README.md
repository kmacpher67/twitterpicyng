# twitterpicyng
Twitter Picture for Youngstown Collaborative

This is a repo to store the code for OakHill Collaborative Makerspace City scape outdoor weather camera project view of the city from the top of the Collaborative big green building. 

This is hastily written code, in python language, by a java programmer, in spare time.  

We have a IPTV cctv camera mounted on the roof of the building.  This code does a few things. Some of which are not used cause, I didn't need it. 

Install on machine 

````
git clone https://github.com/kmacpher67/twitterpicyng.git
````

## Code Review

* Twitter as a content repository.  The code post the pictures to twitter using Twython libary, and https://apps.twitter.com/. Oh god, I put the app keys into the source code in the initial check-in, I'll have to fix that before ISIS or Alquida finds them and starts a twitter storm about porking the west. 
* I'm currently posting the media to my personal feed, I'll be switching it over to the OakHill twitter account. 
* Download the image from the IP Camera using url get and write to local filesystem as weather##.jpg 
* upload the media to twitter 
* attach the media to a status update 
* use twitter search widget to embedd on the http://city.oakhillcollaborative.org/
* stubbed out code to html parse a page get to twitter, never completed that cause the twitter widget is too easy 
* copy and paste twitter widget int index.html on webserver 

## Future enhancements

1. array of status messages for unique messages per event 
2. array of @people targets for better socialization 
3. logic for time and event specific tweeting 
4. interactive logic for uses to request the own custom view of the city
5. interactive tweet reads and reply responses to people (automated bot responses)


## CRONTAB SETUP

created a "cron" job, which is a unix style scheduler that runs every */3 minutes and checks for git hub update, when I push new version of the "weathercap1.py" code to the git hub repository. 

The raspberry pi automatically downloads it and starts using that new version. This is a poor mans hacking trick to get remote access to the raspberry pi until we get a VPN setup for the place. 

The Raspberry PI is setup with two crontab -e (crontab is the command one uses to edit the cron job listsings)

1>  sudo crontab -e 

```
*/30 * * * * python /home/pi/twitterpic/weathercap1.py
```


#2>
```
$ as pi user crontab -e 
*/10 * * * * /home/pi/gitsync.sh 
``` 


gitsync.sh 
----------------
```
#!/bin/bash
cd /home/pi/twitterpic/
git pull 
```

# install twython

```
pi@raspberrypi ~/twitterpicyng $ python camcap.py
Traceback (most recent call last):
  File "camcap.py", line 5, in <module>
    from twython import Twython
ImportError: No module named twython
pi@raspberrypi ~/twitterpicyng $
```
If you get this error then you need to install python library Twython using pip or easy install. Which is easy on Raspberry PI or Linux but not so much on Windows. https://twython.readthedocs.org/en/latest/usage/install.html 

```
sudo pip install twython
```

# Error for properties file 

You need to create a properties file and edit your twitter fun stuff to it. 

```
Traceback (most recent call last):
  File "camcap.py", line 127, in <module>
    rp=ReadProperties()
  File "camcap.py", line 116, in __init__
    with open('filename.properties', 'r') as f:
IOError: [Errno 2] No such file or directory: 'filename.properties'
```

```
cat filename.properties
username=admin
password=admin
CONSUMER_KEY=<<<PUTKEYFROMTWITTERAPP>>
CONSUMER_SECRET=<<PUTSECRETFROMTWITTERAPP>>
ACCESS_KEY=<<FROMTWITTERAPPMUSTCHANGEALLTHESE>>
ACCESS_SECRET=<<ANOTHERBIGLONGTHINGFROMTWITTER>>
test=testie
```
