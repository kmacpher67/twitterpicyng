import datetime
import random
import sys
import urllib2

#http://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today
#location @41.2367389, -80.782401,15z
#     lat=-XX.XXXXX&lng=XX.XXXXX

#request = 'http://api.sunrise-sunset.org/json?lat=80.7824000&lng=-41.2367300&date=today'
request =  "http://api.sunrise-sunset.org/json?lat=80.8184166&lng=41.4203400&date=today"
response = urllib2.urlopen(request)
timestring = response.read()

print timestring

utcsunrise = timestring[34:39]
utcsunset = timestring[71:76]
utcmorning = timestring[182:187]
utcnight = timestring[231:236]

print "utcsunrise"+utcsunrise
print "utcsunset"+utcsunset
print "utcmorning"+utcmorning
print "utcnight"+utcnight

