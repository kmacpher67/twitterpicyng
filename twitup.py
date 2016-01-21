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
statusvalue11="Bring tech to you come visit @OHCollaborative #Youngstown weather camera code events!"
statusvalue12="Hour of Code event tech tues #makers weds 6pm @OHCollaborative #Youngstown weather camera"
statusvalue13="@codegirlmovie code hour girls find inner power @OHCollaborative #Youngstown weather camera"
statusvalue14="community space, and small business incubator @OHCollaborative #Youngstown weather camera"
statusvalue15="Positive force for growth, community, life @OHCollaborative #Youngstown weather camera"
statusvalue16="community revitalization through small biz dev @OHCollaborative #Youngstown weather camera"
statusvalue17="reduce the digital divide TECH, CODE @OHCollaborative #Youngstown weather camera"
statusvalue18="curiosity & imagination incubator @OHCollaborative #Youngstown weather camera"
statusvalue19="neighborhood beautification & quality of life @OHCollaborative #Youngstown weather camera"
statusvalue20="#makerspace community center with tools @OHCollaborative #Youngstown weather camera"
statusvalue21="What can u #makerspace weds 6pm @OHCollaborative #Youngstown weather camera"
statusvalue22="Rock Shots Photography for special events @OHCollaborative #Youngstown weather camera"
statusvalue23="#makerspace Learn Social Media Tues 6pm @OHCollaborative #Youngstown weather camera"
statusvalue24="KBC KIDZ costumed characters & themed cakes #Youngstown weather camera"
statusvalue25="#makerspace training on tech Tues @OHCollaborative #Youngstown weather camera do it!"
statusvalue26="Helping everybody United Returning Citizens @OHCollaborative #Youngstown weather camera"
statusvalue27="Dream, build, innovate YOUR future @OHCollaborative #Youngstown weather camera"
statusvalue28="Tools, Training, technology innovation @OHCollaborative #Youngstown weather camera"
statusvalue29="opportunity Citizens 2 make their story @OHCollaborative #Youngstown weather camera"
statusvalue30="cooperate, collaborate, innovate, & make @OHCollaborative #Youngstown weather camera"
statusvalue31="tech training will set you free! @OHCollaborative #Youngstown weather camera"
statusvalue32="artist makers hackers designers students @OHCollaborative #Youngstown weather camera"
statusvalue33="THINK BUILD SHARE community center @OHCollaborative #Youngstown weather camera"
statusvalue34="community development tech biz incubator @OHCollaborative #Youngstown weather camera"
statusvalue35="#Innovation improving the quality of life @OHCollaborative #Youngstown weather camera"
statusvalue36="#StartUp #Tech 4 stronger community @OHCollaborative #Youngstown weather camera"
statusvalue37="education is eternal @OHCollaborative #Youngstown weather camera Social Media Jan 6@6pm"
statusvalue38="School ends #education does NOT @OHCollaborative #Youngstown weather camera Tues@6pm"
statusvalue39="Meet make collaborate! @OHCollaborative #Youngstown weather camera WEDS@6pm #3dprinting"
statusvalue40="Build it code it Do it #Makerspace @OHCollaborative #Youngstown weather camera WEDS@6pm"
statusvalue41="@OHCollaborative #Youngstown weather camera women innovators makers,& #startups TUES@6pm"
statusvalue42="@OHCollaborative #Youngstown weather camera #innovation WEDS@6pm #makerspace tools & tech"
statusvalue43="@OHCollaborative #Youngstown weather camera nieghborhood tech & love for the good of all"
statusvalue44="build it #Makerspace it they will come @OHCollaborative #Youngstown weather camera"
statusvalue45="#Entrepreneur #Innovative @OHCollaborative #Youngstown weather camera #Tech Tues@6pm"
statusvalue46="Tues@6pm Jan #Social Media @OHCollaborative #Youngstown #accelerator #events #startups"
statusvalue47="#Tech Tues@6pm @OHCollaborative #Youngstown weather camera #accelerator #events #MARKETING #MEDIA"
statusvalue48="@3dprinterworks #CES2016 booth 73133 @3DFuel stop by see accurate, fast & reliable Creatorbot3d think click print "
statusvalue49="#3dPrinting #innovation #Ohio #Manufacturing Industry @OHCollaborative #Youngstown weather camera"
statusvalue50="#3dPrinting #Manufacturing CreatorBot3D Click Print build @OHCollaborative #Youngstown weather camera"
statusvalue51="#cityscape #SeedsOfHope #GrowthHacking #opendata & civic hacking @OHCollaborative #Youngstown weather camera"
statusvalue52="#cityscape #CarpeDiem #civictech open mesh networks @OHCollaborative #Youngstown weather camera"
statusvalue53="#Coding and Beyond! Using Skills to Make Products @OHCollaborative #Youngstown weather camera"
statusvalue54="#Science #STEM catch sunrise #CarpeDiem community @OHCollaborative #Youngstown weather camera"
statusvalue55="#social $TWTR #training Weds 6pm Small Biz #startup @OHCollaborative #Youngstown weather camera"
statusvalue56="Helping folks help themselves https://www.facebook.com/returningcitizen @OHCollaborative #Youngstown weather camera"


