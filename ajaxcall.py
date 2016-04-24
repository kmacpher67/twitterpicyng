import urllib2
import json
import random


data = {"text": "Hello world github/linguist#1 **cool**, and #1!"}
json_data = json.dumps(data)

testURL = "https://api.github.com/markdown"
remoteURL = "http://live.spontaneousorganization.com/appStatus/index1?key=9999"
statusList = []
req = urllib2.Request(remoteURL)
response = urllib2.urlopen(remoteURL)
statusList = json.load(response)   

#print str(response[0].["tweetOutputText"])

statusMax = len(statusList)-1
print ("statusMax=" + str(statusMax))
statusIndex = random.randint(0,statusMax)
print ("statusIndex =" + str(statusIndex))

newStatus = str(statusList[statusIndex]["tweetOutputText"])  #[:104]
print("newStatus=" + newStatus)
print("LENGTH of status=" + str(len(newStatus)))

##prin data
#result = urllib2.urlopen(req, json_data)
#resultstring = str(result.readlines())
#print resultstring
#resultjson = json.loads(resultstring)
#resultjson = json.JSONEncoder().encode(resultstring)
#i=0
#for message in data:
#    print '\n\n',message

#print '\n\n\n'.join(result.readlines())