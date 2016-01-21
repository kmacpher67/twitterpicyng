import xml.etree.ElementTree as ET
import urllib2
import StringIO

urlPage = "http://w1.weather.gov/xml/current_obs/KYNG.xml"

data = urllib2.urlopen(urlPage).read() 
#urllib2.urlopen(urlPage).read()

print data

tree = ET.fromstring(data)
print 'tree:',tree
print 'Cond:',tree.find('weather').text
print 'Temp:',tree.find('temperature_string').text
print 'Wind:',tree.find('wind_string').text
print 'Pres:',tree.find('pressure_in').text
print 'Visb:',tree.find('visibility_mi').text