statusList = [statusvalue1, statusvalue2, statusvalue3, statusvalue4, statusvalue5, statusvalue6, statusvalue7, statusvalue8, statusvalue9,statusvalue0,statusvalue11,statusvalue12,statusvalue13, statusvalue14, statusvalue15,statusvalue16,statusvalue17,statusvalue18,statusvalue19,statusvalue20, statusvalue21, statusvalue22, statusvalue23, statusvalue24, statusvalue25, statusvalue26, statusvalue27, statusvalue28,statusvalue29, statusvalue30, statusvalue31,statusvalue32,statusvalue33,statusvalue34, statusvalue35, statusvalue36, statusvalue37, statusvalue38,statusvalue39, statusvalue40,statusvalue41,statusvalue42, statusvalue43, statusvalue44, statusvalue45, statusvalue46, statusvalue47, statusvalue48, statusvalue49, statusvalue50,statusvalue51, statusvalue52, statusvalue53,statusvalue54,statusvalue55, statusvalue56]

statusMax = len(statusList)-1
print ("statusMax=" + str(statusMax))
statusIndex = random.randint(0,statusMax)
print ("statusIndex =" + str(statusIndex))

shoutOuts = ["@Youngstown_Buzz", "@Youngstown_News","@EricWFMJ","@DOWNTOWNYTOWN","@21WFMJNews","@vindicator","@21WFMJNews","@StormTracker21", "@WKBN", "@PapaMuzz", "@JaladahA", "@wfmjtoday", "@SteveDeGenaro", "@ReeseClarett13", "@Dbetras", "@SteveWFMJ","@21WFMJNews","@LindsayWFMJ","@CatulloMeats","@V2Youngstown","@9teen84","@HudsonFasteners","@TEDxYoungstown","@NeuvooYoungsto","@AmericaMakes", "@RepTimRyan", "@SenSherrodBrown", "@robportman", "@YMCAYoungstown", "@youngstownstate", "@YtownSocial", "@MayorMcNally", "@HenryJGomez", "@DrinkUpYtown", "@YoungstownOHrr", "@NeuvooYoungsto", "@VindyVibe", "@dskolnick","@WYTV","@KristenOlmi", "@YWCAYoungstown", "@traceywinbush", "@JackTorry1", "@rmltaylor", "@JohnKasich", "@sobeditor", "@stormingorman67", "@VindySweetwood", "@Vindykalea", "@realboomboom" , "@ROCCOVTWEETS", "@ajjaffe", "@TpartyAnita", "@Nick3BP", "@TimContinenza", "@TheBizJournal", "@MillCreekMetro", "@DinoRoss", "@BarryDyngles", "@DanShaker", "@coffeeandcode", "@JumpStartInc", "@DanielRYemma", "@ybiTweets", "@AvalonDowntown", "@DrinkUpYtown", "@MVRYoungstown", "@JimTressel5", "@MyCityHangouts", "@ImbibeMartini", "@royaloaksbar", "@RyanYts", "@Bravura3D", "@jessietuscano", "@TechBeltSummit", "@matylda","@vitollubomir", "@Talljiveturkey", "@TimSchu", "@Makerspaces_com", "@EscotRodrigues", "@StartupSupaStar", "@Ted_Strickland", "@OHDems", "@AnthonyVSpano", "@ConniePillich", "@JoeSchiavoni", "@JimCosslerYBI", "@colleenlowry", "@OHHouseDems", "@wytv" , "@StambaughAud", "@newsyoungstown", "@PaulWetzlWKBN", "@DanMartinWKBN", "@RyanHalickiWYTV", "@JasonCEarnhart", "@weisslabs_", "@Andrew_Pavlick", "@suzie_Homemaker", "@HackPGH", "@assemblepgh", "@makerfairepgh", "@HackCleveland", "@JillMillerZimon", "@makeshoppgh", "@opencleveland", "@openneo", "@NavadaGroup", "@codigodelsur", "@stuffprof", "@3dprinterworks" , "@intogreengarage", "@MVYPclub", "@StartupGrind" ,"@buildingshow", "@occipital", "@StayStacked_" ,"@3dprinterworks", "@3dersorg", "@Stratasys", "@OHManufacturing", "@RubiconProject", "@zynga", "@AdditiveManufac", "@Jaaaybi", "@Owen_OS", "@edla", "@ChopDawgStudios", "@Mixergy", "@spencerXsays", "@innvenio", "@investFeed", "@AngryCPU", "@Aymard_Ravignan", "@judochopau", "@scott_dellosso", "@MetaMeshLLC", "@PittMesh", "@Camp1Ventures", "@steve_hanson3", "@archiplain", "@QBHerve", "@GetTwitfox", "@ProCrowdfunder", "@HeckaSacto", "@FollowRocket_VC", "@PStation_games", "@VGUGaming", "@spencershane", "@syedhaider613", "@RocketDept", "@bazooka_tech", "@mjavier_angel", "@ChauvenetB", "@PeterAudu", "@founders", "@Nichelle_McCall", "@PaintNiteYNG", "@josek_net", "@Arinutt", "@TheCityClub", "@OpenNEO", "@BikeCLE" , "@codeforamerica" , "@waldojaquith", "@DaveWaldron", "@YNGAirport", "@LWVGY", "@YoungstownNDC", "@GreenYoungstown", "@Ytownstrong", "@EAG_YO" ,"@YtownPlayhouse", "@V2Youngstown", "@YoungstownSlim", "@johnesimon51", "@dwcyo", "@GrowYoungstown", "@YoungstownCAP", "@YoungstownKidd", "@YoungstownLive_", "@YSU_STEM", "@YoungstownHub", "@wxyoungstown", "@Flautomatic", "@SCORE_YSU", "@YoungstownCorp", "@studentofdesign", "@adamearn", "@Youngstown0hio", "@IdoraMarket", "@Youngstown_WX", "@YoungstownOH", "@HackYSU", "@YtownWiki", "@YSUInteractive", "@REBIRTHTODAY", "@StepOutYtown", "@FADsYoungstown", "@youngstownOH330", "@susieb4YO", "@Youngstown411", "@ErikaThomasTV", "@royaloaksbar", "@ytown100", "@greytogreenfest", "@RonPotesta", "@Youngstown_Arts", "@YoungstownMusic", "@MillCreekmetrop", "@4JRutherford", "@YoungstownRock", "@ThirstyDogBeer", "@YoloGrilleTAP", "@djbreezey614", "@VETastingLounge", "@GLBC_Cleveland", "@StemNewsDesk", "@VasilisPasparas", "@CanfieldTechs", "@TechBeltSummit", "@tmj_OH_it", "@JAV2", "@1MillionCupsCLE", "@bfeld", "@KauffmanFDN", "@OnshoreMomentum", "@codemash", "@davemcclure", "@fredwilson", "@cdixon", "@sjonsson", "@BonnieSalm","@HireTechGroup", "@a16z", "@ycombinator", "@TheLab_ms", "@NorTech", "@ClevelandPlus", "@JumpStartInc", "@raytleach", "@techczarcle", "@findyour_level","@findyour_level", "@jthogg", "@iwpgh", "@alphalab", "@EnterprForumPgh", "@AdtileHQ", "@swpgh", "@TechShopPGH", "@pghtech", "@TBJiuJitsu", "@johnrampton", "@Funding_Ideator", "@StartupPro"]

shoutIndex = random.randint(0,len(shoutOuts)-1)
print("  shoutIndex = " +  str(shoutIndex) +" shoutout size= " + str(len(shoutOuts)) )

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

statusupdate=twitter.update_status(status= newStatus,media_ids=image_ids['media_id'])

print(statusupdate)



