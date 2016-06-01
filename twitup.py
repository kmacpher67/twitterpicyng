import datetime
import random
import sys
import urllib2
import json
from twython import Twython
from HTMLParser import HTMLParser

VERSION="1.0.2015.11.29"
print ("version=" + VERSION)
urlPage = "http://192.168.1.88/tmpfs/auto.jpg"
# puts the time in ms on it. /tmpfs/auto.jpg
url= "http://192.168.1.88/tmpfs/auto.jpg"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
auth ="Basic YWRtaW46YWRtaW4="
headers = { 'User-Agent' : user_agent, 'Authorization': auth }
# username = "user"
# password = "user"
# CONSUMER_KEY = "replace"
# CONSUMER_SECRET = "replace"
# ACCESS_KEY = "replace"
# ACCESS_SECRET = "replace"

dayval = str(datetime.datetime.today().day)
print ("dayval = " + dayval )

hourval = str(datetime.datetime.today().hour)
print ("hourval = " + hourval )

class ReadProperties():
    def __init__(self):
		self.myprops = {}
		with open('filename.properties', 'r') as f:
			for line in f:
				line = line.rstrip() #removes trailing whitespace and '\n' chars
				print("line="+line)
				if "=" not in line: continue #skips blanks and comments w/o =
				if line.startswith("#"): continue #skips comments which contain =

				k, v = line.split("=", 1)
				print("key="+k +" value=" +v)
				self.myprops[k] = v

rp=ReadProperties()
props = rp.myprops
print ("props="+ str(props["ACCESS_KEY"])) 				
print ("test="+ props["test"]) 				

key="1234"

username = props["username"]
password = props["password"]
CONSUMER_KEY = props["CONSUMER_KEY"]
CONSUMER_SECRET = props["CONSUMER_SECRET"]
ACCESS_KEY = props["ACCESS_KEY"]
ACCESS_SECRET = props["ACCESS_SECRET"]

# need key value
try:
	key = props["key"]
	print "key value from props in filename.properties file!"
except: # catch *all* exceptions
	e = sys.exc_info()[0]
	print "key value from props in filename.properties file! = " + str(e)

print ("username=" + username + " password=" + password+ " CONSUMER_KEY =" + CONSUMER_KEY + " CONSUMER_SECRET ="+CONSUMER_SECRET +" ACCESS_KEY=" +ACCESS_KEY)
				
print ("key KEY KEY KEY  =" + key)

testURL = "https://api.github.com/markdown"
remoteURL = "http://live.spontaneousorganization.com/appStatus/index2?key="+key
print("REMOTE URL ="+remoteURL)

statusList = []
req = urllib2.Request(remoteURL)
response = urllib2.urlopen(remoteURL)
statusList = json.load(response)   

print (" statusList = " + str(statusList))

statusMax = len(statusList)-1
print ("statusMax=" + str(statusMax))
### statusIndex = random.randint(0,statusMax)
statusIndex = 0
print ("statusIndex =" + str(statusIndex))


newStatus = str(statusList[statusIndex]["tweetOutputText"])[:124]  
print("newStatus=" + newStatus)
print("LENGTH of status=" + str(len(newStatus)))


fileName = "my_gif.GIF"
print ("fileName = " + fileName )

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# # twitter.update_status(status="Hello world. from ken macpherson test using @twythontest")

photo = open(fileName,'rb')
# If you do not seek(0), the image will be at the end of th=e file and
# unable to be read
photo.seek(0)
print ("photo created rate limit is:" )
# x= twitter.get_home_timeline()
# # print(x)

try:
	image_ids = twitter.upload_media(media=photo)
	print (image_ids)
# except Twython.TwythonError as terr:
	# print "ERROR on twitter = ({0}): {1}".format(terr.errno, terr.strerror)
except TwythonRateLimitError as terr:
	print "ERROR on twitter rate = ({0}): {1}".format(terr1.errno, terr.strerror)
except Exception as err:
	print "ERROR on unknown = " + err
	
y=twitter.get_lastfunction_header('X-Rate-Limit-Reset')
print(y)
z=twitter.get_lastfunction_header('x-rate-limit-remaining')
print(z)

print ("media id = " + str(image_ids['media_id']) )

statusupdate=twitter.update_status(status= newStatus[:116],media_ids=image_ids['media_id'])

print(statusupdate)



