import datetime
import random
import sys
import urllib2
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
# CONSUMER_KEY = "9pDZHBl8diH6nC1n2CdrJXCMo"
# CONSUMER_SECRET = "JuUi3LYJBVhMffihmTGUhAPy3LhVeGPHvGuEfu3IkUBMrEmM65"
# ACCESS_KEY = "17961805-SFeUb1SBg4CjNsepZbC9EGwhx4QbRSAMAaiHTyFQV"
# ACCESS_SECRET = "wftwTZigBEiOzL90SyLSRGRot2Vdk71Y67SkUBw24xQ95"

dayval = str(datetime.datetime.today().day)
print ("dayval = " + dayval )

hourval = str(datetime.datetime.today().hour)
print ("hourval = " + hourval )

# {u'image': {u'image_type': u'image/jpeg', u'h': 352, u'w': 640}, u'media_id_string': u'668837656852348928', u'media_id':
 # 668837656852348928L, u'expires_after_secs': 86400, u'size': 104529}
# 1448301806
# 413
#             1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 1234 6789 
#            "                  2         3         4         5         6         7         8         9         x       110       120        130      140
statusvalue1="@OHCollaborative Live Stream cam #Youngstown city weather action #makerspace http://goo.gl/EgEsfl"
statusvalue2="@OHCollaborative #Youngstown Ohio City scape outdoor weather cam system http://goo.gl/EgEsfl"
statusvalue3="@OHCollaborative #Youngstown city weather view @Youngstown_Buzz #makerspace #RaspberryPI southside"
statusvalue4="@OHCollaborative Check yr hairdo #Youngstown weather #makerspace #RaspberryPI southside"
statusvalue5="@OHCollaborative #Youngstown weather camera #makerspace #RaspberryPI southside @21WFMJ"
statusvalue6="@OHCollaborative #Youngstown weather cam #makerspace tech best southside view city http://goo.gl/EgEsfl"
statusvalue7="@OHCollaborative #Youngstown weather camera #makerspace #RaspberryPI southside @21WFMJ"
statusvalue8="@OHCollaborative #Youngstown weather cam #makerspace training tech innovation southside neighborhood"
statusvalue9="@OHCollaborative #Youngstown weather camera #makerspace #3dprinting startups mentoring"
statusvalue0="@OHCollaborative #Youngstown weather camera #makerspace technology 4 learning to earn"

statusList = [statusvalue1, statusvalue2, statusvalue3, statusvalue4, statusvalue5, statusvalue6, statusvalue7, statusvalue8, statusvalue9,statusvalue0]
statusMax = len(statusList)-1
print ("statusMax=" + str(statusMax))
statusIndex = random.randint(0,statusMax)
print ("statusIndex =" + str(statusIndex))

shoutOuts = ["@Youngstown_Buzz", "@Youngstown_News","@EricWFMJ","@DOWNTOWNYTOWN","@21WFMJNews","@vindicator","@21WFMJNews","@StormTracker21", "@WKBN", "@PapaMuzz", "@JaladahA", "@wfmjtoday", "@SteveDeGenaro", "@ReeseClarett13", "@Dbetras", "@SteveWFMJ","@21WFMJNews","@LindsayWFMJ","@CatulloMeats","@V2Youngstown","@9teen84","@HudsonFasteners","@TEDxYoungstown","@NeuvooYoungsto"]
shoutIndex = random.randint(0,len(shoutOuts)-1)

newStatus = statusList[statusIndex] + " " +hourval+ " " + shoutOuts[shoutIndex]
print("newStatus=" + newStatus)

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

username = props["username"]
password = props["password"]
CONSUMER_KEY = props["CONSUMER_KEY"]
CONSUMER_SECRET = props["CONSUMER_SECRET"]
ACCESS_KEY = props["ACCESS_KEY"]
ACCESS_SECRET = props["ACCESS_SECRET"]

print ("username=" + username + " password=" + password+ " CONSUMER_KEY =" + CONSUMER_KEY + " CONSUMER_SECRET ="+CONSUMER_SECRET +" ACCESS_KEY=" +ACCESS_KEY)
				
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.noImgHtml = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for a in attrs:
                if a[0] == 'src':
                    self.imageUrl = a[1]
        else:
            self.noImgHtml += self.get_starttag_text()


    def handle_endtag(self, tag):
        if tag != 'img':
            self.noImgHtml += '</%s>' % tag

    def handle_data(self, data):
        self.noImgHtml += data
        self.text = data


# create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://192.168.1.88/"
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib2.HTTPBasicAuthHandler(password_mgr)
print("handler chreated for admin user")
# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
urllib2.install_opener(opener)

# r = urllib2.Request( urlPage , headers=headers)
# page = urllib2.urlopen(r).read()

# <img id="img1" border="0" src="tmpfs/auto.jpg">
#  this method would be called as handle_starttag('a', [('href', 'http://www.cwi.nl/')]).
# parser = MyHTMLParser()
# print("PAGE=" + page)

# parser.feed(page)
# print("THIS is image url=" + parser.text)
# urlImageValue = parser.text

# print("THIS is image url=" + urlImageValue)

print ("url=" + url)

imgData = urllib2.urlopen(url).read()
print ("imagedata size = " )
fileName = "weather"+dayval+".jpg"
print ("fileName = " + fileName )

output = open(fileName,'wb')
output.write(imgData)
output.close()

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

statusupdate=twitter.update_status(status= newStatus,media_ids=image_ids['media_id'])

print(statusupdate)

# https://pbs.twimg.com/media/CUgwTiUWwAAGGol.jpg

