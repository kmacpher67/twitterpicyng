import xml.etree.ElementTree as ET

data='''<?xml version="1.0" encoding="ISO-8859-1"?>

<rss version='2.0' xmlns:dc='http://purl.org/dc/elements/1.1/'> 
     <channel>
<title>Weather at Youngstown, Youngstown-Warren Regional Airport, OH - via NOAA's National Weather Service</title>
<link>http://www.weather.gov/xml/current_obs/</link>
     <lastBuildDate>Thu, 21 Jan 2016 14:51:00 -0500</lastBuildDate>
     <ttl>60</ttl>
     <description>Weather conditions from NOAA's National Weather Service. </description>
     <language>en-us</language>
     <managingEditor>robert.bunge@noaa.gov</managingEditor>
     <webMaster>w-nws.webmaster@noaa.gov</webMaster>
     <image>
     <url>http://www.weather.gov/images/xml_logo.gif</url>
     <title>NOAA - National Weather Service</title>
     <link>http://www.weather.gov/xml/current_obs/</link>
     </image> 
    
     <item>
<title>
Light Snow and 22 F at Youngstown, Youngstown-Warren Regional Airport, OH</title>
<link>http://weather.noaa.gov/weather/current/KYNG.html</link> 
<description>
<![CDATA[<img src="http://forecast.weather.gov/images/wtf/small/sn.png" class="noaaWeatherIcon"  width="55" height="58" alt="Light Snow" style="float:left;" /><br />]]>
Winds are Variable at 3.5 MPH (3 KT). The pressure is 1027.7 mb and the humidity is 71%.
 Last Updated on Jan 21 2016, 2:51 pm EST.  
      </description>
      <guid isPermaLink="false">Thu, 21 Jan 2016 14:51:00 -0500</guid>
      </item>
      </channel>
      </rss>'''

tree = ET.fromstring(data)
print 'tree:',tree.text
print 'Name:',tree.find('channel/item/title').text
print 'Attr:',tree.find('channel/item/description').text