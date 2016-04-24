import urllib2
import json
import random

key="9999"

testURL = "https://api.github.com/markdown"
remoteURL = "http://live.spontaneousorganization.com/appStatus/index1?key="+key
statusList = []
req = urllib2.Request(remoteURL)
response = urllib2.urlopen(remoteURL)
statusList = json.load(response)   

#print str(response[0].["tweetOutputText"])

statusMax = len(statusList)-1
print ("statusMax=" + str(statusMax))
statusIndex = random.randint(0,statusMax)
print ("statusIndex =" + str(statusIndex))

newStatus = str(statusList[statusIndex]["tweetOutputText"])[:124]  
print("newStatus=" + newStatus)
print("LENGTH of status=" + str(len(newStatus)))
