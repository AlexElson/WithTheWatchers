import pygame, sys
import os.path
import time
import random
import math
from math import *
import platform
from pygame.locals import *
#import numpy
import psyco
psyco.full()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
fps=60

WIDTH=int(800)
HEIGHT=int(600)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()

#Load Files
sky=pygame.image.load("Images/skyblue.png").convert_alpha()
skyora=pygame.image.load("Images/skyorange.png").convert()
skyblu=pygame.image.load("Images/skyblue.png").convert()
sun=pygame.image.load("Images/sun.png").convert_alpha()
moon=pygame.image.load("Images/moon.png").convert_alpha()
cover=pygame.image.load("Images/cover.png").convert_alpha()
cover2=pygame.image.load("Images/cover2.png").convert_alpha()

tileset=pygame.image.load("Images/isotileset.png").convert_alpha()
tilewall=pygame.image.load("Images/isowall.png").convert_alpha()
misc=pygame.image.load("Images/misc.png").convert()
introblack=pygame.image.load("Images/misc.png").convert_alpha()
miscwhite=pygame.image.load("Images/miscwhite.png").convert()
selectimg=pygame.image.load("Images/select.png").convert_alpha()
selectpathimg=pygame.image.load("Images/selectpath.png").convert_alpha()
selectpath2img=pygame.image.load("Images/selectpath2.png").convert_alpha()
menu_action=pygame.image.load("Images/menu_action.png").convert_alpha()
menu_actiontop=pygame.image.load("Images/menu_actiontop.png").convert_alpha()
menu_stats=pygame.image.load("Images/menu_stats.png").convert_alpha()
menu_stats2=pygame.image.load("Images/menu_stats2.png").convert_alpha()
menu_body=pygame.image.load("Images/menu_body.png").convert_alpha()
actionselectimg=pygame.image.load("Images/actionselectimg.png").convert_alpha()
itemspark=pygame.image.load("Images/itemspark.png").convert_alpha()
staticongray=pygame.image.load("Images/staticongray.png").convert_alpha()
staticonyel=pygame.image.load("Images/staticonyel.png").convert_alpha()
staticonblue=pygame.image.load("Images/staticonblue.png").convert_alpha()
message_item=pygame.image.load("Images/message_item.png").convert_alpha()
bloodimg=pygame.image.load("Images/blood.png").convert_alpha()
bloodline=pygame.image.load("Images/bloodline.png").convert_alpha()
rainpatch=pygame.image.load("Images/rainpatch.png").convert_alpha()
dustpatch=pygame.image.load("Images/dustpatch.png").convert_alpha()
speakeri=pygame.image.load("Images/speaker.png").convert_alpha()
speakerx=pygame.image.load("Images/speakerx.png").convert_alpha()

charwinston=pygame.image.load("Images/charwinston.png").convert_alpha()
charlenna=pygame.image.load("Images/charlenna.png").convert_alpha()
charfloyd=pygame.image.load("Images/charfloyd.png").convert_alpha()
charLucas=pygame.image.load("Images/charlucas.png").convert_alpha()
charelse=pygame.image.load("Images/charelse.png").convert_alpha()
charhurt=pygame.image.load("Images/charhurt.png").convert_alpha()
hurtfloyd=pygame.image.load("Images/hurtfloyd.png").convert_alpha()
hurtlenna=pygame.image.load("Images/hurtlenna.png").convert_alpha()
charally=pygame.image.load("Images/charally.png").convert_alpha()

message=pygame.image.load("Images/message.png").convert_alpha()
message_name=pygame.image.load("Images/message_name.png").convert_alpha()
message_ready=pygame.image.load("Images/message_ready.png").convert_alpha()
message_portrait=pygame.image.load("Images/message_portraits.png").convert_alpha()
option_box=pygame.image.load("Images/option_box.png").convert_alpha()
option_boxlight=pygame.image.load("Images/option_boxlight.png").convert_alpha()

mquit=pygame.image.load("Images/mquit.png").convert_alpha()
mmute=pygame.image.load("Images/mmute.png").convert_alpha()
mnew=pygame.image.load("Images/mnew.png").convert_alpha()
moptions=pygame.image.load("Images/moptions.png").convert_alpha()
mcontinue=pygame.image.load("Images/mcontinue.png").convert_alpha()
mfreebattle=pygame.image.load("Images/mfreebattle.png").convert_alpha()
mfailure=pygame.image.load("Images/mfailure.png").convert_alpha()
mline1=pygame.image.load("Images/mline1.png").convert_alpha()
mline2=pygame.image.load("Images/mline2.png").convert_alpha()
mlucas=pygame.image.load("Images/mlucas.png").convert_alpha()
mfloyd=pygame.image.load("Images/mfloyd.png").convert_alpha()
mlenna=pygame.image.load("Images/mlenna.png").convert_alpha()
mend=pygame.image.load("Images/mend.png").convert_alpha()
menu_levelbottom=pygame.image.load("Images/menu_levelbottom.png").convert_alpha()
menu_levelbottom2=pygame.image.load("Images/menu_levelbottom2.png").convert_alpha()

font = pygame.font.Font("Images/monospaced.ttf", 15)
font2 = pygame.font.Font("Images/arial.ttf", 9)
font3 = pygame.font.Font("Images/arial.ttf", 16)

#Music and Sound
threefour=pygame.mixer.Sound("Music/3444.ogg")
threefour.set_volume(.3)
action=pygame.mixer.Sound("Music/action.ogg")
action.set_volume(.3)
ambient=pygame.mixer.Sound("Music/ambient.ogg")
ambient.set_volume(.5)
calm=pygame.mixer.Sound("Music/calm.ogg")
calm.set_volume(.4)
guitar=pygame.mixer.Sound("Music/guitar.ogg")
guitar.set_volume(.2)
mystery=pygame.mixer.Sound("Music/mystery.ogg")
mystery.set_volume(.45)
ominous=pygame.mixer.Sound("Music/ominous.ogg")
ominous.set_volume(.4)
scary=pygame.mixer.Sound("Music/scary.ogg")
scary.set_volume(.4)
standby=pygame.mixer.Sound("Music/standby.ogg")
standby.set_volume(.45)
crowd=pygame.mixer.Sound("Music/crowd.ogg")
crowd.set_volume(.5)
water=pygame.mixer.Sound("Music/water.ogg")
water.set_volume(.3)
rain=pygame.mixer.Sound("Music/rain.ogg")
rain.set_volume(1)

dialogue=pygame.mixer.Sound("Music/Sound/dialogue.wav")
dialogue.set_volume(.2)
door=pygame.mixer.Sound("Music/Sound/door.wav")
door.set_volume(.17)
fist=pygame.mixer.Sound("Music/Sound/fist.wav")
fist.set_volume(.35)
punch=pygame.mixer.Sound("Music/Sound/punch.wav")
punch.set_volume(.35)
shatter=pygame.mixer.Sound("Music/Sound/shatter.wav")
shatter.set_volume(.1)
slash=pygame.mixer.Sound("Music/Sound/slash.wav")
slash.set_volume(.06)
thud=pygame.mixer.Sound("Music/Sound/thud.wav")
thud.set_volume(.15)
select=pygame.mixer.Sound("Music/Sound/select.wav")
select.set_volume(.3)


#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
GRAY=(160,160,160)
TAN=(200,190,110)

#Variables
right=0
left=0
up=0
down=0
selectx=0
selecty=0
camerax=0
cameray=0
rotDir=0
delay=0
delay2=0
delay2b=0
delaysit=10
thrown=""
throwndir=""
throwx=0.0
throwy=0.0

#Action Menu Variables
actionmenu=0
actionselect=0
am_actions=0
movedchar=0
movedalready=0
actionalready=0
turn=0
tutorialmove=0
tutorialhurt=0
tutorialpick=0
tutorialthrow=0
tutorialarms=0

#Menu Variables
mainmenu=1
menuselect=0
menuy=0
nextLevelMenu=0
pressed=0
rightMouse=0
leftMouse=0
gotoColor=[]
goingColor=[]
for n in range(3):
    gotoColor.append(n); gotoColor[n]=255
    goingColor.append(n); goingColor[n]=255

si=36 #Tile Size
fade=255.0
mapArea=0 #Map (0-large area , 1-zoom in)
zooming=0
waterWave=0.0
waterWaveMax=20.0

#Tiles
lvlW=10
lvlH=10
maxz=HEIGHT*2
tilex=[]
tiley=[]
tilez=[]
wallx=[]
wally=[]
walldir=[]
tilefill=[]

#Level Variables
level=""
movie=1
zoominlevel=1

#Blood Variables
bloodsize=[]
bloodlx=[]
bloodly=[]
bloodvarx=[]
bloodvary=[]
bloodlen=[]
bloodmax=[]
for n in range(11):
    bloodsize.append(n); bloodsize[n]=0
    bloodlx.append(n); bloodlx[n]=0
    bloodly.append(n); bloodly[n]=0
    bloodvarx.append(n); bloodvarx[n]=0
    bloodvary.append(n); bloodvary[n]=0
    bloodlen.append(n); bloodlen[n]=0.0
    bloodmax.append(n); bloodmax[n]=0

#Party Variables
gainparty=""
fakegainparty=""
party=[]
partyselect=[]
partyblood=[]
partyartery=[]
partypara=[]
partyforehead=[]
partyeyes=[]
partynose=[]
partymouth=[]
partyjaw=[]
partytemple=[]
partyneck=[]
partybrain=[]
partyskull=[]
partychest=[]
partychest2=[]
partylungs=[]
partyheart=[]
partyspine=[]
partyback=[]
partygut=[]
partygut2=[]
partyrightarm=[]
partyrighthand=[]
partyleftarm=[]
partylefthand=[]
partyrightleg=[]
partyleftleg=[]
partyheld=[]
partyexp=[]
partylvl=[]
partypierces=[]
partyblunt=[]
partyunarmed=[]
partydefense=[]
partythrowsk=[]
for n in range(21):
    party.append(n); party[n]=""
    partyselect.append(n); partyselect[n]=0
    partyblood.append(n); partyblood[n]=100.0
    partyartery.append(n); partyartery[n]=0
    partypara.append(n); partypara[n]=0
    partyforehead.append(n); partyforehead[n]=0
    partyeyes.append(n); partyeyes[n]=0
    partynose.append(n); partynose[n]=0
    partymouth.append(n); partymouth[n]=0
    partyjaw.append(n); partyjaw[n]=0
    partytemple.append(n); partytemple[n]=0
    partyneck.append(n); partyneck[n]=0
    partybrain.append(n); partybrain[n]=0
    partyskull.append(n); partyskull[n]=0
    partychest.append(n); partychest[n]=0
    partychest2.append(n); partychest2[n]=0
    partylungs.append(n); partylungs[n]=0
    partyheart.append(n); partyheart[n]=0
    partyspine.append(n); partyspine[n]=0
    partyback.append(n); partyback[n]=0
    partygut.append(n); partygut[n]=0
    partygut2.append(n); partygut2[n]=0
    partyrightarm.append(n); partyrightarm[n]=0
    partyrighthand.append(n); partyrighthand[n]=0
    partyleftarm.append(n); partyleftarm[n]=0
    partylefthand.append(n); partylefthand[n]=0
    partyrightleg.append(n); partyrightleg[n]=0
    partyleftleg.append(n); partyleftleg[n]=0
    partyheld.append(n); partyheld[n]=""
    partyexp.append(n); partyexp[n]=0
    partylvl.append(n); partylvl[n]=0
    partypierces.append(n); partypierces[n]=0
    partyblunt.append(n); partyblunt[n]=0
    partyunarmed.append(n); partyunarmed[n]=0
    partydefense.append(n); partydefense[n]=0
    partythrowsk.append(n); partythrowsk[n]=0
party[0]="Winston"; partyheld[0]="Knife"; partydefense[0]=0; partylvl[0]=7
party[1]="Floyd"; partyheld[1]="Knife"
##party[2]="Floyd"; partyheld[2]="Hammer"
party[3]="Kurt"; partyheld[3]="Knife"; partyblood[3]=80; partychest[3]=2; partylungs[3]=1; partyjaw[3]=3; partyforehead[3]=1
partyleftleg[3]=2; partypierces[3]=20; partydefense[3]=3; partythrowsk[3]=1; partylvl[3]=6
party[4]="Frederick"; partyheld[4]="Wrench"; partyblunt[4]=20
party[5]="Ruth"; partyheld[5]="Med Kit"
##party[6]="Lucas"; partyheld[6]="Wrench"
party[7]="Adam";# partyheld[5]="Shiv"
party[8]="Evelyn";# partyheld[6]="Hammer"
party[9]="Matthew";# partyheld[5]="Med Kit"
party[10]="Dinah"
party[2]="Gambler"; partyheld[2]="Dice"

def loadParty(nn):
    for n in range(21):
        if (party[n]!="" and nn==n):
            npcblood[nn]=partyblood[n]
            npcartery[nn]=partyartery[n]
            npcblood[nn]=partyblood[n]
            npcartery[nn]=partyartery[n]
            npcpara[nn]=partypara[n]
            npcforehead[nn]=partyforehead[n]
            npceyes[nn]=partyeyes[n]
            npcnose[nn]=partynose[n]
            npcmouth[nn]=partymouth[n]
            npcjaw[nn]=partyjaw[n]
            npctemple[nn]=partytemple[n]
            npcneck[nn]=partyneck[n]
            npcbrain[nn]=partybrain[n]
            npcskull[nn]=partyskull[n]
            npcchest[nn]=partychest[n]
            npcchest2[nn]=partychest2[n]
            npclungs[nn]=partylungs[n]
            npcheart[nn]=partyheart[n]
            npcspine[nn]=partyspine[n]
            npcback[nn]=partyback[n]
            npcgut[nn]=partygut[n]
            npcgut2[nn]=partygut2[n]
            npcrightarm[nn]=partyrightarm[n]
            npcrighthand[nn]=partyrighthand[n]
            npcleftarm[nn]=partyleftarm[n]
            npclefthand[nn]=partylefthand[n]
            npcrightleg[nn]=partyrightleg[n]
            npcleftleg[nn]=partyleftleg[n]
            npcheld[nn]=partyheld[n]
            npcexp[nn]=partyexp[n]
            npclvl[nn]=partylvl[n]
            
            npcpierces[nn]=partypierces[n]
            npcblunt[nn]=partyblunt[n]
            npcunarmed[nn]=partyunarmed[n]
            npcdefense[nn]=partydefense[n]
            npcthrowsk[nn]=partythrowsk[n]

placeside=1
def loadPartyMembers(nn):
    global placeside
    if (level=="Friends" and lucastwo==0): return
    if (level=="Summit" or level=="Wake" or level=="Robot" or level=="Truth"): return
    for n in range(21):
        if (partyselect[n]==1 and party[n]!="" and party[n]!="Winston" and party[n]!="Floyd" and party[n]!="Lenna" and party[n]!="Lucas"):
            npcside[nn]=party[n]
            for m in range(11):
                if (npcside[m]=="Winston" and level!="Memory" and level!="Jerry2"):
                    npcx[nn]=npcx[m]+placeside; npcy[nn]=npcy[m]; placeside+=1
                    npcdx[nn]=npcx[nn]; npcdy[nn]=npcy[nn]
                    npcdir[nn]=npcdir[m]
                    break
                if (npcside[m]=="Winston" and (level=="Memory" or level=="Jerry2")):
                    npcx[nn]=npcx[m]; npcy[nn]=npcy[m]+placeside; placeside+=1
                    npcdx[nn]=npcx[nn]; npcdy[nn]=npcy[nn]
                    npcdir[nn]=npcdir[m]
                    break
                if (npcside[m]=="Floyd" and level=="Dinah"):
                    npcx[nn]=npcx[m]; npcy[nn]=npcy[m]+placeside; placeside+=1
                    npcdx[nn]=npcx[nn]; npcdy[nn]=npcy[nn]
                    npcdir[nn]=npcdir[m]
                    break                    
            npccontrol[nn]=1
            npc[nn]=1
            partyselect[n]=2
            break
            
def loadPartyInLevel(nn):
    for n in range(21):
        if (party[n]!="" and party[n]==npcside[nn]):
            npcblood[nn]=partyblood[n]
            npcartery[nn]=partyartery[n]
            npcblood[nn]=partyblood[n]
            npcartery[nn]=partyartery[n]
            npcpara[nn]=partypara[n]
            npcforehead[nn]=partyforehead[n]
            npceyes[nn]=partyeyes[n]
            npcnose[nn]=partynose[n]
            npcmouth[nn]=partymouth[n]
            npcjaw[nn]=partyjaw[n]
            npctemple[nn]=partytemple[n]
            npcneck[nn]=partyneck[n]
            npcbrain[nn]=partybrain[n]
            npcskull[nn]=partyskull[n]
            npcchest[nn]=partychest[n]
            npcchest2[nn]=partychest2[n]
            npclungs[nn]=partylungs[n]
            npcheart[nn]=partyheart[n]
            npcspine[nn]=partyspine[n]
            npcback[nn]=partyback[n]
            npcgut[nn]=partygut[n]
            npcgut2[nn]=partygut2[n]
            npcrightarm[nn]=partyrightarm[n]
            npcrighthand[nn]=partyrighthand[n]
            npcleftarm[nn]=partyleftarm[n]
            npclefthand[nn]=partylefthand[n]
            npcrightleg[nn]=partyrightleg[n]
            npcleftleg[nn]=partyleftleg[n]
            npcheld[nn]=partyheld[n]
            npcexp[nn]=partyexp[n]
            npclvl[nn]=partylvl[n]
            npcpierces[nn]=partypierces[n]
            npcblunt[nn]=partyblunt[n]
            npcunarmed[nn]=partyunarmed[n]
            npcdefense[nn]=partydefense[n]
            npcthrowsk[nn]=partythrowsk[n]

def healParty():
    for nn in range(21):
        if (party[nn]!=""): #and (party[nn]=="Winston" or party[nn]=="Floyd" or party[nn]=="Lenna" or party[nn]=="Lucas")):
            partyblood[nn]=100.0
            partyartery[nn]=0
            partyartery[nn]=0
            partypara[nn]=0
            partyforehead[nn]=0
            partyeyes[nn]=0
            partynose[nn]=0
            partymouth[nn]=0
            partyjaw[nn]=0
            partytemple[nn]=0
            partyneck[nn]=0
            partybrain[nn]=0
            partyskull[nn]=0
            partychest[nn]=0
            partychest2[nn]=0
            partylungs[nn]=0
            partyheart[nn]=0
            partyspine[nn]=0
            partyback[nn]=0
            partygut[nn]=0
            partygut2[nn]=0
            partyrightarm[nn]=0
            partyrighthand[nn]=0
            partyleftarm[nn]=0
            partylefthand[nn]=0
            partyrightleg[nn]=0
            partyleftleg[nn]=0

#NPCs
npcframe=0
npcframetick=10
npc=[]
npcx=[]
npcy=[]
npcz=[]
npcdx=[]
npcdy=[]
npcwalk=[]
npcwalkdir=[]
npcwalkspeed=[]
npcwalkspeedc=[]
npcani=[]
npcaniframe=[]
npcdir=[]
npcside=[]
npccontrol=[]
npcturn=[]
npclist=[]
npclist2=[]
whogoes=0
npcheld=[]
npcblood=[] #Atacking NPCs
npcbleeding=[]
npcartery=[]
npcinternal=[]
npcbruise=[]
npcpain=[]
npcoxygen=[]
npcdizzy=[]
npcbreath=[]
npcfainted=[]
npcpara=[]
npcdead=[]
npcstrangle=[]
npcstrangling=[]
npcrunaway=[]
npcknocked=[]
npcstun=[]
npcforehead=[] #Head Variables
npceyes=[]
npcnose=[]
npcnose2=[]
npcmouth=[]
npcjaw=[]
npctemple=[]
npcthroat=[]
npcneck=[]
npcbrain=[]
npcskull=[]
npcchest=[] #Torso
npcchest2=[]
npclungs=[]
npcheart=[]
npcspine=[]
npcback=[]
npcgut=[]
npcgut2=[]
npcrightarm=[] #Arms
npcrighthand=[]
npcleftarm=[]
npclefthand=[]
npcrightleg=[] #Legs
npcleftleg=[]
npcexp=[]
npclvl=[]
npcpierces=[]
npcblunt=[]
npcunarmed=[]
npcdefense=[]
npcthrowsk=[]
for n in range(11):
    npc.append(n); npc[n]=0
    npcx.append(n); npcx[n]=0.0
    npcy.append(n); npcy[n]=0.0
    npcz.append(n); npcz[n]=0.0
    npcdx.append(n); npcdx[n]=0.0
    npcdy.append(n); npcdy[n]=0.0
    npcwalk.append(n); npcwalk[n]=0.0
    npcwalkdir.append(n); npcwalkdir[n]=-1
    npcwalkspeed.append(n); npcwalkspeed[n]=0.05
    npcwalkspeedc.append(n); npcwalkspeedc[n]=0.0
    npcani.append(n); npcani[n]=""
    npcaniframe.append(n); npcaniframe[n]=0.0
    npcdir.append(n); npcdir[n]=0
    npcside.append(n); npcside[n]=""
    npccontrol.append(n); npccontrol[n]=0
    npcturn.append(n); npcturn[n]=0
    npclist.append(n); npclist[n]=-1
    npclist2.append(n); npclist2[n]=""
    npcheld.append(n); npcheld[n]=""
    npcblood.append(n); npcblood[n]=100.0 #Attacking NPCs
    npcbleeding.append(n); npcbleeding[n]=0
    npcartery.append(n); npcartery[n]=0
    npcinternal.append(n); npcinternal[n]=0
    npcpain.append(n); npcpain[n]=0
    npcbruise.append(n); npcbruise[n]=0
    npcoxygen.append(n); npcoxygen[n]=100.0
    npcdizzy.append(n); npcdizzy[n]=0
    npcbreath.append(n); npcbreath[n]=0
    npcfainted.append(n); npcfainted[n]=0
    npcpara.append(n); npcpara[n]=0
    npcdead.append(n); npcdead[n]=0
    npcstrangle.append(n); npcstrangle[n]=0
    npcstrangling.append(n); npcstrangling[n]=-1
    npcrunaway.append(n); npcrunaway[n]=0
    npcknocked.append(n); npcknocked[n]=0
    npcstun.append(n); npcstun[n]=0
    npcforehead.append(n); npcforehead[n]=0 #Head Variables
    npceyes.append(n); npceyes[n]=0
    npcnose.append(n); npcnose[n]=0
    npcnose2.append(n); npcnose2[n]=0
    npcmouth.append(n); npcmouth[n]=0
    npcjaw.append(n); npcjaw[n]=0
    npctemple.append(n); npctemple[n]=0
    npcthroat.append(n); npcthroat[n]=0
    npcneck.append(n); npcneck[n]=0
    npcbrain.append(n); npcbrain[n]=0
    npcskull.append(n); npcskull[n]=0
    npcchest.append(n); npcchest[n]=0 #Torso
    npcchest2.append(n); npcchest2[n]=0
    npclungs.append(n); npclungs[n]=0
    npcheart.append(n); npcheart[n]=0
    npcspine.append(n); npcspine[n]=0
    npcback.append(n); npcback[n]=0
    npcgut.append(n); npcgut[n]=0
    npcgut2.append(n); npcgut2[n]=0
    npcrightarm.append(n); npcrightarm[n]=0 #Arms
    npcrighthand.append(n); npcrighthand[n]=0
    npcleftarm.append(n); npcleftarm[n]=0
    npclefthand.append(n); npclefthand[n]=0
    npcrightleg.append(n); npcrightleg[n]=0 #Legs
    npcleftleg.append(n); npcleftleg[n]=0
    npcexp.append(n); npcexp[n]=0
    npclvl.append(n); npclvl[n]=0
    npcpierces.append(n); npcpierces[n]=0
    npcblunt.append(n); npcblunt[n]=0
    npcunarmed.append(n); npcunarmed[n]=0
    npcdefense.append(n); npcdefense[n]=0
    npcthrowsk.append(n); npcthrowsk[n]=0

def resetNPCs():
    global ruth, extra, twins
    if (level=="" or level=="LevelMenu"):
        for n in range(11): #Add in the NPCs for the Menu
            if (party[n]!=""):
                if (npcside[n]=="Ruth" and npcdead[n]==1 and ruth!=-1): ruth=-1; extra=1 #Certain Characters
                if (npcside[n]=="Adam" and npcdead[n]==1 and twins<=1): twins=-1; extra=1 #Certain Characters
                if (npcside[n]=="Evelyn" and npcdead[n]==1 and twins<=1): twins=-1; extra=1 #Certain Characters
                if (npcside[n]=="Adam" and npcdead[n]==1 and twins>=2): extra=1 #Certain Characters
                if (npcside[n]=="Evelyn" and npcdead[n]==1 and twins>=2): extra=1 #Certain Characters
                if (npcside[n]=="Kurt" and npcdead[n]==1 and extra==0): extra=1 #Certain Characters
                if (npcside[n]=="Frederick" and npcdead[n]==1 and extra==0): extra=1 #Certain Characters
                if (npcside[n]=="Matthew" and npcdead[n]==1 and extra==0): extra=1 #Certain Characters
                if (npcside[n]=="Gambler" and npcdead[n]==1 and extra==0): twins=-1 #Certain Characters
    for n in range(11):
        for nn in range(21):
            if (npcside[n]==party[nn] and npcside[n]!="" and failurepart!=part and npcdead[n]==1):
                party[nn]=""; partyselect[nn]=0
                partyblood[nn]=100.0
                partyartery[nn]=0
                partyartery[nn]=0
                partypara[nn]=0
                partyforehead[nn]=0
                partyeyes[nn]=0
                partynose[nn]=0
                partymouth[nn]=0
                partyjaw[nn]=0
                partytemple[nn]=0
                partyneck[nn]=0
                partybrain[nn]=0
                partyskull[nn]=0
                partychest[nn]=0
                partychest2[nn]=0
                partylungs[nn]=0
                partyheart[nn]=0
                partyspine[nn]=0
                partyback[nn]=0
                partygut[nn]=0
                partygut2[nn]=0
                partyrightarm[nn]=0
                partyrighthand[nn]=0
                partyleftarm[nn]=0
                partylefthand[nn]=0
                partyrightleg[nn]=0
                partyleftleg[nn]=0
                partyexp[nn]=0
                partylvl[nn]=0
                partypierces[nn]=0
                partyblunt[nn]=0
                partyunarmed[nn]=0
                partydefense[nn]=0
                partythrowsk[nn]=0
                partyheld[nn]=""
            if (npcside[n]==party[nn] and npcside[n]!="" and failurepart!=part and (difficulty==1 or (difficulty==0 and npcside[n]!="Winston" and npcside[n]!="Lenna" and npcside[n]!="Floyd" and npcside[n]!="Lucas"))): #Change
                partyblood[nn]=npcblood[n]
                if (partyblood[nn]<50): partyblood[nn]=50
                partyartery[nn]=npcartery[n]
                partyblood[nn]=npcblood[n]
                partyartery[nn]=npcartery[n]
                partypara[nn]=npcpara[n]
                partyforehead[nn]=npcforehead[n]
                partyeyes[nn]=npceyes[n]
                partynose[nn]=npcnose[n]
                partymouth[nn]=npcmouth[n]
                partyjaw[nn]=npcjaw[n]
                partytemple[nn]=npctemple[n]
                partyneck[nn]=npcneck[n]
                partybrain[nn]=npcbrain[n]
                partyskull[nn]=npcskull[n]
                partychest[nn]=npcchest[n]
                partychest2[nn]=npcchest2[n]
                partylungs[nn]=npclungs[n]
                if (partylungs[nn]>=2): partylungs[nn]=1
                partyheart[nn]=npcheart[n]
                if (partyheart[nn]>=2): partyheart[nn]=1
                partyspine[nn]=npcspine[n]
                partyback[nn]=npcback[n]
                partygut[nn]=npcgut[n]
                partygut2[nn]=npcgut2[n]
                partyrightarm[nn]=npcrightarm[n]
                partyrighthand[nn]=npcrighthand[n]
                partyleftarm[nn]=npcleftarm[n]
                partylefthand[nn]=npclefthand[n]
                partyrightleg[nn]=npcrightleg[n]
                partyleftleg[nn]=npcleftleg[n]
            if (npcside[n]==party[nn] and npcside[n]!="" and failurepart!=part):
                partyheld[nn]=npcheld[n]
                partyexp[nn]=npcexp[n]
                partylvl[nn]=npclvl[n]
                partypierces[nn]=npcpierces[n]
                partyblunt[nn]=npcblunt[n]
                partyunarmed[nn]=npcunarmed[n]
                partydefense[nn]=npcdefense[n]
                partythrowsk[nn]=npcthrowsk[n]
        npc[n]=0
        npcx[n]=0.0
        npcy[n]=0.0
        npcz[n]=0.0
        npcdx[n]=0.0
        npcdy[n]=0.0
        npcwalk[n]=0.0
        npcwalkdir[n]=-1
        npcwalkspeed[n]=0.05
        npcwalkspeedc[n]=0.0
        npcani[n]=""
        npcaniframe[n]=0.0
        npcdir[n]=0
        npcside[n]=""
        npccontrol[n]=0
        npcturn[n]=0
        npclist[n]=-1
        npclist2[n]=""
        npcheld[n]=""
        npcblood[n]=100.0 #Attacking NPCs
        npcbleeding[n]=0
        npcartery[n]=0
        npcinternal[n]=0
        npcbruise[n]=0
        npcpain[n]=0
        npcoxygen[n]=100.0
        npcdizzy[n]=0
        npcbreath[n]=0
        npcfainted[n]=0
        npcpara[n]=0
        npcdead[n]=0
        npcstrangle[n]=0
        npcstrangling[n]=-1
        npcrunaway[n]=0
        npcknocked[n]=0
        npcstun[n]=0
        npcforehead[n]=0 #Head Variables
        npceyes[n]=0
        npcnose[n]=0
        npcnose2[n]=0
        npcmouth[n]=0
        npcjaw[n]=0
        npctemple[n]=0
        npcthroat[n]=0
        npcneck[n]=0
        npcbrain[n]=0
        npcskull[n]=0
        npcchest[n]=0 #Torso
        npcchest2[n]=0
        npclungs[n]=0
        npcheart[n]=0
        npcspine[n]=0
        npcback[n]=0
        npcgut[n]=0
        npcgut2[n]=0
        npcrightarm[n]=0 #Arms
        npcrighthand[n]=0
        npcleftarm[n]=0
        npclefthand[n]=0
        npcrightleg[n]=0 #Legs
        npcleftleg[n]=0
        bloodsize[n]=0
        bloodlen[n]=0
        npcexp[n]=0
        npclvl[n]=0
        npcpierces[n]=0
        npcblunt[n]=0
        npcunarmed[n]=0
        npcdefense[n]=0
        npcthrowsk[n]=0
        if (endreset==1):
            for nn in range(21):
                party[nn]=""; partyselect[nn]=0
                partyblood[nn]=100.0
                partyartery[nn]=0
                partyartery[nn]=0
                partypara[nn]=0
                partyforehead[nn]=0
                partyeyes[nn]=0
                partynose[nn]=0
                partymouth[nn]=0
                partyjaw[nn]=0
                partytemple[nn]=0
                partyneck[nn]=0
                partybrain[nn]=0
                partyskull[nn]=0
                partychest[nn]=0
                partychest2[nn]=0
                partylungs[nn]=0
                partyheart[nn]=0
                partyspine[nn]=0
                partyback[nn]=0
                partygut[nn]=0
                partygut2[nn]=0
                partyrightarm[nn]=0
                partyrighthand[nn]=0
                partyleftarm[nn]=0
                partylefthand[nn]=0
                partyrightleg[nn]=0
                partyleftleg[nn]=0
                partyexp[nn]=0
                partylvl[nn]=0
                partypierces[nn]=0
                partyblunt[nn]=0
                partyunarmed[nn]=0
                partydefense[nn]=0
                partythrowsk[nn]=0
                partyheld[nn]=""
            party[0]="Winston"

#Items
item=[]
itemx=[]
itemy=[]
for n in range(19):
    item.append(n); item[n]=""
    itemx.append(n); itemx[n]=0
    itemy.append(n); itemy[n]=0

#Dialogue and Chat
letters1=0.0; letters2=0.0; letters3=0.0
part=-1; oldpart=part; nextDialogue=1; textspeed=10.5
arrowy=0; arrowdy=-1
chat1=[]
chat2=[]
chat3=[]
speaker=[]
choice1=[]
choice2=[]
choice3=[]
choice1go=[]
choice2go=[]
choice3go=[]
gotopart=[]
movenpc=[]
movenpcx=[]
movenpcy=[]
movespeed=[]
createnpc=[]
partdelay=[]
musicplay=[]
controlChar=0
changelevelpart=0
changelevelto=""
for n in range(215):
    chat1.append(n); chat1[n]=""
    chat2.append(n); chat2[n]=""
    chat3.append(n); chat3[n]=""
    speaker.append(n); speaker[n]=""
    choice1.append(n); choice1[n]=""
    choice2.append(n); choice2[n]=""
    choice3.append(n); choice3[n]=""
    choice1go.append(n); choice1go[n]=0
    choice2go.append(n); choice2go[n]=0
    choice3go.append(n); choice3go[n]=0
    gotopart.append(n); gotopart[n]=-1
    movenpc.append(n); movenpc[n]=-1
    movenpcx.append(n); movenpcx[n]=0.0
    movenpcy.append(n); movenpcy[n]=0.0
    movespeed.append(n); movespeed[n]=0.05
    createnpc.append(n); createnpc[n]=0
    partdelay.append(n); partdelay[n]=0
    musicplay.append(n); musicplay[n]=""
def resetDialogue():
    global changelevelpart, changelevelto
    changelevelpart=0
    changelevelto=""
    for n in range(215):
        chat1[n]=""
        chat2[n]=""
        chat3[n]=""
        speaker[n]=""
        choice1.append(n); choice1[n]=""
        choice2.append(n); choice2[n]=""
        choice3.append(n); choice3[n]=""
        choice1go.append(n); choice1go[n]=0
        choice2go.append(n); choice2go[n]=0
        choice3go.append(n); choice3go[n]=0
        gotopart.append(n); gotopart[n]=-1
        movenpc[n]=-1
        movenpcx[n]=0.0
        movenpcy[n]=0.0
        movespeed[n]=0.05
        createnpc[n]=0
        partdelay[n]=0
    
def loseItems():
    for n in range(11):
        npcheld[n]=""
        partyheld[n]=""

cansave=0
def loadLevel():
    global level, load, lvlW, lvlH, selectx, selecty, camerax, cameray, cansave
    global tilex, tiley, tilez, wallx, wally, walldir, delay, part, once, whogoes

    tilex=[]
    tiley=[]
    tilez=[]
    wallx=[]
    wally=[]
    walldir=[]

    if (level=="" or level=="LevelMenu"):
        selectx=4; selecty=2
        if (once==1 and gainparty!=""): #Add in Party NPC once
            if (gainparty!="Adam and Evelyn" and gainparty!="Madison and Robot"):
                for n in range(21):
                    if (party[n]==""):
                        party[n]=gainparty; once=0
                        break
            if (gainparty=="Adam and Evelyn"):
                for m in range(2):
                    for n in range(21):
                        if (party[n]==""):
                            if (m==0): party[n]="Adam"; once=0
                            if (m==1): party[n]="Evelyn"; once=0
                            break
            if (gainparty=="Madison and Robot"):
                for m in range(2):
                    for n in range(21):
                        if (party[n]==""):
                            if (m==0): party[n]="Madison"; once=0
                            if (m==1): party[n]="Robot"; once=0
                            break
    resetNPCs()
    if ((level=="" or level=="LevelMenu") and day!=1 and cansave==1):
        saveGame()
        cansave=0
    story()
    createStats()
    for nn in range(11):
        loadPartyInLevel(nn)
    if (level=="Kurt"): npcheld[0]="Scissors" #Add Status Based on Level
    whogoes=0
    
    delay=1
    part=0
    
    load=open("Levels/"+level+".txt","r")
    lvlW=int(load.readline())
    lvlH=int(load.readline())
    for n in range(lvlW*lvlH):
        tilex.append(n); tilex[n]=0
        tiley.append(n); tiley[n]=0
        tilez.append(n); tilez[n]=0.0
        wallx.append(n); wallx[n]=0
        wally.append(n); wally[n]=0
        walldir.append(n); walldir[n]=0
        tilefill.append(n); tilefill[n]=0
    level2=load.readline()
    w=0
    for n in range(lvlW*lvlH):
        for times in range(5):
            t=0
            for nn in level2:
                t=t+1
                if (nn=="%"):
                    cut=level2[:t-1]
                    if (times==0): tilex[n]=int(cut)
                    if (times==1): tiley[n]=int(cut)
                    if (times==2): wallx[n]=int(cut)
                    if (times==3): wally[n]=int(cut)
                    if (times==4): walldir[n]=int(cut)
                    level2=level2[t:]
                    break
    load.close()

def createStats():
    p=0; b=0; u=0; t=0; d=0; l=0
    ap=0; ab=0; au=0; at=0; ad=0; al=0
    count=0
    for m in range(21): #count through party stats
        if (party[m]!="" and partylvl[m]>partylvl[0]-8):
            if (partypierces[m]>p): p=partypierces[m]
            if (partyblunt[m]>b): b=partyblunt[m]
            if (partyunarmed[m]>u): u=partyunarmed[m]
            if (partythrowsk[m]>t): t=partythrowsk[m]
            if (partydefense[m]>d): d=partydefense[m]
            if (partylvl[m]>l): l=partylvl[m]
            ap=ap+partypierces[m]
            ab=ab+partyblunt[m]
            au=au+partyunarmed[m]
            at=at+partythrowsk[m]
            ad=ad+partydefense[m]
            al=al+partylvl[m]
            count=count+1
    if (count==0): count=1
    for n in range(11):
        a=0
        #if (npcside[n]!="Floyd" and npcside[n]!="Lenna" and npcside[n]!="Winston" and npcside[n]!="Lucas"):
        if (npcside[n]!="Winston"):
            if (npclvl[n]<=0):
                npcpierces[n]=int(al/(count+1))+random.randint(-2,1)
                npcblunt[n]=int(al/(count+1))+random.randint(-2,1)
                npcunarmed[n]=int(al/(count+1))+random.randint(-2,2)
                npcdefense[n]=int(al/(count+1))+random.randint(-2,1)
                #if (npccontrol[n]==0 and day>=18): npcdefense[n]=int(al/(count))+random.randint(3,4)
                npcthrowsk[n]=int(al/(count+1))+random.randint(-2,2)
                npclvl[n]=int(al/count)+random.randint(0,3)
                if (npclvl[n]<0): npclvl[n]=0
                if (npcheld[n]=="Knife" or npcheld[n]=="Shiv" or npcheld[n]=="Glass"): npcpierces[n]=int(npcpierces[n]*2)
                if (npcheld[n]=="Hammer" or npcheld[n]=="Wrench" or npcheld[n]=="Baton"): npcblunt[n]=int(npcblunt[n]*2)
                if (npcheld[n]=="Bottle"): npcblunt[n]=int(npcblunt[n]*1.8); npcpierces[n]=int(npcpierces[n]*1.8)
                if (npcheld[n]=="Cards"): npcthrowsk[n]=int(npcthrowsk[n]*2)
                if (npcheld[n]=="" and npcside[n]!="Floyd" and npcside[n]!="Lenna" and npcside[n]!="Lucas"): npcunarmed[n]=int(npcunarmed[n]*2)
        if (npcside[n]=="Big Brute"): npcpierces[n]=15; npclvl[n]=12; npcdefense[n]=17
        #if (npcside[n]=="Adam"): npcpierces[n]=14; #a=1
        #if (npcside[n]=="Evelyn"): npcblunt[n]=14; #a=1
        if (npcside[n]=="Dinah"): npcunarmed[n]=14; #a=1
        if (npcside[n]=="Matthew"): npcdefense[n]=npcdefense[n]*2; #a=1
        if (npcside[n]=="Robot"): npcunarmed[n]=12; npcdefense[n]=16; npcblunt[n]=0; npcpierces[n]=0; npcthrowsk[n]=0
        if (npcside[n]=="Gambler"): npcthrowsk[n]=npcthrowsk[n]*2
        if (level=="Friends"):
            if (npcside[n]=="Floyd"):
                npcpierces[n]=16; npcblunt[n]=10; npclvl[n]=20; npcdefense[n]=16; npcthrowsk[n]=18; npcunarmed[n]=20
            if (npcside[n]=="Lenna"):
                npcpierces[n]=8; npcblunt[n]=14; npclvl[n]=15; npcdefense[n]=8; npcthrowsk[n]=9; npcunarmed[n]=16
        if (level=="Escape"):
            if (npccontrol[n]==0):
                npcpierces[n]+=2; npcblunt[n]+=2; npcunarmed[n]+=5; npcdefense[n]+=2; npcthrowsk[n]+=2; npclvl[n]+=3
            if (npcside[n]=="Commander"):
                npcpierces[n]=20; npcblunt[n]=20; npclvl[n]=20; npcdefense[n]=20; npcthrowsk[n]=20; npcunarmed[n]=20
        if (level=="Summit"):
            if (npcside[n]=="Host"):
                npclvl[n]=18
                npcdefense[n]=20
        if (level=="Speechless"):
            if (npcside[n]=="Lenna"):
                npcpierces[n]=8; npcblunt[n]=16; npclvl[n]=16; npcdefense[n]=20; npcthrowsk[n]=9; npcunarmed[n]=20
        if (level=="Unity"):
            if (npccontrol[n]==0):
                npcpierces[n]+=2; npcblunt[n]+=2; npcunarmed[n]+=5; npcdefense[n]+=2; npcthrowsk[n]+=2; npclvl[n]+=3
            if (npcside[n]=="Sanders"):
                npcpierces[n]=20; npcblunt[n]=20; npclvl[n]=20; npcdefense[n]=20; npcthrowsk[n]=20; npcunarmed[n]=20
        if (level=="Science"):
            if (npccontrol[n]==0):
                npcpierces[n]+=2; npcblunt[n]+=2; npcunarmed[n]+=5; npcdefense[n]+=2; npcthrowsk[n]+=2; npclvl[n]+=3
        if (a==1 and npcside[n]!="Robot"): #For Recruitable Characters
            npclvl[n]=int(al/count)+random.randint(1,2)
            npcpierces[n]+=int(al/count)+random.randint(-1,1)
            npcblunt[n]+=int(al/count)+random.randint(-1,1)
            if (npcside[n]!="Dinah"):
                npcunarmed[n]+=int(al/count)+random.randint(-1,1)
            npcdefense[n]+=int(al/count)+random.randint(-1,1)
            npcthrowsk[n]+=int(al/count)+random.randint(-1,1)
        if (npcpierces[n]<0): npcpierces[n]=0
        if (npcpierces[n]>20): npcpierces[n]=20
        if (npcblunt[n]<0): npcblunt[n]=0
        if (npcblunt[n]>20): npcblunt[n]=20
        if (npcunarmed[n]<0): npcunarmed[n]=0
        if (npcunarmed[n]>20): npcunarmed[n]=20
        if (npcdefense[n]<0): npcdefense[n]=0
        if (npcdefense[n]>20): npcdefense[n]=20
        if (npcthrowsk[n]<0): npcthrowsk[n]=0
        if (npcthrowsk[n]>20): npcthrowsk[n]=20
        if (npclvl[n]<0): npclvl[n]=0
        if (npclvl[n]>20): npclvl[n]=20

pathchosen1=0
pathchosen2=0
dorandomizeItems=0
failurepart=-1
def story():
    global part, chat1, chat2, chat3, speaker, level, sky
    global selectx, selecty, camerax, cameray, day, chapter, tutorialpick, tutorialthrow
    global changelevelpart, changelevelto, controlChar, tutorialmove, tutorialhurt, tutorialarms
    global pathchosen1, pathchosen2, dorandomizeItems, tileset, tilewall, whogoes, failurepart
    failurepart=-1; controlChar=-1
    if (level=="LevelMenu" or level==""):
        if (day>=42 and day<50):
            sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        else:
            tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
            tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
    else:
        tileset=pygame.image.load("Images/isotileset.png").convert_alpha()
        tilewall=pygame.image.load("Images/isowall.png").convert_alpha()
    if (level=="Floor"):
        gx=19; gy=4
        selectx=29-gx; camerax=selectx #Camera Position
        selecty=14-gy; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=29-gx; npcy[npcc]=12-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Porter"; npcx[npcc]=29-gx; npcy[npcc]=10-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0 #Create NPCs
        part=1
        movenpc[part]=0; movenpcx[part]=26-gx; movenpcy[part]=13-gy; movespeed[part]=.05 #Move NPCs
        part=2; speaker[part]="Winston"
        chat1[part]="Room 417..."
        chat2[part]="Looks like this is where I'll be staying."
        chat3[part]=""
        part=3
        movenpc[part]=0; movenpcx[part]=26-gx; movenpcy[part]=14-gy
        musicplay[part]="standby"
        part=4; speaker[part]="Winston"
        chat1[part]="It's a bit small though. The cheap rooms"
        chat2[part]="are always this small."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=26-gx; movenpcy[part]=15-gy
        part=5; speaker[part]="Winston"
        chat1[part]="But hey, whatever gets me through the next"
        chat2[part]="few days."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=25-gx; movenpcy[part]=19-gy
        part=6
        movenpc[part]=0; movenpcx[part]=24-gx; movenpcy[part]=20-gy
        part=7; speaker[part]="Winston"
        chat1[part]="I knew my room would be pretty high up,"
        chat2[part]="but I didn't expect a view like this."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=24-gx; movenpcy[part]=22-gy
        part=8
        movenpc[part]=1; movenpcx[part]=29-gx; movenpcy[part]=11-gy; createnpc[part]=1 #Moving the Porter
        part=9
        movenpc[part]=1; movenpcx[part]=29-gx; movenpcy[part]=12-gy
        part=10
        movenpc[part]=1; movenpcx[part]=26-gx; movenpcy[part]=13-gy
        part=11; speaker[part]=" "
        chat1[part]="You hear someone knocking on your door."
        chat2[part]=""
        chat3[part]=""
        part=12; speaker[part]="Winston"
        chat1[part]="That's probably an employee here to"
        chat2[part]="greet me. I guess I'd better answer..."
        chat3[part]=""
        part=13
        controlChar=part; tutorialmove=1
        part=14; speaker[part]="Porter"
        chat1[part]="Sir. We hope you've had a fine time settling"
        chat2[part]="into your room. Is there else anything you"
        chat3[part]="might need?"
        part=15; speaker[part]="Winston"
        chat1[part]="No, I'm fine."
        chat2[part]=""
        chat3[part]=""
        part=16; speaker[part]="Porter"
        chat1[part]="Are you sure? I could tidy up your room again"
        chat2[part]="if you would like."
        chat3[part]=""
        choice1[part]="On second thought, that would be great."; choice1go[part]=17 #Choices Given
        choice2[part]="No thanks. I said that I'm fine."; choice2go[part]=50
        part=17; speaker[part]="Winston" #Option 1
        chat1[part]="On second thought, that would be great."
        chat2[part]="I may have tracked in some dirt by accident."
        chat3[part]="Sorry about that."
        movenpc[part]=0; movenpcx[part]=25-gx; movenpcy[part]=15-gy
        part=18; speaker[part]="Porter"
        chat1[part]="I'll be just a minute."
        chat2[part]=""
        chat3[part]=""
        part=19
        movenpc[part]=1; movenpcx[part]=27-gx; movenpcy[part]=16-gy
        part=20; speaker[part]="Porter"
        chat1[part]="Your bathroom looks fine."
        chat2[part]=""
        chat3[part]=""
        part=21
        movenpc[part]=1; movenpcx[part]=24-gx; movenpcy[part]=20-gy
        part=22; speaker[part]="Porter"
        chat1[part]="As does your balcony."
        chat2[part]=""
        chat3[part]=""
        part=23
        movenpc[part]=1; movenpcx[part]=23-gx; movenpcy[part]=18-gy
        part=24; speaker[part]="Porter"
        chat1[part]="Your room is spotless."
        chat2[part]=""
        chat3[part]=""
        part=25; speaker[part]="Winston"
        chat1[part]="Yep, just how I found it. Sorry to waste your time."
        chat2[part]=""
        chat3[part]=""
        part=26
        partdelay[part]=1
        part=27; speaker[part]="Porter"
        chat1[part]="Again, have a fine stay at our Hotel. Your luggage"
        chat2[part]="will be brought up shortly."
        chat3[part]=""
        part=28; speaker[part]="Winston"
        chat1[part]="Yeah, thanks."
        chat2[part]=""
        chat3[part]=""
        part=29
        movenpc[part]=1; movenpcx[part]=29-gx; movenpcy[part]=12-gy
        part=30
        movenpc[part]=1; movenpcx[part]=29-gx; movenpcy[part]=11-gy
        part=31; speaker[part]="Winston"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=26-gx; movenpcy[part]=15-gy; createnpc[part]=-1 #Destroy Porter
        part=32; speaker[part]="Winston"
        chat1[part]="Well, that was a waste of time."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=24-gx; movenpcy[part]=19-gy
        part=33; speaker[part]="Winston"
        chat1[part]="When did I become so anti-social? I feel as though"
        chat2[part]="her visit could have gone a different way. Maybe"
        chat3[part]="I'm just stressed out..."
        musicplay[part]="None"
        part=34; speaker[part]="Winston"
        chat1[part]="I should just take things slowly. Everything will"
        chat2[part]="be fine..."
        chat3[part]=""
        part=35
        changelevelpart=part; changelevelto="LevelMenu"; day=2; chapter+=1
        part=50; speaker[part]="Winston" #Option 2
        chat1[part]="No thanks. I said that I'm fine. I'd prefer"
        chat2[part]="to arrange things myself."
        chat3[part]=""
        part=51; speaker[part]="Porter"
        chat1[part]="I understand. Again, thank you for choosing to stay"
        chat2[part]="with us."
        chat3[part]=""
        part=52
        movenpc[part]=1; movenpcx[part]=26-gx; movenpcy[part]=14-gy
        part=53
        movenpc[part]=1; movenpcx[part]=29-gx; movenpcy[part]=12-gy
        part=54
        movenpc[part]=1; movenpcx[part]=29-gx; movenpcy[part]=11-gy
        part=55; speaker[part]="Winston"
        chat1[part]="...I should have reminded her that this is the only"
        chat2[part]="hotel in this city."
        chat3[part]=""
        createnpc[part]=-1 #Destroy Porter
        part=56; speaker[part]="Winston"
        chat1[part]="Well, I have a bathroom. My balcony is right over"
        chat2[part]="there..."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=27-gx; movenpcy[part]=16-gy
        part=57; speaker[part]="Winston"
        chat1[part]="Good thing I didn't waste my time with some"
        chat2[part]="unneeded room analysis."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=23-gx; movenpcy[part]=19-gy
        part=58
        gotopart[part]=33
        part=0
    if (level=="Murder"):
        gx=19; gy=4
        selectx=29-19; camerax=selectx #Camera Position
        selecty=14-4; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="???"; npcx[npcc]=29-gx; npcy[npcc]=10-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Resident"; npcx[npcc]=32-gx; npcy[npcc]=7-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0 #Create NPCs
        part=1
        partdelay[part]=20
        part=2
        movenpc[part]=0; movenpcx[part]=29-gx; movenpcy[part]=11-gy
        musicplay[part]="scary"
        part=3; speaker[part]="???"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=29-gx; movenpcy[part]=12-gy
        part=4
        movenpc[part]=0; movenpcx[part]=33-gx; movenpcy[part]=12-gy
        part=5; speaker[part]="???"
        chat1[part]="I have to do this. It's the only way."
        chat2[part]=""
        chat3[part]=""
        part=6
        movenpc[part]=0; movenpcx[part]=35-gx; movenpcy[part]=12-gy
        part=7; speaker[part]="Resident"
        chat1[part]="Hello? Who're you, some maid?"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=32-gx; movenpcy[part]=8-gy
        part=8; speaker[part]="???"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=35-gx; movenpcy[part]=11-gy
        part=9; speaker[part]="Resident"
        chat1[part]="Don't come in, Intruder! Come to steal my"
        chat2[part]="things, have ya? I'm warning ya, I've fought"
        chat3[part]="guys twice your size."
        movenpc[part]=1; movenpcx[part]=32-gx; movenpcy[part]=9-gy
        part=10
        controlChar=part; tutorialhurt=1
        part=11
        partdelay[part]=100
        part=12
        partdelay[part]=200
        part=13; speaker[part]="???"
        chat1[part]="..."
        musicplay[part]="None"
        part=14; speaker[part]="???"
        chat1[part]="It is finished."
        part=15
        changelevelpart=part; changelevelto="LevelMenu"; day=3; chapter+=1
        part=99; speaker[part]="???"
        chat1[part]="Gah! E-Ev-Everything...it's all ruined!"
        chat2[part]=""
        chat3[part]=""
        part=100
        musicplay[part]="None"
        failurepart=part
    if (level=="Accused"):
        gx=19; gy=4
        selectx=28-gx; camerax=selectx #Camera Position
        selecty=13-gy; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=29-gx; npcy[npcc]=16-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1 #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Lenna"; npcx[npcc]=30-gx; npcy[npcc]=12-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1 #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=26-gx; npcy[npcc]=14-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1 #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Floyd"; npcx[npcc]=32-gx; npcy[npcc]=14-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1 #Create NPCs
        part=1
        partdelay[part]=100
        part=2; speaker[part]=" "
        chat1[part]="Winston wakes up after a restless night. He"
        chat2[part]="is in his restroom, staring at himself in the"
        chat3[part]="mirror."
        part=3; speaker[part]="Voices"
        chat1[part]="I don't kno...what did...hey, make...!"
        chat2[part]=""
        chat3[part]=""
        part=4; speaker[part]="Winston"
        chat1[part]="Hm? Someone in the hallway needs to calm down."
        part=5; speaker[part]=" "
        chat1[part]="Winston ignores the voices and prepares to"
        chat2[part]="clean himself with sink water."
        chat3[part]=""
        part=6; speaker[part]="Voices"
        chat1[part]="Quit...What did I...Sir, what do you..."
        chat2[part]="Okay, okay...going..."
        chat3[part]=""
        part=7; speaker[part]=" "
        chat1[part]="Winston hears heavy footsteps approaching his door."
        part=8; speaker[part]=" "
        chat1[part]="A knock is heard on Winston's room door."
        part=9; speaker[part]="Winston"
        chat1[part]="Weird. Hold on! I'm coming!"
        part=10
        controlChar=part
        part=11; speaker[part]=" "
        chat1[part]="Another knock is heard on the room door."
        partdelay[part]=100
        part=12
        part=13
        partdelay[part]=50
        part=14
        partdelay[part]=50
        part=15
        partdelay[part]=50
        createnpc[part]=2
        part=16; speaker[part]="Winston"
        chat1[part]="Hello?"
        part=17; speaker[part]="Officer"
        chat1[part]="Exit your room and head towards the elevator door."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="scary"
        part=18; speaker[part]="Winston"
        chat1[part]="Huh? What is this? I didn't do anything!"
        part=19; speaker[part]="Officer"
        chat1[part]="Please, I just want to talk to you."
        chat2[part]=""
        chat3[part]=""
        part=20; speaker[part]=" "
        chat1[part]="Winston does as asked."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=25-gx; movenpcy[part]=14-gy
        part=21
        createnpc[part]=1
        partdelay[part]=1
        part=22
        createnpc[part]=3
        partdelay[part]=1
        part=23
        movenpc[part]=0; movenpcx[part]=27-gx; movenpcy[part]=13-gy
        part=24; speaker[part]="Winston"
        chat1[part]="Wha-What happened here!?"
        chat2[part]=""
        chat3[part]=""
        part=25; speaker[part]="Lenna"
        chat1[part]="Question of the day, ain't it?"
        part=26; speaker[part]="Floyd"
        chat1[part]="Someone was murdered in the room down at the"
        chat2[part]="end of the hallway. We're all suspects."
        chat3[part]=""
        part=27
        movenpc[part]=2; movenpcx[part]=29-gx; movenpcy[part]=14-gy
        part=28; speaker[part]="Officer"
        chat1[part]="Settle down. I'm going to need you three"
        chat2[part]="to answer some questions for me."
        chat3[part]=""
        part=29; speaker[part]="Officer"
        chat1[part]="How about you, old man. What's your side"
        chat2[part]="of the story?"
        chat3[part]=""
        part=30; speaker[part]="Floyd"
        chat1[part]="Look, Officer, I didn't kill or help anyone"
        chat2[part]="kill anyone. I was sleeping all night."
        chat3[part]=""
        part=31; speaker[part]="Officer"
        chat1[part]="We'll have to confirm that. How about you,"
        chat2[part]="lady?"
        chat3[part]=""
        part=32; speaker[part]="Lenna"
        chat1[part]="Do you really think a \"lady\" would ever hurt"
        chat2[part]="someone? I was sleeping when it happened, just"
        chat3[part]="like everyone else here."
        part=33; speaker[part]="Officer"
        chat1[part]="That's where you're wrong. One of you must be"
        chat2[part]="the murderer. One of you got up in the middle"
        chat3[part]="of the night..."
        part=34; speaker[part]="Winston"
        chat1[part]="H-How can you know for certain? What if"
        chat2[part]="it was someone from another floor?"
        chat3[part]=""
        part=35; speaker[part]="Officer"
        chat1[part]="Hotel security shows that this elevator was used"
        chat2[part]="once before the murder, and then never again."
        chat3[part]="The murderer went back to sleep after the killing."
        part=36; speaker[part]="Officer"
        chat1[part]="And lastly, you. What do you think?"
        chat2[part]=""
        chat3[part]=""
        choice1[part]="The murderer isn't any one of us."; choice1go[part]=40 #Choices Given
        choice2[part]="You're right. One of us is the murderer."; choice2go[part]=50
        part=40; speaker[part]="Winston" #Choice 1
        chat1[part]="The murderer isn't any one of us. I know"
        chat2[part]="what you're doing...trying to close this case"
        chat3[part]="as fast as you can. You'd arrest an innocent!"
        part=41; speaker[part]="Officer"
        chat1[part]="Something only a murderer would say."
        chat2[part]=""
        chat3[part]=""
        part=42; speaker[part]="Winston"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        part=43; speaker[part]="Floyd"
        chat1[part]="Quit picking on him! I swear, Officer, I"
        chat2[part]="will bring my lawyer into this and get you"
        chat3[part]="fired if you so as touch one of us."
        part=44
        gotopart[part]=60
        part=50; speaker[part]="Winston"
        chat1[part]="You're right, one of us is the murderer."
        chat2[part]="But I swear it's not me. Aren't I innocent"
        chat3[part]="till proven guilty?"
        part=51; speaker[part]="Floyd"
        chat1[part]="The boy and girl are innocent, as am I. We"
        chat2[part]="were all sound asleep when, well, the"
        chat3[part]="crime took place!"
        part=52
        gotopart[part]=60
        part=60; speaker[part]="Officer"
        chat1[part]="Excuse me, what was your name again?"
        part=61; speaker[part]="Floyd"
        chat1[part]="Floyd."
        part=62; speaker[part]="Officer"
        chat1[part]="Floyd, I need you to come in and answer a"
        chat2[part]="few more questions."
        chat3[part]=""
        part=63; speaker[part]="Floyd"
        chat1[part]="W-What? Are you saying you think I did it?"
        chat2[part]="Can you not tell by my age? What would be my"
        chat3[part]="motive? I-I-I..."
        part=64; speaker[part]="Lenna"
        chat1[part]="And now you're gonna pick on an old man?"
        chat2[part]=""
        chat3[part]=""
        part=65; speaker[part]="Officer"
        chat1[part]="Please, Floyd. I just want to bring you in"
        chat2[part]="to closer examine the evidence. If you didn't"
        chat3[part]="commit the crime, you don't have to worry."
        movenpc[part]=2; movenpcx[part]=30-gx; movenpcy[part]=14-gy
        part=66; speaker[part]="Floyd"
        chat1[part]="Hrmm. Fine. I'll go. I just want to prove"
        chat2[part]="my innocence."
        chat3[part]=""
        musicplay[part]="None"
        part=67; speaker[part]="Officer"
        chat1[part]="Again, if you're innocent, you have nothing"
        chat2[part]="to fear...I'm sure this won't take long"
        chat3[part]="at all."
        part=68
        changelevelpart=part; changelevelto="LevelMenu"; day=4; chapter+=1
    if (level=="Fight"):
        item[0]="Bottle"; itemx[0]=12; itemy[0]=7
        selectx=10; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=14; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; npcheld[npcc]=""; npcdead[npcc]=0 #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=11; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; npcheld[npcc]=""; npcdead[npcc]=0 #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Thug"; npcx[npcc]=1; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]=""; npcdead[npcc]=0 #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Thug"; npcx[npcc]=14; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]=""; npcdead[npcc]=0 #Create NPCs
        npcturn[1]=10
        npcturn[2]=10
        part=1
        partdelay[part]=100
        part=2; speaker[part]="Winston"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="mystery"
        part=3
        partdelay[part]=100
        part=4; speaker[part]="Lenna"
        chat1[part]="So, hey...kind of wish that they'd let us back"
        chat2[part]="into our rooms. Getting kind of tired standing"
        chat3[part]="here, eh?"
        part=5; speaker[part]="Winston"
        chat1[part]="...Hey. And yeah..."
        chat2[part]=""
        chat3[part]=""
        part=6; speaker[part]="Lenna"
        chat1[part]="Look, everything will be all right."
        chat2[part]="Ya know? I mean, that guy, Floyd, right?"
        chat3[part]="He'll be fine. And that other guy..."
        part=7; speaker[part]="Winston"
        chat1[part]="...Did you kill him?"
        chat2[part]=""
        chat3[part]=""
        part=8; speaker[part]="Lenna"
        chat1[part]="What? No! Are you gonna start accusing me"
        chat2[part]="now? What are you, a cop?"
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=12; movenpcy[part]=8
        part=9; speaker[part]="Winston"
        chat1[part]="I'm just curious, all right? It wasn't"
        chat2[part]="Floyd, he's just an old man! Who's the"
        chat3[part]="killer then, huh?"
        part=10; speaker[part]="Lenna"
        chat1[part]="I don't know! Ask an Officer!"
        chat2[part]=""
        chat3[part]=""
        part=11; speaker[part]="Winston"
        chat1[part]="You killed him, admit it! You're going to"
        chat2[part]="kill me next, aren't you?"
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=13; movenpcy[part]=7
        part=12; speaker[part]="Lenna"
        chat1[part]="Shut up!"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=8
        part=13; speaker[part]="Winston"
        chat1[part]="So why did you do it? For money? No..."
        chat2[part]="Maybe you just felt like it?"
        chat3[part]=""
        part=14; speaker[part]="Lenna"
        chat1[part]="Anyone in the entire hotel could have done"
        chat2[part]="it. I don't believe those lying Officers"
        chat3[part]="for a second!"
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=8
        part=15; speaker[part]="Winston"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        choice1[part]="Pressure Lenna"; choice1go[part]=20 #Choices Given
        choice2[part]="Calm Down"; choice2go[part]=30
        musicplay[part]="None"
        part=20; speaker[part]="Winston" #Choice 1
        chat1[part]="You're the liar! I heard footsteps from your room"
        chat2[part]="on that night!"
        chat3[part]=""
        part=21; speaker[part]="Lenna"
        chat1[part]="Trying too hard to point fingers, aren't you?"
        chat2[part]="Who's to say you didn't wake up while we"
        chat3[part]="were all sleeping and kill him yourself?"
        part=22
        gotopart[part]=35
        part=30; speaker[part]="Winston" #Choice 2
        chat1[part]="...Sorry...I just have a lot of"
        chat2[part]="thoughts going through my head right now."
        chat3[part]="Sorry that I accused you."
        part=31; speaker[part]="Lenna"
        chat1[part]="Winston...are you the killer?"
        chat2[part]=""
        chat3[part]=""
        part=32
        gotopart[part]=35
        part=35; speaker[part]="Winston"
        chat1[part]="Heh. Wouldn't you like to know."
        chat2[part]=""
        chat3[part]=""
        part=36; speaker[part]="Lenna"
        chat1[part]="I'm leaving. You're just so..."
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=8
        part=37
        movenpc[part]=2; movenpcx[part]=2; movenpcy[part]=5
        part=38
        createnpc[part]=2
        partdelay[part]=40
        part=39; speaker[part]="Thug"
        chat1[part]="Hey, bro, I found 'em! Them two killers!"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="threefour"
        part=40; speaker[part]="Thug"
        chat1[part]="Thought you could get away with it, huh?"
        chat2[part]="Your buddy Floyd's in some seeeerrrious"
        chat3[part]="trouble thanks to you."
        part=41; speaker[part]="Winston"
        chat1[part]="What!?"
        part=42; speaker[part]="Lenna"
        chat1[part]="Back off! We didn't kill anyone!"
        chat2[part]=""
        chat3[part]=""
        part=43; speaker[part]="Thug"
        chat1[part]="The Officers are too light-hearted,"
        chat2[part]="I'm gonna kill you both!"
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=3; movenpcy[part]=6
        part=44; speaker[part]="Lenna"
        chat1[part]="Winston, throw that bottle on the floor"
        chat2[part]="to me! Just don't hit me! Hurry!"
        chat3[part]=""
        part=45
        controlChar=part; tutorialpick=1
        part=47; speaker[part]="Lenna"
        chat1[part]="Watch it, another one's coming from down the"
        chat2[part]="hall."
        chat3[part]=""
        createnpc[part]=3
        part=48
        part=49
        partdelay[part]=100
        part=50; speaker[part]="Lenna"
        chat1[part]="It doesn't look like any more are coming."
        chat2[part]="And what just happened? How would they"
        chat3[part]="know we're suspects in the murder?"
        musicplay[part]="None"
        part=51; speaker[part]="Winston"
        chat1[part]="..."
        choice1[part]="Who cares. Who were they even?"; choice1go[part]=52 #Choices Given
        choice2[part]="Connections with the man killed?"; choice2go[part]=60
        choice3[part]="Maybe they overheard some Officers."; choice3go[part]=70
        part=52; speaker[part]="Winston" #Choice 1
        chat1[part]="Who cares. Who were they even? Some gang?"
        chat2[part]="How'd a gang get into this hotel?"
        chat3[part]=""
        part=53; speaker[part]="Lenna"
        chat1[part]="No...they weren't some gangsters. They look like"
        chat2[part]="regular people. Just like us. They just wanted"
        chat3[part]="to enact what they thought was justice."
        part=54
        gotopart[part]=80
        part=60; speaker[part]="Winston" #Choice 2
        chat1[part]="Connections with the man killed? What if the"
        chat2[part]="the man that was murdered was some sort of"
        chat3[part]="gang overlord?"
        part=61; speaker[part]="Lenna"
        chat1[part]="No...they weren't some gangsters. They look like"
        chat2[part]="regular people. Just like us. They just wanted"
        chat3[part]="to enact what they thought was justice."
        part=62
        gotopart[part]=80
        part=70; speaker[part]="Winston" #Choice 3
        chat1[part]="Maybe they overheard some Officers. Either way,"
        chat2[part]="I'm sure the murder isn't some secret. It's"
        chat3[part]="probably already been on the news."
        part=71; speaker[part]="Lenna"
        chat1[part]="So wouldn't that mean that these thugs are"
        chat2[part]="just...regular guys? They just wanted to"
        chat3[part]="enact what they thought was justice."
        part=72
        gotopart[part]=80
        part=80; speaker[part]="Lenna"
        chat1[part]="But now...we really ARE killers. You think"
        chat2[part]="anyone's gonna think we were just defending"
        chat3[part]="ourselves?"
        part=81; speaker[part]="Winston"
        chat1[part]="...Didn't one of them say something about Floyd?"
        chat2[part]=""
        chat3[part]=""
        part=82; speaker[part]="Lenna"
        chat1[part]="Oh yeah...doesn't that mean that Floyd is...?"
        chat2[part]=""
        chat3[part]=""
        part=83; speaker[part]="Winston"
        chat1[part]="They must want to kill Floyd too. We need"
        chat2[part]="to save him."
        chat3[part]=""
        part=84
        changelevelpart=part; changelevelto="LevelMenu"; day=5; chapter+=1
        part=91; speaker[part]="Lenna"
        chat1[part]="No! Winston! Get up, get up! We're innocent!"
        chat2[part]=""
        chat3[part]=""
        part=92
        gotopart[part]=100
        part=99; speaker[part]="Winston"
        chat1[part]="Lenna, wake up! This isn't your fault, you're"
        chat2[part]="innocent!"
        chat3[part]=""
        part=100
        musicplay[part]="None"
        failurepart=part
    if (level=="Kurt"):
        item[0]="Glass"; itemx[0]=12; itemy[0]=7
        selectx=5; camerax=selectx #Camera Position
        selecty=5; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=2; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; npcheld[npcc]="Scissors"; npcdead[npcc]=0 #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Kurt"; npcx[npcc]=8; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Knife"; npcdead[npcc]=0 #Create NPCs      
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Winston"
        chat1[part]="Hello?"
        chat2[part]=""
        chat3[part]=""
        part=3
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=5
        part=4
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=5
        part=5; speaker[part]="Kurt"
        chat1[part]="Welcome! Come in, my friend!"
        chat2[part]="I have not seen you in ages!"
        chat3[part]=""
        musicplay[part]="standby"
        part=6
        movenpc[part]=0; movenpcx[part]=3; movenpcy[part]=3
        part=7; speaker[part]="Winston"
        chat1[part]="Listen, Kurt, I've been having some problems"
        chat2[part]="lately. You've always been there for me, so"
        chat3[part]="I was hoping that you would, well..."
        part=8; speaker[part]="Kurt"
        chat1[part]="Ah! Winston, do not worry yourself..."
        chat2[part]="I, Kurt, am always here to help a friend in "
        chat3[part]="need!"
        part=9; speaker[part]="Winston"
        chat1[part]="Haha! Do you at least have a weapon to use?"
        chat2[part]=""
        chat3[part]=""
        part=10
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=3
        part=11
        movenpc[part]=1; movenpcx[part]=4; movenpcy[part]=3
        part=12; speaker[part]="Kurt"
        chat1[part]="Always! See this? She is beautiful, is"
        chat2[part]="she not? Never seen a sharper knife, have"
        chat3[part]="you?"
        part=13; speaker[part]="Kurt"
        chat1[part]="Have you forgotten the skill of the brawl?"
        chat2[part]="Let me refresh your memory..."
        chat3[part]=""
        part=14; speaker[part]="Kurt"
        chat1[part]="Piercing weapons are useful for causing bleeding."
        chat2[part]="As blood is lost, effects such as dizziness and"
        chat3[part]="even fainting or death can occur."
        part=15; speaker[part]="Kurt"
        chat1[part]="Ah, sharp weapons can pierce internal organs"
        chat2[part]="like none other."
        chat3[part]=""
        part=16; speaker[part]="Kurt"
        chat1[part]="The most powerful piercing weapon is the Knife."
        chat2[part]="Then, there is the Shiv, followed by Glass."
        chat3[part]=""
        part=17; speaker[part]="Kurt"
        chat1[part]="Still with me? Focus!"
        chat2[part]=""
        chat3[part]=""
        part=18; speaker[part]="Kurt"
        chat1[part]="Blunt weapons include the powerful Hammer and"
        chat2[part]="the less but still powerful Wrench. Batons"
        chat3[part]="are okay...but you desire strength, ah ha?"
        part=19; speaker[part]="Kurt"
        chat1[part]="Blunt weapons cause no bleeding, but will"
        chat2[part]="deal much more pain! Use them to shatter bones"
        chat3[part]="and leave enemies incapacitated!"
        part=20; speaker[part]="Kurt"
        chat1[part]="Remember, the more pain someone is in, the more"
        chat2[part]="powerful future blows will be."
        chat3[part]=""
        part=21; speaker[part]="Kurt"
        chat1[part]="You will faint after too much pain, leaving you"
        chat2[part]="open to direct, powerful blows. It is not a"
        chat3[part]="situation you want to be in!"
        part=22; speaker[part]="Kurt"
        chat1[part]="Other, less common weapons you might find are"
        chat2[part]="a mixed bag...they can be extraordinarily weak"
        chat3[part]="or have a unique gimmick."
        part=23; speaker[part]="Kurt"
        chat1[part]="Are you just skipping the text? I assure you,"
        chat2[part]="this is important!"
        chat3[part]=""
        part=24; speaker[part]="Kurt"
        chat1[part]="Weapons are not commonly found simply lying on"
        chat2[part]="the floor, I can assure you. Attack your foes'"
        chat3[part]="hands! They may drop theirs!"
        part=25; speaker[part]="Kurt"
        chat1[part]="One last bit of advice...throw old weapons when"
        chat2[part]="you can easily pick up another afterwards. The"
        chat3[part]="further it travels, the more damage it will do."
        part=26; speaker[part]="Kurt"
        chat1[part]="Er, where were we? Yes...yes, you most likely"
        chat2[part]="need a weapon as well, hmmm? The plain fist is"
        chat3[part]="not very strong, as they say!"
        part=27; speaker[part]="Kurt"
        chat1[part]="Sadly, I have no weapon to offer to you, only"
        chat2[part]="these scissors... But scissors are better than"
        chat3[part]="nothing! Let us go onward, my friend!"
        musicplay[part]="None"
        part=28
        changelevelpart=part; changelevelto="LevelMenu"; day=5; chapter+=1
    if (level=="Outside"):
        selectx=12; camerax=selectx #Camera Position
        selecty=19; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=1; npc[npcc]=0; npcside[npcc]="Winston"; npcx[npcc]=9; npcy[npcc]=27; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0 #Create NPCs
        npcc=0; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=8; npcy[npcc]=23; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0  #Create NPCs      
        npcc=2; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=9; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1  #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=8; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=10; npcy[npcc]=15; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Pacifist"; npcx[npcc]=6; npcy[npcc]=20; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Pencil" #Create NPCs
        npcc=6; npc[npcc]=1; npcside[npcc]="Activist"; npcx[npcc]=11; npcy[npcc]=21; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Wrench" #Create NPCs
        npcc=7; npc[npcc]=1; npcside[npcc]="Protester"; npcx[npcc]=12; npcy[npcc]=20; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Shiv" #Create NPCs        
        part=1
        partdelay[part]=50
        musicplay[part]="crowd"
        part=2
        movenpc[part]=3; movenpcx[part]=8; movenpcy[part]=15
        part=3; speaker[part]="Officer"
        chat1[part]="Listen! We hear your concerns, but there"
        chat2[part]="simply is not enough evidence to convict"
        chat3[part]="any suspects of the murder."
        part=4; speaker[part]="Floyd"
        chat1[part]="Let me go, you hooligans! I'm innocent!"
        chat2[part]="Don't believe the media, I swear I'm no"
        chat3[part]="killer!"
        part=5
        createnpc[part]=1
        partdelay[part]=1
        part=6
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=23
        part=7; speaker[part]="Winston"
        chat1[part]="I'm here."
        chat2[part]=""
        chat3[part]=""
        part=8; speaker[part]="Lenna"
        chat1[part]="See the guy in the center? That's Floyd."
        chat2[part]=""
        chat3[part]=""
        part=9; speaker[part]=" "
        chat1[part]="Yelling is heard from the protesters."
        chat2[part]=""
        chat3[part]=""
        part=10; speaker[part]="Protester"
        chat1[part]="That's the killer! You have him right there!"
        chat2[part]="Just kill him! He's a murder!"
        chat3[part]=""
        part=11; speaker[part]="Activist"
        chat1[part]="Yeah! I saw him on TV! He's a danger to"
        chat2[part]="society! If you let him free, he'll kill"
        chat3[part]="again!"
        part=12; speaker[part]="Winston"
        chat1[part]="TV? Lenna, you don't think that the media"
        chat2[part]="has drawn the public eye to us too, right?"
        chat3[part]=""
        part=13; speaker[part]="Lenna"
        chat1[part]="I'm sure they have, remember earlier today?"
        chat2[part]=""
        chat3[part]=""
        part=14; speaker[part]="Lenna"
        chat1[part]="We were attacked because those guys thought"
        chat2[part]="they were doing a good thing, ya know? Killing"
        chat3[part]="the \"murders\". Killing us."
        part=15; speaker[part]="Winston"
        chat1[part]="Let's be careful then, or this crowd might realize"
        chat2[part]="who we are."
        chat3[part]=""
        part=16; speaker[part]="Pacifist"
        chat1[part]="Come on guys, let's get him ourselves! Let's put"
        chat2[part]="justice into our own hands!"
        chat3[part]=""
        part=17; speaker[part]="Lenna"
        chat1[part]="Ugh, looks like this isn't a peaceful"
        chat2[part]="protest."
        chat3[part]=""
        part=18; speaker[part]="Lenna"
        chat1[part]="We need to fight the protesters or else"
        chat2[part]="they'll kill Floyd. If he dies, it's over."
        chat3[part]=""
        musicplay[part]="None"
        part=19; speaker[part]="Lenna"
        chat1[part]="Let's sit back and wait for the Officers to thin"
        chat2[part]="out some of the fighting before jumping in. We"
        chat3[part]="could throw our weapons into the fight if it helps."
        part=20
        controlChar=part; tutorialarms=1
        musicplay[part]="action"
        part=24
        partdelay[part]=50
        part=25; speaker[part]="Lenna"
        chat1[part]="Floyd! Floyd! Are you all right?"
        part=26; speaker[part]="Floyd"
        chat1[part]="I'm fine. But we won't be for long."
        musicplay[part]="None"
        part=27; speaker[part]="Winston"
        chat1[part]="What do you mean?"
        part=28; speaker[part]="Floyd"
        chat1[part]="Can't you see what you've done? You're both"
        chat2[part]="killers, and I'm going to be branded an"
        chat3[part]="accomplice."
        musicplay[part]="ominous"
        part=29; speaker[part]="Lenna"
        chat1[part]="They were going to kill you if we hadn't"
        chat2[part]="stepped in. You should be grateful!"
        chat3[part]=""
        part=30; speaker[part]="Floyd"
        chat1[part]="Don't misunderstand me..."
        chat2[part]="We're going to be the top story on the"
        chat3[part]="news, for sure."
        part=31; speaker[part]="Floyd"
        chat1[part]="It's all the media's fault, either way. Accuse"
        chat2[part]="some suspects before the verdict is given and"
        chat3[part]="the viewers'll be eat it up!"
        part=32; speaker[part]="Floyd"
        chat1[part]="Some viewers will be so inclined to become"
        chat2[part]="apart of what they don't understand...as"
        chat3[part]="you just witnessed."
        part=33; speaker[part]="Floyd"
        chat1[part]="Tell me, Winston, who's fault is all of this?"
        chat2[part]=""
        chat3[part]=""
        choice1[part]="The Officers'"; choice1go[part]=35 #Choices Given
        choice2[part]="The Media's"; choice2go[part]=40
        part=35; speaker[part]="Winston"
        chat1[part]="I...I still think it's the Officers' faults."
        chat2[part]="Don't you think that the whole police system"
        chat3[part]="is just too corrupt?"
        part=36; speaker[part]="Floyd"
        chat1[part]="No...As with all cases, we're innocent until"
        chat2[part]="proven guilty. The Officers understand that..."
        chat3[part]=""
        part=37; speaker[part]="Lenna"
        chat1[part]="I agree Winston, they shouldn't have messed"
        chat2[part]="with us in the first place."
        chat3[part]=""
        part=38
        gotopart[part]=59
        part=40; speaker[part]="Winston"
        chat1[part]="You're right, it's the media's. They blew"
        chat2[part]="this whole story way out of proportion."
        chat3[part]=""
        part=41; speaker[part]="Floyd"
        chat1[part]="And it's viewers...mindless!"
        chat2[part]=""
        chat3[part]=""
        part=41; speaker[part]="Lenna"
        chat1[part]="Hey, this wouldn't have been a problem in the"
        chat2[part]="first place if the Officers hadn't accused"
        chat3[part]="us."
        part=42
        gotopart[part]=59
        part=59; speaker[part]="Lenna"
        chat1[part]="Look, as long as we're all safe for now."
        chat2[part]="Let's get out of here."
        chat3[part]=""
        musicplay[part]="None"
        part=60
        changelevelpart=part; changelevelto="LevelMenu"; day=6; chapter+=1
        part=96; speaker[part]="Floyd"
        chat1[part]="What a way to go."
        chat2[part]=""
        chat3[part]=""
        part=97
        gotopart[part]=105
        part=98; speaker[part]="Floyd"
        chat1[part]="What a way to go."
        chat2[part]=""
        chat3[part]=""
        part=99
        gotopart[part]=105
        part=100; speaker[part]="Lenna"
        chat1[part]="Floyd! No!...We couldn't save him..."
        part=101
        gotopart[part]=105
        part=105
        musicplay[part]="None"
        failurepart=part
    if (level=="Frederick"):
        dorandomizeItems=0
        selectx=29; camerax=selectx #Camera Position
        selecty=14; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=26; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0;  #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=25; npcy[npcc]=18; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=26; npcy[npcc]=17; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Frederick"; npcx[npcc]=32; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Wrench" #Create NPCs
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Frederick"
        chat1[part]="Ah, yes! I see it now! \"An Indepth Look at the"
        chat2[part]="Scene of the Crime\". It'll make headlines,"
        chat3[part]="I'll be top reporter for sure!"
        musicplay[part]="standby"
        part=3; speaker[part]="Winston"
        chat1[part]="H-Hey! Who are you!?"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=27; movenpcy[part]=13
        part=4; speaker[part]="Frederick"
        chat1[part]="And truly, an interview with the killers themselves!?"
        chat2[part]="What a scoop, it just might go national!"
        chat3[part]=""
        movenpc[part]=3; movenpcx[part]=31; movenpcy[part]=13
        part=5; speaker[part]="Winston"
        chat1[part]="Huh? Can you calm down for just a sec-"
        chat2[part]=""
        chat3[part]=""
        part=6; speaker[part]="Frederick"
        chat1[part]="News waits on no one, Winston. If there's a story"
        chat2[part]="out there, the public needs to know!"
        chat3[part]=""
        part=7; speaker[part]="Winston"
        chat1[part]="But I-"
        chat2[part]=""
        chat3[part]=""
        part=8; speaker[part]="Frederick"
        chat1[part]="You've really got the public all riled-up! Your"
        chat2[part]="murders were top news today. Did you know that?"
        chat3[part]="He-he!"
        part=9; speaker[part]="Frederick"
        chat1[part]="But as you're probably already aware, the media"
        chat2[part]="likes to exaggerate...it likes to twist stories"
        chat3[part]="just to get the news out fast."
        part=10; speaker[part]="Frederick"
        chat1[part]="A half-truth is the most difficult lie to discern,"
        chat2[part]="after all. You can't be the original killers, the"
        chat3[part]="evidence just doesn't stack up!"
        part=11; speaker[part]="Frederick"
        chat1[part]="But honest news'll never die, if I have anything"
        chat2[part]="to say about it! Would ya let me join you guys?"
        chat3[part]="Come on, the people must know the truth!"
        part=12; speaker[part]="Winston"
        chat1[part]="I..."
        musicplay[part]="None"
        part=13; speaker[part]="Winston"
        chat1[part]="...Sure?"
        part=14
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Ruth"):
        dorandomizeItems=0
        selectx=29; camerax=selectx #Camera Position
        selecty=14; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=31; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=25; npcy[npcc]=18; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=26; npcy[npcc]=17; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Ruth"; npcx[npcc]=29; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Med Kit" #Create NPCs
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Winston"
        chat1[part]="Hm? The elevator's moving. Someone's here. Hey,"
        chat2[part]="guys! Be careful, someone's about to arrive!"
        chat3[part]=""
        part=3
        movenpc[part]=3; movenpcx[part]=29; movenpcy[part]=11
        part=4
        createnpc[part]=3
        partdelay[part]=1
        part=5
        movenpc[part]=3; movenpcx[part]=29; movenpcy[part]=12
        part=6
        partdelay[part]=1
        part=7; speaker[part]="Winston"
        chat1[part]="Hey! Hands up!"
        chat2[part]=""
        chat3[part]=""
        part=8; speaker[part]="Ruth"
        chat1[part]="Oh, sorry...I'm not dangerous, if you were"
        chat2[part]="wondering..."
        chat3[part]=""
        musicplay[part]="ambient"
        part=9; speaker[part]=" "
        chat1[part]="Winston puts his weapon away."
        chat2[part]=""
        chat3[part]=""
        part=10; speaker[part]="Winston"
        chat1[part]="Er, sorry, uh, sorry for yelling. Who are you,"
        chat2[part]="exactly?"
        chat3[part]=""
        part=11; speaker[part]="Ruth"
        chat1[part]="My name is Ruth. I..I work as as a"
        chat2[part]="nurse here, in this hotel. I heard about your"
        chat3[part]="story on the news...and..."
        part=12; speaker[part]="Ruth"
        chat1[part]="I just want to help. Everyone thinks you're"
        chat2[part]="killers. I mean...besides your fight earlier"
        chat3[part]="today, you would never kill an innocent, right?"
        movenpc[part]=3; movenpcx[part]=30; movenpcy[part]=12
        part=13; speaker[part]="Winston"
        chat1[part]="Yeah...we're in a bit of a mess. Supposedly,"
        chat2[part]="one of us killed someone on this floor last"
        chat3[part]="night...But we didn't! I swear!"
        part=14; speaker[part]="Winston"
        chat1[part]="At least, I didn't."
        chat2[part]=""
        chat3[part]=""
        part=15
        movenpc[part]=2; movenpcx[part]=26; movenpcy[part]=15
        part=16; speaker[part]="Floyd"
        chat1[part]="And who might this pretty young lady be?"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=26; movenpcy[part]=14
        part=17
        movenpc[part]=2; movenpcx[part]=26; movenpcy[part]=13
        part=18; speaker[part]="Ruth"
        chat1[part]="I'm Ruth, Sir. I want to join your party."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=3; movenpcx[part]=30; movenpcy[part]=13
        part=19; speaker[part]="Winston"
        chat1[part]="What!? No! I, er, I mean. You'll...your'll"
        chat2[part]="get hurt!"
        chat3[part]=""
        part=20; speaker[part]="Winston"
        chat1[part]="Er, I mean..."
        chat2[part]=""
        chat3[part]=""
        part=21; speaker[part]="Ruth"
        chat1[part]="I'm not the best fighter, but I can heal."
        chat2[part]=""
        chat3[part]=""
        part=22; speaker[part]="Ruth"
        chat1[part]="In fights, I can stop bleeding"
        chat2[part]="and relieve pain, though at the cost"
        chat3[part]="of my fighting ability."
        part=22; speaker[part]="Ruth"
        chat1[part]="Did you know, the more pain you're in, the more"
        chat2[part]="damage you'll take when attacked? It's always a"
        chat3[part]="good idea heal pain and bleeding."
        part=23; speaker[part]="Ruth"
        chat1[part]="I can simultaneously transfuse blood, so I can"
        chat2[part]="prevent your blood from falling to dangerously"
        chat3[part]="low levels."
        part=24; speaker[part]="Floyd"
        chat1[part]="Sweety, it looks like we have a deal. Welcome"
        chat2[part]="to the gang."
        chat3[part]=""
        part=25; speaker[part]="Winston"
        chat1[part]="She's not your \"sweety\", pops!"
        chat2[part]=""
        chat3[part]=""
        part=26; speaker[part]="Ruth"
        chat1[part]="Come this way, let me mend to your wounds..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=27
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Lucas"):
        dorandomizeItems=0
        selectx=8; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Commander"; npcx[npcc]=4; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=5; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=4; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=3; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Commander"
        chat1[part]="Men..."
        chat2[part]=""
        chat3[part]=""
        part=3; speaker[part]="Commander"
        chat1[part]="We face a great crisis. Two Officers were"
        chat2[part]="killed earlier today in a riot over one of the"
        chat3[part]="murder suspects, Floyd."
        musicplay[part]="mystery"
        part=4; speaker[part]="Commander"
        chat1[part]="However, his likely accomplices were the ones"
        chat2[part]="to grab him. Lenna and Winston, these are their"
        chat3[part]="names."
        part=5; speaker[part]="Commander"
        chat1[part]="All three are to be considered armed and"
        chat2[part]="dangerous."
        chat3[part]=""
        part=6; speaker[part]="Commander"
        chat1[part]="Your assignment is to find and capture all"
        chat2[part]="three of them. The safety of the citizens"
        chat3[part]="residing in this hotel depends on it."
        part=7; speaker[part]="Officers"
        chat1[part]="Sir, yes Sir!"
        chat2[part]=""
        chat3[part]=""
        part=8; speaker[part]="Commander"
        chat1[part]="Lucas, step forth."
        chat2[part]=""
        chat3[part]=""
        part=9
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=5
        part=10; speaker[part]="Lucas"
        chat1[part]="Sir."
        chat2[part]=""
        chat3[part]=""
        part=11; speaker[part]="Commander"
        chat1[part]="I know you're a newer recruit, but I want"
        chat2[part]="you in charge of this assignment."
        chat3[part]=""
        part=12; speaker[part]="Commander"
        chat1[part]="Your recent performance speaks for itself."
        chat2[part]=""
        chat3[part]=""
        part=13; speaker[part]="Lucas"
        chat1[part]="I won't disappoint you, Commander."
        chat2[part]=""
        chat3[part]=""
        part=14; speaker[part]="Commander"
        chat1[part]="Haha! No wonder you're my star pupil, the"
        chat2[part]="best Officer here no doubt!"
        chat3[part]=""
        part=15; speaker[part]="Commander"
        chat1[part]="You'll have command of this unit for your"
        chat2[part]="mission. I hope you'll be able to"
        chat3[part]="fulfill your assignment before morning."
        part=16; speaker[part]="Lucas"
        chat1[part]="Sir, yes Sir!"
        musicplay[part]="None"
        part=17
        changelevelpart=part; changelevelto="LevelMenu"; day=7; chapter+=1
    if (level=="Ambush"):
        dorandomizeItems=1
        selectx=10; camerax=selectx #Camera Position
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=9; npcy[npcc]=1; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Floyd"; npcx[npcc]=8; npcy[npcc]=1; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=2; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Shiv" #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=8; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=4; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=15; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        npcc=5; npc[npcc]=0; npcside[npcc]="Lucas"; npcx[npcc]=15; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1 #Create NPCs
        part=1
        partdelay[part]=100
        part=2
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=2
        part=3; speaker[part]="Winston"
        chat1[part]="This is the place."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="water"
        part=4
        createnpc[part]=1
        partdelay[part]=1
        part=5
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=3
        part=6; speaker[part]="Floyd"
        chat1[part]="The hotel's pool? Are you sure? There"
        chat2[part]="doesn't seem to be anyone here."
        chat3[part]=""
        part=7; speaker[part]="Winston"
        chat1[part]="This is where the message said to go."
        chat2[part]="Someone is supposed to be here to help"
        chat3[part]="prove our innocence."
        part=8; speaker[part]="Floyd"
        chat1[part]="After that grand display at the riot"
        chat2[part]="earlier today? We'd be better off"
        chat3[part]="running away and starting new lives."
        part=9; speaker[part]="Winston"
        chat1[part]="Maybe they're just around one of those"
        chat2[part]="corners. Try..."
        chat3[part]=""
        choice1[part]="Checking the closer exit."; choice1go[part]=12 #Choices Given
        choice2[part]="Checking the further exit."; choice2go[part]=16
        part=12; speaker[part]="Floyd"
        chat1[part]="That one to the right? Well, if you say so."
        chat2[part]=""
        chat3[part]=""
        part=13
        movenpc[part]=1; movenpcx[part]=4; movenpcy[part]=7
        part=14; speaker[part]="Winston"
        chat1[part]="You see anyone?"
        chat2[part]=""
        chat3[part]=""
        part=15
        gotopart[part]=20 #End Choice 1
        part=16; speaker[part]="Floyd"
        chat1[part]="The one across the water? Well, if you say"
        chat2[part]="so."
        chat3[part]=""
        part=17
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=12
        part=18; speaker[part]="Winston"
        chat1[part]="You see anyone?"
        part=19
        gotopart[part]=20 #End Choice 2
        part=20; speaker[part]="Floyd"
        chat1[part]="There isn't anyone here."
        musicplay[part]="None"
        part=21; speaker[part]="Floyd"
        chat1[part]="But...no, wait. Here? Of all places?"
        part=22; speaker[part]="Winston"
        chat1[part]="Floyd? What is it?"
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=2
        part=23
        createnpc[part]=2
        partdelay[part]=60
        musicplay[part]="threefour"
        part=24
        createnpc[part]=3
        partdelay[part]=60
        part=25
        createnpc[part]=4
        partdelay[part]=60
        part=26; speaker[part]="Lucas"
        chat1[part]="They're here, get in position!"
        chat2[part]=""
        chat3[part]=""
        part=27; speaker[part]="Officer"
        chat1[part]="Get on the ground!"
        part=28; speaker[part]="Winston"
        chat1[part]="Get out of there, Floyd! Run!"
        chat2[part]=""
        chat3[part]=""
        part=29
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=13
        part=30; speaker[part]="Floyd"
        chat1[part]="I'm surrounded!"
        chat2[part]=""
        chat3[part]=""
        part=31
        controlChar=part
        part=39
        partdelay[part]=50
        part=40
        createnpc[part]=5
        partdelay[part]=1
        part=41; speaker[part]="Lucas"
        chat1[part]="Calling in...why is no one replying?"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=42; speaker[part]="Winston"
        chat1[part]="Hey, kid, aren't you a little young to be"
        chat2[part]="commanding your own unit?"
        chat3[part]=""
        part=43; speaker[part]="Lucas"
        chat1[part]="I...I..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="mystery"
        part=44; speaker[part]="Floyd"
        chat1[part]="Anyone ever to tell you to respect the"
        chat2[part]="elderly?"
        chat3[part]=""
        part=45; speaker[part]="Lucas"
        chat1[part]="Please, spare me!"
        chat2[part]=""
        chat3[part]=""
        part=46; speaker[part]="Winston"
        chat1[part]="Woah, woah, woah...calm down. We aren't going"
        chat2[part]="to hurt some kid."
        chat3[part]=""
        part=47; speaker[part]="Lucas"
        chat1[part]="Then what will you do with me?"
        chat2[part]=""
        chat3[part]=""
        part=48; speaker[part]="Floyd"
        chat1[part]="Winston, we should bring him with us. He might"
        chat2[part]="end up being useful."
        chat3[part]=""
        part=49; speaker[part]="Winston"
        chat1[part]="Are you implying we use him as blackmail?"
        chat2[part]=""
        chat3[part]=""
        part=50; speaker[part]="Floyd"
        chat1[part]="I'd prefer to eschew from a word with such a "
        chat2[part]="strong connotation, but yes, we could bargain "
        chat3[part]="for our safety."
        part=51; speaker[part]="Lucas"
        chat1[part]="I'm the son of the Commander himself, they'll"
        chat2[part]="come and save me!"
        chat3[part]=""
        part=52; speaker[part]="Winston"
        chat1[part]="The Commander? Even better."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=53
        changelevelpart=part; changelevelto="LevelMenu"; day=8; chapter+=1
        part=100; speaker[part]="Floyd"
        chat1[part]="How tragic."
        part=101
        gotopart[part]=110
        part=102; speaker[part]="Winston"
        chat1[part]="Floyd! Gah, I couldn't save you..."
        part=103
        gotopart[part]=110        
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Blackmail"):
        dorandomizeItems=0
        selectx=29; camerax=selectx #Camera Position
        selecty=14; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background 29/12 elevator door
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=29; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=33; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=28; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=30; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=25; npcy[npcc]=18; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=26; npcy[npcc]=17; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs        
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Lenna"
        chat1[part]="So who's this guy?"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="guitar"
        part=3; speaker[part]="Lucas"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        part=4; speaker[part]="Winston"
        chat1[part]="He sent us a fake message saying someone at"
        chat2[part]="the pool could help us, but it turned out to"
        chat3[part]="be an ambush."
        part=5; speaker[part]="Floyd"
        chat1[part]="We brought him along because I thought he might"
        chat2[part]="be useful in getting the Commander to comply with"
        chat3[part]="us. He says he's the Commander's son."
        part=6; speaker[part]="Lucas"
        chat1[part]="...Yeah, well, they're going to save me."
        chat2[part]=""
        chat3[part]=""
        part=7; speaker[part]="Lenna"
        chat1[part]="Oh shut up, kid."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=32; movenpcy[part]=13
        part=8; speaker[part]="Lucas"
        chat1[part]="Ah, don't hit me!"
        chat2[part]=""
        chat3[part]=""
        part=9; speaker[part]="Lenna"
        chat1[part]="And he's really the best Officer they had?"
        chat2[part]="Kind of a baby if you ask me."
        chat3[part]=""
        part=10; speaker[part]="Lucas"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        part=11; speaker[part]="Winston"
        chat1[part]="It doesn't matter. This could be our best chance"
        chat2[part]="at negotiation."
        chat3[part]=""
        part=12; speaker[part]="Floyd"
        chat1[part]="I'll send a message to the Commander. In return"
        chat2[part]="for letting us leave freely, we give him back"
        chat3[part]="his favorite son."
        part=13; speaker[part]="Winston"
        chat1[part]="Sounds good."
        part=14; speaker[part]="Winston"
        chat1[part]="*Sigh* Man, what a day. Let's head to sleep."
        chat2[part]="Hopefully, we'll have our names cleared by"
        chat3[part]="the end of tomorrow."
        part=15; speaker[part]="Lenna"
        chat1[part]="Let's go, kid. I'm gonna keep at eye on you"
        chat2[part]="tonight."
        chat3[part]=""
        part=16; speaker[part]="Lucas"
        chat1[part]="I...can you at least not call me \"Kid\""
        chat2[part]="anymore? My name's Lucas."
        chat3[part]=""
        musicplay[part]="None"
        part=17
        changelevelpart=part; changelevelto="LevelMenu"; day=9; chapter+=1
    if (level=="Ruth1"):
        dorandomizeItems=0
        selectx=29; camerax=selectx #Camera Position
        selecty=14; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background 29/12 elevator door
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=25; npcy[npcc]=15; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Ruth"; npcx[npcc]=25; npcy[npcc]=22; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs     
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=24; movenpcy[part]=20
        part=3
        partdelay[part]=60
        part=4; speaker[part]="Winston"
        chat1[part]="Hey."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="calm"
        part=5
        partdelay[part]=60
        part=6; speaker[part]="Ruth"
        chat1[part]="Winston? What are you doing here?"
        part=7
        movenpc[part]=0; movenpcx[part]=24; movenpcy[part]=21
        part=8
        movenpc[part]=0; movenpcx[part]=24; movenpcy[part]=22
        part=9; speaker[part]="Winston"
        chat1[part]="I...um, I just, well..."
        part=10; speaker[part]="Winston"
        chat1[part]="You know that you don't have to help us. Every"
        chat2[part]="moment you're here, your life is in danger..."
        chat3[part]=""
        part=11; speaker[part]="Ruth"
        chat1[part]="Winston, I know. But I don't care."
        part=12; speaker[part]="Winston"
        chat1[part]="So then, why?"
        chat2[part]=""
        chat3[part]=""
        part=13; speaker[part]="Ruth"
        chat1[part]="Winston, today isn't the first day we've met."
        chat2[part]=""
        chat3[part]=""
        part=14; speaker[part]="Winston"
        chat1[part]="Huh?"
        part=15; speaker[part]="Ruth"
        chat1[part]="Remember when I told you I work as a nurse"
        chat2[part]="at the medical center?"
        part=16; speaker[part]="Winston"
        chat1[part]="I've never had the best memory. I think you"
        chat2[part]="mentioned it..."
        part=17; speaker[part]="Ruth"
        chat1[part]="But that's not the whole truth. I actually"
        chat2[part]="work multiple jobs."
        chat3[part]=""
        part=18; speaker[part]="Ruth"
        chat1[part]="I knew you had a kind heart the moment I"
        chat2[part]="opened your door. Room 417 - This room."
        chat3[part]=""
        part=19; speaker[part]="Winston"
        chat1[part]="You were the porter...?"
        chat2[part]=""
        part=20
        movenpc[part]=1; movenpcx[part]=24; movenpcy[part]=21
        part=21; speaker[part]="Ruth"
        chat1[part]="I trust you aren't the killer,"
        chat2[part]="Winston...I'll talk to you later."
        chat3[part]=""
        part=22
        movenpc[part]=1; movenpcx[part]=24; movenpcy[part]=20
        part=23
        createnpc[part]=-1
        partdelay[part]=200
        part=24; speaker[part]="Winston"
        chat1[part]="At least one good thing has come out of all of"
        chat2[part]="this."
        chat3[part]=""
        musicplay[part]="None"
        part=25
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Break"):
        item[0]="Bottle"; itemx[0]=31-19; itemy[0]=9-4
        dorandomizeItems=1
        selectx=29-19; camerax=selectx #Camera Position
        selecty=14-4; cameray=selecty; gx=19; gy=4
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=26-gx; npcy[npcc]=19-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=32-gx; npcy[npcc]=9-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=26-gx; npcy[npcc]=6-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=8; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=33-gx; npcy[npcc]=6-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=33-gx; npcy[npcc]=5-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=4; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=24-gx; npcy[npcc]=5-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs
        npcc=5; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=24-gx; npcy[npcc]=22-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Wrench" #Create NPCs
        npcc=6; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=34-gx; npcy[npcc]=21-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs
        part=1
        partdelay[part]=100
        part=2; speaker[part]="Winston"
        chat1[part]="Something feels...ominous."
        musicplay[part]="ambient"
        part=3
        partdelay[part]=100
        part=4; speaker[part]="Floyd"
        chat1[part]="I can almost make out a person's silhouette"
        chat2[part]="outside this window. Is it...climbing up?"
        chat3[part]=""
        part=5
        partdelay[part]=100
        part=6; speaker[part]="Lucas"
        chat1[part]="They'll come, you'll see! Y-you guys are"
        chat2[part]="terrorists! The Commander told us that you killed"
        chat3[part]="an innocent man two nights ago!"
        part=7; speaker[part]="Lenna"
        chat1[part]="How many times do I need to tell you that we"
        chat2[part]="DIDN'T kill him!? And your Officer friends? Well,"
        chat3[part]="yeah, but we're just trying to defend ourselves!"
        musicplay[part]="None"
        part=8; speaker[part]="Lucas"
        chat1[part]="...But the news said tha-"
        chat2[part]=""
        chat3[part]=""
        part=10
        createnpc[part]=3
        partdelay[part]=1
        part=9
        movenpc[part]=3; movenpcx[part]=32-gx; movenpcy[part]=5-gy
        part=11; speaker[part]="Officer"
        chat1[part]="Calling in: I've found the Commander's"
        chat2[part]="son. Room 415. I repeat: break into Room 415."
        chat3[part]=""
        musicplay[part]="action"
        part=12; speaker[part]="Lenna"
        chat1[part]="Woah! Back up, Lucas."
        part=13; speaker[part]="Lucas"
        chat1[part]="Ha! I knew it!"
        movenpc[part]=3; movenpcx[part]=32-gx; movenpcy[part]=6-gy
        part=14; speaker[part]="Officer"
        chat1[part]="The Commander understands you intend to"
        chat2[part]="bargain with his son."
        chat3[part]=""
        part=15
        partdelay[part]=1
        part=16; speaker[part]="Officer"
        chat1[part]="Calling in: I've found one of the culprits. I'm"
        chat2[part]="going to neutralize her before she can hurt Lucas."
        part=17; speaker[part]="Lucas"
        chat1[part]="What!? But what about capturing her first?"
        chat2[part]="Y-you can't just kill her like this! H-help!"
        chat3[part]=""
        part=18; speaker[part]="Floyd"
        chat1[part]="Now what's all that ruckus?"
        movenpc[part]=2; movenpcx[part]=26-gx; movenpcy[part]=7-gy
        part=19; speaker[part]="Lenna"
        chat1[part]="Gah! Floyd, Winston, I need some help over"
        chat2[part]="here!"
        chat3[part]=""
        part=20 #NPCs appear at the windows
        movenpc[part]=4; movenpcx[part]=23-gx; movenpcy[part]=5-gy
        part=21
        createnpc[part]=4
        partdelay[part]=50
        part=22
        movenpc[part]=4; movenpcx[part]=23-gx; movenpcy[part]=6-gy
        part=23
        movenpc[part]=5; movenpcx[part]=24-gx; movenpcy[part]=21-gy
        part=24
        createnpc[part]=5
        partdelay[part]=50
        part=25
        movenpc[part]=5; movenpcx[part]=24-gx; movenpcy[part]=20-gy
        part=26
        movenpc[part]=6; movenpcx[part]=35-gx; movenpcy[part]=21-gy
        part=27
        createnpc[part]=6
        partdelay[part]=50
        part=28
        movenpc[part]=6; movenpcx[part]=35-gx; movenpcy[part]=20-gy
        part=29; speaker[part]="Lucas"
        chat1[part]="(What do I do? How can I...)"
        chat2[part]=""
        chat3[part]=""
        part=30
        controlChar=part
        part=40
        partdelay[part]=50
        part=41; speaker[part]="Lucas"
        chat1[part]="Lenna, are you okay?"
        chat2[part]=""
        chat3[part]=""
        part=42; speaker[part]="Lenna"
        chat1[part]="What was that all about? You attacked your"
        chat2[part]="own team!"
        chat3[part]=""
        part=43; speaker[part]="Lucas"
        chat1[part]="I...I didn't want to. I had to...I didn't want"
        chat2[part]="any one of you to die."
        chat3[part]=""
        part=44; speaker[part]="Winston"
        chat1[part]="Guys, talk later! Get in the elevator, we're"
        chat2[part]="getting out of here before more of them come!"
        chat3[part]=""
        musicplay[part]="None"
        part=45
        changelevelpart=part; changelevelto="LevelMenu"; day=10; chapter+=1
        part=100; speaker[part]="Officer"
        chat1[part]="One target eliminated. Lucas, you've been"
        chat2[part]="ordered to follow us and report to the"
        chat3[part]="Commander."
        part=101; speaker[part]="Lucas"
        chat1[part]="Understood..."
        chat2[part]=""
        chat3[part]=""
        part=102
        gotopart[part]=110
        part=105; speaker[part]="Lucas"
        chat1[part]="No! She was innocent!"
        chat2[part]=""
        chat3[part]=""
        part=106; speaker[part]="Officer"
        chat1[part]="Mission objective updated. Eliminate the remaining"
        chat2[part]="targets and bring Lucas to the Commander as soon"
        chat3[part]="as possible."
        part=107
        gotopart[part]=110
        part=108; speaker[part]="Lenna"
        chat1[part]="Looks like bargaining wasn't a good idea, guys."
        chat2[part]="Lucas just took a pretty bad hit..."
        chat3[part]=""
        part=109
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Split"):
        dorandomizeItems=0
        selectx=4; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=6; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=5; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs     
        npcc=2; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=5; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs     
        npcc=3; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=5; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Baton" #Create NPCs     
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=10
        part=3; speaker[part]="Lenna"
        chat1[part]="Come on, let's go!"
        musicplay[part]="ambient"
        part=4; speaker[part]="Lucas"
        chat1[part]="Lenna, slow down!"
        part=5
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=12
        part=6; speaker[part]="Lenna"
        chat1[part]="What, so they can find us again and"
        chat2[part]="kill you for backstabbing them?"
        chat3[part]=""
        part=7; speaker[part]="Lucas"
        chat1[part]="I saved your life! And I'm not on anyone's"
        chat2[part]="\"side\", all right? I just did what was right"
        chat3[part]="at the moment."
        movenpc[part]=2; movenpcx[part]=5; movenpcy[part]=13
        part=8; speaker[part]="Winston"
        chat1[part]="Um, hey guys...Floyd?"
        part=9; speaker[part]="Lucas"
        chat1[part]="Sometimes you're put into a situation where"
        chat2[part]="you need to hurt someone to help others."
        chat3[part]="Does it matter who's \"side\" I'm on!?"
        part=10; speaker[part]="Lenna"
        chat1[part]="Well...thanks for saving me then, I guess."
        chat2[part]=""
        chat3[part]=""
        part=11; speaker[part]="Winston"
        chat1[part]="Guys! Where's Floyd!?"
        chat2[part]=""
        chat3[part]=""
        part=12; speaker[part]="Lenna"
        chat1[part]="He's right over- Huh? I swear he went down"
        chat2[part]="the elevator with us."
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=10
        part=13; speaker[part]="Lucas"
        chat1[part]="Maybe he went further ahead?"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=14; speaker[part]="Lenna"
        chat1[part]="I'll check it out."
        chat2[part]=""
        chat3[part]=""
        part=15
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=2
        part=16
        createnpc[part]=-1
        partdelay[part]=10
        part=17; speaker[part]="Winston"
        chat1[part]="Lenna, wait for us!"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=6; movenpcy[part]=12
        part=18
        movenpc[part]=3; movenpcx[part]=5; movenpcy[part]=8
        part=19
        createnpc[part]=3
        partdelay[part]=50
        part=20; speaker[part]="Officer"
        chat1[part]="Lucas! What are you doing? Get away from the"
        chat2[part]="killer!"
        chat3[part]=""
        musicplay[part]="threefour"
        part=21; speaker[part]="Lucas"
        chat1[part]="I don't want to work with security anymore. Get"
        chat2[part]="away from me!"
        chat3[part]=""
        part=22; speaker[part]="Officer"
        chat1[part]="Then I'll force you apart!"
        chat2[part]=""
        chat3[part]=""
        part=23
        controlChar=part
        part=40
        partdelay[part]=50
        part=41
        partdelay[part]=50
        part=42; speaker[part]="Lucas"
        chat1[part]="..."
        part=43; speaker[part]="Winston"
        chat1[part]="Come on, let's get out of here. We can"
        chat2[part]="talk later."
        chat3[part]=""
        musicplay[part]="None"
        part=44
        changelevelpart=part; changelevelto="LevelMenu"; day=11; chapter+=1
        part=100; speaker[part]="Lucas"
        chat1[part]="You crook! Get your hands off me!"
        chat2[part]=""
        chat3[part]=""
        part=101
        gotopart[part]=110
        part=102; speaker[part]="Winston"
        chat1[part]="Lucas? What did we do to get into this mess...?"
        chat2[part]=""
        chat3[part]=""
        part=103
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Main"):
        dorandomizeItems=0
        selectx=9; camerax=selectx #Camera Position EnterGrayDoor 12,11
        selecty=11; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=11; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=14; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs             part=1
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=1; movenpcx[part]=11; movenpcy[part]=11
        part=3
        partdelay[part]=50
        part=4; speaker[part]="Lucas"
        chat1[part]="A maintenance shaft? I thought when you said"
        chat2[part]="you knew about a nice hiding spot, it'd actually"
        chat3[part]="be \"nice\"."
        musicplay[part]="mystery"
        part=5; speaker[part]="Winston"
        chat1[part]="At least it's safe. We can't return to our hotel"
        chat2[part]="floor. Seems like everyone knew we were camping out"
        chat3[part]="up there."
        movenpc[part]=0; movenpcx[part]=11; movenpcy[part]=10
        part=6; speaker[part]="Lucas"
        chat1[part]="So what do we do now? Where do we go?"
        chat2[part]=""
        chat3[part]=""
        part=7; speaker[part]="Winston"
        chat1[part]="First things first, we need to find Lenna and"
        chat2[part]="Floyd."
        chat3[part]=""
        part=8; speaker[part]="Winston"
        chat1[part]="Then, after we find them, well...I don't think"
        chat2[part]="the Officers'll just forget about all the violence"
        chat3[part]="we've carried out."
        part=9; speaker[part]="Lucas"
        chat1[part]="And they're probably not going to be too"
        chat2[part]="friendly with me either, huh?"
        chat3[part]=""
        musicplay[part]="None"
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=13
        part=10
        partdelay[part]=70
        part=11; speaker[part]="Lucas"
        chat1[part]="...Let's escape the hotel."
        musicplay[part]="scary"
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=13
        part=12; speaker[part]="Winston"
        chat1[part]="Escape!? And how do you plan on doing that?"
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=10
        part=13; speaker[part]="Lucas"
        chat1[part]="I don't know. Any ideas?"
        part=14; speaker[part]="Winston"
        chat1[part]="How about, not that?"
        part=15; speaker[part]="Lucas"
        chat1[part]="I was thinking, maybe we could try brute"
        chat2[part]="forcing our way out."
        chat3[part]=""
        part=16; speaker[part]="Lucas"
        chat1[part]="We could head straight to the bottom floor"
        chat2[part]="and fight our way out the front entrance."
        chat3[part]=""
        part=17; speaker[part]="Winston"
        chat1[part]="Do you not hear how crazy that sounds!? It's"
        chat2[part]="a last resort, for sure."
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=10
        part=18; speaker[part]="Lucas"
        chat1[part]="We'd need a lot of man-power to fight an army"
        chat2[part]="that size, for sure."
        chat3[part]=""
        part=19; speaker[part]="Winston"
        chat1[part]="We'll find a better way. Let's rest a little,"
        chat2[part]="then we'll head out looking for Lenna and Floyd."
        chat3[part]=""
        part=20; speaker[part]="Lucas"
        chat1[part]="...If they're still alive..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=21
        changelevelpart=part; changelevelto="LevelMenu"; day=12; chapter+=1
    if (level=="Twins"):
        dorandomizeItems=0
        selectx=9; camerax=selectx #Camera Position
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 14/4 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=14; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs     
        npcc=1; npc[npcc]=1; npcside[npcc]="Adam"; npcx[npcc]=6; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs     
        npcc=2; npc[npcc]=1; npcside[npcc]="Evelyn"; npcx[npcc]=10; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Sanders"; npcx[npcc]=5; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs  
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=14; movenpcy[part]=6
        part=3; speaker[part]="Winston"
        chat1[part]="Maybe one of them has seen Lenna or Floyd."
        part=4
        movenpc[part]=0; movenpcx[part]=11; movenpcy[part]=9
        part=5; speaker[part]="Winston"
        chat1[part]="Uh, hello?"
        chat2[part]=""
        chat3[part]=""
        part=6
        movenpc[part]=2; movenpcx[part]=10; movenpcy[part]=10
        part=7; speaker[part]="Evelyn"
        chat1[part]="Oh! I didn't see you there."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="standby"
        part=8
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=9
        part=9; speaker[part]="Adam"
        chat1[part]="Who's this guy?"
        part=10; speaker[part]="Winston"
        chat1[part]="I'm Winston. I was wondering if either"
        chat2[part]="of you had seen a blond haired girl - about"
        chat3[part]="yay tall - or an old man with a weird hat."
        part=11; speaker[part]=" "
        chat1[part]="Winston describes Lenna and Floyd."
        chat2[part]=""
        chat3[part]=""
        part=12; speaker[part]="Evelyn"
        chat1[part]="Sorry, but I haven't seen either one of them."
        chat2[part]="Actually, me and Adam are looking for something we"
        chat3[part]="lost ourselves."
        part=13; speaker[part]="Adam"
        chat1[part]="Woah, sis! Don't go blabbing about it!"
        chat2[part]=""
        chat3[part]=""
        part=14; speaker[part]="Evelyn"
        chat1[part]="Quiet! He might be able to help us."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=8; movenpcy[part]=10
        part=15; speaker[part]="Evelyn"
        chat1[part]="Ahem, Winston, was it?"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=10; movenpcy[part]=10
        part=16; speaker[part]="Evelyn"
        chat1[part]="How about this. We'll help you find your"
        chat2[part]="friends, and in return, you help us find"
        chat3[part]="what we're looking for."
        part=17; speaker[part]="Winston"
        chat1[part]="Sounds like a deal."
        part=18; speaker[part]="Winston"
        chat1[part]="But, what exactly ARE you looking for?"
        part=19; speaker[part]="Adam"
        chat1[part]="You'll find out soon enough. Just make sure"
        chat2[part]="you keep us safe, you know? If one of us dies"
        chat3[part]="we'll never find it."
        musicplay[part]="None"
        part=20
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Matthew"):
        dorandomizeItems=0
        selectx=9; camerax=selectx #Camera Position
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 14/4 elevator door
        npcc=0; npc[npcc]=0; npcside[npcc]="Man"; npcx[npcc]=1; npcy[npcc]=1; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs     
        npcc=3; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=9; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs     
        npcc=2; npc[npcc]=1; npcside[npcc]="Matthew"; npcx[npcc]=12; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; npcheld[npcc]="Med Kit" #Create NPCs     
        npcc=1; npc[npcc]=0; npcside[npcc]="Sanders "; npcx[npcc]=6; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Matthew"
        chat1[part]="I'm sorry Winston, but I haven't seen either"
        chat2[part]="of them. They haven't visited my clinic."
        chat3[part]=""
        musicplay[part]="standby"
        part=3; speaker[part]="Winston"
        chat1[part]="Contact me if you hear any word of them."
        chat2[part]="Thanks again."
        chat3[part]=""
        part=4
        movenpc[part]=3; movenpcx[part]=8; movenpcy[part]=7
        musicplay[part]="None"
        part=5
        movenpc[part]=3; movenpcx[part]=7; movenpcy[part]=7
        part=6
        movenpc[part]=3; movenpcx[part]=3; movenpcy[part]=4
        part=7
        createnpc[part]=-3
        partdelay[part]=50
        part=8
        createnpc[part]=1
        partdelay[part]=1
        part=9
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=7
        part=10
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=7
        part=11; speaker[part]="Sanders"
        chat1[part]="Matthew... How are you doing?"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="scary"
        part=12; speaker[part]="Matthew"
        chat1[part]="Here for another go, Sanders?"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=7
        part=13; speaker[part]="Sanders"
        chat1[part]="He-he! But, O Doctor, wouldn't it be in your best"
        chat2[part]="interest to charge your patients a little more?"
        chat3[part]=""
        part=14; speaker[part]="Sanders"
        chat1[part]="I'm not getting a large enough cut from your"
        chat2[part]="business...And I don't think your suppliers"
        chat3[part]="are very happy!"
        part=15; speaker[part]="Matthew"
        chat1[part]="For the last time, I'm not going to deny"
        chat2[part]="care to any one."
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=11; movenpcy[part]=8
        part=16; speaker[part]="Sanders"
        chat1[part]="Am I going to have to do it the hard way again,"
        chat2[part]="Matthew? Business doesn't work this way!"
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=7
        part=17; speaker[part]="Matthew"
        chat1[part]="You devil!"
        part=18
        createnpc[part]=3
        partdelay[part]=10
        part=19
        movenpc[part]=3; movenpcx[part]=5; movenpcy[part]=4
        part=20; speaker[part]="Winston"
        chat1[part]="Matthew? I'm coming!"
        part=21
        controlChar=part
        part=40
        partdelay[part]=50
        part=41; speaker[part]="Matthew"
        chat1[part]="Winston, that's enough!"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=42
        createnpc[part]=-1
        partdelay[part]=15
        part=43; speaker[part]="Winston"
        chat1[part]="Matthew, are you okay!? That guy...he got"
        chat2[part]="away."
        part=44; speaker[part]="Matthew"
        chat1[part]="I'm fine...just let him go for now."
        part=45; speaker[part]="Winston"
        chat1[part]="Who was that, even?"
        part=46; speaker[part]="Matthew"
        chat1[part]="His name is Sanders. He's a rich tycoon"
        chat2[part]="who preys on organizations he thinks aren't"
        chat3[part]="doing enough for him."
        part=47; speaker[part]="Matthew"
        chat1[part]="Sanders practically owns this hotel."
        chat2[part]=""
        chat3[part]=""
        part=48; speaker[part]="Winston"
        chat1[part]="I see."
        part=49; speaker[part]="Matthew"
        chat1[part]="Winston, I want to come with you."
        musicplay[part]="standby"
        part=50; speaker[part]="Winston"
        chat1[part]="Huh?"
        chat2[part]=""
        chat3[part]=""
        part=51; speaker[part]="Matthew"
        chat1[part]="You've done me a favor. Now, I want to help"
        chat2[part]="you find your friends."
        chat3[part]=""
        part=52; speaker[part]="Matthew"
        chat1[part]="I have plenty of supplies. I should be able"
        chat2[part]="to heal all of your injuries at least once."
        chat3[part]=""
        part=53; speaker[part]="Winston"
        chat1[part]="It's a deal, Doctor."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=54
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        part=100; speaker[part]="Winston"
        chat1[part]="Matthew! Who is this guy!?"
        chat2[part]=""
        chat3[part]=""
        part=101
        musicplay[part]="None"
        failurepart=part
    if (level=="Jerry"):
        dorandomizeItems=0
        selectx=12; camerax=selectx #Camera Position
        selecty=12; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 14/4 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=8; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs     
        npcc=1; npc[npcc]=0; npcside[npcc]="Winston"; npcx[npcc]=7; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs     
        npcc=2; npc[npcc]=1; npcside[npcc]="Thug"; npcx[npcc]=20; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="" #Create NPCs     
        npcc=3; npc[npcc]=1; npcside[npcc]="Jerry"; npcx[npcc]=20; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs     
        npcc=4; npc[npcc]=0; npcside[npcc]="Thug"; npcx[npcc]=17; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Wrench"  #Create NPCs     
        #npcc=5; npc[npcc]=0; npcside[npcc]="Thug"; npcx[npcc]=17; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv"  #Create NPCs     
        npcc=5; npc[npcc]=0; npcside[npcc]="Thug"; npcx[npcc]=19; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Shiv"  #Create NPCs     
        npcc=6; npc[npcc]=0; npcside[npcc]="Thug"; npcx[npcc]=19; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Bottle"  #Create NPCs     
        part=1
        partdelay[part]=50
        part=2
        movenpc[part]=0; movenpcx[part]=8; movenpcy[part]=10
        part=3; speaker[part]="Lucas"
        chat1[part]="Huh?"
        musicplay[part]="ambient"
        part=4
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=10
        part=5
        partdelay[part]=50
        part=6; speaker[part]="Thug"
        chat1[part]="So you really think it's him?"
        chat2[part]=""
        chat3[part]=""
        part=7; speaker[part]="Man"
        chat1[part]="Of course. Those Officers would pay a hefty"
        chat2[part]="sum for him."
        chat3[part]=""
        part=8; speaker[part]="Thug"
        chat1[part]="But Jerry - er, I mean, Boss...how do ya know"
        chat2[part]="they'll pay to get'im?"
        chat3[part]=""
        part=9; speaker[part]="Jerry"
        chat1[part]="Quiet! My plan is flawless! Just make sure the"
        chat2[part]="captive stays captured this time!"
        chat3[part]=""
        part=10; speaker[part]="Thug"
        chat1[part]="Whatevah ya say, Boss."
        chat2[part]=""
        chat3[part]=""
        part=11
        movenpc[part]=3; movenpcx[part]=19; movenpcy[part]=12
        part=12
        movenpc[part]=3; movenpcx[part]=19; movenpcy[part]=13
        part=13
        movenpc[part]=3; movenpcx[part]=18; movenpcy[part]=15
        part=14
        movenpc[part]=2; movenpcx[part]=17; movenpcy[part]=11
        part=15; speaker[part]="Lucas"
        chat1[part]="(Floyd!?)"
        part=16
        movenpc[part]=0; movenpcx[part]=8; movenpcy[part]=11
        part=17
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=11
        part=18
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=12
        part=19; speaker[part]="Lucas"
        chat1[part]="Winston!"
        part=20
        createnpc[part]=1
        partdelay[part]=50
        part=21
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=16
        part=22
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=14
        part=23; speaker[part]="Winston"
        chat1[part]="I heard."
        part=24; speaker[part]="Lucas"
        chat1[part]="Whatever we do, their Boss, Jerry, needs to"
        chat2[part]="remain alive to tell us where Floyd is"
        chat3[part]="being kept."
        musicplay[part]="None"
        part=25
        createnpc[part]=4
        partdelay[part]=1
        musicplay[part]="threefour"
        part=26
        createnpc[part]=5
        partdelay[part]=1
        part=27
        createnpc[part]=6
        partdelay[part]=1
        part=28
        #createnpc[part]=7
        partdelay[part]=1  
        part=29
        controlChar=part
        part=40; speaker[part]="Lucas"
        chat1[part]="Jerry, tell me where Floyd is!"
        chat2[part]=""
        chat3[part]=""
        part=41; speaker[part]="Jerry"
        chat1[part]="Woah, woah! Hold on there, kiddo. Can't we just"
        chat2[part]="talk about this?"
        chat3[part]=""
        musicplay[part]="None"
        part=42; speaker[part]="Lucas"
        chat1[part]="Look around you, Jerry. Don't make this hard."
        chat2[part]=""
        chat3[part]=""
        part=43; speaker[part]="Jerry"
        chat1[part]="Hehehe...of course. Your friend - I presume he"
        chat2[part]="is your friend - is being taken care, don't you"
        chat3[part]="worry..."
        part=44; speaker[part]="Lucas"
        chat1[part]="Tell me where he is or I-I'll kill you!"
        musicplay[part]="scary"
        part=45; speaker[part]="Winston"
        chat1[part]="Lucas, calm down! He's going to tell us!"
        part=46; speaker[part]="Winston"
        chat1[part]="Man..."
        part=47; speaker[part]="Jerry"
        chat1[part]="All right, already! H-He's locked up tight three"
        chat2[part]="floors up! Just p-please, don't hurt me!"
        chat3[part]=""
        part=48; speaker[part]="Lucas"
        chat1[part]="You heard him, let's get going."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=49
        changelevelpart=part; changelevelto="LevelMenu"; day=13; chapter+=1
        part=100; speaker[part]="Winston"
        chat1[part]="Lucas, stay with me!"
        chat2[part]=""
        chat3[part]=""
        part=101
        gotopart[part]=110
        part=102; speaker[part]="Lucas"
        chat1[part]="Winston, I promise I'll save Floyd...even if"
        chat2[part]="you don't make it."
        chat3[part]=""
        part=103
        gotopart[part]=110
        part=104; speaker[part]="Jerry"
        chat1[part]="With me gone...you'll never...find, *cough*"
        chat2[part]="...find out where the captive is...!"
        chat3[part]=""
        part=105
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Questions"):
        dorandomizeItems=0
        selectx=9; camerax=selectx #Camera Position EnterGrayDoor 12,11
        selecty=11; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=14; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=10; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=6; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=8; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=9
        part=3; speaker[part]="Winston"
        chat1[part]="Hey, Lucas."
        part=4; speaker[part]="Lucas"
        chat1[part]="Hey."
        musicplay[part]="mystery"
        part=5; speaker[part]="Winston"
        chat1[part]="You know, you've changed a lot."
        part=6; speaker[part]="Winston"
        chat1[part]="You were the shy one when you joined us."
        chat2[part]="That's not a bad thing, but you've grown..."
        chat3[part]="differently...just so, quickly."
        part=7; speaker[part]="Lucas"
        chat1[part]="So would that make you the shy one now?"
        chat2[part]=""
        chat3[part]=""
        part=8; speaker[part]="Lucas"
        chat1[part]="Winston, I've had a change of heart. I really"
        chat2[part]="have."
        chat3[part]=""
        part=9; speaker[part]="Winston"
        chat1[part]="Do you think that you could maybe, I don't"
        chat2[part]="know, tone down some of the aggression?"
        chat3[part]=""
        part=10
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=11
        part=11; speaker[part]="Lucas"
        chat1[part]="Tone down the \"aggression\"!? Winston, I was"
        chat2[part]="forced to betray my friends! My Commander!"
        chat3[part]="And now, I'm an outcast."
        part=12; speaker[part]="Lucas"
        chat1[part]="The question should be, how are you NOT angry!?"
        chat2[part]="You've been wrongly convicted! We can't even"
        chat3[part]="figure out a way out of this hotel!"
        part=13; speaker[part]="Lucas"
        chat1[part]="But that could all be forgiven...overlooked..."
        chat2[part]="If, just if...the Officers weren't just so wrong."
        chat3[part]="So wrong about their methods..."
        part=14; speaker[part]="Lucas"
        chat1[part]="So wrong about who they're even trying to kill!"
        chat2[part]="I...I hate them! I hate those corrupt, power-"
        chat3[part]="hungry phonies!"
        part=15; speaker[part]="Winston"
        chat1[part]="..."
        part=16; speaker[part]="Lucas"
        chat1[part]="Tell me, do you believe that you should be able to"
        chat2[part]="live above the law...if the law is wrong in your"
        chat3[part]="eyes?"
        choice1[part]="Yes"; choice1go[part]=20 #Choices Given
        choice2[part]="No"; choice2go[part]=25
        part=20; speaker[part]="Winston"  #Choice 1
        chat1[part]="Yes, I understand what you mean..."
        chat2[part]=""
        chat3[part]=""
        part=21; speaker[part]="Lucas"
        chat1[part]="Two days ago, I would have disagreed."
        chat2[part]="But...the law is imperfect, it needs"
        chat3[part]="reform."
        part=22
        gotopart[part]=29
        part=25; speaker[part]="Winston"  #Choice 2
        chat1[part]="No...I-I think that the law is not something"
        chat2[part]="meant to be broken."
        chat3[part]=""
        part=26; speaker[part]="Lucas"
        chat1[part]="I disagree, the law is imperfect! Shouldn't"
        chat2[part]="we stand up for what we believe is right!?"
        chat3[part]=""
        part=27
        gotopart[part]=29
        part=29; speaker[part]="Lucas"
        chat1[part]="I now understand that the law shouldn't determine"
        chat2[part]="right and wrong...people decide their own morals,"
        chat3[part]="their own rights and wrongs! Don't you agree?"
        choice1[part]="Yes"; choice1go[part]=30 #Choices Given
        choice2[part]="No"; choice2go[part]=35
        part=30; speaker[part]="Winston" #Choice 1
        chat1[part]="Of course, I don't believe in absolutes."
        chat2[part]=""
        chat3[part]=""
        part=31; speaker[part]="Lucas"
        chat1[part]="Yes, absolute truth! What a lie! How can we"
        chat2[part]="know what the absolute truth even is? How?"
        chat3[part]="We can't...everyone has different \"truths\"."
        part=32
        gotopart[part]=39
        part=35; speaker[part]="Winston" #Choice 2
        chat1[part]="No, I believe that it's absolute. Right and wrong"
        chat2[part]="does not change..."
        chat3[part]=""
        part=36; speaker[part]="Lucas"
        chat1[part]="But shouldn't people decide their own"
        chat2[part]="truths?"
        chat3[part]=""
        part=37
        gotopart[part]=39
        part=39; speaker[part]="Lucas"
        chat1[part]="If you feel the ends justify the means, go for"
        chat2[part]="it. Would you kill a murderer, knowing if you"
        chat3[part]="didn't, they'd continue to murdering?"
        part=40; speaker[part]="Lucas"
        chat1[part]="Would you break the law, knowing you could"
        chat2[part]="create a new, better law in it's place? I would..."
        chat3[part]=""
        part=40; speaker[part]="Lucas"
        chat1[part]="...So let's break our way out of this hotel. We'll"
        chat2[part]="fight our way out! We'll destroy the law! Are you up"
        chat3[part]="for it, Winston?"
        choice1[part]="Yes"; choice1go[part]=41 #Choices Given
        choice2[part]="No"; choice2go[part]=45
        part=41; speaker[part]="Winston"
        chat1[part]="That's looking like a pretty good option..."
        chat2[part]="But for now, let's focus on saving Floyd."
        chat3[part]=""
        part=42
        gotopart[part]=50
        part=45; speaker[part]="Winston"
        chat1[part]="I don't think that's a good idea...We need to focus"
        chat2[part]="on saving Floyd."
        chat3[part]=""
        part=46
        gotopart[part]=50
        part=50; speaker[part]="Lucas"
        chat1[part]="Yes...sorry, I'm a bit overworked right now."
        chat2[part]="Come on, let's head out."
        chat3[part]=""
        musicplay[part]="None"
        part=51
        changelevelpart=part; changelevelto="LevelMenu"; day=14; chapter+=1
    if (level=="Ruth2"):
        dorandomizeItems=0
        selectx=9; camerax=selectx #Camera Position EnterGrayDoor 12,11
        selecty=11; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Ruth"; npcx[npcc]=5; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=5; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=6; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=8; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=9
        part=3; speaker[part]="Ruth"
        chat1[part]="Oh, Winston."
        musicplay[part]="calm"
        part=4
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=12
        part=5; speaker[part]="Winston"
        chat1[part]="Ruth?"
        part=6; speaker[part]="Ruth"
        chat1[part]="I heard your conversation with Lucas..."
        chat2[part]=""
        chat3[part]=""
        part=7; speaker[part]="Ruth"
        chat1[part]="Winston, don't tell me you agree with anything"
        chat2[part]="he says!"
        chat3[part]=""
        part=8
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=13
        part=9; speaker[part]="Winston"
        chat1[part]="Ruth...I don't know what I believe."
        chat2[part]=""
        chat3[part]=""
        part=10
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=10
        part=11; speaker[part]="Ruth"
        chat1[part]="I can't make your decisions for you, but I'd"
        chat2[part]="be careful around Lucas, he's changing. You've"
        chat3[part]="taken note of it, haven't you?"
        part=12; speaker[part]="Winston"
        chat1[part]="Then why are you still helping us?"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=12
        part=13
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=8
        part=14; speaker[part]="Ruth"
        chat1[part]="I'm here because I want to help you, Winston."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=15
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=5
        part=16
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Save"):
        dorandomizeItems=0
        selectx=8; camerax=selectx #Camera Position EnterGrayDoor 12,11
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background 29/12 elevator door
        npcc=0; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=10; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Winston"; npcx[npcc]=5; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Lucas"; npcx[npcc]=9; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Strangler"; npcx[npcc]=6; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Hammer" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Brute"; npcx[npcc]=8; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Thug"; npcx[npcc]=7; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Wrench" #Create NPCs
        npcc=6; npc[npcc]=1; npcside[npcc]="Thug"; npcx[npcc]=2; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Knife" #Create NPCs
        npcc=7; npc[npcc]=1; npcside[npcc]="Brute"; npcx[npcc]=14; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Hammer" #Create NPCs
        part=1
        partdelay[part]=1
        part=2; speaker[part]="Floyd"
        chat1[part]="Let me out of here!"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="ambient"
        part=3
        movenpc[part]=3; movenpcx[part]=6; movenpcy[part]=6
        part=4; speaker[part]="Thug"
        chat1[part]="Hey, quiet down, old man!"
        chat2[part]=""
        chat3[part]=""
        part=5; speaker[part]="Brute"
        chat1[part]="Let him yell...once the boss arrives"
        chat2[part]="we can finish the deal with those Officers."
        chat3[part]=""
        part=6; speaker[part]="Thug"
        chat1[part]="Pfff, Jerry shoulda been here an hour ago. He's"
        chat2[part]="really draggin' this deal out."
        chat3[part]=""
        movenpc[part]=3; movenpcx[part]=6; movenpcy[part]=7
        part=7; speaker[part]="Brute"
        chat1[part]="Doesn't matter, I'm gonna go keep a lookout."
        chat2[part]=""
        chat3[part]=""
        part=8
        movenpc[part]=4; movenpcx[part]=9; movenpcy[part]=11
        part=9
        movenpc[part]=4; movenpcx[part]=9; movenpcy[part]=12
        musicplay[part]="None"
        part=10
        movenpc[part]=4; movenpcx[part]=10; movenpcy[part]=12
        part=11
        partdelay[part]=60
        createnpc[part]=1
        part=12
        partdelay[part]=60
        createnpc[part]=2
        part=13
        partdelay[part]=50
        part=14; speaker[part]="Lucas"
        chat1[part]="This is the floor Jerry mentioned."
        part=15; speaker[part]="Winston"
        chat1[part]="Let's save Floyd."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="action"
        part=16
        controlChar=part
        part=30; speaker[part]="Lucas"
        chat1[part]="Haha! I've never felt so alive!"
        part=31; speaker[part]="Winston"
        chat1[part]="Floyd! Are you all right!?"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=32; speaker[part]="Floyd"
        chat1[part]="Yes...yes..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="guitar"
        part=33; speaker[part]="Lucas"
        chat1[part]="What happened to you?"
        chat2[part]=""
        chat3[part]=""
        part=32; speaker[part]="Floyd"
        chat1[part]="After we split, I was wandering around,"
        chat2[part]="looking for you both."
        chat3[part]=""
        part=33; speaker[part]="Floyd"
        chat1[part]="But, they found me first. They said there's a"
        chat2[part]="big price on my head... so, that was their"
        chat3[part]="motive."
        part=34; speaker[part]="Floyd"
        chat1[part]="At this point, who around here hasn't heard of"
        chat2[part]="us?"
        chat3[part]=""
        part=35; speaker[part]="Winston"
        chat1[part]="As long as you're okay. Let's get out of here."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=36
        changelevelpart=part; changelevelto="LevelMenu"; day=15; chapter+=1
        part=100; speaker[part]="Floyd"
        chat1[part]="Winston? Lucas!? Don't die! Not here!"
        chat2[part]=""
        chat3[part]=""
        part=101; speaker[part]="Thug"
        chat1[part]="Let's wrap this up, boys. They ain't so tough!"
        chat2[part]=""
        chat3[part]=""
        part=102
        gotopart[part]=110
        part=105; speaker[part]="Lucas"
        chat1[part]="Wha-? Tell me Floyd is okay..."
        chat2[part]=""
        chat3[part]=""
        part=106
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Gone"):
        dorandomizeItems=1
        selectx=9; camerax=selectx #Camera Position EnterGrayDoor 12,11
        selecty=11; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha()
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=16; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Floyd"; npcx[npcc]=16; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Lucas"; npcx[npcc]=16; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=6; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Knife"  #Create NPCs
        #npcc=4; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=9; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=5; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Hammer"  #Create NPCs
        #npcc=6; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=8; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Wrench"  #Create NPCs
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=15; movenpcy[part]=11
        part=3
        movenpc[part]=0; movenpcx[part]=12; movenpcy[part]=11
        part=4
        createnpc[part]=1
        partdelay[part]=1
        part=5
        movenpc[part]=1; movenpcx[part]=12; movenpcy[part]=12
        part=6; speaker[part]="Floyd"
        chat1[part]="Not here too..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="threefour"
        part=7
        createnpc[part]=2
        partdelay[part]=1
        part=8
        movenpc[part]=2; movenpcx[part]=13; movenpcy[part]=10
        part=9; speaker[part]="Lucas"
        chat1[part]="Officers!"
        part=10
        movenpc[part]=3; movenpcx[part]=7; movenpcy[part]=13
        part=11; speaker[part]="Officer"
        chat1[part]="Calling in: You were right! Lucas just entered"
        chat2[part]="the room!"
        chat3[part]=""
        part=12; speaker[part]="Officer"
        chat1[part]="Surrender and make this easy on yourselves!"
        part=13; speaker[part]="Lucas"
        chat1[part]="Over my dead body!"
        part=14
        controlChar=part
        part=30
        partdelay[part]=50
        part=31; speaker[part]="Floyd"
        chat1[part]="That was the last one."
        chat2[part]=""
        chat3[part]=""
        part=32; speaker[part]="Lucas"
        chat1[part]="No! They're just going to keep coming, and coming,"
        chat2[part]="and coming, and..."
        chat3[part]=""
        musicplay[part]="None"
        part=33; speaker[part]="Winston"
        chat1[part]="Lucas, it's over!"
        part=34; speaker[part]="Lucas"
        chat1[part]="As long as we're stuck in this hotel..."
        chat2[part]="we're just targets! And there's no way out!"
        chat3[part]=""
        musicplay[part]="mystery"
        part=35; speaker[part]="Lucas"
        chat1[part]="Sorry Winston, but I need to go somewhere..."
        chat2[part]=""
        chat3[part]=""
        part=36
        createnpc[part]=-2
        partdelay[part]=30
        part=37; speaker[part]="Winston"
        chat1[part]="Lucas!"
        part=38; speaker[part]="Floyd"
        chat1[part]="Did something occur in my absence?"
        chat2[part]=""
        chat3[part]=""
        part=39; speaker[part]="Winston"
        chat1[part]="Lucas was the best Officer they had. Now he wants"
        chat2[part]="to be something even greater."
        chat3[part]=""
        part=40; speaker[part]="Floyd"
        chat1[part]="I see."
        chat2[part]=""
        chat3[part]=""
        part=41; speaker[part]="Floyd"
        chat1[part]="Is Lenna missing as well?"
        part=42; speaker[part]="Winston"
        chat1[part]="Oh yeah, right. Let's keep looking for her."
        chat2[part]=""
        chat3[part]=""
        part=43; speaker[part]="Floyd"
        chat1[part]="But first, we must find a new safehouse."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=44
        changelevelpart=part; changelevelto="LevelMenu"; day=16; chapter+=1
        part=100; speaker[part]="Officer"
        chat1[part]="Backup is here! We're barging in 3, 2, 1...!"
        chat2[part]=""
        chat3[part]=""
        part=101; speaker[part]="Floyd"
        chat1[part]="There's nowhere to run now..."
        chat2[part]=""
        chat3[part]=""
        part=102
        gotopart[part]=110
        part=105; speaker[part]="Lucas"
        chat1[part]="Floyd's not going to make it! We're done, Winston!"
        chat2[part]=""
        chat3[part]=""
        part=106; speaker[part]="Officer"
        chat1[part]="Backup is here! We're barging in 3, 2, 1...!"
        chat2[part]=""
        chat3[part]=""
        part=107
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Weapons"):
        dorandomizeItems=0
        selectx=8; camerax=selectx #Camera Position EnterGrayDoor 12,11
        selecty=10; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha()
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=5; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=8; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Man"; npcx[npcc]=13; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=3; movenpcy[part]=11
        part=3
        movenpc[part]=0; movenpcx[part]=3; movenpcy[part]=7
        part=4
        movenpc[part]=0; movenpcx[part]=4; movenpcy[part]=7
        part=5
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=7
        part=6; speaker[part]="Winston"
        chat1[part]="You were right, this'll be a great place to stay."
        chat2[part]="At least for now."
        chat3[part]=""
        musicplay[part]="standby"
        part=7; speaker[part]="Floyd"
        chat1[part]="Hhehe. And right next to a bathroom too."
        part=8
        movenpc[part]=2; movenpcx[part]=12; movenpcy[part]=7
        part=9
        createnpc[part]=2
        partdelay[part]=1
        part=10
        movenpc[part]=2; movenpcx[part]=11; movenpcy[part]=7
        part=11
        movenpc[part]=2; movenpcx[part]=8; movenpcy[part]=8
        part=12; speaker[part]="Man"
        chat1[part]="S'cuse me, Sir. Just passin' through."
        chat2[part]=""
        chat3[part]=""
        part=13; speaker[part]="Floyd"
        chat1[part]="Ah! Watch where you're going!"
        part=14
        movenpc[part]=2; movenpcx[part]=6; movenpcy[part]=7
        part=15; speaker[part]="Man"
        chat1[part]="Woops! He-he, awfully clumsy today."
        part=16; speaker[part]="Winston"
        chat1[part]="Woah, are you okay?"
        part=17; speaker[part]="Man"
        chat1[part]="Yes...yes. I'll be going now."
        part=18
        movenpc[part]=2; movenpcx[part]=6; movenpcy[part]=6       
        part=19
        movenpc[part]=2; movenpcx[part]=6; movenpcy[part]=5
        part=20
        createnpc[part]=-2
        partdelay[part]=50
        part=21; speaker[part]="Floyd"
        chat1[part]="What a strange man."
        part=22; speaker[part]="Floyd"
        chat1[part]="Wait..."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=7
        part=23; speaker[part]="Floyd"
        chat1[part]="I may have misplaced my belongings."
        part=24; speaker[part]="Winston"
        chat1[part]="If you need a weapon, you can borrow..."
        part=25; speaker[part]="Winston"
        chat1[part]="Huh? It was here just a second ago."
        movenpc[part]=0; movenpcx[part]=6; movenpcy[part]=7
        part=26; speaker[part]="Floyd"
        chat1[part]="Confound it! That man, he took our things!"
        chat2[part]=""
        chat3[part]=""
        part=27
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=7
        part=28; speaker[part]="Winston"
        chat1[part]="Lenna, Lucas, and now our items...what isn't"
        chat2[part]="missing?"
        chat3[part]=""
        part=29; speaker[part]="Floyd"
        chat1[part]="Hmmm. Let's start asking around. Someone might"
        chat2[part]="give us a hint pertaining to Lenna's whereabouts."
        chat3[part]=""
        musicplay[part]="None"
        part=30
        changelevelpart=part; changelevelto="LevelMenu"; day=17; chapter+=1
    if (level=="Brawl"):
        dorandomizeItems=0
        item[0]="Med Kit"; itemx[0]=10; itemy[0]=3
        selectx=7; camerax=selectx #Camera Position EnterGrayDoor 12,11
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha()
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=8; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=5; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Man"; npcx[npcc]=11; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=9; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Woman"; npcx[npcc]=10; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=5; npc[npcc]=0; npcside[npcc]="Big Brute"; npcx[npcc]=3; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Shiv" #Create NPCs
        part=1
        partdelay[part]=50
        part=2
        createnpc[part]=2
        partdelay[part]=1
        musicplay[part]="crowd"
        part=3
        movenpc[part]=2; movenpcx[part]=9; movenpcy[part]=6
        part=4
        movenpc[part]=0; movenpcx[part]=8; movenpcy[part]=6
        part=5; speaker[part]="Winston"
        chat1[part]="Ma'am! You haven't happened to have have seen..."
        part=6; speaker[part]=" "
        chat1[part]="Winston describes Lenna to the Woman."
        part=7; speaker[part]="Ma'am"
        chat1[part]="Sorry, deary. Now excuse me, I'm almost late for"
        chat2[part]="an appointment."
        chat3[part]=""
        part=8
        movenpc[part]=2; movenpcx[part]=7; movenpcy[part]=5
        part=9
        movenpc[part]=2; movenpcx[part]=7; movenpcy[part]=4
        part=10
        createnpc[part]=-2
        partdelay[part]=20
        part=11; speaker[part]="Floyd"
        chat1[part]="It's no use, Winston. We'd have better luck"
        chat2[part]="searching every nook and cranny for her."
        chat3[part]=""
        part=12; speaker[part]="Winston"
        chat1[part]="We can't just give up, though! Someone must have"
        chat2[part]="seen her."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=4; movenpcy[part]=6
        part=13; speaker[part]="Floyd"
        chat1[part]="You're bound to attract the wrong type of"
        chat2[part]="attention."
        chat3[part]=""
        part=14
        partdelay[part]=50
        part=15; speaker[part]="Broadcast"
        chat1[part]="And we are back with the news!"
        part=16; speaker[part]="Floyd"
        chat1[part]="Look, the televisions turned on."
        part=17; speaker[part]="Broadcast"
        chat1[part]="As many of you know, the hotel serial killers"
        chat2[part]="are still on the loose..."
        chat3[part]=""
        musicplay[part]="None"
        part=18; speaker[part]="Winston"
        chat1[part]="Uh oh."
        part=19; speaker[part]="Broadcast"
        chat1[part]="Beginning with one murder in room 415, killer"
        chat2[part]="Floyd and his accomplices, Lenna and Winston, have"
        chat3[part]="wreaked havoc in the past two days."
        part=20; speaker[part]="Broadcast"
        chat1[part]="Officers say the killings were in cold-blood and"
        chat2[part]="unprovoked."
        chat3[part]=""
        part=21; speaker[part]="Broadcast"
        chat1[part]="Anyone who has seen any of these persons should"
        chat2[part]="contact the Officers immediately."
        chat3[part]=""
        part=22; speaker[part]=" "
        chat1[part]="Pictures of Lenna, Winston, and Floyd appear"
        chat2[part]="on-screen."
        chat3[part]=""
        part=23; speaker[part]="Floyd"
        chat1[part]="Unprovoked!? I've been attacked God knows how many"
        chat2[part]="times just today!"
        chat3[part]=""
        musicplay[part]="ambient"
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=5
        part=24
        movenpc[part]=3; movenpcx[part]=8; movenpcy[part]=11
        part=25; speaker[part]="Man"
        chat1[part]="Hey, look over there! That's those guys on the"
        chat2[part]="TV!"
        chat3[part]=""
        part=26; speaker[part]="Woman"
        chat1[part]="Should we call an Officer?"
        movenpc[part]=4; movenpcx[part]=10; movenpcy[part]=9
        part=27; speaker[part]="Man"
        chat1[part]="No way! Let's get em' ourselves! We'll be"
        chat2[part]="like superheroes!"
        chat3[part]=""
        part=28; speaker[part]="Winston"
        chat1[part]="Get ready for a brawl, Floyd."
        chat2[part]=""
        chat3[part]=""
        part=29; speaker[part]="Floyd"
        chat1[part]="But these people are innocents! We can't just kill"
        chat2[part]="them!"
        chat3[part]=""
        part=30; speaker[part]="Winston"
        chat1[part]="Yeah...let's just bruise them up a little, then"
        chat2[part]="they'll retreat."
        chat3[part]=""
        musicplay[part]="None"
        part=31
        musicplay[part]="threefour"
        controlChar=part
        part=40
        partdelay[part]=50
        part=41; speaker[part]="Man"
        chat1[part]="Woah! Ouch! Come on, let's get out of here!"
        chat2[part]=""
        chat3[part]=""
        part=42; speaker[part]="Woman"
        chat1[part]="*Crying* I-I'm not a fighter..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=43; speaker[part]="Floyd"
        chat1[part]="People, don't believe everything you see on TV!"
        chat2[part]=""
        chat3[part]=""
        part=44
        createnpc[part]=-3
        partdelay[part]=1
        part=45
        createnpc[part]=-4
        partdelay[part]=50
        part=46; speaker[part]="Winston"
        chat1[part]="Floyd, I asked a lot of people about Lenna..."
        chat2[part]=""
        chat3[part]=""
        part=47
        createnpc[part]=5
        partdelay[part]=1
        part=48; speaker[part]="Brute"
        chat1[part]="Agh! You thought you could slip right past me!?"
        musicplay[part]="action"
        part=49; speaker[part]="Floyd"
        chat1[part]="I don't think a little bruising is going to get"
        chat2[part]="us anywhere with him."
        chat3[part]=""
        part=50; speaker[part]="Winston"
        chat1[part]="Watch out! He has a knife!"
        chat2[part]=""
        chat3[part]=""
        part=51
        part=60
        partdelay[part]=100
        part=61; speaker[part]="Floyd"
        chat1[part]="He's dead. We killed him."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=62; speaker[part]="Winston"
        chat1[part]="He attacked us with a weapon..."
        chat2[part]=""
        chat3[part]=""
        part=63; speaker[part]="Floyd"
        chat1[part]="Oh, but he didn't know! He was brainwashed by"
        chat2[part]="the media. The media, a bunch of liars!"
        chat3[part]=""
        musicplay[part]="ominous"
        part=64; speaker[part]="Broadcast"
        chat1[part]="And coming up right now, we have a special guest"
        chat2[part]="speaking."
        chat3[part]=""
        part=65; speaker[part]="Floyd"
        chat1[part]="And the darn television won't shut up!"
        part=66; speaker[part]="Broadcast"
        chat1[part]="...Everyone, welcome Lenna to the stage!"
        part=67; speaker[part]="Winston"
        chat1[part]="Huh, what!?"
        part=68; speaker[part]=" "
        chat1[part]="Lenna is seen speaking on the television."
        part=69; speaker[part]="Lenna"
        chat1[part]="I...I don't even remember doing any of this..."
        chat2[part]="Everyone, please know I am not associated with"
        chat3[part]="these Winston and Floyd persons..."
        part=70; speaker[part]="Broadcast"
        chat1[part]="You heard it here, folks! But, the search continues."
        chat2[part]="Let's see what happens next. And now onto sports"
        chat3[part]="with..."
        part=71; speaker[part]="Winston"
        chat1[part]="..."
        part=72; speaker[part]="Floyd"
        chat1[part]="The little two-timing rat! I oughta..."
        chat2[part]=""
        chat3[part]=""
        part=73; speaker[part]="Winston"
        chat1[part]="Something doesn't seem quite right. Lenna doesn't"
        chat2[part]="act like that."
        chat3[part]=""
        part=74; speaker[part]="Floyd"
        chat1[part]="What do you mean?"
        part=75; speaker[part]="Winston"
        chat1[part]="I say we check out wherever they're filming these"
        chat2[part]="reports before jumping to conclusions. At least"
        chat3[part]="we finally know where Lenna is."
        musicplay[part]="None"
        part=76
        changelevelpart=part; changelevelto="LevelMenu"; day=18; chapter+=1
        part=100; speaker[part]="Man"
        chat1[part]="The killers are dying! Keep at it!"
        chat2[part]=""
        chat3[part]=""
        part=101
        musicplay[part]="None"
        failurepart=part
    if (level=="Dinah"):
        dorandomizeItems=0
        selectx=7; camerax=selectx
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha()
        npcc=1; npc[npcc]=0; npcside[npcc]="Floyd"; npcx[npcc]=2; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=0; npc[npcc]=1; npcside[npcc]="Dinah"; npcx[npcc]=10; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Drunkard"; npcx[npcc]=7; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Fool"; npcx[npcc]=6; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Bottle" #Create NPCs
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Drunkard"
        chat1[part]="Hehe...you're so feisty, ya know that?"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="standby"
        part=3; speaker[part]="Dinah"
        chat1[part]="Back off!"
        chat2[part]=""
        chat3[part]=""
        part=4
        movenpc[part]=3; movenpcx[part]=7; movenpcy[part]=8
        part=5; speaker[part]="Fool"
        chat1[part]="Who? We? You think we're just joking?"
        chat2[part]="Let's get her!"
        chat3[part]=""
        part=6
        createnpc[part]=1
        partdelay[part]=20
        part=7
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=6
        part=8; speaker[part]="Floyd"
        chat1[part]="Gentlemen, care to step down?"
        part=9; speaker[part]="Drunkard"
        chat1[part]="Ha! Get ready for a fight!"
        part=10
        controlChar=part
        part=29
        partdelay[part]=50
        part=30; speaker[part]="Floyd"
        chat1[part]="Are you okay?"
        part=31; speaker[part]="Dinah"
        chat1[part]="Yeah, I'm fine. And my name's Dinah."
        part=32; speaker[part]="Floyd"
        chat1[part]="Lassy, try to stay safe next time, all right?"
        chat2[part]=""
        chat3[part]=""
        part=33; speaker[part]="Dinah"
        chat1[part]="Wait! What's your name?"
        part=34; speaker[part]="Floyd"
        chat1[part]="My name's Floyd."
        part=35; speaker[part]="Dinah"
        chat1[part]="Floyd, I want to join you. If it weren't"
        chat2[part]="for me, those two guys would've killed you!"
        chat3[part]=""
        part=36; speaker[part]="Floyd"
        chat1[part]="I...what?"
        part=37; speaker[part]="Dinah"
        chat1[part]="Usually it's my dad who protects me. His name"
        chat2[part]="is Jacob, by the way. But he left on a trip..."
        chat3[part]=""
        part=38; speaker[part]="Floyd"
        chat1[part]="Hehe, at least you've got spirit."
        musicplay[part]="None"
        part=39
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        part=100; speaker[part]="Dinah"
        chat1[part]="Ahh! Dad, where are you!?"
        chat2[part]=""
        chat3[part]=""
        part=101
        musicplay[part]="None"
        failurepart=part
    if (level=="Choose"):
        dorandomizeItems=0
        selectx=9; camerax=selectx
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha()
        npcc=6; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=14; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Adam"; npcx[npcc]=14; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Evelyn"; npcx[npcc]=11; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Sanders"; npcx[npcc]=14; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs        
        npcc=1; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=11; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=14; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs        
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=6; movenpcx[part]=12; movenpcy[part]=9
        part=3; speaker[part]="Adam"
        chat1[part]="As promised, we helped you, but now we need"
        chat2[part]="you to return the favor."
        chat3[part]=""
        musicplay[part]="standby"
        part=4; speaker[part]="Evelyn"
        chat1[part]="Winston, we still haven't found what we've been"
        chat2[part]="looking for, it must be somewhere here."
        chat3[part]=""
        part=5; speaker[part]="Winston"
        chat1[part]="Yes, whatever IT is."
        part=6
        movenpc[part]=4; movenpcx[part]=14; movenpcy[part]=11
        part=7; speaker[part]="Adam"
        chat1[part]="But we've looked everywhere!"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=8
        createnpc[part]=3
        partdelay[part]=40
        part=9; speaker[part]="Sanders"
        chat1[part]="Gentlemen...and...lady!"
        musicplay[part]="mystery"
        movenpc[part]=3; movenpcx[part]=14; movenpcy[part]=5
        part=10; speaker[part]="Winston"
        chat1[part]="Sanders!"
        movenpc[part]=6; movenpcx[part]=13; movenpcy[part]=8
        part=11; speaker[part]="Evelyn"
        chat1[part]="Winston, do you know this man?"
        part=12; speaker[part]="Sanders"
        chat1[part]="Adam...Evelyn, unlike Winston, I actually"
        chat2[part]="KNOW what you're looking for! Yes, YES! And..."
        chat3[part]="I KNOW where it is!"
        part=13; speaker[part]="Winston"
        chat1[part]="Back up! Don't listen to him, he's trying to"
        chat2[part]="trick you!"
        part=14
        movenpc[part]=5; movenpcx[part]=12; movenpcy[part]=10
        part=15; speaker[part]="Evelyn"
        chat1[part]="Winston, don't be so rash."
        part=16; speaker[part]="Evelyn"
        chat1[part]="Sanders, was it? Excuse our friend, but if you are"
        chat2[part]="as you say you are...where is it then?"
        chat3[part]=""
        part=17; speaker[part]="Sanders"
        chat1[part]="Ah! He-he! Glorious Evelyn! But...it's fallen off"
        chat2[part]="the edge over there. I swear, I was just passing"
        chat3[part]="by a few days ago when I saw it..."
        part=18
        movenpc[part]=5; movenpcx[part]=11; movenpcy[part]=12
        part=19; speaker[part]="Evelyn"
        chat1[part]="You mean here?"
        part=20; speaker[part]="Winston"
        chat1[part]="Careful!"
        movenpc[part]=6; movenpcx[part]=13; movenpcy[part]=9
        part=21; speaker[part]="Adam"
        chat1[part]="We're in this together, Evelyn. Do you see"
        chat2[part]="it?"
        chat3[part]=""
        movenpc[part]=4; movenpcx[part]=13; movenpcy[part]=12
        part=22; speaker[part]="Sanders"
        chat1[part]="Oh, don't you see it on the railing below?"
        chat2[part]="One of you should go get it...!"
        chat3[part]=""
        part=23
        createnpc[part]=1
        partdelay[part]=1
        part=24
        createnpc[part]=2
        partdelay[part]=30
        part=25; speaker[part]="Evelyn"
        chat1[part]="What are you doing?"
        chat2[part]=""
        chat3[part]=""
        part=26
        controlChar=part
        part=30
        partdelay[part]=10
        part=31
        partdelay[part]=300
        part=32; speaker[part]="Sanders"
        chat1[part]="Truly, I'm not the fallen one now!"
        part=33; speaker[part]="Sanders"
        chat1[part]="Choose wisely Winston."
        chat2[part]="Consider this the first of much retribution!"
        part=34
        createnpc[part]=-3
        partdelay[part]=1
        part=35; speaker[part]="Winston"
        chat1[part]="Sanders! You...!"
        movenpc[part]=6; movenpcx[part]=13; movenpcy[part]=8
        part=36; speaker[part]="Winston"
        chat1[part]="Where did you go...?"
        part=37
        movenpc[part]=6; movenpcx[part]=13; movenpcy[part]=9
        part=38; speaker[part]="Adam"
        chat1[part]="Winston, help!"
        chat2[part]=""
        chat3[part]=""
        part=39; speaker[part]="Evelyn"
        chat1[part]="Save Adam, not me! This isn't his fault...!"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=40; speaker[part]="Winston"
        chat1[part]="\"Choose\"...?"
        chat2[part]=""
        chat3[part]=""
        choice1[part]="Save Adam"; choice1go[part]=41 #Choices Given
        choice2[part]="Save Evelyn"; choice2go[part]=99
        part=41
        movenpc[part]=5; movenpcx[part]=11; movenpcy[part]=16
        part=42; speaker[part]="Adam"
        chat1[part]="NOOOOooooo!!!"
        musicplay[part]="scary"
        part=43; speaker[part]="Adam"
        chat1[part]="Get off me!"
        part=44
        createnpc[part]=-1
        partdelay[part]=1
        part=45
        createnpc[part]=-2
        partdelay[part]=1
        part=46; speaker[part]="Adam"
        chat1[part]="Evelyn! Evelyn!...Evelyn!!"
        chat2[part]=""
        chat3[part]=""     
        movenpc[part]=4; movenpcx[part]=12; movenpcy[part]=12
        part=47
        partdelay[part]=60
        part=48; speaker[part]="Winston"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        part=49
        partdelay[part]=60
        part=50; speaker[part]="Adam"
        chat1[part]="...Why did you choose me?"
        chat2[part]=""
        chat3[part]=""
        part=51; speaker[part]="Winston"
        chat1[part]="I had to choose someone. Sanders...that scum."
        chat2[part]=""
        chat3[part]=""
        part=52; speaker[part]="Adam"
        chat1[part]="Evelyn is dead, but...I'm not angry with you,"
        chat2[part]="Winston."
        chat3[part]=""
        part=53; speaker[part]="Adam"
        chat1[part]="We weren't supposed to have it anyway."
        part=54; speaker[part]="Winston"
        chat1[part]="Will you at least tell me what IT is?"
        part=55; speaker[part]="Adam"
        chat1[part]="It makes no difference...Actually, it does now,"
        chat2[part]="and that's what scares me. I don't actually know,"
        chat3[part]="I was just going along with Evelyn..."
        musicplay[part]="None"
        part=56 #End 1
        part=99
        movenpc[part]=4; movenpcx[part]=13; movenpcy[part]=16  
        part=100; speaker[part]="Evelyn"
        chat1[part]="Adam!"
        musicplay[part]="scary"
        part=101
        createnpc[part]=-1
        partdelay[part]=1
        part=102
        createnpc[part]=-2
        partdelay[part]=1
        part=103; speaker[part]="Evelyn"
        chat1[part]="..."    
        movenpc[part]=5; movenpcx[part]=12; movenpcy[part]=12
        part=104
        movenpc[part]=5; movenpcx[part]=13; movenpcy[part]=12
        part=105
        partdelay[part]=30
        part=106
        movenpc[part]=5; movenpcx[part]=12; movenpcy[part]=12
        part=107
        partdelay[part]=30
        part=108
        movenpc[part]=5; movenpcx[part]=13; movenpcy[part]=12
        part=109; speaker[part]="Winston"
        chat1[part]="You okay?"
        part=110; speaker[part]="Evelyn"
        chat1[part]="*Sob* W-why...I told you to save him!"
        chat2[part]=""
        chat3[part]=""
        part=111; speaker[part]="Winston"
        chat1[part]="I had to save someone! Sanders...that scum!"
        part=112; speaker[part]="Evelyn"
        chat1[part]="I hate you!"
        part=113; speaker[part]="Winston"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        part=114; speaker[part]="Evelyn"
        chat1[part]="And I hate myself..."
        part=115; speaker[part]="Winston"
        chat1[part]="...What exactly were you looking for?"
        chat2[part]=""
        chat3[part]=""
        part=116; speaker[part]="Evelyn"
        chat1[part]="It was stupid anyway. But it's effects"
        chat2[part]="will be long lasting...I don't actually"
        chat3[part]="know, I was just going along with Adam."
        musicplay[part]="None"
        part=117 #End 2
    if (level=="Report"):
        dorandomizeItems=0
        selectx=9; camerax=selectx
        selecty=12; cameray=selecty
        item[0]="Wrench"; itemx[0]=3; itemy[0]=13
        item[1]="Bottle"; itemx[1]=14; itemy[1]=12
        sky=pygame.image.load("Images/skyorange.png").convert_alpha()
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=14; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=15; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Guard"; npcx[npcc]=11; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Baton" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Guard"; npcx[npcc]=5; npcy[npcc]=15; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]=""  #Create NPCs        
        npcc=4; npc[npcc]=1; npcside[npcc]="Security"; npcx[npcc]=5; npcy[npcc]=17; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Baton"  #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Guard"; npcx[npcc]=13; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife"  #Create NPCs        
        npcc=6; npc[npcc]=1; npcside[npcc]="Security"; npcx[npcc]=6; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton"  #Create NPCs        
        npcc=7; npc[npcc]=0; npcside[npcc]="Host"; npcx[npcc]=10; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs        
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Floyd"
        chat1[part]="Is there really no way you'd let us in?"
        musicplay[part]="crowd"
        part=3; speaker[part]="Guard"
        chat1[part]="For the last time, I can't let you talk to"
        chat2[part]="the Host."
        chat3[part]=""
        part=4; speaker[part]="Winston"
        chat1[part]="But he would know where Lenna is. This is an"
        chat2[part]="emergency, Sir."
        chat3[part]=""
        part=5; speaker[part]="Guard"
        chat1[part]="Lenna? Let me ask the Host. Give me a moment."
        chat2[part]=""
        chat3[part]=""
        part=6
        movenpc[part]=2; movenpcx[part]=10; movenpcy[part]=16
        part=7; speaker[part]=" "
        chat1[part]="The Guard begins to speak into a small device."
        chat2[part]=""
        chat3[part]=""
        part=8; speaker[part]="Guard"
        chat1[part]="Yes...of course...What? Them?"
        musicplay[part]="None"
        part=9; speaker[part]=" "
        chat1[part]="Someone's voice is heard through the speaker"
        chat2[part]="on the wall."
        chat3[part]=""
        musicplay[part]="ambient"
        part=10; speaker[part]="Host"
        chat1[part]="Winston, Floyd? What a surprise! Lenna really did"
        chat2[part]="a wonder in exposing you, didn't she?"
        chat3[part]=""
        part=11; speaker[part]="Host"
        chat1[part]="The whole hotel, nay, the whole WORLD knows"
        chat2[part]="you both! Isn't instant communication wonderful?"
        chat3[part]=""
        part=12; speaker[part]="Winston"
        chat1[part]="We demand to see Lenna!"
        part=13; speaker[part]="Host"
        chat1[part]="Hahahaha! Security, expose of these MURDERS!"
        musicplay[part]="None"
        part=14
        movenpc[part]=2; movenpcx[part]=11; movenpcy[part]=16
        part=15; speaker[part]="Guard"
        chat1[part]="Sorry, orders are orders."
        chat2[part]=""
        chat3[part]=""
        part=16
        musicplay[part]="threefour"
        controlChar=part
        part=29
        partdelay[part]=50
        part=30
        createnpc[part]=7
        partdelay[part]=1
        part=31; speaker[part]="Host"
        chat1[part]="Woah! Hold up! Security, why are they HERE!?"
        chat2[part]=""
        chat3[part]=""
        part=32; speaker[part]="Winston"
        chat1[part]="Don't you move!"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=33; speaker[part]="Host"
        chat1[part]="Security, security!"
        chat2[part]=""
        chat3[part]=""
        part=34; speaker[part]="Floyd"
        chat1[part]="You false witness! This is all your fault! Your lies,"
        chat2[part]="the way you twist the truth and bias the news!"
        chat3[part]=""
        musicplay[part]="ominous"
        part=35; speaker[part]="Host"
        chat1[part]="Don't be such a critic! Gah, so annoying..."
        chat2[part]=""
        chat3[part]=""
        part=36; speaker[part]="Winston"
        chat1[part]="Where's Lenna!?"
        chat2[part]=""
        chat3[part]=""
        part=37; speaker[part]="Host"
        chat1[part]="Wouldn't you like to know? You missed her! She left"
        chat2[part]="thirty minutes ago. Who knows where she wandered"
        chat3[part]="off to."
        part=38; speaker[part]="Winston"
        chat1[part]="We're too late..."
        chat2[part]=""
        chat3[part]=""
        part=39; speaker[part]="Host"
        chat1[part]="Exit's right over there, buddy. My next show is"
        chat2[part]="about to begin."
        chat3[part]=""
        part=40; speaker[part]="Floyd"
        chat1[part]="Unfortunately, your news station's permanently"
        chat2[part]="off-air. Get out of here!"
        chat3[part]=""
        part=41
        movenpc[part]=7; movenpcx[part]=7; movenpcy[part]=3
        part=42; speaker[part]="Floyd"
        chat1[part]="And if you return...may God have mercy on you."
        chat2[part]=""
        chat3[part]=""
        part=43
        movenpc[part]=7; movenpcx[part]=7; movenpcy[part]=4
        part=44
        createnpc[part]=-7
        partdelay[part]=50
        part=45
        movenpc[part]=7; movenpcx[part]=7; movenpcy[part]=3
        part=46
        movenpc[part]=7; movenpcx[part]=7; movenpcy[part]=4
        part=47; speaker[part]="Floyd"
        chat1[part]="I'm sorry, Winston."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=48; speaker[part]="Winston"
        chat1[part]="His stories were phony. He said we were murderers..."
        chat2[part]=""
        chat3[part]=""
        part=49; speaker[part]="Floyd"
        chat1[part]="...And isn't that what we've become?"
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=50
        changelevelpart=part; changelevelto="LevelMenu"; day=19; chapter+=1
        part=100; speaker[part]="Winston"
        chat1[part]="No! Almost reunited...!"
        chat2[part]=""
        chat3[part]=""
        part=101
        musicplay[part]="None"
        failurepart=part
    if (level=="Idea"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=6; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=10; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Lenna"; npcx[npcc]=3; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        part=1
        partdelay[part]=5
        part=2
        partdelay[part]=5
        part=3
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=6
        part=4
        partdelay[part]=40
        part=5; speaker[part]="Floyd"
        chat1[part]="What a waste of time."
        chat2[part]=""
        chat3[part]=""
        part=6; speaker[part]="Winston"
        chat1[part]="We're going around in circles. Lenna, Lucas..."
        chat2[part]="and no plan once we find them."
        chat3[part]=""
        part=7; speaker[part]="Floyd"
        chat1[part]="Plan, you say?"
        musicplay[part]="ominous"
        part=8; speaker[part]="Winston"
        chat1[part]="What? You have a plan on escaping this hotel too?"
        part=9; speaker[part]="Floyd"
        chat1[part]="Not escaping, per say. No, not something quite so"
        chat2[part]="violent or brutish."
        chat3[part]=""
        part=10; speaker[part]="Winston"
        chat1[part]="What's your idea?"
        part=11; speaker[part]="Floyd"
        chat1[part]="...How tall do you reckon this hotel is?"
        part=12; speaker[part]="Winston"
        chat1[part]="Er, I don't know, pretty tall, I guess..."
        part=13; speaker[part]="Floyd"
        chat1[part]="It's not just tall, it's the tallest structure ever"
        chat2[part]="built. This hotel has everything..."
        chat3[part]=""
        part=14; speaker[part]="Winston"
        chat1[part]="Well, we did just visit a news station."
        part=15
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=6
        part=16; speaker[part]="Floyd"
        chat1[part]="People want to group together, Winston. They"
        chat2[part]="built this tower as a symbol of unity, a showing"
        chat3[part]="of how far we've come."
        part=17; speaker[part]="Winston"
        chat1[part]="What are you getting at?"
        part=18
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=7
        part=19; speaker[part]="Floyd"
        chat1[part]="But what unity have we created!? A unity by error!"
        chat2[part]="By lies!"
        chat3[part]=""
        part=20; speaker[part]="Floyd"
        chat1[part]="What is true? Are we killers?"
        choice1[part]="We've become killers."; choice1go[part]=25 #Choices Given
        choice2[part]="This isn't our fault."; choice2go[part]=30
        part=25; speaker[part]="Winston" #Choice 1
        chat1[part]="We've become killers. The news told a lie and it got"
        chat2[part]="out of hand, but we should have handled it"
        chat3[part]="better..."
        part=26; speaker[part]="Floyd"
        chat1[part]="We're victims, Winston. Victims of solidarity."
        chat2[part]="People would rather cooperate by error than be"
        chat3[part]="divided by truth."
        part=27
        gotopart[part]=40
        part=30; speaker[part]="Winston" #Choice 2
        chat1[part]="This isn't our fault. People saw us on the news and"
        chat2[part]="wanted to enact justice...but, they just don't know"
        chat3[part]="the whole story."
        part=31; speaker[part]="Floyd"
        chat1[part]="And look at the result. Needless bloodshed. People"
        chat2[part]="would rather cooperate by error than be divided"
        chat3[part]="by truth."
        part=32
        gotopart[part]=40
        part=40; speaker[part]="Floyd"
        chat1[part]="But what about you? Would you act differently,"
        chat2[part]="maybe even tell a little lie, just to cooperate"
        chat3[part]="better with someone?"
        choice1[part]="If it means progress, I would."; choice1go[part]=42 #Choices Given
        choice2[part]="Never."; choice2go[part]=46
        part=42; speaker[part]="Winston" #Choice 1
        chat1[part]="If it means progress, I would. People can't get"
        chat2[part]="anywhere if they don't at least try to settle"
        chat3[part]="their differences."
        part=43; speaker[part]="Floyd"
        chat1[part]="Even if what they do is wrong? Banded together"
        chat2[part]="for a futile effort, I'd say."
        chat3[part]=""
        part=44
        gotopart[part]=50
        part=46; speaker[part]="Winston" #Choice 2
        chat1[part]="Never. I wouldn't betray myself to fit in with"
        chat2[part]="others."
        chat3[part]=""
        part=47; speaker[part]="Floyd"
        chat1[part]="You wouldn't even attempt to settle your"
        chat2[part]="differences?"
        chat3[part]=""
        part=48
        gotopart[part]=50
        part=50; speaker[part]="Floyd"
        chat1[part]="Really, it's an issue on whether you believe"
        chat2[part]="in absolute truth."
        chat3[part]=""
        part=51; speaker[part]="Winston"
        chat1[part]="Absolute truth? (Just like Lucas...)"
        chat2[part]=""
        chat3[part]=""
        part=52; speaker[part]="Floyd"
        chat1[part]="I believe there is only one truth to everything."
        chat2[part]="Two people can believe different things, but"
        chat3[part]="both cannot be right."
        part=53; speaker[part]="Winston"
        chat1[part]="Okay, sure. But, what does that have to do with"
        chat2[part]="your plan?"
        chat3[part]=""
        part=54; speaker[part]="Floyd"
        chat1[part]="Answer something for me. And please"
        chat2[part]="don't straddle the fence, give a definite answer."
        chat3[part]=""
        part=55; speaker[part]="Floyd"
        chat1[part]="Do you believe in God?"
        chat2[part]=""
        chat3[part]=""
        choice1[part]="Yes"; choice1go[part]=57 #Choices Given
        choice2[part]="No"; choice2go[part]=62
        part=57; speaker[part]="Winston" #Choice 1
        chat1[part]="Yes, I believe in God."
        part=58; speaker[part]="Floyd"
        chat1[part]="And how do you know you're right? Only one side is"
        chat2[part]="correct, one side has the truth. Or maybe you believe"
        chat3[part]="that because the people around you believe it."
        part=59; speaker[part]="Floyd"
        chat1[part]="If you're curious - Yes, I believe in God as"
        chat2[part]="well."
        chat3[part]=""
        part=60
        gotopart[part]=70
        part=62; speaker[part]="Winston" #Choice 2
        chat1[part]="No, I don't believe."
        part=63; speaker[part]="Floyd"
        chat1[part]="And how do you know you're right? Only one side is"
        chat2[part]="correct, one side has the truth. Or maybe you believe"
        chat3[part]="that because the people around you believe it."      
        part=64; speaker[part]="Floyd"
        chat1[part]="If you're curious - I for one, do believe in God."
        part=65
        gotopart[part]=70
        part=70; speaker[part]="Winston"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        part=71
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=8
        part=72; speaker[part]="Floyd"
        chat1[part]="I want to destroy this tower. Destroy"
        chat2[part]="this symbol of false unity."
        part=73; speaker[part]="Winston"
        chat1[part]="And how will you go about doing that?"
        part=74; speaker[part]="Floyd"
        chat1[part]="I don't know yet..."
        chat2[part]=""
        chat3[part]=""
        part=75; speaker[part]="Floyd"
        chat1[part]="But if the only way out of this is to end all"
        chat2[part]="communication, then that's what I plan on"
        chat3[part]="doing."
        part=76
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=8
        part=77; speaker[part]="Floyd"
        chat1[part]="I'm going to go find a way."
        part=78; speaker[part]="Winston"
        chat1[part]="You're leaving too?"
        part=79; speaker[part]="Floyd"
        chat1[part]="I'll be back. Go and find Lenna."
        musicplay[part]="None"
        part=80
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=6
        part=81
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=5
        part=82
        createnpc[part]=-1
        partdelay[part]=60
        part=83
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=7
        part=84; speaker[part]="Winston"
        chat1[part]="Just great. First Lucas, now Floyd. When'll"
        chat2[part]="they come back?"
        chat3[part]=""
        part=85
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=7
        part=86
        createnpc[part]=2
        partdelay[part]=60
        part=87
        movenpc[part]=0; movenpcx[part]=4; movenpcy[part]=7
        part=88; speaker[part]="Winston"
        chat1[part]="L-Lenna!?"
        musicplay[part]="calm"
        part=89
        movenpc[part]=2; movenpcx[part]=3; movenpcy[part]=10
        part=90; speaker[part]="Lenna"
        chat1[part]="Ah! Who are you!? What are you doing here?"
        part=91; speaker[part]="Winston"
        chat1[part]="Woah, woah! Lenna, we're friends! Don't you"
        chat2[part]="remember?"
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=4; movenpcy[part]=8
        part=92; speaker[part]="Lenna"
        chat1[part]="Don't get closer! What's your name!?"
        part=93; speaker[part]="Winston"
        chat1[part]="Huh? Are you serious? I'm Winston!"
        part=94; speaker[part]="Lenna"
        chat1[part]="Winston? But you're one of those killers!"
        chat2[part]="Don't hurt me!"
        chat3[part]=""
        part=95; speaker[part]="Winston"
        chat1[part]="I'm not going to hurt you! Just quiet down!"
        part=96; speaker[part]="Lenna"
        chat1[part]="But, everyone thinks your dangerous!"
        part=97; speaker[part]="Winston"
        chat1[part]="Yeah, I know. Lenna, what are you doing here?"
        part=98; speaker[part]="Lenna"
        chat1[part]="Me? This is my room! I rented it a few days ago."
        chat2[part]="Question is, what are you doing here?"
        chat3[part]=""
        part=99; speaker[part]="Winston"
        chat1[part]="(And Floyd said it was abandoned...)"
        part=100; speaker[part]="Winston"
        chat1[part]="I've been looking for you everywhere!"
        part=101; speaker[part]="Lenna"
        chat1[part]="You must have me confused with someone else. Please,"
        chat2[part]="leave before they begin thinking I'm in any way"
        chat3[part]="associated with you again."
        part=102; speaker[part]="Winston"
        chat1[part]="But we helped each other! We worked together! Do you"
        chat2[part]="really not remember...?"
        chat3[part]=""
        part=103; speaker[part]="Lenna"
        chat1[part]="I don't have any friends and I don't like fighting."
        chat2[part]=""
        chat3[part]=""
        part=104; speaker[part]="Winston"
        chat1[part]="You must have lost your memory."
        part=105; speaker[part]="Lenna"
        chat1[part]="Everything is fuzzy to me. To be honest, I'm not"
        chat2[part]="even sure I ever rented this room. It just feels"
        chat3[part]="as though I did..."
        part=106; speaker[part]="Lenna"
        chat1[part]="Officers arrived to ask me some questions. I was"
        chat2[part]="told there are murderers on the loose. And that"
        chat3[part]="one of them is named \"Winston\"."
        part=107; speaker[part]="Winston"
        chat1[part]="(Does she have amnesia?)"
        chat2[part]=""
        chat3[part]=""
        part=108; speaker[part]="Lenna"
        chat1[part]="I was asked to speak on a news show. I just said"
        chat2[part]="what I thought I remembered..."
        chat3[part]=""
        part=109; speaker[part]="Lenna"
        chat1[part]="But who's right? You? - Or what I think I remember?"
        part=110; speaker[part]="Winston"
        chat1[part]="Do you remember how you lost your memory?"
        part=111; speaker[part]="Lenna"
        chat1[part]="No. No, I don't...I'm sorry..."
        part=112; speaker[part]="Winston"
        chat1[part]="You used to be rougher, meaner, more direct...It's"
        chat2[part]="as though your personality's changed."
        chat3[part]=""
        part=113; speaker[part]="Lenna"
        chat1[part]="...Will you help me then?"
        part=114; speaker[part]="Winston"
        chat1[part]="Help you?"
        part=115; speaker[part]="Lenna"
        chat1[part]="Help me regain my memory. I want to remember."
        musicplay[part]="None"
        part=116
        changelevelpart=part; changelevelto="LevelMenu"; day=20; chapter+=1
    if (level=="Ruth3"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=12; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Ruth"; npcx[npcc]=13; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=13; movenpcy[part]=7
        part=3; speaker[part]="Winston"
        chat1[part]="Ruth?"
        musicplay[part]="calm"
        part=4
        movenpc[part]=0; movenpcx[part]=13; movenpcy[part]=8
        part=5; speaker[part]="Ruth"
        chat1[part]="So Floyd is gone too?"
        part=6; speaker[part]="Winston"
        chat1[part]="Yeah..."
        part=7
        movenpc[part]=1; movenpcx[part]=13; movenpcy[part]=10
        part=8; speaker[part]="Ruth"
        chat1[part]="Are you paying attention, Winston? Lucas and Floyd"
        chat2[part]="have told you their beliefs - their plans on"
        chat3[part]="resolving everything."
        part=9; speaker[part]="Winston"
        chat1[part]="I'm not sure what to do. We'll find a way out"
        chat2[part]="though."
        part=10; speaker[part]="Ruth"
        chat1[part]="Do you feel indecisive?"
        part=11; speaker[part]="Ruth"
        chat1[part]="Lucas and Floyd present opposing outcomes..."
        chat2[part]="You won't be able to help both. You won't be"
        chat3[part]="able to bring everyone along either."
        part=12; speaker[part]="Winston"
        chat1[part]="...How can you say that? You're a nurse, right?"
        chat2[part]="How do you choose one person over another?"
        chat3[part]=""
        part=13; speaker[part]="Ruth"
        chat1[part]="I do it all of the time. Not every patient can be"
        chat2[part]="saved. You can't save the whole world."
        chat3[part]=""
        part=14; speaker[part]="Winston"
        chat1[part]="You're right...I can't. But they don't need the"
        chat2[part]="saving, I do..."
        part=15; speaker[part]="Ruth"
        chat1[part]="You have a big decision coming up."
        chat2[part]="But where will you turn if no one will help you?"
        chat3[part]=""
        part=16; speaker[part]="Ruth"
        chat1[part]="Stay indecisive, Winston, for as long as you can."
        musicplay[part]="None"
        part=17
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Memory"):
        dorandomizeItems=0
        selectx=10; camerax=selectx
        selecty=10; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=7; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Lenna"; npcx[npcc]=8; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Gambler"; npcx[npcc]=15; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Dice" #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Cutthroat"; npcx[npcc]=15; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs
        npcc=4; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=15; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        #npcc=5; npc[npcc]=0; npcside[npcc]="Gambler"; npcx[npcc]=16; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Dice" #Create NPCs
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=9
        part=3; speaker[part]="Winston"
        chat1[part]="...And just down there we saved Floyd for the"
        chat2[part]="first time, you and me!"
        chat3[part]=""
        musicplay[part]="water"
        part=4
        createnpc[part]=1
        partdelay[part]=1
        part=5
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=11
        part=6; speaker[part]="Lenna"
        chat1[part]="I...hurt people?"
        part=7; speaker[part]="Winston"
        chat1[part]="Unfortunately, we both have."
        part=8; speaker[part]="Lenna"
        chat1[part]="..."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=11
        part=9; speaker[part]="Winston"
        chat1[part]="Hey, cheer up, all right?"
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=10
        part=10; speaker[part]="Lenna"
        chat1[part]="What if you get caught out here?"
        chat2[part]=""
        chat3[part]=""
        part=11; speaker[part]="Lenna"
        chat1[part]="You said the Officers are looking for you. And"
        chat2[part]="residents wouldn't take too kindly to seeing"
        chat3[part]="a murderer walking around."
        part=12; speaker[part]="Winston"
        chat1[part]="It's dark out, they won't find us here."
        chat2[part]=""
        chat3[part]=""
        part=13; speaker[part]="Winston"
        chat1[part]="Can you see it, though? Right over the waters lies"
        chat2[part]="freedom."
        chat3[part]=""
        part=14; speaker[part]="Lenna"
        chat1[part]="What sort of freedom is that? Just running from your"
        chat2[part]="problems..."
        chat3[part]=""
        part=15; speaker[part]="Winston"
        chat1[part]="Hrmm, that's Lucas's idea."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=8
        part=16; speaker[part]="Lenna"
        chat1[part]="Lucas doesn't sound all too patient. Would you"
        chat2[part]="really do something so risky...?"
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=10
        part=17; speaker[part]="Winston"
        chat1[part]="Well, a lot has happened. You really don't remember"
        chat2[part]="anything?"
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=9
        part=18; speaker[part]="Lenna"
        chat1[part]="Only faintly. But if what you've said is true,"
        chat2[part]="why would I want my memory back?"
        chat3[part]=""
        part=19; speaker[part]="Winston"
        chat1[part]="What do you mean by that?"
        part=20; speaker[part]="Lenna"
        chat1[part]="I don't want to be the angry, naive girl you've"
        chat2[part]="described."
        chat3[part]=""
        musicplay[part]="None"
        part=21; speaker[part]="Winston"
        chat1[part]="Lenna, I -"
        part=22
        createnpc[part]=2
        partdelay[part]=50
        part=23; speaker[part]="Man"
        chat1[part]="You monsters!"
        musicplay[part]="scary"
        part=24; speaker[part]="Lenna"
        chat1[part]="Excuse me?"
        part=25; speaker[part]="Man"
        chat1[part]="P-playing dumb? Y-you heartless woman. No one with"
        chat2[part]="a conscious would do what you did."
        chat3[part]=""
        part=26; speaker[part]="Winston"
        chat1[part]="Lenna? What is he talking about?"
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=6
        part=27; speaker[part]="Lenna"
        chat1[part]="Please, I don't remember doing anything..."
        part=28; speaker[part]="Man"
        chat1[part]="Y-you liar! *Sob* You'd lie in the face of me after"
        chat2[part]="all that?"
        chat3[part]=""
        musicplay[part]="None"
        part=29; speaker[part]="Man"
        chat1[part]="G-get her! Make her pay!"
        part=30
        createnpc[part]=3
        partdelay[part]=50
        musicplay[part]="action"
        part=31
        createnpc[part]=4
        partdelay[part]=50
        part=32
        #createnpc[part]=5
        partdelay[part]=50
        part=33
        controlChar=part
        part=35
        partdelay[part]=10
        part=36
        partdelay[part]=100
        part=37; speaker[part]="Winston"
        chat1[part]="Who were these people, Lenna?"
        musicplay[part]="None"
        part=38; speaker[part]="Lenna"
        chat1[part]="...I...I don't remember."
        part=39; speaker[part]="Winston"
        chat1[part]="What could you have done to them...?"
        musicplay[part]="calm"
        part=40; speaker[part]="Winston"
        chat1[part]="You must have done something, something bad, after"
        chat2[part]="you split from our group."
        part=41; speaker[part]="Lenna"
        chat1[part]="..."
        part=42; speaker[part]="Lenna"
        chat1[part]="So you weren't lying to me...this is all real..."
        chat2[part]="It's not like I needed any proof, my hazy memory"
        chat3[part]="is proof enough..."
        part=43; speaker[part]=" "
        chat1[part]="Lenna begins to cry."
        part=44; speaker[part]="Winston"
        chat1[part]="Hey now, don't cry."
        part=45; speaker[part]="Lenna"
        chat1[part]="M-my head...it hurts so much..."
        part=46; speaker[part]="Winston"
        chat1[part]="Just take it easy, I don't want you to faint."
        part=47; speaker[part]="Lenna"
        chat1[part]="I'm remem-...I think I recall something..."
        part=48; speaker[part]="Winston"
        chat1[part]="Hey, don't hurt yourself."
        part=49; speaker[part]="Lenna"
        chat1[part]="I remember...a-a white room..."
        part=50; speaker[part]="Winston"
        chat1[part]="A white room? Try to think, any other details?"
        part=51; speaker[part]="Lenna"
        chat1[part]="Follow me. I'll show you the way..."
        musicplay[part]="None"
        part=52
        changelevelpart=part; changelevelto="LevelMenu"; day=21; chapter+=1
        part=100; speaker[part]="Lenna"
        chat1[part]="Winston...at least now you can finally forget."
        part=101
        gotopart[part]=110
        part=105; speaker[part]="Winston"
        chat1[part]="Lenna! What did you do!?"
        part=106
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Gamble"):
        dorandomizeItems=0
        item[0]="Dice"; itemx[0]=4; itemy[0]=7
        item[1]="Cards"; itemx[1]=4; itemy[1]=7
        selectx=8; camerax=selectx
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=5; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=6; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Security"; npcx[npcc]=5; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Guard"; npcx[npcc]=8; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Debter"; npcx[npcc]=7; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Cards" #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Gambler"; npcx[npcc]=7; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Cards" #Create NPCs
        npcc=6; npc[npcc]=0; npcside[npcc]="Bettor"; npcx[npcc]=10; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Cards" #Create NPCs
        npcc=7; npc[npcc]=0; npcside[npcc]="Dicer"; npcx[npcc]=3; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Dice" #Create NPCs
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=7
        part=3; speaker[part]="Winston"
        chat1[part]="A casino? Why are we here, Lenna?"
        musicplay[part]="standby"
        part=4; speaker[part]="Lenna"
        chat1[part]="I just...I-I remember this casino. I faintly"
        chat2[part]="remember being here..."
        chat3[part]=""
        part=5
        partdelay[part]=35
        part=6; speaker[part]="Security"
        chat1[part]="Next!"
        part=7
        movenpc[part]=4; movenpcx[part]=7; movenpcy[part]=3
        part=8; speaker[part]="Security"
        chat1[part]="ID."
        part=9; speaker[part]=" "
        chat1[part]="The man hands over identification."
        part=10; speaker[part]="Security"
        chat1[part]="You're clear. Have a good time."
        part=11; speaker[part]="Debtor"
        chat1[part]="I heard about what happened earlier today..."
        chat2[part]="Whatever man, maybe I'll finally be able to pay off"
        chat3[part]="my dept after tonight."
        part=12
        movenpc[part]=4; movenpcx[part]=7; movenpcy[part]=2
        part=13
        partdelay[part]=10
        createnpc[part]=-4
        part=14; speaker[part]="Winston"
        chat1[part]="Did you hear what he said? Something happened"
        chat2[part]="here... It wouldn't happen to have concerned"
        chat3[part]="you, would it?"
        part=15; speaker[part]="Lenna"
        chat1[part]="I'm trying to remember..."
        part=16
        movenpc[part]=5; movenpcx[part]=7; movenpcy[part]=7
        part=17; speaker[part]="Gambler"
        chat1[part]="Sorry to eavesdrop, but you look pretty darn"
        chat2[part]="similiar to a peculiar girl who came through here"
        chat3[part]="this morning."
        part=18; speaker[part]="Lenna"
        chat1[part]="What did I do...?"
        part=19; speaker[part]="Gambler"
        chat1[part]="Hehe...Here's my ID card, go in and see for"
        chat2[part]="yourself."
        chat3[part]=""
        part=20; speaker[part]=" "
        chat1[part]="The gambler hands an ID card over to Winston."
        part=21; speaker[part]="Gambler"
        chat1[part]="And if you're curious. Cards can be sharp throwing"
        chat2[part]="weapons. Not much use close-up, though. Also,"
        chat3[part]="you'll never run out of cards to throw."
        part=22; speaker[part]="Gambler"
        chat1[part]="Dice will deal random damage. If you're lucky,"
        chat2[part]="they can get you out of anything."
        chat3[part]=""
        part=23
        movenpc[part]=5; movenpcx[part]=7; movenpcy[part]=3
        part=24; speaker[part]="Security"
        chat1[part]="ID...You're clear. Stay out of trouble."     
        part=25
        movenpc[part]=5; movenpcx[part]=7; movenpcy[part]=2
        part=26
        partdelay[part]=10
        createnpc[part]=-5
        part=27; speaker[part]="Lenna"
        chat1[part]="Cards? Dice?"
        part=28; speaker[part]="Winston"
        chat1[part]="Sounds like advice. I'm going after him."
        part=29
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=3
        musicplay[part]="None"
        part=30; speaker[part]="Security"
        chat1[part]="ID."
        chat2[part]=""
        chat3[part]=""
        part=31; speaker[part]="Winston"
        chat1[part]="Right here."
        part=32
        partdelay[part]=50
        part=33; speaker[part]="Security"
        chat1[part]="...That your friend over there, Jacob?"
        choice1[part]="Jacob?"; choice1go[part]=34 #Choices Given
        choice2[part]="She's not with me."; choice2go[part]=34
        choice3[part]="That's Lenna."; choice3go[part]=36
        part=34; speaker[part]="Winston"
        chat1[part]="Jaco-? Er, um, yeah, that's me all right. That"
        chat2[part]="girl? She's not coming in with me, don't worry"
        chat3[part]="about her."
        part=35; speaker[part]="Guard"
        chat1[part]="Don't she look awfully familiar?"
        part=36; speaker[part]="Security"
        chat1[part]="That's the girl! Security, apprehend her!"
        musicplay[part]="threefour"
        part=37; speaker[part]="Winston"
        chat1[part]="Uh-oh."
        part=38
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=7
        part=39
        createnpc[part]=6
        partdelay[part]=30
        part=40
        movenpc[part]=6; movenpcx[part]=10; movenpcy[part]=10
        part=41; speaker[part]="Bettor"
        chat1[part]="I knew she'd come back!"
        part=42
        createnpc[part]=7
        partdelay[part]=30
        part=43
        partdelay[part]=5
        part=44; speaker[part]="Dicer"
        chat1[part]="Let's get our money back!"
        part=45
        controlChar=part
        part=50; speaker[part]="Winston" #Defeated all Enemies
        chat1[part]="Let's get out of here before more of them come!"
        part=51
        createnpc[part]=4
        partdelay[part]=20
        musicplay[part]="None"
        part=52; speaker[part]="Gambler"
        chat1[part]="Hold on! I'm coming with you!"
        musicplay[part]="guitar"
        part=53; speaker[part]="Winston"
        chat1[part]="Huh, why?"
        part=54; speaker[part]="Gambler"
        chat1[part]="I'll have better luck with you guys. Maybe"
        chat2[part]="I could get some of that money too, eh, Lenna?"
        chat3[part]=""
        part=55; speaker[part]="Lenna"
        chat1[part]="...Money?"
        part=56; speaker[part]="Gambler"
        chat1[part]="You did steal a ton of money, didn't you?"
        chat2[part]="You must've hid it somewhere."
        part=57; speaker[part]="Winston"
        chat1[part]="That's right, one of those guys said something"
        chat2[part]="about getting their money back. If you were to"
        chat3[part]="remember where you put it..."
        part=58; speaker[part]="Gambler"
        chat1[part]="Odds are, you'll remember. I'd bet my life"
        chat2[part]="on it."
        chat3[part]=""
        part=59; speaker[part]="Lenna"
        chat1[part]="Oww...my head..."
        part=60; speaker[part]="Lenna"
        chat1[part]="I-I'm remembering another place..."
        part=61; speaker[part]="Lenna"
        chat1[part]="Follow me..."
        part=62; speaker[part]="Gambler"
        chat1[part]="You heard the girl, let's head out!"
        musicplay[part]="None"
        part=63
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        part=100; speaker[part]="Winston"
        chat1[part]="Run away, Lenna! Forget about me!"
        part=101; speaker[part]="Lenna"
        chat1[part]="I already have..."
        part=102
        gotopart[part]=110
        part=105; speaker[part]="Winston"
        chat1[part]="Lenna!"
        part=106; speaker[part]="Lenna"
        chat1[part]="I finally remember...and I deserve this death"
        chat2[part]="because of it."
        chat3[part]=""
        part=107
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Lab"):
        dorandomizeItems=0
        item[0]="Bottle"; itemx[0]=9; itemy[0]=13
        item[1]="Med Kit"; itemx[1]=9; itemy[1]=13
        selectx=7; camerax=selectx
        selecty=7; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        #tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        #tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=9; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=8; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Cutthroat"; npcx[npcc]=13; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Bottle" #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Experiment"; npcx[npcc]=1; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Shiv" #Create NPCs
        npcc=4; npc[npcc]=0; npcside[npcc]="Experiment"; npcx[npcc]=7; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        #npcc=5; npc[npcc]=0; npcside[npcc]="Experiment"; npcx[npcc]=2; npcy[npcc]=1; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        part=1
        partdelay[part]=1
        part=2
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=10
        part=3; speaker[part]="Winston"
        chat1[part]="Lenna, what are we doing here?"
        musicplay[part]="ambient"
        part=4; speaker[part]="Lenna"
        chat1[part]="I'm not sure. I just had an urge to go to"
        chat2[part]="the hotel's basement."
        chat3[part]=""
        part=5; speaker[part]="Winston"
        chat1[part]="Huh...we're wasting our time here."
        part=6
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=8
        part=7; speaker[part]="Lenna"
        chat1[part]="Maybe we are. But, the walls..."
        part=8
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=10
        part=9; speaker[part]="Winston"
        chat1[part]="The walls? You remember something about"
        chat2[part]="the walls?"
        chat3[part]=""
        part=10
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=7
        part=11; speaker[part]="Lenna"
        chat1[part]="Yes...give me a moment. I'm feeling around"
        chat2[part]="for something."
        chat3[part]=""
        part=12; speaker[part]="Winston"
        chat1[part]="We really should be looking for Lucas and"
        chat2[part]="Floyd..."
        chat3[part]=""
        musicplay[part]="None"
        part=13
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=7
        part=14; speaker[part]="Lenna"
        chat1[part]="Aha! Found it!"
        part=15; speaker[part]="Winston"
        chat1[part]="A secret door!? When did you come to"
        chat2[part]="find this?"
        chat3[part]=""
        musicplay[part]="scary"
        part=16; speaker[part]="Lenna"
        chat1[part]="Maybe some exploring will help jog my memory."
        part=17
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=5
        part=18; speaker[part]="Winston"
        chat1[part]="A hallway? Do employees here even know about"
        chat2[part]="this place?"
        chat3[part]=""
        part=19
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=6
        part=20
        createnpc[part]=3
        partdelay[part]=50
        part=21
        partdelay[part]=5
        part=22; speaker[part]="Lenna"
        chat1[part]="Excuse me, but who are you?"
        part=23; speaker[part]="Experiment"
        chat1[part]="Me? Who am I!? I don't REMEMBER, Gah! Where"
        chat2[part]="am I going!? Have you come to save me...?"
        chat3[part]=""
        part=24; speaker[part]="Winston"
        chat1[part]="What the-? This guy doesn't remember anything,"
        chat2[part]="just like you, Lenna."
        chat3[part]=""
        part=25; speaker[part]="Lenna"
        chat1[part]="Sir, I'm sorry...I've lost my memory too..."
        part=26; speaker[part]="Experiment"
        chat1[part]="If you won't let me out, I - I - I'll kill you"
        chat2[part]="all! You're working with that scientist, aren't"
        chat3[part]="you? You're gonna pay for what you did to us!"
        part=27; speaker[part]="Winston"
        chat1[part]="Scientist? No point asking right now, he won't"
        chat2[part]="listen."
        chat3[part]=""
        musicplay[part]="None"
        part=28
        createnpc[part]=2
        partdelay[part]=30
        part=29
        createnpc[part]=4
        partdelay[part]=30
        part=30
        #createnpc[part]=5
        partdelay[part]=30
        musicplay[part]="action"
        part=31
        controlChar=part
        part=50
        partdelay[part]=10
        part=51
        partdelay[part]=50
        part=52; speaker[part]="Winston"
        chat1[part]="These people all look like residents of this"
        chat2[part]="hotel. But their minds were warped..."
        chat3[part]=""
        musicplay[part]="None"
        part=53; speaker[part]="Lenna"
        chat1[part]="Ugh...my head...the pain is returning..."
        part=54; speaker[part]="Winston"
        chat1[part]="Are you remembering something?"
        part=55; speaker[part]="Lenna"
        chat1[part]="..."
        part=56; speaker[part]="Lenna"
        chat1[part]="Th-this is a laboratory."
        musicplay[part]="calm"
        part=57; speaker[part]="Lenna"
        chat1[part]="Just like these people, I was an experiment"
        chat2[part]="here."
        chat3[part]=""
        part=58; speaker[part]="Lenna"
        chat1[part]="But then, I escaped. It feels like it was years"
        chat2[part]="ago, but I know it was just earlier today..."
        chat3[part]=""
        part=59; speaker[part]="Lenna"
        chat1[part]="I must have been captured when I split from you,"
        chat2[part]="Winston."
        chat3[part]=""
        part=60; speaker[part]="Winston"
        chat1[part]="He said something about a scientist."
        part=61; speaker[part]="Lenna"
        chat1[part]="The scientist...Yes...This lab is run by a single"
        chat2[part]="scientist. He captured me and took me here."
        chat3[part]=""
        part=62; speaker[part]="Lenna"
        chat1[part]="...He experiments on people in this hotel. To"
        chat2[part]="some people, like me, he erases memories."
        chat3[part]=""
        part=63; speaker[part]="Winston"
        chat1[part]="Jeeze, a whole lot happened to you in just one day."
        part=64; speaker[part]="Lenna"
        chat1[part]="I escaped before he could do anything else to me."
        chat2[part]="All I lost is my memory."
        chat3[part]=""
        part=65; speaker[part]="Winston"
        chat1[part]="You lost a lot more than just some memory. You"
        chat2[part]="lost your personality, your recollection of me..."
        chat3[part]=""
        part=66; speaker[part]="Lenna"
        chat1[part]="And is that a bad thing, Winston? It's been"
        chat2[part]="better for me to rediscover these things,"
        chat3[part]="don't you think?"
        part=67; speaker[part]="Winston"
        chat1[part]="Well...let's get out of here before more of them"
        chat2[part]="come. We can talk then."
        chat3[part]=""
        musicplay[part]="None"
        part=68
        changelevelpart=part; changelevelto="LevelMenu"; day=22; chapter+=1
        part=100; speaker[part]="Winston"
        chat1[part]="Run away, Lenna! Forget about me!"
        part=101; speaker[part]="Lenna"
        chat1[part]="I already have..."
        part=102
        gotopart[part]=110
        part=105; speaker[part]="Winston"
        chat1[part]="Lenna!"
        part=106; speaker[part]="Lenna"
        chat1[part]="I finally remember...and I deserve this death"
        chat2[part]="because of it."
        chat3[part]=""
        part=107
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Talk"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=3; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=3; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        part=1
        partdelay[part]=40
        part=2; speaker[part]="Winston"
        chat1[part]="How do you feel?"
        part=3; speaker[part]="Lenna"
        chat1[part]="How should I feel...? My memory was taken from me"
        chat2[part]="for \"science\". At least, right now, I don't"
        chat3[part]="feel much of anything."
        part=4; speaker[part]="Winston"
        chat1[part]="Then let's go back to the lab. Maybe we could"
        chat2[part]="find a way to get you your memory back."
        chat3[part]=""
        part=5
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=10
        part=6; speaker[part]="Lenna"
        chat1[part]="Wait. No, I-I don't want my memory back..."
        musicplay[part]="calm"
        part=7; speaker[part]="Winston"
        chat1[part]="Huh? Why?"
        part=8; speaker[part]="Lenna"
        chat1[part]="Be honest, Winston. Don't you think I'm"
        chat2[part]="a better person now? You said it yourself:"
        chat3[part]="I used to be mean, rude..."
        choice1[part]="You were who you were."; choice1go[part]=10 #Choices Given
        choice2[part]="You've improved."; choice2go[part]=13
        part=10; speaker[part]="Winston" #Choice 1
        chat1[part]="You were who you were. It doesn't matter if"
        chat2[part]="you're better off this way."
        chat3[part]=""
        part=11; speaker[part]="Lenna"
        chat1[part]="I've completely changed...Why go back to"
        chat2[part]="my old self and remember whatever angry,"
        chat3[part]="bitter thoughts made me who I was."
        part=12
        gotopart[part]=15
        part=13; speaker[part]="Winston" #Choice 2
        chat1[part]="Well, you've improved."
        part=14; speaker[part]="Lenna"
        chat1[part]="I've completely changed...Why go back to"
        chat2[part]="my old self and remember whatever angry,"
        chat3[part]="bitter thoughts made me who I was."
        part=15; speaker[part]="Lenna"
        chat1[part]="And you too..."
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=11
        part=16; speaker[part]="Winston"
        chat1[part]="What about me?"
        part=17; speaker[part]="Lenna"
        chat1[part]="Oh, uh, forget I mentioned you...I'll tell"
        chat2[part]="you later."
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=10
        part=18
        partdelay[part]=50
        part=19; speaker[part]="Lenna"
        chat1[part]="You'd rather forget too, I can feel it."
        chat2[part]=""
        chat3[part]=""        
        choice1[part]="I'd rather forget this whole mess."; choice1go[part]=20 #Choices Given
        choice2[part]="I'd rather try to overcome it."; choice2go[part]=25
        part=20; speaker[part]="Winston" #Choice 1
        chat1[part]="You're right, I'd rather forget this whole"
        chat2[part]="mess."
        chat3[part]=""
        part=21; speaker[part]="Lenna"
        chat1[part]="I knew you'd feel the same way. We're very"
        chat2[part]="similar, Winston. You and me..."
        chat3[part]=""
        part=22
        gotopart[part]=30
        part=25; speaker[part]="Winston" #Choice 2
        chat1[part]="I'd rather try and overcome it. Isn't that what"
        chat2[part]="you said earlier? Forgetting is just running"
        chat3[part]="away from our problems."
        part=26; speaker[part]="Lenna"
        chat1[part]="What other choice is there? You either forget..."
        chat2[part]="or die."
        chat3[part]=""
        part=27
        gotopart[part]=30
        part=30; speaker[part]="Lenna"
        chat1[part]="You've heard that old dilemma, haven't you?"
        chat2[part]="The one with the tree. It goes something like"
        chat3[part]="this..."
        part=31; speaker[part]="Lenna"
        chat1[part]="\"If a tree falls in the woods and no one is"
        chat2[part]="around to hear it, does it make a sound?\""
        chat3[part]=""
        part=32; speaker[part]="Lenna"
        chat1[part]="I've thought about that a lot. Most people would"
        chat2[part]="say: yes, it did make a sound. The event still"
        chat3[part]="occured, right? Those people miss the point..."
        part=33; speaker[part]="Lenna"
        chat1[part]="Now, what if everyone in this hotel were to"
        chat2[part]="forget our crimes? Then, did they ever happen?"
        chat3[part]=""
        part=34; speaker[part]="Lenna"
        chat1[part]="Maybe I'm thinking too much...B-but, I have one"
        chat2[part]="last question. Do you think ignorance is bliss?"
        chat3[part]=""
        choice1[part]="It is."; choice1go[part]=35 #Choices Given
        choice2[part]="It's not."; choice2go[part]=40
        part=35; speaker[part]="Winston" #Choice 1
        chat1[part]="I think it is."
        chat2[part]=""
        chat3[part]=""
        part=36; speaker[part]="Lenna"
        chat1[part]="It's such a scary word - ignorance. Ignorance..."
        chat2[part]="But really, it's the very opposite."
        chat3[part]="Wouldn't you be happier not knowing the truth?"
        part=37
        gotopart[part]=43
        part=40; speaker[part]="Winston" #Choice2
        chat1[part]="No, it's not. Ignorance is not bliss."
        chat2[part]=""
        chat3[part]=""
        part=41; speaker[part]="Lenna"
        chat1[part]="Wouldn't you be happier not knowing the truth?"
        chat2[part]="Everything is meaningless anyway! Oh, vanity"
        chat3[part]="of vanities! Our effort is futile..."
        part=42
        gotopart[part]=43
        part=43; speaker[part]="Lenna"
        chat1[part]="What I'm trying to get at is - well, I..."
        part=44; speaker[part]="Lenna"
        chat1[part]="Let's forget together, Winston. We'll go back"
        chat2[part]="to the lab and see if we can find whatever"
        chat3[part]="device was used to erase my memory, a-and..."
        part=45; speaker[part]="Lenna"
        chat1[part]="And th-then...we'll be happy."
        part=46; speaker[part]="Winston"
        chat1[part]="I guess, in a way, everything that's happened"
        chat2[part]="in the last few days...wouldn't have happened."
        chat3[part]=""
        part=47; speaker[part]=" "
        chat1[part]="Lenna begins to cry."
        part=48; speaker[part]="Lenna"
        chat1[part]="*Sniff*"
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=9
        part=49; speaker[part]="Winston"
        chat1[part]="H-hey...get some sleep, all right? We'll think"
        chat2[part]="of what to do tomorrow morning."
        chat3[part]=""
        part=50; speaker[part]="Lenna"
        chat1[part]="You don't even care!"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=11
        part=51; speaker[part]="Winston"
        chat1[part]="Don't be like that..."
        part=52; speaker[part]="Lenna"
        chat1[part]="...I need to think alone."
        part=53; speaker[part]="Winston"
        chat1[part]="I'll be in the other room, okay?"
        musicplay[part]="None"
        part=54; speaker[part]="Winston"
        chat1[part]="*Sigh*"
        part=55
        changelevelpart=part; changelevelto="LevelMenu"; day=23; chapter+=1
    if (level=="Extra"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=11; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="David"; npcx[npcc]=6; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=10
        part=2; speaker[part]="Winston"
        chat1[part]="Lenna, try to hurry up!"
        part=3; speaker[part]="Winston"
        chat1[part]="Hrmph."
        part=4
        createnpc[part]=1
        partdelay[part]=40
        part=5; speaker[part]="Winston"
        chat1[part]="Hey, who're you?"
        part=6
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=7
        part=7
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=7
        part=8; speaker[part]="David"
        chat1[part]="Your party's not as full as it could be."
        chat2[part]="You know that already though, right?"
        chat3[part]=""
        musicplay[part]="mystery"
        part=9
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=7
        part=10; speaker[part]="David"
        chat1[part]="How'd that happen? Were you ignoring your"
        chat2[part]="friends? Or, was it death?"
        chat3[part]=""
        part=11; speaker[part]="Winston"
        chat1[part]="What?"
        part=12; speaker[part]="David"
        chat1[part]="It doesn't matter. I'm here to help."
        chat2[part]=""
        chat3[part]=""
        part=13; speaker[part]="Winston"
        chat1[part]="That's great and all, but who exactly are you?"
        part=14; speaker[part]="David"
        chat1[part]="Want my help or not? Do you know Kurt, Frederick,"
        chat2[part]="or Matthew? Or has your carelessness killed them?"
        chat3[part]=""
        musicplay[part]="None"
        part=15
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="NoRuth"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=7; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Winston"
        chat1[part]="It's time to make my choice. It's time to"
        chat2[part]="end this nightmare. If I wait any longer,"
        chat3[part]="I'll go insane."
        musicplay[part]="calm"
        part=3; speaker[part]="Winston"
        chat1[part]="I wonder what Lenna thinks of me. Her idea"
        chat2[part]="sounds crazy..."
        chat3[part]=""
        if (lenna>=2):
            part=4; speaker[part]="Winston"
            chat1[part]="Erase the memory of everyone in the hotel?"
            chat2[part]="I mean, it might work, but...is ignorance"
            chat3[part]="really bliss?"
        if (lenna<2):
            part=4; speaker[part]="Winston"
            chat1[part]="Erase the memory of everyone in the hotel?"
            chat2[part]="Doesn't matter, she won't help me. Not after"
            chat3[part]="the way I replied to her."            
        part=5; speaker[part]="Winston"
        chat1[part]="What about Lucas? Floyd...? I could go find"
        chat2[part]="them...even if it means abandoning Lenna."
        chat3[part]=""
        if (lucas>=2):
            part=6; speaker[part]="Winston"
            chat1[part]="Lucas wants to escape the hotel. It's not just"
            chat2[part]="for himself, he wants to liberate the people from"
            chat3[part]="the law upheld by the Officers."
        if (lucas<2):
            part=6; speaker[part]="Winston"
            chat1[part]="Lucas won't want anything to do with me. He's"
            chat2[part]="gone rogue. I mean, escape the hotel? ...He's"
            chat3[part]="too prideful to follow the law."
        if (floyd>=2):
            part=7; speaker[part]="Winston"
            chat1[part]="Then there's Floyd. He wants to destroy the hotel..."
            chat2[part]="But how? End all communcation...? They sound like"
            chat3[part]="awful extremes."
        if (floyd<2):
            part=7; speaker[part]="Winston"
            chat1[part]="Floyd is out of the picture. Ending all"
            chat2[part]="communication and destroying the hotel sound like"
            chat3[part]="awful extremes."
        if (ruth!=4):
            part=8; speaker[part]="Winston"
            chat1[part]="Are there really no other options? Oh, Ruth, if"
            chat2[part]="only you were here! You'd know what to do!"
            chat3[part]=""
        if (ruth==0):
            part=8; speaker[part]="Winston"
            chat1[part]="Are there really no other options? Did I miss"
            chat2[part]="something on the way here?"
            chat3[part]=""
        part=9; speaker[part]="Winston"
        chat1[part]="...I have to choose. It's now or never."
        chat2[part]="I wonder, what would I do if none of"
        chat3[part]="my friends were willing to help me?"
        musicplay[part]="None"
        part=10
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Ruth4"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=13; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Ruth"; npcx[npcc]=13; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=1; movenpcx[part]=13; movenpcy[part]=9
        part=3; speaker[part]="Ruth"
        chat1[part]="Lenna fell asleep. I thought I'd try to find you,"
        chat2[part]="Winston."
        chat3[part]=""
        musicplay[part]="calm"
        part=4; speaker[part]="Winston"
        chat1[part]="Thanks, Ruth..."
        part=5; speaker[part]="Ruth"
        chat1[part]="It's been a long time coming, but now you need"
        chat2[part]="to choose."
        chat3[part]=""
        part=6; speaker[part]="Winston"
        chat1[part]="Choose? You mean, finally end this nightmare?"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=13; movenpcy[part]=11
        part=7; speaker[part]="Ruth"
        chat1[part]="You could stay here with Lenna. You've heard"
        chat2[part]="her side: erasing everyone's memory. But is"
        chat3[part]="ignorance truly bliss?"
        if (lenna>=2):
            part=8; speaker[part]="Winston"
            chat1[part]="It's crazy, but...it might work. How"
            chat2[part]="could I abandon Lenna, though?"
            chat3[part]=""
        if (lenna<2):
            part=8; speaker[part]="Winston"
            chat1[part]="Doesn't matter, she won't help me. Not"
            chat2[part]="after the way I replied to her."
            chat3[part]=""
        part=9; speaker[part]="Ruth"
        chat1[part]="Then there's Lucas and Floyd. Each has his"
        chat2[part]="own plan."
        chat3[part]=""        
        part=10; speaker[part]="Ruth"
        chat1[part]="Maybe the Officer gone rogue, Lucas? He wants"
        chat2[part]="to escape the hotel and destroy the law being"
        chat3[part]="upheld by the Officers."
        if (lucas>=2):
            part=11; speaker[part]="Winston"
            chat1[part]="Definitely the more violent option. It's not just"
            chat2[part]="for himself, it's to lift the oppression of"
            chat3[part]="the Officers. He's too prideful for rules."
        if (lucas<2):
            part=11; speaker[part]="Winston"
            chat1[part]="Lucas won't want anything to do with me."
            chat2[part]="Definitely the more violent option...He's"
            chat3[part]="too prideful for the Officer's rules."
        part=12; speaker[part]="Ruth"
        chat1[part]="And finally, Floyd. Destroy the hotel and end all"
        chat2[part]="communication - that's his plan. Sounds rather"
        chat3[part]="extreme, don't you think?"
        if (floyd>=2):
            part=13; speaker[part]="Winston"
            chat1[part]="It's something this hotel has had a long time"
            chat2[part]="coming. My question is: how will he achieve"
            chat3[part]="it?"
        if (floyd<2):
            part=13; speaker[part]="Winston"
            chat1[part]="Floyd is out of the picture. Ending all"
            chat2[part]="communication and destroying the hotel sound like"
            chat3[part]="awful extremes."
        part=14; speaker[part]="Winston"
        chat1[part]="Are there really no other options?"
        part=15; speaker[part]="Ruth"
        chat1[part]="None offered by your friends."
        part=16; speaker[part]="Ruth"
        chat1[part]="You are too reliant on sinful, flawed people."
        chat2[part]="I'm no exception, am I not?"
        chat3[part]=""
        part=17; speaker[part]="Winston"
        chat1[part]="B-but, they're offering me a way out. With friends,"
        chat2[part]="I always have support when I need it!"
        part=18; speaker[part]="Ruth"
        chat1[part]="Maybe a little hopelessness will show you another"
        chat2[part]="way. If none of your friends were willing to"
        chat3[part]="help you, would another path open up?"
        part=19; speaker[part]="Ruth"
        chat1[part]="This is where my advice ends, Winston. You"
        chat2[part]="must make a choice."
        chat3[part]=""
        part=20; speaker[part]="Winston"
        chat1[part]="...It's now or never. Thank you, Ruth."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=21
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="LucasChoice"):
        dorandomizeItems=0
        selectx=9; camerax=selectx
        selecty=10; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=14; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Lucas"; npcx[npcc]=14; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=10
        part=2; speaker[part]="Winston"
        chat1[part]="Lucas!"
        part=3
        movenpc[part]=0; movenpcx[part]=11; movenpcy[part]=11
        part=4; speaker[part]="Winston"
        chat1[part]="Lucas! You here?"
        part=5
        movenpc[part]=0; movenpcx[part]=11; movenpcy[part]=9
        part=6; speaker[part]="Winston"
        chat1[part]="You were right! Let's fight the Officers! We'll"
        chat2[part]="escape!"
        chat3[part]=""
        part=7
        movenpc[part]=0; movenpcx[part]=11; movenpcy[part]=12
        part=8; speaker[part]="Winston"
        chat1[part]="..."
        part=9
        createnpc[part]=1
        partdelay[part]=40
        part=10; speaker[part]="Lucas"
        chat1[part]="I thought you might try to find me. And where's"
        chat2[part]="Floyd?"
        chat3[part]=""
        musicplay[part]="mystery"
        part=11; speaker[part]="Winston"
        chat1[part]="Lucas! And, Floyd has his own idea on escaping."
        chat2[part]="He left me to pursue it."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=12; movenpcy[part]=12
        part=12; speaker[part]="Lucas"
        chat1[part]="What a boring old man. He can sit on the sidelines,"
        chat2[part]="but I - no, we...won't play cautiously while"
        chat3[part]="enforcers of the law hunt us down."
        movenpc[part]=1; movenpcx[part]=13; movenpcy[part]=11
        part=13; speaker[part]="Winston"
        chat1[part]="What do you propose we do now?"
        part=14; speaker[part]="Lucas"
        chat1[part]="I've scouted out the bottom floor front exit."
        chat2[part]="Officers are guarding it, most likely to prevent"
        chat3[part]="us from leaving."
        part=15; speaker[part]="Winston"
        chat1[part]="And we'll be taking the direct approach, huh?"
        part=16; speaker[part]="Lucas"
        chat1[part]="We go big or die trying. Past the exit is the front"
        chat2[part]="courtyard. The gate to freedom lies right ahead."
        chat3[part]=""
        part=17; speaker[part]="Lucas"
        chat1[part]="We'll show them! The law is imperfect! You're here,"
        chat2[part]="so you agree, right?"
        chat3[part]=""
        part=18; speaker[part]="Lucas"
        chat1[part]="We're fighting for ourselves...but in the process,"
        chat2[part]="we're destroying the law. Without Officers,"
        chat3[part]="residents will live unoppressed and free!"
        part=19; speaker[part]="Lucas"
        chat1[part]="We'll take the elevator. Come on, a bright"
        chat2[part]="future awaits for us and everyone else!"
        chat3[part]=""
        musicplay[part]="None"
        part=20
        changelevelpart=part; changelevelto="LevelMenu"; day=30; chapter+=1
    if (level=="Lobby"):
        dorandomizeItems=0
        item[0]="Bottle"; itemx[0]=3; itemy[0]=16
        item[1]="Med Kit"; itemx[1]=3; itemy[1]=16
        selectx=5; camerax=selectx
        selecty=10; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=2; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=6; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=3; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=6; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=4; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=1; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Knife" #Create NPCs
        npcc=5; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=8; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        npcc=6; npc[npcc]=0; npcside[npcc]="Officer"; npcx[npcc]=8; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=13
        part=3; speaker[part]="Lucas"
        chat1[part]="This is it? Let's make quick work of them."
        chat2[part]="Are you ready, Winston?"
        chat3[part]=""
        part=4; speaker[part]="Winston"
        chat1[part]="I'm ready."
        part=5; speaker[part]="Officer"
        chat1[part]="Do not let them escape!"
        musicplay[part]="threefour"
        part=6
        controlChar=part
        part=10
        partdelay[part]=10
        part=11
        partdelay[part]=20
        part=12
        createnpc[part]=4
        partdelay[part]=30
        part=13
        createnpc[part]=5
        partdelay[part]=30
        part=14
        createnpc[part]=6
        partdelay[part]=30
        part=15; speaker[part]="Lucas"
        chat1[part]="More? Doesn't matter, we'll kill all"
        chat2[part]="ten thousand of you!"
        chat3[part]=""
        part=16; speaker[part]="Winston"
        chat1[part]="Let's start with these three first, all"
        chat2[part]="right?"
        chat3[part]=""
        part=17
        part=20; speaker[part]="Winston"
        chat1[part]="I - I don't feel right about this..."
        chat2[part]=""
        chat3[part]=""
        part=21; speaker[part]="Lucas"
        chat1[part]="What? Murder?"
        musicplay[part]="None"
        part=22; speaker[part]="Winston"
        chat1[part]="With no Officers, who's to keep the hotel residents"
        chat2[part]="in line? I haven't seen a single innocent resident"
        chat3[part]="since I first came here three days ago."
        musicplay[part]="mystery"
        part=23; speaker[part]="Lucas"
        chat1[part]="People will follow theirselves. Maybe follow an"
        chat2[part]="\"Eye for an Eye\" philosophy if you so will..."
        chat3[part]=""
        part=24; speaker[part]="Lucas"
        chat1[part]="Do you really want other people's beliefs to intrude"
        chat2[part]="on what you can and can't do?"
        chat3[part]=""
        part=25; speaker[part]="Lucas"
        chat1[part]="Push past the entrance before more of them appear."
        chat2[part]="It's a race to the gate!"
        chat3[part]=""
        musicplay[part]="None"
        part=26
        changelevelpart=part; changelevelto="LevelMenu"; day=31; chapter+=1
        part=100; speaker[part]="Lucas"
        chat1[part]="I'll go on without you."
        chat2[part]=""
        chat3[part]=""
        part=101
        gotopart[part]=110
        part=105; speaker[part]="Winston"
        chat1[part]="I surrender!"
        chat2[part]=""
        chat3[part]=""
        part=106
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Sanders"):
        selectx=12; camerax=selectx #Camera Position
        selecty=19; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=1; npc[npcc]=0; npcside[npcc]="Winston"; npcx[npcc]=15; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=14; npcy[npcc]=15; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Sanders"; npcx[npcc]=9; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=3; movenpcx[part]=11; movenpcy[part]=15
        part=3; speaker[part]="Lucas"
        chat1[part]="The Officers' headquarters."
        part=4
        createnpc[part]=1
        partdelay[part]=20
        part=5
        movenpc[part]=1; movenpcx[part]=11; movenpcy[part]=14
        part=6; speaker[part]="Winston"
        chat1[part]="But where are all the Officers?"
        part=7; speaker[part]="Lucas"
        chat1[part]="They must be guarding the gate. It'll be one"
        chat2[part]="final fight. Keep going, we can't stop."
        chat3[part]=""
        part=8
        movenpc[part]=3; movenpcx[part]=6; movenpcy[part]=15
        part=9
        createnpc[part]=2
        partdelay[part]=30
        part=10; speaker[part]="Sanders"
        chat1[part]="Why the hurry?"
        musicplay[part]="mystery"
        part=11
        movenpc[part]=3; movenpcx[part]=7; movenpcy[part]=15
        part=12; speaker[part]="Lucas"
        chat1[part]="Who're you!? Some Officer?"
        part=13; speaker[part]="Winston"
        chat1[part]="He's no enforcer, that's Sanders! Careful,"
        chat2[part]="Lucas, he's got dangerous influence."
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=14
        part=14; speaker[part]="Sanders"
        chat1[part]="Shut it, you little - Hrmph, where are my manners,"
        chat2[part]="now?"
        chat3[part]=""
        part=15; speaker[part]="Sanders"
        chat1[part]="Lucas, he called you? Greetings, my name is Sanders."
        chat2[part]="I'm but an entrepreneur, you see..."
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=8; movenpcy[part]=12
        part=16; speaker[part]="Winston"
        chat1[part]="After what you did to Adam and Evelyn? Don't trust"
        chat2[part]="him for a second, Lucas!"
        chat3[part]=""
        part=17; speaker[part]="Sanders"
        chat1[part]="Ah, can we not begin anew, Winston? Grudges are not"
        chat2[part]="healthy..."
        chat3[part]=""
        part=18; speaker[part]="Lucas"
        chat1[part]="We don't have time for this...Look, uh - Sanders? -"
        chat2[part]="what do you want from us? We really need to get"
        chat3[part]="going."
        part=19; speaker[part]="Sanders"
        chat1[part]="It appears patience develops with age. Aren't you"
        chat2[part]="a little young to be killing, anyway?"
        part=20; speaker[part]="Sanders"
        chat1[part]="Ah! He-he! But let us not mince words! You've caused"
        chat2[part]="quite a stir with the residents here. \"Where did"
        chat3[part]="the Officers go?\", they vainly ponder."
        part=21; speaker[part]="Sanders"
        chat1[part]="And, lo, how many supporters you've amassed! I"
        chat2[part]="being one of them."
        chat3[part]=""
        part=22; speaker[part]="Winston"
        chat1[part]="So what, you want to help us!?"
        part=23; speaker[part]="Sanders"
        chat1[part]="Please do not interrupt."
        part=24; speaker[part]="Sanders"
        chat1[part]="I simply desire to further this \"ideal\" of yours."
        chat2[part]="A life without law sounds... like my life!"
        chat3[part]=""
        part=25; speaker[part]="Lucas"
        chat1[part]="Whatever, the more we have fighting the better."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=3; movenpcx[part]=3; movenpcy[part]=15
        part=26
        createnpc[part]=-3
        partdelay[part]=20
        part=27; speaker[part]="Sanders"
        chat1[part]="He-he! Such a bright dawn, don't you think,"
        chat2[part]="Winston? Let us weaken this nation!"
        chat3[part]=""
        part=28; speaker[part]="Winston"
        chat1[part]="...You won't deceive me!"
        movenpc[part]=2; movenpcx[part]=3; movenpcy[part]=15
        part=29
        createnpc[part]=-2
        partdelay[part]=60
        part=30; speaker[part]="Winston"
        chat1[part]="Seeing them together made it obvious..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=31; speaker[part]="Winston"
        chat1[part]="Sanders really does look like an older Lucas."
        part=32
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=14
        part=33
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
    if (level=="Friends"):
        dorandomizeItems=0
        selectx=5; camerax=selectx
        selecty=6; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=1; npc[npcc]=0; npcside[npcc]="Winston"; npcx[npcc]=4; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=0; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=5; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Floyd"; npcx[npcc]=4; npcy[npcc]=1; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Lenna"; npcx[npcc]=5; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=2; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=4; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1 #Create NPCs
        npcc=6; npc[npcc]=1; npcside[npcc]="Woman"; npcx[npcc]=7; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=7
        part=3; speaker[part]="Woman"
        chat1[part]="Lucas, Winston! We support you!"
        musicplay[part]="crowd"
        movenpc[part]=5; movenpcx[part]=4; movenpcy[part]=4
        part=4
        createnpc[part]=1
        partdelay[part]=10
        part=5
        movenpc[part]=1; movenpcx[part]=4; movenpcy[part]=8
        part=6; speaker[part]="Winston"
        chat1[part]="Who are these people?"
        part=7; speaker[part]="Man"
        chat1[part]="We're tired of oppressive Officers! Show em'"
        chat2[part]="who's boss! About a whole third of the hotel"
        chat3[part]="supports you guys!"
        part=8; speaker[part]="Lucas"
        chat1[part]="Like I thought, our actions haven't gone"
        chat2[part]="unnoticed."
        chat3[part]=""
        part=9; speaker[part]="Lucas"
        chat1[part]="People, we'd prefer if you'd stay out of our"
        chat2[part]="goals."
        chat3[part]=""
        part=10; speaker[part]="???"
        chat1[part]="Unfortunately, not everyone agrees with your"
        chat2[part]="decision, Winston."
        chat3[part]=""
        musicplay[part]="None"
        part=11
        movenpc[part]=4; movenpcx[part]=1; movenpcy[part]=2
        part=12
        createnpc[part]=-4
        partdelay[part]=10
        part=13
        movenpc[part]=5; movenpcx[part]=1; movenpcy[part]=5
        part=14
        createnpc[part]=-5
        partdelay[part]=10
        part=15
        movenpc[part]=6; movenpcx[part]=8; movenpcy[part]=3
        part=16
        createnpc[part]=-6
        partdelay[part]=10
        part=17; speaker[part]="Winston"
        chat1[part]="Lenna? Floyd?"
        part=18
        createnpc[part]=2
        partdelay[part]=1
        part=19
        movenpc[part]=2; movenpcx[part]=4; movenpcy[part]=4
        part=20
        createnpc[part]=3
        partdelay[part]=1
        part=21
        movenpc[part]=3; movenpcx[part]=5; movenpcy[part]=3
        part=22; speaker[part]="Floyd"
        chat1[part]="This stops here."
        musicplay[part]="ambient"
        part=23; speaker[part]="Lucas"
        chat1[part]="Old man! What do you know of anything?"
        part=24; speaker[part]="Floyd"
        chat1[part]="Rebellious youth! How many more innocents will"
        chat2[part]="you kill? How much longer will you resist"
        chat3[part]="your own morality, your conscience?"
        part=25; speaker[part]="Floyd"
        chat1[part]="And you, Winston! Don't you feel anything creating"
        chat2[part]="disorder?"
        chat3[part]=""
        part=26; speaker[part]="Lucas"
        chat1[part]="Everyone has his or her own idea of morality...there"
        chat2[part]="are no absolute truths."
        chat3[part]=""
        part=27; speaker[part]="Lucas"
        chat1[part]="While you sat around, doing nothing, Winston and me"
        chat2[part]="decided to take action!"
        chat3[part]=""
        part=28; speaker[part]="Lenna"
        chat1[part]="Winston..."
        part=29; speaker[part]="Winston"
        chat1[part]="Lenna? You shouldn't be here, this doesn't"
        chat2[part]="concern you!"
        chat3[part]=""
        part=30; speaker[part]="Lenna"
        chat1[part]="You left me to save yourself. There's no real right"
        chat2[part]="nor wrong to you, it's only right if it benefits"
        chat3[part]="you...What about your friends, Winston?"
        part=31; speaker[part]="Winston"
        chat1[part]="Lenna, I'm sorry!"
        part=32; speaker[part]="Winston"
        chat1[part]="You can escape with us! We'll all leave this place,"
        chat2[part]="together!"
        chat3[part]=""
        part=33; speaker[part]="Floyd"
        chat1[part]="What you do is by error. I'd rather be divided by"
        chat2[part]="truth than united by error."
        chat3[part]=""
        part=34; speaker[part]="Lucas"
        chat1[part]="It's too late to stop us. If you won't let us pass,"
        chat2[part]="we'll kill both of you!"
        chat3[part]=""
        part=35; speaker[part]="Lenna"
        chat1[part]="..."
        musicplay[part]="None"
        part=36; speaker[part]="Floyd"
        chat1[part]="Fight us when we're clearly outnumbered? Fight"
        chat2[part]="us two on two! At the very least, retain your"
        chat3[part]="honor!"
        choice1[part]="Fight Two on Two"; choice1go[part]=40 #Choices Given
        choice2[part]="Fight With Allies"; choice2go[part]=45
        part=40; speaker[part]="Floyd"
        chat1[part]="No longer hiding behind others, Winston? Know this,"
        chat2[part]="this fight is not personal...especially after"
        chat3[part]="our struggles together. But..."
        part=41
        gotopart[part]=49
        part=45; speaker[part]="Floyd"
        chat1[part]="Even at the end, you still can't save yourself,"
        chat2[part]="can you, Winston?"
        chat3[part]=""
        part=46
        gotopart[part]=49
        part=49; speaker[part]="Floyd"
        chat1[part]="We won't let you escape! Order depends on it!"
        musicplay[part]="action"
        part=50
        controlChar=part
        part=55
        partdelay[part]=60
        part=56; speaker[part]="Winston"
        chat1[part]="Farewell, Friends..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=57; speaker[part]="Lucas"
        chat1[part]="Weaklings! They don't understand our power!"
        chat2[part]="Don't you see, Winston? Our victory was"
        chat3[part]="inevitable, our ideals are strong!"
        musicplay[part]="guitar"
        part=58; speaker[part]="Winston"
        chat1[part]="But Lenna...! Floyd! Is it nothing to you!?"
        part=59; speaker[part]="Lucas"
        chat1[part]="It's too late for feelings. They tried to"
        chat2[part]="hamper our progress, and this is what they"
        chat3[part]="get."
        part=60; speaker[part]="Lucas"
        chat1[part]="What sort of belief is one of obedience?"
        chat2[part]="The two had no passion, Winston!"
        chat3[part]=""
        part=61; speaker[part]="Lucas"
        chat1[part]="But we...WE take risk, we live for ourselves!"
        chat2[part]="See the gate ahead?"
        chat3[part]=""
        part=62; speaker[part]="Lucas"
        chat1[part]="It's not just escape...we're here to show the"
        chat2[part]="Officers what happens when you're falsely"
        chat3[part]="accused - we remodel the law!"
        part=63; speaker[part]="Winston"
        chat1[part]="I and...Lenna and Floyd...we were"
        chat2[part]="all accused of the murder...of that man..."
        chat3[part]=""
        part=64; speaker[part]="Winston"
        chat1[part]="The Officers told us it had to have been someone"
        chat2[part]="from our floor."
        chat3[part]=""
        part=65; speaker[part]="Lucas"
        chat1[part]="And who do you think the original killer was?"
        part=66; speaker[part]="Winston"
        chat1[part]="Floyd? Lenna?...It doesn't matter anymore."
        chat2[part]="Whoever did is dead, in more than one way."
        chat3[part]=""
        part=67; speaker[part]="Lucas"
        chat1[part]="The past is gone. Our future awaits ahead."
        chat2[part]=""
        chat3[part]=""
        part=68; speaker[part]="Winston"
        chat1[part]="This is the final battle, I'm ready to escape."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="None"
        part=69
        changelevelpart=part; changelevelto="LevelMenu"; day=32; chapter+=1
        part=100; speaker[part]="Lucas"
        chat1[part]="Weakling! I'll go on without you."
        chat2[part]=""
        chat3[part]=""
        part=101
        gotopart[part]=110
        part=105; speaker[part]="Winston"
        chat1[part]="...And at your hands? Friends, right?"
        part=106
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Escape"): #Escape
        dorandomizeItems=0
        selectx=10; camerax=selectx
        selecty=15; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=7; npcy[npcc]=22; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=12; npcy[npcc]=22; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0 #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Enforcer"; npcx[npcc]=9; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Enforcer"; npcx[npcc]=10; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Cutthroat"; npcx[npcc]=7; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=13; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Hammer" #Create NPCs
        #npcc=6; npc[npcc]=1; npcside[npcc]="Enforcer"; npcx[npcc]=6; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=6; npc[npcc]=1; npcside[npcc]="Commander"; npcx[npcc]=10; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        part=1
        partdelay[part]=10
        part=2; speaker[part]="Officer"
        chat1[part]="Commander, they're here!"
        musicplay[part]="ambient"
        part=3; speaker[part]="Lucas"
        chat1[part]="The Commander?"
        part=4; speaker[part]="Commander"
        chat1[part]="Lucas, My boy! Is there no way to persuade"
        chat2[part]="you to change your mind? Turn back, you'll"
        chat3[part]="be forgiven!"
        part=5; speaker[part]="Lucas"
        chat1[part]="No! We're sick of you, the Officers, and your"
        chat2[part]="corrupted law! This is where it ends. We're"
        chat3[part]="escaping and there's no stopping us!"
        part=6; speaker[part]="Commander"
        chat1[part]="Know that this pains me, Lucas. You were the"
        chat2[part]="greatest Officer I had, but if you won't back"
        chat3[part]="down, feel my judgment!"
        musicplay[part]="None"
        part=7
        musicplay[part]="action"
        controlChar=part
        part=10
        partdelay[part]=60
        part=11; speaker[part]="Winston"
        chat1[part]="They're dead, every one of them."
        musicplay[part]="None"
        part=12; speaker[part]="Lucas"
        chat1[part]="Finally. Now quickly, to the gate!"
        part=13; speaker[part]="Lucas"
        chat1[part]="We've broken the shackles of law, Winston!"
        chat2[part]="Freedom awaits us!"
        chat3[part]=""
        part=14; speaker[part]="Winston"
        chat1[part]="Wait, does the ground feel...odd to you?"
        part=15
        partdelay[part]=300
        musicplay[part]="scary"
        part=16; speaker[part]="Winston"
        chat1[part]="W-what...? What is this!?"
        part=17; speaker[part]="Voice"
        chat1[part]="My creations!"
        part=18; speaker[part]="Winston"
        chat1[part]="Hello? Who is this!?"
        part=19; speaker[part]="Voice"
        chat1[part]="For thou has said in thine heart, I will ascend"
        chat2[part]="into heaven, I will exalt my throne above the"
        chat3[part]="stars..."
        part=20; speaker[part]="Voice"
        chat1[part]="You were the brightest of them all, and thou"
        chat2[part]="hast forsaken thyself! Thy pride is your"
        chat3[part]="undoing! How art thou fallen!"
        part=21; speaker[part]="Lucas"
        chat1[part]="But I defeated you! I'm supposed to be the"
        chat2[part]="greatest now!"
        chat3[part]=""
        part=22; speaker[part]="Winston"
        chat1[part]="Lucas? Greatest? I want answers!"
        part=23; speaker[part]="Lucas"
        chat1[part]="And what of this world? What have you done to it?"
        part=24; speaker[part]="Lucas"
        chat1[part]="The water is unending. Has the whole world become"
        chat2[part]="without form and void?"
        chat3[part]=""
        part=25; speaker[part]="Voice"
        chat1[part]="Behold, the cities are broken down by My presence,"
        chat2[part]="and my fierce anger."
        chat3[part]=""
        part=26; speaker[part]="Voice"
        chat1[part]="For this shall the earth mourn, and the heavens"
        chat2[part]="above be black;"
        chat3[part]=""
        part=27; speaker[part]="Voice"
        chat1[part]="...because I have spoken it, I have purposed it,"
        chat2[part]="and will not repent, neither will I turn back from"
        chat3[part]="it."
        part=28; speaker[part]="Lucas"
        chat1[part]="Was our stance truly wicked? Creating a world where"
        chat2[part]="law does not exist, and every one may live his"
        chat3[part]="life however he desires?"
        part=29; speaker[part]="Voice"
        chat1[part]="For ye are foolish, and know me not! Ye are wise"
        chat2[part]="to do evil, but to do good ye have no knowledge."
        chat3[part]=""
        part=30; speaker[part]="Winston"
        chat1[part]="It would have been a world of disorder and"
        chat2[part]="sorrow...Lenna and Floyd are dead because"
        chat3[part]="of it!"
        part=31; speaker[part]="Lucas"
        chat1[part]="So quick to turn on me, Winston? Always a"
        chat2[part]="coward!"
        chat3[part]=""
        part=32; speaker[part]="Voice"
        chat1[part]="The whold land is desolate; yet I will not"
        chat2[part]="make a full end."
        chat3[part]=""
        part=33; speaker[part]="Lucas"
        chat1[part]="What will happen now?"
        part=34; speaker[part]="Voice"
        chat1[part]="Genesis will begin."
        part=35; speaker[part]="Voice"
        chat1[part]="Woe to the inhabitants of the earth and the"
        chat2[part]="earth and the sea!"
        chat3[part]=""
        part=36; speaker[part]="Voice"
        chat1[part]="For the devil has come down to you, having"
        chat2[part]="great wrath, becuase he knows that he has a"
        chat3[part]="short time."
        part=37; speaker[part]="Lucas"
        chat1[part]="One day, I'll fight again! I shall become"
        chat2[part]="the god of this new world! I will finally"
        chat3[part]="rule...!"
        part=38
        partdelay[part]=120
        createnpc[part]=-1
        part=39; speaker[part]="Voice"
        chat1[part]="And you, Holy one!"
        part=40; speaker[part]="Winston"
        chat1[part]="H-Holy...? Me!?"
        part=41; speaker[part]="Voice"
        chat1[part]="I will spare not those who have sinned, but cast"
        chat2[part]="them down to hell, and deliver them into chains of"
        chat3[part]="darkness, to be reserved unto judgment."
        part=42; speaker[part]="Voice"
        chat1[part]="Thy part will be in the lake that burns"
        chat2[part]="with fire and brimstone!"
        chat3[part]=""
        part=43; speaker[part]="Winston"
        chat1[part]="Hell!? No, please!"
        part=44; speaker[part]="Voice"
        chat1[part]="I never knew you: depart from me, ye"
        chat2[part]="that practice iniquity!"
        chat3[part]=""
        part=45
        partdelay[part]=100
        part=46
        partdelay[part]=70
        part=47; speaker[part]="Winston"
        chat1[part]="Agahhh!"
        part=48
        partdelay[part]=100
        part=49
        partdelay[part]=500
        part=50; speaker[part]=" "
        chat1[part]="The End."
        chat2[part]=""
        chat3[part]=""
        part=51 #Escape
        musicplay[part]="None"
        changelevelpart=part; changelevelto="LevelMenu"; day=33; chapter+=1
        part=100; speaker[part]="Commander"
        chat1[part]="I'll cut you to the ground!"
        part=101
        gotopart[part]=110
        part=105; speaker[part]="Commander"
        chat1[part]="How art thou fallen!"
        part=106
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="FloydChoice"):
        dorandomizeItems=0
        selectx=9; camerax=selectx
        selecty=12; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha()
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=12; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=0; npcside[npcc]="Floyd"; npcx[npcc]=10; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        part=1
        partdelay[part]=5
        part=2
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=16
        part=3; speaker[part]="Winston"
        chat1[part]="Floyd! Floyd?"
        part=4
        movenpc[part]=0; movenpcx[part]=4; movenpcy[part]=16
        part=5
        movenpc[part]=0; movenpcx[part]=4; movenpcy[part]=13
        part=6; speaker[part]="Winston"
        chat1[part]="Are you here?"
        part=7
        movenpc[part]=0; movenpcx[part]=5; movenpcy[part]=13
        part=8
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=8
        part=9
        createnpc[part]=1
        partdelay[part]=50
        part=10; speaker[part]="Winston"
        chat1[part]="Floyd!"
        musicplay[part]="ominous"
        part=11; speaker[part]="Floyd"
        chat1[part]="Hrm? Winston? What are you doing here?"
        part=12; speaker[part]="Winston"
        chat1[part]="I thought you'd be here, so I came..."
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=7
        part=13; speaker[part]="Winston"
        chat1[part]="I've decided to help you. You said you wanted"
        chat2[part]="to destroy the hotel, right? At this point,"
        chat3[part]="that looks like our best option."
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=6
        part=14; speaker[part]="Floyd"
        chat1[part]="And what of Lenna? Is she with you?"
        part=15; speaker[part]="Winston"
        chat1[part]="N-no...I left her, she had other plans..."
        part=16; speaker[part]="Floyd"
        chat1[part]="Hopefully she can forgive you after all is"
        chat2[part]="done."
        chat3[part]=""
        part=17; speaker[part]="Winston"
        chat1[part]="Yeah..."
        part=18; speaker[part]="Winston"
        chat1[part]="So, uh, what's the plan?"
        part=19; speaker[part]="Floyd"
        chat1[part]="Yes, time is short..."
        movenpc[part]=1; movenpcx[part]=12; movenpcy[part]=3
        part=20; speaker[part]="Floyd"
        chat1[part]="Do you remember this room, Winston? This"
        chat2[part]="is where the news was being broadcast. Because"
        chat3[part]="of liars is why we're in this situation!"
        part=21; speaker[part]="Floyd"
        chat1[part]="See what happens when men are bound together?"
        part=22; speaker[part]="Floyd"
        chat1[part]="This hotel is the result of man's unified"
        chat2[part]="efforts...it's a symbol of unity!"
        chat3[part]=""
        part=23; speaker[part]="Floyd"
        chat1[part]="False unity, Winston! Everyone is connected!"
        chat2[part]="With the media, especially, lies are spread!"
        chat3[part]=""
        part=24; speaker[part]="Floyd"
        chat1[part]="As I've said before, I'd rather be divided"
        chat2[part]="by truth than united by error!"
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=3
        part=25; speaker[part]="Floyd"
        chat1[part]="No one dares disagree with one another..."
        chat2[part]="it's all about preserving the peace, the love,"
        chat3[part]="the unity!"
        part=26; speaker[part]="Floyd"
        chat1[part]="Yet in your time at this hotel, have you met a"
        chat2[part]="single soul not saturated in sin? The gangs,"
        chat3[part]="gamblers, drunkards, liars..."
        part=27; speaker[part]="Floyd"
        chat1[part]="There is none righteous, no, not one..."
        part=28; speaker[part]="Floyd"
        chat1[part]="They've forgotten God, Winston! They don't fear"
        chat2[part]="Him! They don't even believe in Him!"
        chat3[part]=""
        part=29; speaker[part]="Winston"
        chat1[part]="But how'll we destroy the hotel? Not to"
        chat2[part]="mention it's the tallest building in the"
        chat3[part]="world!"
        part=30; speaker[part]="Floyd"
        chat1[part]="I have been here since I left you last night."
        chat2[part]="I've found that the power supply to all"
        chat3[part]="communications is on the roof of this hotel."
        part=31; speaker[part]="Floyd"
        chat1[part]="Television, phones...internet, even. A start"
        chat2[part]="would be finding a way to disable it."
        chat3[part]=""
        part=32; speaker[part]="Winston"
        chat1[part]="...That's the plan? How will that accomplish"
        chat2[part]="anything?"
        chat3[part]=""
        part=33; speaker[part]="Floyd"
        chat1[part]="That isn't all. WE won't have to do much else"
        chat2[part]="though, don't worry."
        chat3[part]=""
        part=34; speaker[part]="Winston"
        chat1[part]="T-then, how...?"
        part=35; speaker[part]="Floyd"
        chat1[part]="Trust me, Winston."
        part=36; speaker[part]="Floyd"
        chat1[part]="Now, let's head off. We're going to need to"
        chat2[part]="pass a few floors on the way to the roof,"
        chat3[part]="so don't let your guard down."
        musicplay[part]="None"
        part=37
        changelevelpart=part; changelevelto="LevelMenu"; day=40; chapter+=1
    if (level=="Jerry2"):
        selectx=10; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=1; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=2; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Jerry"; npcx[npcc]=10; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Wrench" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=1; movenpcy[part]=8
        part=3; speaker[part]="Winston"
        chat1[part]="Why'd you stop? The elevator's up ahead."
        musicplay[part]="standby"
        part=4; speaker[part]="Floyd"
        chat1[part]="Don't you hear it? Footsteps. From the other"
        chat2[part]="side of these doors."
        chat3[part]=""
        part=5
        movenpc[part]=1; movenpcx[part]=2; movenpcy[part]=7
        part=6; speaker[part]="Floyd"
        chat1[part]="I'm opening the door."
        musicplay[part]="None"
        part=7
        movenpc[part]=1; movenpcx[part]=2; movenpcy[part]=8
        part=8
        partdelay[part]=30
        createnpc[part]=2
        part=9
        movenpc[part]=1; movenpcx[part]=4; movenpcy[part]=8
        part=10
        movenpc[part]=0; movenpcx[part]=3; movenpcy[part]=8
        part=11
        movenpc[part]=0; movenpcx[part]=4; movenpcy[part]=4
        part=12; speaker[part]="Jerry"
        chat1[part]="Gah! Don't scare me like that!"
        musicplay[part]="ominous"
        movenpc[part]=2; movenpcx[part]=10; movenpcy[part]=6
        part=13; speaker[part]="Winston"
        chat1[part]="Wha-Jerry!?"
        part=14; speaker[part]="Jerry"
        chat1[part]="Oh no, no, no! Not you again! G-get away!"
        chat2[part]="Get away from me!"
        chat3[part]=""
        part=15; speaker[part]="Winston"
        chat1[part]="Calm it. What are you doing here?"
        part=16; speaker[part]="Floyd"
        chat1[part]="You know this man, Winston?"
        part=17; speaker[part]="Winston"
        chat1[part]="He's the one who's idea it was to kidnap"
        chat2[part]="you after you split from us."
        chat3[part]=""
        part=18; speaker[part]="Jerry"
        chat1[part]="I-I've changed! I'm not some thug no more!"
        chat2[part]="See? I ain't even have gangsters protecting"
        chat3[part]="me. I quit! It's over!"
        part=19; speaker[part]="Winston"
        chat1[part]="Do you think he means it?"
        part=20; speaker[part]="Floyd"
        chat1[part]="He may be sincere, but that doesn't change"
        chat2[part]="what he did to us, especially me. His death"
        chat3[part]="may serve as an example to others..."
        part=21; speaker[part]="Jerry"
        chat1[part]="P-Please! I'm sorry! I get it, what I did"
        chat2[part]="was wrong! Just don't hurt me!"
        chat3[part]=""
        musicplay[part]="None"
        part=22; speaker[part]="Floyd"
        chat1[part]="It's your choice, Winston. Will you show your"
        chat2[part]="wrath or be his salvation?"
        chat3[part]=""
        choice1[part]="Judgment"; choice1go[part]=30 #Choices Given
        choice2[part]="Forgive"; choice2go[part]=35
        part=30; speaker[part]="Winston"
        chat1[part]="I will judge him. We can't grow soft now."
        part=31; speaker[part]="Jerry"
        chat1[part]="This is what I get for my actions? A deserving"
        chat2[part]="fate...? I'll fightcha till the end!"
        chat3[part]=""
        part=32
        musicplay[part]="action"
        controlChar=part
        part=35; speaker[part]="Winston"
        chat1[part]="I will forgive him."
        musicplay[part]="guitar"
        part=36; speaker[part]="Jerry"
        chat1[part]="Thank you, Winston. I promise, I'm with ya"
        chat2[part]="wherever you go!"
        chat3[part]=""
        part=37; speaker[part]="Jerry"
        chat1[part]="I ain't much help now that I don't have"
        chat2[part]="a gang backing me up, but I still want to"
        chat3[part]="join."
        part=38; speaker[part]="Winston"
        chat1[part]="The more help, the better. Glad to see you've"
        chat2[part]="turned a new leaf."
        chat3[part]=""
        part=39; speaker[part]="Jerry"
        chat1[part]="He..he! I'm glad you found me, and not some"
        chat2[part]="Officer."
        chat3[part]=""
        part=40; speaker[part]="Winston"
        chat1[part]="I'd rather no one perish, but everyone come to"
        chat2[part]="repentance."
        chat3[part]=""
        part=41; speaker[part]="Floyd"
        chat1[part]="But watch yourself, boy. I don't forgive"
        chat2[part]="so easily."
        chat3[part]=""
        musicplay[part]="None"
        part=42
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        part=100; speaker[part]="Jerry"
        chat1[part]="Better go find the old gang once I finish ya off,"
        chat2[part]="at least I was safe with em'!"
        part=101
        gotopart[part]=110
        part=105; speaker[part]="Jerry"
        chat1[part]="Better go find the old gang once I finish ya off,"
        chat2[part]="at least I was safe with em'!"
        part=106
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
        part=45
        partdelay[part]=40
        part=46; speaker[part]="Floyd"
        chat1[part]="Buncha hooligans, finally some consequence for"
        chat2[part]="their actions."
        chat3[part]=""
        musicplay[part]="None"
        part=47; speaker[part]="Winston"
        chat1[part]="We're still killers, but at least it's for"
        chat2[part]="justice now...right?"
        chat3[part]=""
        part=48; speaker[part]="Floyd"
        chat1[part]="Of course! Justice! Winston, my boy, after"
        chat2[part]="days of being threatened by those thugs,"
        chat3[part]="we're finally upholding the law!"
        part=49; speaker[part]="Winston"
        chat1[part]="Yeah, um, sure. And I'm not your boy."
        part=50
        gotopart[part]=42
    if (level=="Climb"):
        selectx=11; camerax=selectx #Camera Position
        selecty=13; cameray=selecty
        item[0]="Bottle"; itemx[0]=15; itemy[0]=8
        item[1]="Hammer"; itemx[1]=8; itemy[1]=9
        item[2]="Med Kit"; itemx[2]=15; itemy[2]=8
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=13; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=15; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=10; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Woman"; npcx[npcc]=13; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Wrench" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Strangler"; npcx[npcc]=7; npcy[npcc]=15; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Bottle" #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Resident"; npcx[npcc]=5; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Shiv" #Create NPCs
        npcc=6; npc[npcc]=1; npcside[npcc]="Cutthroat"; npcx[npcc]=4; npcy[npcc]=13; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Knife" #Create NPCs
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Winston"
        chat1[part]="Looks like you're right, this elevator doesn't go"
        chat2[part]="straight to the roof."
        chat3[part]=""
        musicplay[part]="standby"
        part=3; speaker[part]="Floyd"
        chat1[part]="There should be another on this floor. Once one of"
        chat2[part]="us finds it, we should be able to reach the roof."
        chat3[part]=""
        part=4
        movenpc[part]=0; movenpcx[part]=11; movenpcy[part]=16
        part=5; speaker[part]="Man"
        chat1[part]="Woah, hey, it's one of those killers from the news!"
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=10; movenpcy[part]=10
        part=6; speaker[part]="Winston"
        chat1[part]="Huh? Hey, quit shouting!"
        part=7; speaker[part]="Man"
        chat1[part]="Everyone, the killer's here! He's trying to kill"
        chat2[part]="me! Help, somebody, help!"
        chat3[part]=""
        musicplay[part]="None"
        part=8; speaker[part]="Winston"
        chat1[part]="Great."
        musicplay[part]="threefour"
        part=9
        controlChar=part
        part=15
        partdelay[part]=40
        part=16; speaker[part]="Floyd"
        chat1[part]="This is the correct elevator, I presume?"
        part=17; speaker[part]="Winston"
        chat1[part]="It's the only other one on this floor."
        chat2[part]="Stop what you're doing and get in, we're gonna"
        chat3[part]="get out of this all right!"
        musicplay[part]="None"
        part=18
        changelevelpart=part; changelevelto="LevelMenu"; day=41; chapter+=1
        part=100; speaker[part]="Floyd"
        chat1[part]="You fought valiantly for our cause, Winston."
        chat2[part]="God will remember this once I reach the rooftop."
        chat3[part]=""
        part=101; speaker[part]="Winston"
        chat1[part]="G-God? I...*cough*...I don't deserve salvation..."
        chat2[part]="after what I..."
        chat3[part]=""
        part=102; speaker[part]="Floyd"
        chat1[part]="It is unfortunate you were not able to experience"
        chat2[part]="a new world..."
        chat3[part]=""
        part=103
        gotopart[part]=110
        part=105; speaker[part]="Winston"
        chat1[part]="Floyd! You've gotta get up! I can't destroy"
        chat2[part]="a hotel by myself! What was your plan!?"
        part=106; speaker[part]="Resident"
        chat1[part]="Hurry, someone call an Officer! Tell them"
        chat2[part]="we took down one of the killers!"
        chat3[part]=""
        part=107
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Summit"):
        selectx=9; camerax=selectx #Camera Position
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=9; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=8; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=0; npcside[npcc]="Host"; npcx[npcc]=4; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Wrench" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=8
        part=3; speaker[part]="Winston"
        chat1[part]="So we're here, what now?"
        musicplay[part]="rain"
        part=4; speaker[part]="Floyd"
        chat1[part]="The moment is nigh, Winston."
        part=5; speaker[part]="Winston"
        chat1[part]="Where is the power supply? What about cutting off"
        chat2[part]="the hotel's communications?"
        chat3[part]=""
        part=6; speaker[part]="Floyd"
        chat1[part]="The hotel's...? Ah, forgive me for not being"
        chat2[part]="specific."
        chat3[part]=""
        part=7; speaker[part]="Floyd"
        chat1[part]="We are about to destroy all forms of communication"
        chat2[part]="on earth."
        chat3[part]=""
        part=8; speaker[part]="Winston"
        chat1[part]="W-What!? Are you insane!? You can't just...I mean,"
        chat2[part]="how would you even do that!?"
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=9
        part=9; speaker[part]="Floyd"
        chat1[part]="Why the many questions? You've seen the results of"
        chat2[part]="a world that is of one language, of one speech..."
        chat3[part]=""
        part=10; speaker[part]="Floyd"
        chat1[part]="Nothing is restraining these people. Everything"
        chat2[part]="they can imagine they can do. Look at this tower"
        chat3[part]="they have built."
        part=11; speaker[part]="Floyd"
        chat1[part]="This tower...that has reached the heavens!"
        part=12; speaker[part]="Floyd"
        chat1[part]="And now we will end all that!"
        part=13; speaker[part]="Winston"
        chat1[part]="B-But, I...Floyd!?"
        part=14; speaker[part]="Floyd"
        chat1[part]="God! These sinful people that have forgotten you..."
        chat2[part]="scatter them abroad from thence upon the face of"
        chat3[part]="all the earth!"
        part=15; speaker[part]="Floyd"
        chat1[part]="Confound their language, that they may not"
        chat2[part]="understand one another's speech!"
        chat3[part]=""
        part=16
        partdelay[part]=30
        part=17
        partdelay[part]=1
        createnpc[part]=2
        part=18
        movenpc[part]=2; movenpcx[part]=5; movenpcy[part]=3
        part=19
        movenpc[part]=2; movenpcx[part]=6; movenpcy[part]=3
        part=20
        movenpc[part]=2; movenpcx[part]=7; movenpcy[part]=3
        part=21
        partdelay[part]=5
        movenpc[part]=2; movenpcx[part]=7; movenpcy[part]=4
        part=22; speaker[part]="Host"
        chat1[part]="There you are!"
        part=23; speaker[part]="Floyd"
        chat1[part]="Winston, protect me!"
        part=24; speaker[part]="Host"
        chat1[part]="Winston, can't you see what you're doing?"
        chat2[part]="You're about to destroy everything! All that"
        chat3[part]="humanity has worked so hard to achieve!"
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=8
        part=25; speaker[part]="Host"
        chat1[part]="Without communication, what'll happen to the"
        chat2[part]="news, huh? What job'll I have?"
        chat3[part]=""
        part=26; speaker[part]="Floyd"
        chat1[part]="Even in the end, you still only think of"
        chat2[part]="your yourself. Your job, reputation, money..."
        chat3[part]=""
        part=27; speaker[part]="Floyd"
        chat1[part]="Mankind isn't getting better, it is getting"
        chat2[part]="morally and spiritually worse!"
        chat3[part]=""
        part=28
        controlChar=part
        part=39
        partdelay[part]=20
        part=40
        partdelay[part]=60
        part=41; speaker[part]="Floyd"
        chat1[part]="God has answered!"
        musicplay[part]="None"
        part=42
        partdelay[part]=100
        musicplay[part]="scary"
        part=43
        partdelay[part]=1
        part=44
        partdelay[part]=200
        part=45
        partdelay[part]=1
        part=46
        partdelay[part]=300
        musicplay[part]="None"
        part=47
        changelevelpart=part; changelevelto="LevelMenu"; day=42; chapter+=1
        part=100
        musicplay[part]="None"
        failurepart=part
    if (level=="Wake"):
        selectx=8; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=1; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=11; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; npcfainted[npcc]=5; npcaniframe[npcc]=3 #Create NPCs
        part=1
        partdelay[part]=300
        musicplay[part]="ominous"
        part=2
        controlChar=part
        part=3
        partdelay[part]=1
        part=4
        partdelay[part]=60
        part=5; speaker[part]="Winston"
        chat1[part]="...Uhhh, my head hurts..."
        part=6
        partdelay[part]=100
        part=7; speaker[part]="Winston"
        chat1[part]="...Where am I?"
        movenpc[part]=1; movenpcx[part]=11; movenpcy[part]=9
        part=8; speaker[part]="Winston"
        chat1[part]="It's a vast emptiness. Almost like a desert."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=9
        part=9; speaker[part]="Winston"
        chat1[part]="Floyd!"
        part=10; speaker[part]="Winston"
        chat1[part]="..."
        part=11; speaker[part]="Winston"
        chat1[part]="No reply."
        part=12; speaker[part]="Winston"
        chat1[part]="We were at the top of the hotel and-..."
        chat2[part]="Wait, where's the hotel? I can't see it"
        chat3[part]="anywhere."
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=9
        part=13; speaker[part]="Winston"
        chat1[part]="I'll be wandering forever...But, eventually"
        chat2[part]="I'll find someone. Eventually."
        chat3[part]=""
        part=14
        movenpc[part]=1; movenpcx[part]=14; movenpcy[part]=9
        part=15
        createnpc[part]=-1
        partdelay[part]=120
        musicplay[part]="None"
        part=16
        changelevelpart=part; changelevelto="LevelMenu"; day=43; chapter+=1
    if (level=="Speechless"):
        selectx=8; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=6; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0 #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=6; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcfainted[npcc]=1; npcaniframe[npcc]=3; npcheld[npcc]="Hammer" #Create NPCs
        if (floyd2==1):
            npcc=2; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=10; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        part=1
        movenpc[part]=0; movenpcx[part]=6; movenpcy[part]=9
        part=2; speaker[part]="Winston"
        chat1[part]="Is that who I think it is?"
        musicplay[part]="ominous"
        part=3; speaker[part]="Winston"
        chat1[part]="Lenna! Don't worry, I'm coming!"
        part=4
        controlChar=part
        part=6; speaker[part]="Lenna"
        chat1[part]="..."
        part=7; speaker[part]="Winston"
        chat1[part]="Oh, Lenna! Thank goodness! I'm sorry I left you,"
        chat2[part]="and that the world is in this mess...Come on, we'll"
        chat3[part]="go and find others, together!"
        part=8; speaker[part]="Lenna"
        chat1[part]="Tag yise sanor otiter noruk pibet ce, la"
        chat2[part]="saloniw cesatal pir cosehon heyefa? Cenomu "
        chat3[part]="ireha hiepe birogoh leninu."
        part=9; speaker[part]="Winston"
        chat1[part]="Yeah, and..! W-Wait, what?"
        part=10; speaker[part]="Lenna"
        chat1[part]="Ze dar genarar mu rero orucihi leyi!"
        if (floyd2==0):
            part=11; speaker[part]="Winston"
            chat1[part]="I can't understand anything you're saying...!?"
            chat2[part]="Is this part of what Floyd did on the hotel"
            chat3[part]="rooftop?"
        if (floyd2==1):
            part=11; speaker[part]="Floyd"
            chat1[part]="Don't waste your breath, Winston. She cannot"
            chat2[part]="understand our language, and we cannot understand"
            chat3[part]="her speech."
        part=12; speaker[part]=" "
        chat1[part]="Lenna looks as though she wants to attack!"
        musicplay[part]="None"
        part=13
        musicplay[part]="threefour"
        part=15
        partdelay[part]=1
        part=16
        partdelay[part]=60
        part=17; speaker[part]="Winston"
        chat1[part]="Goodbye, Lenna..."
        musicplay[part]="None"
        part=18
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        if (floyd2==1 and lucas2==1 and lenna2==1): day=44
        part=100
        partdelay[part]=30
        part=101; speaker[part]="Lenna"
        chat1[part]="Huc ner na atiti edata ece donu necido...!"
        part=102
        musicplay[part]="None"
        failurepart=part
    if (level=="World"):
        selectx=8; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=1; npc[npcc]=0; npcside[npcc]="Winston"; npcx[npcc]=2; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0 #Create NPCs
        npcc=0; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=9; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0
        part=1
        partdelay[part]=50
        part=2; speaker[part]="Floyd"
        chat1[part]="Hehe, the middle of nowhere? I was expecting"
        chat2[part]="worse, to be honest."
        chat3[part]=""
        musicplay[part]="ominous"
        part=3; speaker[part]="???"
        chat1[part]="Floyd!"
        part=4; speaker[part]="Floyd"
        chat1[part]="Strange. And here I was thinking humanity's"
        chat2[part]="speech had become babeled."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=7
        part=5; speaker[part]="Floyd"
        chat1[part]="Unless, that's no man at all."
        part=6
        createnpc[part]=1
        partdelay[part]=30
        part=7; speaker[part]="Winston"
        chat1[part]="Floyd! There you are!"
        part=8; speaker[part]="Floyd"
        chat1[part]="Reunited once more, are we?"
        movenpc[part]=0; movenpcx[part]=8; movenpcy[part]=7
        part=9; speaker[part]="Winston"
        chat1[part]="I've been wandering in this wasteland for"
        chat2[part]="what feels like hours. What happened up"
        chat3[part]="there, on the-...what used to be the rooftop?"
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=6
        part=10; speaker[part]="Floyd"
        chat1[part]="I asked God of what He felt would provide a"
        chat2[part]="sufficient solution to the hotel's \"sin\""
        chat3[part]="problem."
        part=11; speaker[part]="Floyd"
        chat1[part]="You were there, were you not? Speech"
        chat2[part]="has been garbled and humanity has been"
        chat3[part]="scattered abroad the planet."
        part=12; speaker[part]="Winston"
        chat1[part]="...But what about-"
        part=13; speaker[part]="Floyd"
        chat1[part]="Save your questions, Winston. Danger lurks."
        chat2[part]="Sin has not been completely eradicated...Let us"
        chat3[part]="travel onward, as entities of judgment."
        musicplay[part]="None"
        part=14
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        if (floyd2==1 and lucas2==1 and lenna2==1): day=44
    if (level=="Confusion"):
        dorandomizeItems=1
        selectx=8; camerax=selectx #Camera Position
        selecty=10; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=12; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0 #Create NPCs
        npcc=6; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=5; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Bottle"
        npcc=2; npc[npcc]=1; npcside[npcc]="Woman"; npcx[npcc]=0; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Hammer"
        npcc=3; npc[npcc]=1; npcside[npcc]="Resident"; npcx[npcc]=11; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Shiv"
        npcc=5; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=2; npcy[npcc]=15; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Bottle"
        npcc=4; npc[npcc]=1; npcside[npcc]="Cutthroat"; npcx[npcc]=4; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Knife"
        npcc=1; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=10; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton"
        if (floyd2==1):
            npcc=7; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=16; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        part=1
        partdelay[part]=50
        musicplay[part]="ominous"
        if (floyd2==0):
            part=2; speaker[part]="Winston"
            chat1[part]="People. They don't look too happy, either."
        if (floyd2==1):
            part=2; speaker[part]="Floyd"
            chat1[part]="A conflict's stirring."
        part=3; speaker[part]="Resident"
        chat1[part]="Solefi bila ti rego tieyidam tabiyab liludic le"
        chat2[part]="orate cumet dolit aciemac..."
        chat3[part]=""        
        part=4; speaker[part]="Woman"
        chat1[part]="!@^!&8139!284639087*8130813"
        chat2[part]="(&^*)#*^-236!#8758907!6324&"
        chat3[part]="!(!93146^@*1231#(&!)(_!+!8?"
        part=5; speaker[part]="Officer"
        chat1[part]="Tired tedobor ceg pemaber tir nemeha hifi nat"
        chat2[part]="tacan!? Tote ele net!"
        chat3[part]=""
        if (floyd2==0):
            part=6; speaker[part]="Winston"
            chat1[part]="It doesn't look like they can understand each"
            chat2[part]="other. Sounds like a bunch of gibberish."
            chat3[part]=""
        if (floyd2==1):
            part=6; speaker[part]="Floyd"
            chat1[part]="Despite their efforts, they cannot understand"
            chat2[part]="one another."
            chat3[part]=""
        part=7; speaker[part]="Winston"
        chat1[part]="And...is that Lucas!? Right in the center!"
        part=8; speaker[part]=" "
        chat1[part]="The people look as though they are prepared to"
        chat2[part]="fight."
        chat3[part]=""
        musicplay[part]="None"
        part=9; speaker[part]="Cutthroat"
        chat1[part]="!6898@#^:@&>4278*@2{}27:82...!"
        part=10
        musicplay[part]="threefour"
        controlChar=part
        part=20
        partdelay[part]=60
        part=21; speaker[part]="Winston"
        chat1[part]="Lucas...why? What were those last words you"
        chat2[part]="uttered...?"
        chat3[part]=""
        musicplay[part]="None"
        part=22
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        if (floyd2==1 and lucas2==1 and lenna2==1): day=44
        part=100
        partdelay[part]=30
        part=101; speaker[part]="Lucas"
        chat1[part]="*Cough*..."
        part=102
        musicplay[part]="None"
        failurepart=part
    if (level=="Unity"):
        dorandomizeItems=1
        selectx=10; camerax=selectx #Camera Position
        selecty=10; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=8; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0 #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=12; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0
        npcc=2; npc[npcc]=1; npcside[npcc]="Sanders"; npcx[npcc]=10; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer"
        npcc=3; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=14; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton"
        npcc=4; npc[npcc]=1; npcside[npcc]="Host"; npcx[npcc]=6; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer"
        npcc=5; npc[npcc]=1; npcside[npcc]="Drunkard"; npcx[npcc]=16; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Bottle"
        npcc=6; npc[npcc]=1; npcside[npcc]="Thug"; npcx[npcc]=4; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife"
        part=1
        partdelay[part]=60
        part=2; speaker[part]="Winston"
        chat1[part]="What the...What is this?"
        musicplay[part]="ambient"
        part=3; speaker[part]="Sanders"
        chat1[part]="This is the center of where the hotel"
        chat2[part]="once stood. The hotel you destroyed, he-he!"
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=10; movenpcy[part]=3
        part=4; speaker[part]="Floyd"
        chat1[part]="Sanders, what in the devil do you think you're"
        chat2[part]="doing!?"
        chat3[part]=""
        part=5; speaker[part]="Winston"
        chat1[part]="You know this guy, Floyd?"
        part=6; speaker[part]="Floyd"
        chat1[part]="He's a double-crossing snake, he is! Hear"
        chat2[part]="that, Sanders?"
        chat3[part]=""
        part=7; speaker[part]="Sanders"
        chat1[part]="Oh my! He-he! What was that? I can't hear"
        chat2[part]="you over the sandstorm you summoned!"
        chat3[part]=""
        part=8; speaker[part]="Floyd"
        chat1[part]="We summoned nothing! The greed, fornification,"
        chat2[part]="and lies you all once lived in have been"
        chat3[part]="purified by God!"
        part=9; speaker[part]="Sanders"
        chat1[part]="Tsk-tsk-tsk...It's but a small dent in my own"
        chat2[part]="plan for humanity, Floyd."
        chat3[part]=""
        part=10; speaker[part]="Floyd"
        chat1[part]="You furnish them to their heart's content but"
        chat2[part]="deny them ultimate salvation! Why do you all"
        chat3[part]="collectively reject God...?"
        part=11; speaker[part]="Thug"
        chat1[part]="Nepon egenason yebovix bar alateted sevaz!"
        part=12; speaker[part]=" "
        chat1[part]="The people appear angry."
        part=13; speaker[part]="Winston"
        chat1[part]="Wait, Floyd - Why can we understand Sanders"
        chat2[part]="but not the others?"
        chat3[part]=""
        musicplay[part]="None"
        part=14
        musicplay[part]="action"
        controlChar=part
        part=20
        partdelay[part]=1
        part=21
        partdelay[part]=100
        part=22; speaker[part]="Floyd"
        chat1[part]="And finally, humanity can begin anew."
        musicplay[part]="None"
        part=23
        changelevelpart=part; changelevelto="LevelMenu"; day=45; chapter+=1
        part=100
        partdelay[part]=60
        part=101; speaker[part]="Sanders"
        chat1[part]="The foolish child falls first. What a poor"
        chat2[part]="guardian angel you are, Floyd!"
        chat3[part]=""
        part=102
        gotopart[part]=110
        part=105
        partdelay[part]=60
        part=106; speaker[part]="Sanders"
        chat1[part]="Ouch, what a hit you took!"
        chat2[part]=""
        chat3[part]=""
        part=107
        gotopart[part]=110
        part=110
        musicplay[part]="None"
        failurepart=part
    if (level=="Watchers"):
        selectx=8; camerax=selectx #Camera Position
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=2; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=13; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=6; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        part=1
        partdelay[part]=5
        part=2
        movenpc[part]=2; movenpcx[part]=9; movenpcy[part]=10
        part=3; speaker[part]=" "
        chat1[part]="Winston stands limp. The scorching heat has"
        chat2[part]="turned lukewarm."
        musicplay[part]="guitar"
        part=4; speaker[part]="Winston"
        chat1[part]="*Sigh* *Pant* Huh... *Cough*"
        part=5; speaker[part]="Floyd"
        chat1[part]="Stand up straight, boy. Now is not the time"
        chat2[part]="to dilly-dally."
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=9
        part=6; speaker[part]="Winston"
        chat1[part]="How can you...huh...run...*Pant*...for so"
        chat2[part]="...long...?"
        chat3[part]=""
        part=7; speaker[part]="Floyd"
        chat1[part]="The sandstorm is subsiding. You see?"
        part=8; speaker[part]="Winston"
        chat1[part]="Haha...yeah. Better than that, all the danger has"
        chat2[part]="subsided."
        chat3[part]=""
        part=9; speaker[part]="Winston"
        chat1[part]="Hey, listen...I've been wondering..."
        part=10; speaker[part]="Floyd"
        chat1[part]="...How we are able to understand one another?"
        chat2[part]="How we were able to understand Sanders?"
        chat3[part]=""
        part=11; speaker[part]="Winston"
        chat1[part]="Well...is there a reason?"
        part=12; speaker[part]="Floyd"
        chat1[part]="I told you before, humanity's speech has been"
        chat2[part]="garbled. The only sound you can hear from them"
        chat3[part]="is simple babeling."
        musicplay[part]="None"
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=9
        part=13; speaker[part]="Floyd"
        chat1[part]="Make no mistake, Winston, we are not a part of"
        chat2[part]="humanity."
        chat3[part]=""
        musicplay[part]="mystery"
        movenpc[part]=1; movenpcx[part]=7; movenpcy[part]=9
        part=14; speaker[part]="Winston"
        chat1[part]="Huh!?"
        part=15; speaker[part]="Floyd"
        chat1[part]="Have you truly forgotten our purpose? As Watchers,"
        chat2[part]="we make known to the living of the Most High. That"
        chat3[part]="is, God."
        part=16; speaker[part]="Winston"
        chat1[part]="Watcher? I'm an angel...?"
        part=17; speaker[part]="Floyd"
        chat1[part]="Of course. But not all of us are Holy. Sanders"
        chat2[part]="believed in God, and lo, did he tremble."
        chat3[part]=""
        part=18; speaker[part]="Floyd"
        chat1[part]="Humanity will one day regather, albeit in a"
        chat2[part]="different sort of way. When that time of unity comes,"
        chat3[part]="Satan will again return to tempt the sons of man."
        part=19; speaker[part]="Winston"
        chat1[part]="Hmmm. Floyd, I'm just curious, but, uh- Do you know"
        chat2[part]="who killed that man...? You know, before this all"
        chat3[part]="started?"
        part=20; speaker[part]="Floyd"
        chat1[part]="The first blood? Rest assured, it was not me. Lenna,"
        chat2[part]="perhaps? Maybe another resident. Either way, they"
        chat3[part]="are dead now."
        part=21; speaker[part]="Winston"
        chat1[part]="Heh...yeah, they're dead all right. So, what"
        chat2[part]="do we do now?"
        chat3[part]=""
        part=22; speaker[part]="Floyd"
        chat1[part]="Now, let us be off, ascension to Heaven awaits."
        movenpc[part]=1; movenpcx[part]=6; movenpcy[part]=9
        part=23
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=9
        part=24
        partdelay[part]=60
        createnpc[part]=-1
        part=25; speaker[part]="Winston"
        chat1[part]="A Watcher..."
        part=26
        movenpc[part]=2; movenpcx[part]=3; movenpcy[part]=10
        part=27
        partdelay[part]=60
        createnpc[part]=-2
        part=28
        partdelay[part]=400
        part=29; speaker[part]=" "
        chat1[part]="The End."
        musicplay[part]="None"
        part=30
        changelevelpart=part; changelevelto="LevelMenu"; day=46; chapter+=1
    if (level=="LennaChoice"):
        selectx=8; camerax=selectx #Camera Position
        selecty=9; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=3; npcy[npcc]=11; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0 #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=3; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        part=1
        partdelay[part]=5
        part=2
        movenpc[part]=1; movenpcx[part]=3; movenpcy[part]=8
        part=3; speaker[part]="Winston"
        chat1[part]="Up already?"
        musicplay[part]="calm"
        part=4; speaker[part]="Lenna"
        chat1[part]="Yes, yes I am."
        part=5; speaker[part]="Winston"
        chat1[part]="So, what now?"
        part=6; speaker[part]="Lenna"
        chat1[part]="We're going to go back to the lab, past the"
        chat2[part]="fake wall. Then we find whatever device"
        chat3[part]="was used to erase my memories."
        part=7; speaker[part]="Lenna"
        chat1[part]="Then we use it...a-and then..."
        part=8; speaker[part]="Winston"
        chat1[part]="We forget."
        part=9; speaker[part]="Lenna"
        chat1[part]="Do you think there will be...fighting?"
        part=10; speaker[part]="Winston"
        chat1[part]="Still can't stand violence, huh? That's"
        chat2[part]="a good thing, you know. I'm already"
        chat3[part]="desensitized to it."
        part=11; speaker[part]="Winston"
        chat1[part]="So don't worry yourself. I'll protect you!"
        chat2[part]=""
        chat3[part]=""
        part=12; speaker[part]="Lenna"
        chat1[part]="Haha, I'm glad you're here, Winston."
        part=13; speaker[part]="Lenna"
        chat1[part]="Come on, let's get going."
        part=14
        musicplay[part]="None"
        changelevelpart=part; changelevelto="LevelMenu"; day=50; chapter+=1
    if (level=="Robot"):
        dorandomizeItems=0
        selectx=7; camerax=selectx
        selecty=7; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=9; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=8; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Gambler"; npcx[npcc]=7; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Bottle" #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Madison"; npcx[npcc]=13; npcy[npcc]=5; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; npcheld[npcc]="Wrench" #Create NPCs
        npcc=4; npc[npcc]=0; npcside[npcc]="Robot"; npcx[npcc]=13; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; npcheld[npcc]="" #Create NPCs
        part=1
        partdelay[part]=20
        part=2; speaker[part]="Lenna"
        chat1[part]="The secret door's somewhere here."
        musicplay[part]="ambient"
        part=3
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=7
        part=4; speaker[part]="Lenna"
        chat1[part]="There it is!"
        part=5
        movenpc[part]=0; movenpcx[part]=9; movenpcy[part]=5
        part=6
        movenpc[part]=0; movenpcx[part]=2; movenpcy[part]=5
        part=7; speaker[part]="Winston"
        chat1[part]="I'll go on ahead, to see if it's safe."
        chat2[part]="Stay here until I come back, all right?"
        chat3[part]=""
        movenpc[part]=1; movenpcx[part]=1; movenpcy[part]=6
        part=8
        movenpc[part]=1; movenpcx[part]=1; movenpcy[part]=1
        part=9
        createnpc[part]=-1
        partdelay[part]=10
        movenpc[part]=2; movenpcx[part]=9; movenpcy[part]=6
        part=10; speaker[part]="Gambler"
        chat1[part]="Woah, hold up there!"
        musicplay[part]="None"
        part=11
        movenpc[part]=0; movenpcx[part]=3; movenpcy[part]=5
        part=12; speaker[part]="Lenna"
        chat1[part]="Excuse me?"
        part=13; speaker[part]="Gambler"
        chat1[part]="I came along to get some of that money you"
        chat2[part]="stashed away. And this doesn't look like any"
        chat3[part]="sort of place you'd hide a fortune."
        musicplay[part]="scary"
        movenpc[part]=2; movenpcx[part]=8; movenpcy[part]=5
        part=14; speaker[part]="Lenna"
        chat1[part]="I'm not making any promises. Honestly, I don't"
        chat2[part]="even remember stealing anything. If we end up"
        chat3[part]="finding it, you can just take it all."
        part=15; speaker[part]="Gambler"
        chat1[part]="And how do I know you won't just ditch me, huh?"
        chat2[part]="Quit pretending, all right? You know where the"
        chat3[part]="money is, quit faking it!"
        part=16; speaker[part]="Gambler"
        chat1[part]="And you'd better tell me where it is!"
        part=17; speaker[part]=" "
        chat1[part]="The Gambler takes out his weapon."
        musicplay[part]="None"
        part=18; speaker[part]="Lenna"
        chat1[part]="Aah! Winston, help!"
        part=19
        createnpc[part]=3
        partdelay[part]=30
        part=20
        createnpc[part]=4
        partdelay[part]=30
        part=21; speaker[part]="Madison"
        chat1[part]="Robot, I command you to save her!"
        musicplay[part]="action"
        part=22
        movenpc[part]=4; movenpcx[part]=12; movenpcy[part]=6
        part=23; speaker[part]="Robot"
        chat1[part]="..."
        part=24
        controlChar=part
        part=30
        partdelay[part]=30
        part=31; speaker[part]="Lenna"
        chat1[part]="*Sigh* Thanks."
        musicplay[part]="None"
        part=32; speaker[part]="Madison"
        chat1[part]="Don't mention it! You're Lenna, right? I heard"
        chat2[part]="your friend call you that."
        chat3[part]=""
        musicplay[part]="guitar"
        part=33; speaker[part]="Lenna"
        chat1[part]="That's right. But who are you?"
        part=34; speaker[part]="Madison"
        chat1[part]="Name's Madison. Basically, I'm the engineer"
        chat2[part]="around here. The ONLY engineer. You've"
        chat3[part]="met my friend here."
        part=35; speaker[part]="Robot"
        chat1[part]="..."
        part=36; speaker[part]="Lenna"
        chat1[part]="\"Robot\" is an awfully strange name."
        part=37; speaker[part]="Madison"
        chat1[part]="That's because he is one! I built him myself."
        chat2[part]="Looks human on the outside, doesn't he? He even"
        chat3[part]="has artificial blood!"
        part=38; speaker[part]="Lenna"
        chat1[part]="You said you're an engineer, so why did you help"
        chat2[part]="me?"
        chat3[part]=""
        part=39; speaker[part]="Madison"
        chat1[part]="The big bad scientist who hired me has been"
        chat2[part]="fuming over some escaped girl, must be you,"
        chat3[part]="right?"
        part=40; speaker[part]="Madison"
        chat1[part]="Said he'd need another girl if he couldn't"
        chat2[part]="find you. And I'm next on the list! So I want"
        chat3[part]="to team up with you before he gets me!"
        part=41; speaker[part]="Lenna"
        chat1[part]="You'd be wonderful on the team! And Robot"
        chat2[part]="too! Though, it's not really a very creative"
        chat3[part]="name, don't you think?"
        part=42; speaker[part]="Robot"
        chat1[part]="..."
        part=43; speaker[part]="Madison"
        chat1[part]="Hey now, I didn't name him, he named himself!"
        musicplay[part]="None"
        part=44
        changelevelpart=part; changelevelto="LevelMenu"; day=day; chapter+=1
        part=100
        partdelay[part]=100
        part=101; speaker[part]="Winston"
        chat1[part]="Huh? Did someone call my name?"
        part=102
        musicplay[part]="None"
        failurepart=part
    if (level=="Experiment"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=1; npcy[npcc]=2; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=5; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Experiment"; npcx[npcc]=8; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Bottle" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Experiment"; npcx[npcc]=3; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Wrench" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Experiment"; npcx[npcc]=2; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="Hammer" #Create NPCs
        npcc=5; npc[npcc]=1; npcside[npcc]="Experiment"; npcx[npcc]=11; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=6; npc[npcc]=1; npcside[npcc]="Experiment"; npcx[npcc]=13; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        npcc=7; npc[npcc]=1; npcside[npcc]="Strangler"; npcx[npcc]=12; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=3; movenpcy[part]=2
        part=3; speaker[part]="Lenna"
        chat1[part]="Would you look at that."
        musicplay[part]="ambient"
        part=4; speaker[part]="Lenna"
        chat1[part]="See all the machines down there?"
        part=5; speaker[part]="Winston"
        chat1[part]="I wouldn't have ever thought something like"
        chat2[part]="this was hidden in the hotel's basement."
        chat3[part]=""
        part=6; speaker[part]="Lenna"
        chat1[part]="What's over here?"
        movenpc[part]=1; movenpcx[part]=5; movenpcy[part]=7
        part=7; speaker[part]="Lenna"
        chat1[part]="Ah!"
        part=8; speaker[part]="Winston"
        chat1[part]="Back up, Lenna!"
        movenpc[part]=0; movenpcx[part]=6; movenpcy[part]=6
        part=9; speaker[part]="Lenna"
        chat1[part]="Phew, no, it's fine. Look, it's not moving."
        part=10; speaker[part]="Winston"
        chat1[part]="Who, or what, is that?"
        part=11; speaker[part]="Lenna"
        chat1[part]="A robot, maybe? Or another escaped"
        chat2[part]="experiment?"
        chat3[part]=""
        musicplay[part]="None"
        part=12; speaker[part]="Figure"
        chat1[part]="..."
        part=13; speaker[part]="Figure"
        chat1[part]="Intruders alert! Prepare to be annihilated."
        musicplay[part]="threefour"
        part=14
        controlChar=part
        part=20
        partdelay[part]=30
        part=21; speaker[part]="Lenna"
        chat1[part]="At least they're not actually, you know,"
        chat2[part]="real people."
        chat3[part]=""
        part=22; speaker[part]="Winston"
        chat1[part]="But were they at one point?"
        musicplay[part]="None"
        part=23
        changelevelpart=part; changelevelto="LevelMenu"; day=51; chapter+=1
        part=100
        partdelay[part]=30
        part=101; speaker[part]="Experiment"
        chat1[part]="Threat Neutralized."
        part=102
        musicplay[part]="None"
        failurepart=part
    if (level=="Science"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=8; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=10; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Scientist"; npcx[npcc]=9; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="" #Create NPCs
        npcc=3; npc[npcc]=0; npcside[npcc]="Experiment"; npcx[npcc]=2; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Glass" #Create NPCs
        npcc=4; npc[npcc]=0; npcside[npcc]="Experiment"; npcx[npcc]=17; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        npcc=5; npc[npcc]=0; npcside[npcc]="Experiment"; npcx[npcc]=7; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        npcc=6; npc[npcc]=0; npcside[npcc]="Experiment"; npcx[npcc]=10; npcy[npcc]=1; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=7; npc[npcc]=0; npcside[npcc]="Strangler"; npcx[npcc]=12; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Wrench" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=1; movenpcx[part]=10; movenpcy[part]=15
        part=3; speaker[part]="Winston"
        chat1[part]="Hey, are you the scientist?"
        part=4; speaker[part]="???"
        chat1[part]="..."
        part=5; speaker[part]="Lenna"
        chat1[part]="I think it's another one of those experiments."
        chat2[part]=""
        chat3[part]=""
        part=6; speaker[part]="Scientist"
        chat1[part]="...Power is verking efficiently..."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="mystery"
        movenpc[part]=2; movenpcx[part]=9; movenpcy[part]=9
        part=7; speaker[part]="Winston"
        chat1[part]="He's real, all right!"
        part=8; speaker[part]="Scientist"
        chat1[part]="Vat is it?"
        movenpc[part]=2; movenpcx[part]=9; movenpcy[part]=10
        part=9; speaker[part]="Scientist"
        chat1[part]="Please excuze me, sometimes I am so abzorbed in"
        chat2[part]="in my research I lose sense of my peripherals."
        chat3[part]=""
        part=10; speaker[part]="Scientist"
        chat1[part]="And you, little mizz, muzt be ze, ehh, girl zat"
        chat2[part]="ezcaped, ah?"
        chat3[part]=""
        part=11; speaker[part]="Winston"
        chat1[part]="Vat-er, What are you doing down here!? Some sort"
        chat2[part]="of mad laboratory! Do the Officers even know"
        chat3[part]="about you!?"
        part=12; speaker[part]="Scientist"
        chat1[part]="Ah, so much noize..."
        part=13; speaker[part]="Scientist"
        chat1[part]="How could mere children underztand the"
        chat2[part]="potential of my verk?"
        chat3[part]=""
        part=14; speaker[part]="Lenna"
        chat1[part]="I should be thanking you for erasing my memory."
        chat2[part]="I'm a better person because of it!"
        chat3[part]=""
        part=15; speaker[part]="Scientist"
        chat1[part]="But my rezearch vas not complete. I am going"
        chat2[part]="to...need you again, mizz."
        chat3[part]=""
        part=16; speaker[part]="Lenna"
        chat1[part]="Eeek! Get away!"
        part=17; speaker[part]="Scientist"
        chat1[part]="Hmmm, not complying?"
        musicplay[part]="None"
        part=18
        movenpc[part]=2; movenpcx[part]=9; movenpcy[part]=6
        part=18; speaker[part]="Scientist"
        chat1[part]="Creations! Avaken! Capture zis girl, alive or"
        chat2[part]="dead!"
        chat3[part]=""
        musicplay[part]="action"
        part=19
        createnpc[part]=3
        partdelay[part]=30
        part=20
        createnpc[part]=4
        partdelay[part]=30
        part=21
        createnpc[part]=5
        partdelay[part]=30
        part=22
        createnpc[part]=6
        partdelay[part]=30
        part=23
        createnpc[part]=7
        partdelay[part]=30
        part=24; speaker[part]="Scientist"
        chat1[part]="If my calculations are correct, ve vill meet"
        chat2[part]="again."
        chat3[part]=""
        movenpc[part]=2; movenpcx[part]=9; movenpcy[part]=1
        part=25
        createnpc[part]=-2
        partdelay[part]=1
        part=26
        movenpc[part]=1; movenpcx[part]=12; movenpcy[part]=14
        part=27
        controlChar=part
        part=40
        partdelay[part]=30
        part=41; speaker[part]="Lenna"
        chat1[part]="Ugh, my head...it's hurting..."
        musicplay[part]="None"
        part=42; speaker[part]="Winston"
        chat1[part]="Didn't get a concussion, did you?"
        part=43; speaker[part]="Lenna"
        chat1[part]="No...I'm remembering something."
        part=44; speaker[part]="Lenna"
        chat1[part]="The device...i-it's, right ahead. I remember"
        chat2[part]="running down these corridors...Down the"
        chat3[part]="next hall and through the first right door..."
        part=45
        changelevelpart=part; changelevelto="LevelMenu"; day=52; chapter+=1
        part=100
        partdelay[part]=30
        part=101; speaker[part]="Scientist"
        chat1[part]="Hmmm, my calculations vere incorrect."
        part=102
        musicplay[part]="None"
        failurepart=part
    if (level=="Device"):
        dorandomizeItems=0
        selectx=8; camerax=selectx
        selecty=8; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=6; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=11; npcy[npcc]=9; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=6; movenpcy[part]=6
        part=3; speaker[part]="Winston"
        chat1[part]="That's the memory machine, whatever it's called..."
        chat2[part]="down there?"
        chat3[part]=""
        musicplay[part]="ambient"
        part=4; speaker[part]="Lenna"
        chat1[part]="I remember the scientist pushing a bunch of buttons."
        chat2[part]="In a very specific order too."
        chat3[part]=""
        part=5
        movenpc[part]=1; movenpcx[part]=11; movenpcy[part]=7
        part=6; speaker[part]="Winston"
        chat1[part]="Careful with that. You might break it."
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=8
        part=7; speaker[part]="Lenna"
        chat1[part]="I'm setting it to affect the entire hotel."
        chat2[part]="Everything that's happened in the past few"
        chat3[part]="days will be forgotten. Reset, you could say."
        movenpc[part]=1; movenpcx[part]=13; movenpcy[part]=7
        part=8; speaker[part]="Lenna"
        chat1[part]="That also means...it will have been as though"
        chat2[part]="we never met."
        chat3[part]=""
        part=9; speaker[part]="Winston"
        chat1[part]="I'm sure we'll meet again, wherever we end up."
        part=10; speaker[part]=" "
        chat1[part]="The device below lights up."
        chat2[part]=""
        chat3[part]=""
        part=11; speaker[part]="Voice"
        chat1[part]="45 seconds remaining until memory wipe."
        part=12; speaker[part]="Lenna"
        chat1[part]="You think...? Maybe. Winston, I'm having regrets"
        chat2[part]="about this."
        chat3[part]=""
        musicplay[part]="None"
        movenpc[part]=1; movenpcx[part]=9; movenpcy[part]=8
        part=13; speaker[part]="Winston"
        chat1[part]="About what?"
        part=14; speaker[part]="Lenna"
        chat1[part]="I don't want to forget you, Winston! We won't ever"
        chat2[part]="get to a point like this again!"
        chat3[part]=""
        musicplay[part]="calm"
        part=15; speaker[part]="Winston"
        chat1[part]="Lenna, I'm sorry."
        part=16; speaker[part]="Lenna"
        chat1[part]="I know...we have to do this...But, don't you think"
        chat2[part]="we could have been even happier together, despite"
        chat3[part]="all the trouble?"
        part=17; speaker[part]="Voice"
        chat1[part]="30 seconds."
        part=18; speaker[part]="Winston"
        chat1[part]="All flesh is not the same flesh: but there is one"
        chat2[part]="kind of flesh of men, another flesh of beasts,"
        chat3[part]="another of fishes, and another of birds."
        part=19; speaker[part]="Winston"
        chat1[part]="There are also celestial bodies, and bodies"
        chat2[part]="terrestrial: but the glory of the celestial is one,"
        chat3[part]="and the glory of the terrestrial is another."
        part=20; speaker[part]="Winston"
        chat1[part]="We are different, Lenna. Something like that would"
        chat2[part]="have been impossible."
        chat3[part]=""
        part=21; speaker[part]="Lenna"
        chat1[part]="Huh...?"
        part=22; speaker[part]="Voice"
        chat1[part]="20 seconds."
        part=23; speaker[part]="Lenna"
        chat1[part]="What do you mean I'm a terrestrial? Are you"
        chat2[part]="not?"
        chat3[part]=""
        part=24; speaker[part]="Winston"
        chat1[part]="No Lenna, I'm not..."
        movenpc[part]=0; movenpcx[part]=6; movenpcy[part]=8
        part=25; speaker[part]="Lenna"
        chat1[part]="But...I love you!"
        part=26; speaker[part]="Voice"
        chat1[part]="10 seconds."
        part=27; speaker[part]="Winston"
        chat1[part]="..."
        part=28; speaker[part]="Winston"
        chat1[part]="At least tell me, do you know who killed"
        chat2[part]="the resident? The man on our floor on the first"
        chat3[part]="night..."
        movenpc[part]=0; movenpcx[part]=7; movenpcy[part]=8
        part=29; speaker[part]="Lenna"
        chat1[part]="It wasn't me...I don't know who did it."
        chat2[part]="Floyd...Lucas, maybe?"
        chat3[part]=""
        part=30; speaker[part]="Winston"
        chat1[part]="Heh, doesn't matter anymore."
        part=31; speaker[part]="Winston"
        chat1[part]="I'm sorry, Lenna. For everything."
        musicplay[part]="None"
        part=32
        partdelay[part]=400
        part=33
        changelevelpart=part; changelevelto="LevelMenu"; day=53; chapter+=1
    if (level=="Reset"):
        selectx=29; camerax=selectx #Camera Position
        selecty=14; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=29; npcy[npcc]=12; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        part=1
        movenpc[part]=0; movenpcx[part]=26; movenpcy[part]=13; movespeed[part]=.05 #Move NPCs
        part=2; speaker[part]="Winston"
        chat1[part]="Room 417..."
        chat2[part]="Looks like this is where I'll be staying."
        chat3[part]=""
        musicplay[part]="standby"
        part=3
        movenpc[part]=0; movenpcx[part]=26; movenpcy[part]=14
        part=4; speaker[part]="Winston"
        chat1[part]="It feels eerily familar, as though I've"
        chat2[part]="been here before."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=26; movenpcy[part]=15
        part=5; speaker[part]="Winston"
        chat1[part]="Just a case of deja vu, my memory's never"
        chat2[part]="been the best anyway."
        chat3[part]=""
        movenpc[part]=0; movenpcx[part]=25; movenpcy[part]=19
        part=6
        movenpc[part]=0; movenpcx[part]=24; movenpcy[part]=20
        part=7; speaker[part]="Winston"
        chat1[part]="It feels so good to finally get some time"
        chat2[part]="to relax. Not a care in the world! I've never"
        chat3[part]="been happier!"
        movenpc[part]=0; movenpcx[part]=24; movenpcy[part]=22
        musicplay[part]="None"
        part=8
        gotopart[part]=11
        part=11; speaker[part]=" "
        chat1[part]="You hear someone knocking on your door."
        chat2[part]=""
        chat3[part]=""
        musicplay[part]="scary"
        part=12; speaker[part]="Winston"
        chat1[part]="That's probably an employee here to"
        chat2[part]="greet me. I guess I'd better answer..."
        chat3[part]=""
        part=13
        partdelay[part]=400
        part=14; speaker[part]=" "
        chat1[part]="The End."
        part=15
        musicplay[part]="None"
        changelevelpart=part; changelevelto="LevelMenu"; day=54; chapter+=1
    if (level=="WinstonChoice"):
        gx=19; gy=4
        selectx=29-gx; camerax=selectx #Camera Position
        selecty=14-gy; cameray=selecty
        sky=pygame.image.load("Images/skylight.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=26-gx; npcy[npcc]=15-gy; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1 #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=26-gx; movenpcy[part]=17-gy
        part=3; speaker[part]="Winston"
        chat1[part]="Someone, help me!"
        musicplay[part]="ambient"
        part=4; speaker[part]="Winston"
        chat1[part]="Isn't there anything I can do!? The Officers"
        chat2[part]="will kill me when they find me...if the hotel"
        chat3[part]="residents don't get me first."
        part=5; speaker[part]="Winston"
        chat1[part]="Man..."
        part=6
        movenpc[part]=0; movenpcx[part]=24-gx; movenpcy[part]=20-gy
        part=7
        movenpc[part]=0; movenpcx[part]=24-gx; movenpcy[part]=21-gy
        part=8
        movenpc[part]=0; movenpcx[part]=24-gx; movenpcy[part]=22-gy
        part=9; speaker[part]="Winston"
        chat1[part]="It's all my fault, and my friends don't even"
        chat2[part]="know the truth..."
        chat3[part]=""
        part=10; speaker[part]="Winston"
        chat1[part]="I brought them into this mess. Lucas, Floyd,"
        chat2[part]="Lenna, I'm sorry!"
        chat3[part]=""
        part=11; speaker[part]="Winston"
        chat1[part]="They don't even agree with each other on how"
        chat2[part]="to get out of this whole ordeal. Eventually"
        chat3[part]="they'll be found, and killed..."
        part=12
        partdelay[part]=200
        musicplay[part]="None"
        part=13; speaker[part]="Winston"
        chat1[part]="Will I be their savior...?"
        part=14; speaker[part]="Winston"
        chat1[part]="Heh, after these last three days, I never thought"
        chat2[part]="it would come down to this."
        chat3[part]=""
        part=15
        changelevelpart=part; changelevelto="LevelMenu"; day=60; chapter+=1
    if (level=="Truth"):
        selectx=11; camerax=selectx #Camera Position
        selecty=13; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Winston"; npcx[npcc]=10; npcy[npcc]=14; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; npcheld[npcc]="Knife" #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Resident"; npcx[npcc]=11; npcy[npcc]=15; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="" #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Woman"; npcx[npcc]=10; npcy[npcc]=4; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=0; npcheld[npcc]="" #Create NPCs
        npcc=3; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=11; npcy[npcc]=3; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Hammer" #Create NPCs
        npcc=4; npc[npcc]=1; npcside[npcc]="Officer"; npcx[npcc]=14; npcy[npcc]=16; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; npcheld[npcc]="Baton" #Create NPCs
        part=1
        partdelay[part]=10
        part=2
        movenpc[part]=0; movenpcx[part]=10; movenpcy[part]=9
        part=3; speaker[part]="Winston"
        chat1[part]="..."
        part=4
        partdelay[part]=60
        part=5
        movenpc[part]=1; movenpcx[part]=11; movenpcy[part]=14
        part=6; speaker[part]="Resident"
        chat1[part]="Huh? He looks familiar...That's right, he"
        chat2[part]="was on the news."
        chat3[part]=""
        part=7; speaker[part]="Resident"
        chat1[part]="Hey, everyone, that's him! That's the serial"
        chat2[part]="killer!"
        part=8
        movenpc[part]=2; movenpcx[part]=10; movenpcy[part]=5
        part=9; speaker[part]="Woman"
        chat1[part]="My goodness! Officer, help!"
        movenpc[part]=3; movenpcx[part]=11; movenpcy[part]=4
        part=10
        movenpc[part]=4; movenpcx[part]=10; movenpcy[part]=16
        part=11; speaker[part]="Officer"
        chat1[part]="He's armed with a knife! Everyone, stay away while"
        chat2[part]="I radio in for backup!"
        chat3[part]=""
        movenpc[part]=4; movenpcx[part]=10; movenpcy[part]=15
        part=12; speaker[part]="Winston"
        chat1[part]="..."
        part=13; speaker[part]="Winston"
        chat1[part]="It's true! I killed him! I killed the man"
        chat2[part]="in his apartment three days ago!"
        chat3[part]=""
        musicplay[part]="calm"
        part=14; speaker[part]="Winston"
        chat1[part]="I confess! Drop the charges on Lucas, Floyd, and"
        chat2[part]="Lenna!"
        chat3[part]=""
        part=15; speaker[part]="Winston"
        chat1[part]="With these words, I take my own life...as a martyr"
        chat2[part]="for everyone!"
        part=16
        controlChar=part
        part=25
        partdelay[part]=10
        part=26
        partdelay[part]=60
        part=27
        partdelay[part]=200
        musicplay[part]="None"
        part=28
        changelevelpart=part; changelevelto="LevelMenu"; day=61; chapter+=1
        part=100
        partdelay[part]=30
        part=101; speaker[part]="Winston"
        chat1[part]="I must save everyone, and this is the"
        chat2[part]="only way to do it."
        part=102
        failurepart=part
    if (level=="TrueEnd"):
        dorandomizeItems=0
        selectx=10; camerax=selectx
        selecty=10; cameray=selecty
        sky=pygame.image.load("Images/skyblue.png").convert_alpha() #Set Background
        tileset=pygame.image.load("Images/isotilesetdark.png").convert_alpha() #Set Background
        tilewall=pygame.image.load("Images/isowalldark.png").convert_alpha() #Set Background
        npcc=3; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=13; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Floyd"; npcx[npcc]=11; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Lucas"; npcx[npcc]=14; npcy[npcc]=7; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=0; npcdir[npcc]=1; #Create NPCs
        part=1
        partdelay[part]=60
        part=2; speaker[part]="Host"
        chat1[part]="The mystery has been solved. Winston,"
        chat2[part]="previous murder suspect committed suicide"
        chat3[part]="yesterday evening."
        musicplay[part]="rain"
        part=3; speaker[part]="Host"
        chat1[part]="Suspicions against aforementioned Lenna and Floyd"
        chat2[part]="have been dropped, Officers say there is not"
        chat3[part]="enough evidence to warrant continued search."
        part=4; speaker[part]="Host"
        chat1[part]="Crime involving drugs, gambling, and gang"
        chat2[part]="warfare has plummeted."
        chat3[part]=""
        part=5; speaker[part]="Host"
        chat1[part]="The Officers' Commander said, I quote, \"I am"
        chat2[part]="relieved to have my son, Lucas, back with me"
        chat3[part]="after being kidnapped by the serial killer.\""
        part=6; speaker[part]="Host"
        chat1[part]="The law will continue to be enforced swiftly and"
        chat2[part]="in justice by the Officers, as well as Lucas,"
        chat3[part]="who has returned to the force."
        part=7; speaker[part]="Host"
        chat1[part]="In other news, today's forecast shows heavy rain"
        chat2[part]="tonight..."
        chat3[part]=""
        part=8
        partdelay[part]=60
        part=9
        partdelay[part]=60
        part=10
        partdelay[part]=60
        part=11
        partdelay[part]=120
        part=12; speaker[part]="Lenna"
        chat1[part]="So he's really dead."
        part=13; speaker[part]="Lucas"
        chat1[part]="Who would have thought he was the"
        chat2[part]="killer?"
        chat3[part]=""
        part=14; speaker[part]="Floyd"
        chat1[part]="Lenna and I were framed so he could hide"
        chat2[part]="his secret, but it looks like the grief"
        chat3[part]="got to him."
        part=15; speaker[part]="Lenna"
        chat1[part]="It was more than that...he wanted to save us."
        part=16; speaker[part]="Floyd"
        chat1[part]="And so he did. The crime rate has dropped"
        chat2[part]="significantly since his death. I used to complain"
        chat3[part]="about how sinful this whole hotel was..."
        part=17; speaker[part]="Floyd"
        chat1[part]="But, they have found their way."
        part=18; speaker[part]="Floyd"
        chat1[part]="I am no longer needed here. If you'll"
        chat2[part]="both excuse me, I must return elsewhere."
        chat3[part]=""
        part=19
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=7
        part=20
        movenpc[part]=1; movenpcx[part]=8; movenpcy[part]=4
        part=21
        createnpc[part]=-1
        partdelay[part]=30
        part=22; speaker[part]="Lenna"
        chat1[part]="Thank you for everything, Winston."
        chat2[part]=""
        chat3[part]=""
        movenpc[part]=3; movenpcx[part]=13; movenpcy[part]=8
        part=23; speaker[part]="Lucas"
        chat1[part]="Why do you think he did it? You know..."
        chat2[part]="kill the resident on your floor?"
        chat3[part]=""
        part=24; speaker[part]="Lenna"
        chat1[part]="It's difficult to say. My memory of everything"
        chat2[part]="is still fuzzy, but I feel as though bits"
        chat3[part]="and pieces are coming back to me."
        part=25; speaker[part]="Lenna"
        chat1[part]="I think we'll never know his true motives."
        chat2[part]="They're lost with his death."
        chat3[part]=""
        part=26; speaker[part]="Lucas"
        chat1[part]="Maybe he was hoping for a different outcome."
        part=27; speaker[part]="Lenna"
        chat1[part]="Yeah, maybe."
        part=28; speaker[part]="Lenna"
        chat1[part]="Come on, let's head back in. The rain is"
        chat2[part]="getting heavy."
        chat3[part]=""
        movenpc[part]=3; movenpcx[part]=13; movenpcy[part]=7
        part=29; speaker[part]="Lucas"
        chat1[part]="I'll meet up with you."
        part=30
        movenpc[part]=3; movenpcx[part]=8; movenpcy[part]=7
        part=31
        movenpc[part]=3; movenpcx[part]=8; movenpcy[part]=13
        part=32
        createnpc[part]=-3
        partdelay[part]=200
        musicplay[part]="None"
        part=33; speaker[part]="Lucas"
        chat1[part]="Is this but a shadow of what's to come?"
        chat2[part]="The coming Messiah...? Ha...Winston,"
        chat3[part]="you're really something."
        musicplay[part]="guitar"
        movenpc[part]=2; movenpcx[part]=14; movenpcy[part]=8
        part=34
        movenpc[part]=2; movenpcx[part]=8; movenpcy[part]=8
        part=35
        movenpc[part]=2; movenpcx[part]=8; movenpcy[part]=13
        part=36
        createnpc[part]=-2
        partdelay[part]=200
        part=37
        partdelay[part]=500
        part=38; speaker[part]=" "
        chat1[part]="The End."
        chat2[part]=""
        chat3[part]=""
        part=39
        musicplay[part]="None"
        changelevelpart=part; changelevelto="LevelMenu"; day=62; chapter+=1        
    if (level=="Test"):
        dorandomizeItems=1
        selectx=14; camerax=selectx #Camera Position
        selecty=4; cameray=selecty
        sky=pygame.image.load("Images/skyorange.png").convert_alpha() #Set Background
        npcc=0; npc[npcc]=1; npcside[npcc]="Lenna"; npcx[npcc]=8; npcy[npcc]=6; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; npcheld[npcc]="Med Kit" #Create NPCs
        npcc=1; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=8; npcy[npcc]=10; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=0; npcheld[npcc]="Knife" #Create NPCs
        npcc=2; npc[npcc]=1; npcside[npcc]="Man"; npcx[npcc]=12; npcy[npcc]=8; npcdx[npcc]=npcx[npcc]; npcdy[npcc]=npcy[npcc]; npccontrol[npcc]=1; npcdir[npcc]=1; npcheld[npcc]="Bottle" #Create NPCs
        part=1
        partdelay[part]=50
        part=2
        controlChar=part;# tutorialhurt=1
        '''
        part=; speaker[part]=""
        chat1[part]=""
        chat2[part]=""
        chat3[part]=""
        '''
    



def storyTriggers():
    global part, tutorialmove, tutorialhurt, tutorialpick, tutorialthrow, controlChar, selectx, selecty, whogoes
    global showDist, showDist2, updating, am_actions, showPaths, actionselect, bodyselect, openbody, bodymenu, endlevel
    global lucas, floyd, lenna, lucastwo, gainparty
    if ((part==controlChar or level=="Questions" or level=="Idea" or level=="Talk" or level=="Friends") and lvlingup==0 and failurepart!=part):# and npcani[whogoes]==""):
        if (level=="Truth"):
            if (npcdead[0]==1):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=25
            if (npcpain[1]!=0 or npcpain[2]!=0 or npcpain[3]!=0 or npcpain[4]!=0): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Science"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=40
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1 and npcdead[7]==1):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1 or npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Experiment"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=20
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1 and npcdead[7]==1):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1 or npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Robot"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=30
            if (True): #if (npcani[0]=="" and npcani[3]=="" and npcdead[2]==1):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1 or npcdead[3]==1 or npcdead[4]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Unity"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=20
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1        
        if (level=="Confusion"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=20
            if (True): #if (npcani[0]=="" and npcdead[1]==1 and npcdead[2]==1 and npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[7]==1 and floyd2==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1        
        if (level=="Speechless"):
            if (npcturn[1]>=10 and part==4):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=6; controlChar=13
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=15
            if (True): #if (npcdead[1]==1 and npcani[0]=="" and part==13):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[2]==1 and floyd2==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1        
        if (level=="Wake"):
            if (npcfainted[1]<=0):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=3
        if (level=="Summit"):
            if (npcturn[0]>=20):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=39
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1        
            if (npcdead[2]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1        
        if (level=="Climb"):
            for m in range(11): #17/5
                if (True): #if (npcy[m]==17 and npcx[m]==5 and lvlingup==0 and wally[int(npcx[m])+int(npcy[m]-1)*lvlW]==1):
                    actionmenu=0; showDist=-1; showDist2=-1; updating=2
                    am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                    part=15
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Jerry2"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=45; gainparty=""
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1        
        if (level=="Escape"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=10
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Friends"):
            if (part==45):
                lucastwo=1
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=55
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and controlChar==part):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[0]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Lobby"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=20
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1 and part==17):
                endlevel=1
            else:
                endlevel=0
            if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and part==6):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                npcturn[4]=npcturn[0]-20; whogoes=4
                npcturn[5]=npcturn[0]-20
                npcturn[6]=npcturn[0]-20
                part=10; controlChar=17
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Talk"):
            if ((part==13 or part==20 or part==35) and letters1==0 and lvlingup==0):
                lenna=lenna+1
        if (level=="Lab"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=50
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and npcdead[4]==1): # and npcdead[5]==1 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Gamble"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=50
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[3]==1 and npcdead[6]==1 and npcdead[7]==1 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Memory"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=35
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and npcdead[4]==1): # and npcdead[5]==1 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        #if (level=="Memory"):
        #    if ((part==30 or part==46 or part==57) and letters1==0 and lvlingup==0):
        #        lenna=lenna+1
        if (level=="Idea"):
            if ((part==30 or part==46 or part==57) and letters1==0 and lvlingup==0):
                floyd=floyd+1
        if (level=="Report"):
            for m in range(11):
                if (True): #if (npcy[m]==8 and npcx[m]==10 and lvlingup==0 and wally[int(npcx[m])+int(npcy[m]-1)*lvlW]==1):
                    actionmenu=0; showDist=-1; showDist2=-1; updating=2
                    am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                    part=29
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Choose"):
            if (npcani[4]!="" and npcani[5]!="" and npcani[6]!=""):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=30       
        if (level=="Dinah"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=29
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[2]==1 and npcdead[3]==1 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Brawl"):
            if ((npcpain[3]>=4 or npcpain[4]>=4) and part==31 and lvlingup==0):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                whogoes=0; npcturn[5]=npcturn[0]
                part=40; controlChar=51
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=60
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcdead[5]==1 and part==51 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Floor"):
            if (npcx[0]==26-19 and npcy[0]==15-4 and lvlingup==0):
                part+=1; tutorialmove=0
        if (level=="Murder"): #end chapter
            if (endlevel==2):
                part+=1; tutorialhurt=0; actionmenu=0
                showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (True): #if (npcdead[1]==1 and npcani[1]=="Fall" and npcani[0]==""):
                endlevel=1
            else:
                endlevel=0
        if (level=="Murder" and npcdead[0]==1): #Failure on this Level
            part=99; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Accused"):
            if (npcx[0]==28-19 and npcy[0]==16-4 and part==10):
                part=11; controlChar=12
            if (npcx[0]==26-19 and npcy[0]==15-4 and part==12):
                part=13
        if (level=="Fight"):
            if (npcheld[0]!="" and tutorialpick==1):
                tutorialpick=0; tutorialthrow=1
            if (npcheld[0]=="" and tutorialthrow==1):
                tutorialthrow=0
            if (part==45 and npcdead[2]==1 and npcani[0]=="" and npcani[1]=="" and lvlingup==0):
                controlChar=48; part=47
                selectx=14; selecty=3
                npcturn[3]=npcturn[0]
                showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (endlevel==2):
                controlChar=1; part=49
                showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (True): #if (part==48 and npcdead[3]==1 and npcstrangle[2]!=1 and npcstrangle[3]!=1 and npcani[0]=="" and npcani[1]==""):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): #Failure on this Level
                part=91; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1):
                part=99; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Outside"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=24
            if (True): #if (npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1 and npcdead[7]==1 and npcani[0]=="" and npcani[1]=="" and npcani[2]=="" and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=96; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=98; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[2]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Ambush"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=39
            if (True): #if (npcdead[2]==1 and npcdead[3]==1 and npcdead[4]==1 and npcani[0]=="" and npcani[1]=="" and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=102; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Break"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=40
            if (True): #if (npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1 and npcani[0]=="" and npcani[1]=="" and npcani[2]=="" and npcani[8]=="" and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=108; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[2]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[8]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Split"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=40
            if (True): #if (npcdead[3]==1 and npcani[0]=="" and npcani[1]=="" and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=102; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Matthew"):
            if ((npcpain[1]+npcbleeding[1]>=8 or npcdead[1]==1) and npcani[0]=="" and npcani[2]=="" and lvlingup==0):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                npcpain[1]=0; npcbleeding[1]=0; npcdead[1]=0
                part=40
            if (npcdead[3]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[2]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Jerry"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=40
            if (True): #if (npcani[0]=="" and npcdead[2]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1): #and npcdead[6]==1 and npcdead[7]==1 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=102; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1             
            if (npcdead[3]==1): part=104; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Questions"):
            if ((part==20 or part==30 or part==41) and letters1==0 and lvlingup==0):
                lucas=lucas+1
        if (level=="Save"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=30
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcani[2]=="" and npcdead[3]==1 and npcdead[4]==1 and npcdead[5]==1 and npcdead[6]==1 and npcdead[7]==1 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1          
            if (npcdead[2]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (level=="Gone"):
            if (endlevel==2):
                actionmenu=0; showDist=-1; showDist2=-1; updating=2
                am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
                part=30
            if (True): #if (npcani[0]=="" and npcani[1]=="" and npcani[2]=="" and npcdead[3]==1 and npcdead[4]==1): #and npcdead[5]==1 and npcdead[6]==1 and lvlingup==0):
                endlevel=1
            else:
                endlevel=0
            if (npcdead[0]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[1]==1): part=105; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
            if (npcdead[2]==1): part=100; actionmenu=0; showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1



































 













def displaySky():
    screen.blit(sky,(0,0))

def displayRain():
    global updating
    for n in range(5):
        updating=1
        x=random.randint(-300,WIDTH+300)
        y=random.randint(-300,HEIGHT+300)
        screen.blit(rainpatch,(x,y))

def displayDust():
    global updating
    for n in range(5):
        updating=1
        x=random.randint(-300,WIDTH+300)
        y=random.randint(-300,HEIGHT+300)
        screen.blit(dustpatch,(x,y))    

delay4=0
waterWaveMax=5.0
moved=0
textspeed=10.7
mmx=100
mmy=50
loadedparty=0
doored=0
lucastwo=0
dp=0
def displayTiles():
    global npcframetick, npcframe, showDist, showDist2, showPaths, actionmenu, actionselect, delay4
    global delay, delay2, moved, part, movie, pressed, movedalready, actionalready, delaysit, updating, updatefix
    global selectx, selecty, itemsparksize, event00, showhurt, mmx, mmy, npcdist, loadedparty, placeside, doored, flashdelay
    global npcframetick, pressed, showDist, showPaths
    global arrowyy, arrowdyy, showhurt, fallz, updating, twins, changelevelpart, changelevelto, chapter, dp
    if (level=="LevelMenu"): mmx=0; mmy=50
    if (level!="LevelMenu"): mmx=0; mmy=0
    if (npcframetick<=0): npcframetick=30; npcframe+=1
    if (npcframe>3): npcframe=0
    if (showhurt>0): showhurt-=1
    if (showhurt<=0): showhurt=100
    if (dp>0): dp-=1
    if (level=="Classroom"): #Sitting NPC Head Bob Tile Change
        if (delaysit<=0):
            delaysit=80; updating=1
            for n in range(lvlH*lvlW):
                c=0
                if (tilex[n]==4 and tiley[n]==4 and c==0): c=1; tilex[n]=5
                if (tilex[n]==5 and tiley[n]==4 and c==0): c=1; tilex[n]=4
        if (delaysit>0): delaysit-=1
    npcframetick-=1
    if (part==controlChar and loadedparty==0): #Load Party into Level
        loadedparty=1
        if (level!="LevelMenu" and level!="" and level!="Split" and level!="Choose"): #Load Party into Level
            for nn in range(11):
                if (npcside[nn]=="" and npc[nn]==0):
                    loadPartyMembers(nn)
            placeside=1
            for n in range(21):
                if (partyselect[n]==2): partyselect[n]=1
        if (level!="LevelMenu" and level!=""):
            for nn in range(11):
                loadPartyInLevel(nn)
    if (part==controlChar and movie==1): #In a Cutscene?
        movie=0
        selectx=npcx[0]; selecty=npcy[0]
    if (part!=controlChar and movie==0):
        movie=1
    if (movenpc[part]>-1 and delay<=0): #Cutscene Move Check
        npcdx[movenpc[part]]=movenpcx[part]
        npcdy[movenpc[part]]=movenpcy[part]
        npcwalkspeed[movenpc[part]]=movespeed[part]
    if (moved==1 and movie==1): #Done Moving Cutscene
        a=int(npcx[movenpc[part]])+int(npcy[movenpc[part]])*lvlW #Open/Close Doors
        dpp=0
        if (wallx[a]>=5): wally[a]=1-wally[a]; dpp=1
        if (wallx[a+1]>=5 and walldir[a+1]==0): wally[a+1]=1-wally[a+1]; dpp=1
        if (wallx[a-1]>=5 and walldir[a-1]==3): wally[a-1]=1-wally[a-1]; dpp=1
        if (wallx[a+lvlW]>=5 and walldir[a+lvlW]==1): wally[a+lvlW]=1-wally[a+lvlW]; dpp=1
        if (wallx[a-lvlW]>=5 and walldir[a-lvlW]==2): wally[a-lvlW]=1-wally[a-lvlW]; dpp=1
        if (dpp==1 and dp<=0):
            dp=30
            if (mute==0): door.play()
        movenpc[part]=-1
        moved=0
        if (chat1[part]=="" and chat2[part]=="" and chat3[part]=="" and part!=controlChar):
            nextMessage()
    if (showDist2>-1 and npccontrol[showDist2]==1 and showDist2==whogoes):
        actionmenu=1
        if (movedalready==1 and actionalready==1 and thrown=="" and (npcani[whogoes]!="Attack" and npcani[whogoes]!="End Attack") and npccontrol[whogoes]==1): nextTurn()
    if (showDist2<=-1 or npccontrol[showDist2]==0): actionmenu=0
    if (createnpc[part]!=0): #Create NPC/ Destroy NPC
        if (createnpc[part]>0): npc[createnpc[part]]=1; createnpc[part]=0
        if (createnpc[part]<0): npc[abs(createnpc[part])]=0; createnpc[part]=0
    for nn in range(11): #NPC Walk
        if (npccontrol[nn]==0 and part==controlChar and nn==whogoes and delay2<=0 and npcani[whogoes]==""): #NPC Not Controllable
            if (lagging==0): updating=1
            d=random.randint(0,3)
            lows=10000
            sd=nn; unmoved=0
            for m in range(11): #Which NPC to go to, AI (artificial intelligence)
                a=0
                if (level=="Summit" and npcside[m]=="Floyd"): a=1
                if (level=="Outside" and (npcside[m]=="Floyd" or npcside[m]=="Officer") and npcside[nn]!="Officer"): a=1
                if (level=="Outside" and (npcside[m]!="Officer" and npcside[m]!="Floyd") and npcside[nn]=="Officer"): a=1
                if (level!="Outside" and level!="Floor" and level!="Summit" and npccontrol[m]==1): a=1
                if (level=="Save" and npcside[nn]=="Floyd"): a=0
                if (level=="Confusion" and m!=nn): a=1
                if (level=="Truth"): a=1
                if (a==1 and npc[m]==1 and npcdead[m]==0 and npcbleeding[m]<14 and npcthroat[m]<2 and npclungs[m]<2 and npcheart[m]<2):
                    a=npcx[m]-npcx[nn]; b=npcy[m]-npcy[nn]
                    c=a*a+b*b; c**.5
                    if (c<lows): lows=c; sd=m; unmoved=1
            lows=0; sdtile=0
            if (npcside[sd]=="Floyd" and level=="Outside"): unmoved=0
            if (unmoved==1 and (npcpain[nn]>7 or npcrunaway[nn]>=1)): #Run Away
                pathFinding(nn)
                for mm in range(lvlW*lvlH):
                    if (tilefill[mm]>1):
                        aa=int(mm%lvlW)-npcx[sd]
                        bb=int(mm/lvlW)-npcy[sd]
                        cc=(aa*aa+bb*bb)**.5
                        if (cc>lows): lows=cc; sdtile=mm
                npcdx[nn]=int(sdtile%lvlW); npcdy[nn]=int(sdtile/lvlW)
            else:
                npcdx[nn]=npcx[sd]; npcdy[nn]=npcy[sd]

            '''pathFinding(nn)
            if (tilefill[int(npcdx[nn])+int(npcdy[nn])*lvlW]==0): #If Not Moving, Open Nearby Doors #################################################
                pathFinding(nn)
                for mm in range(lvlW*lvlH):
                    if (tilefill[mm]>1):
                        a=0
                        if (wallx[mm]==6 and wally[mm]==0): a=1
                        if (wallx[mm+1]==6 and walldir[mm+1]==0 and wally[mm+1]==0): a=1
                        if (wallx[mm-1]==6 and walldir[mm-1]==3 and wally[mm-1]==0): a=1
                        if (wallx[mm+lvlW]==6 and walldir[mm+lvlW]==1 and wally[mm+lvlW]==0): a=1
                        if (wallx[mm-lvlW]==6 and walldir[mm-lvlW]==2 and wally[mm-lvlW]==0): a=1
                        if (a==1):
                            aa=int(mm%lvlW)-npcx[sd]
                            bb=int(mm/lvlW)-npcy[sd]
                            cc=(aa*aa+bb*bb)**.5
                            if (cc>lows): lows=cc; sdtile=mm
                npcdx[nn]=int(sdtile%lvlW); npcdy[nn]=int(sdtile/lvlW)
                doored=1'''
                
            if (npcx[nn]==npcdx[nn] and npcy[nn]==npcdy[nn]): #If Not Moving, End Turn
                nextTurn()
            else:
                if (delay4<=0):
                    pathFinding(nn)
        d=0
        if (npccontrol[nn]==1 and part==controlChar and nn==whogoes): #NPC Controllable
            if (pressed==1 and selectx==npcx[nn] and selecty==npcy[nn] and showDist2<=-1): #Pressed Enter Over NPC that is Controllable
                showDist=-1; showDist2=-1; showPaths=0
                showDist2=nn; actionmenu=1; pressed=0; actionselect=0; d=1
        if (d==0 and part==controlChar and npc[nn]==1):
            if (pressed==1 and selectx==npcx[nn] and selecty==npcy[nn] and showDist2<=-1 and (nn!=whogoes or npccontrol[nn]==0)):  #Pressed Enter Over Other NPC
                if (nn!=whogoes and npccontrol[whogoes]==1):
                    showDist=-1; showDist2=-1; showPaths=0
                    showDist2=nn; actionmenu=0; pressed=0; showDist=showDist2
                    showPaths=1
                    pathFinding(nn)
        if (showDist==nn and actionselect==0 and showPaths==0): #Show Walking Distance
            showPaths=1
            pathFinding(nn)
        if (npcwalk[nn]>=1.0): npcwalk[nn]+=.2; updating=1
        if (npcwalk[nn]>5.0): npcwalk[nn]=1.0
        if (npcwalkspeedc[nn]<=0 and npcwalkdir[nn]>-1):
            npcx[nn]=round(npcx[nn]); npcy[nn]=round(npcy[nn]); delay2=0
        estop=0
        if ((npcdx[nn]!=npcx[nn] or npcdy[nn]!=npcy[nn]) and delay2<=0 and delay4<=0): #Not on the right tile
            a=0
            if (npccontrol[nn]==0): #Stop Right Before NPC
                if (npcdx[nn]==npcx[nn]-1 and npcdy[nn]==npcy[nn]): a=1
                if (npcdx[nn]==npcx[nn]+1 and npcdy[nn]==npcy[nn]): a=1
                if (npcdx[nn]==npcx[nn] and npcdy[nn]==npcy[nn]-1): a=1
                if (npcdx[nn]==npcx[nn] and npcdy[nn]==npcy[nn]+1): a=1
                if (a==1):
                    for m in range(11):
                        if (npcdx[nn]==npcx[m] and npcdy[nn]==npcy[m] and npc[m]==1 and m!=nn): a=1; break
                        if (m==10): a=0
            timess=5
            if (npcrightleg[nn]>2 or npcleftleg[nn]>2): timess=3
            if (npcrightleg[nn]>2 and npcleftleg[nn]>2): timess=1
            if (npcpara[nn]==1): timess=1
            if (npcdead[nn]==1): timess=0
            if (npcdist>timess and controlChar==part): a=-1
            if (a==1 or a==-1): #npcdist>=5
                npcx[nn]=round(npcx[nn]); npcy[nn]=round(npcy[nn]); sd=nn
                if ((a==1 or a==-1) and (npcpain[nn]<=7 and npcrunaway[nn]==0) and doored==0): ################################################################
                    for m in range(11):
                        if (npcdx[nn]==npcx[m] and npcdy[nn]==npcy[m] and npc[m]==1 and m!=nn): sd=m; break
                    if (npcx[nn]==npcx[sd]-1 and npcy[nn]==npcy[sd]): #Force Change Direction Upon Attack
                        npcdir[nn]=0
                        if (npcfainted[sd]<=0): npcdir[sd]=1
                    if (npcx[nn]==npcx[sd]+1 and npcy[nn]==npcy[sd]):
                        npcdir[nn]=1;
                        if (npcfainted[sd]<=0): npcdir[sd]=0
                    if (npcx[nn]==npcx[sd] and npcy[nn]==npcy[sd]-1):
                        npcdir[nn]=1;
                        if (npcfainted[sd]<=0): npcdir[sd]=0
                    if (npcx[nn]==npcx[sd] and npcy[nn]==npcy[sd]+1):
                        npcdir[nn]=0;
                        if (npcfainted[sd]<=0): npcdir[sd]=1
                    estop=1
                    npcx[nn]=int(npcx[nn]); npcy[nn]=int(npcy[nn])
                    npcx[sd]=int(npcx[sd]); npcy[sd]=int(npcy[sd])
                    if (npcpain[sd]+npcbleeding[sd]<15):
                        bp1a=random.randint(0,5); b=0
                    else:
                        bp1a=random.randint(0,1); b=0
                    if (bp1a==0): bp2a=random.randint(1,6)
                    if (bp1a==1): bp2a=random.randint(2,4)
                    if (bp1a==2): bp2a=random.randint(3,6)
                    if (bp1a==3): bp2a=random.randint(4,5)
                    if (bp1a==4): bp2a=random.randint(1,6); bp1a=0
                    if (bp1a==5): bp2a=random.randint(2,4); bp1a=1
                    if (npcdx[nn]==npcx[nn]-1 and npcdy[nn]==npcy[nn]): b=1
                    if (npcdx[nn]==npcx[nn]+1 and npcdy[nn]==npcy[nn]): b=1
                    if (npcdx[nn]==npcx[nn] and npcdy[nn]==npcy[nn]-1): b=1
                    if (npcdx[nn]==npcx[nn] and npcdy[nn]==npcy[nn]+1): b=1
                    if (npcside[nn]=="Cutthroat"):
                        bp1a=0; bp2a=6
                    if (npcpain[sd]>16 or npcfainted[sd]>5):
                        bp1a=0
                        bb=random.randint(1,2)
                        if (bb==1): bp2a=1
                        if (bb==2): bp2a=6
                    if (npccontrol[nn]==0 and npcani[nn]=="" and nn==whogoes and b==1):
                        if ((npcside[nn]!="Strangler" and npcside[nn]!="Sanders ") or npcrunaway[nn]==-1):
                            if (npcside[nn]!="Lenna" or level!="Speechless"):
                                AttSave(bp1a,bp2a,sd)
                                Attack()
                        if ((npcside[nn]=="Strangler" or npcside[nn]=="Sanders " or (npcside[nn]=="Lenna" and level=="Speechless")) and npcrunaway[nn]==0):
                            npcstrangle[nn]=2; npcstrangle[sd]=1; npcstrangling[nn]=sd; event00="The Strangler begins choking "+npcside[sd]+"."
                npcdx[nn]=int(npcx[nn]); npcdy[nn]=int(npcy[nn])
                npcdist=0
            if (a==-1):
                npcx[nn]=round(npcx[nn]); npcy[nn]=round(npcy[nn])
                npcdx[nn]=int(npcx[nn]); npcdy[nn]=int(npcy[nn])
                npcdist=0
            if (a==0):
                pathFinding(nn)
                if (tilefill[int(npcdx[nn])+int(npcdy[nn])*lvlW]==0 and npccontrol[nn]==0 and level!="LevelMenu"):
                    npcx[nn]=round(npcx[nn]); npcy[nn]=round(npcy[nn]) #Cannot find Destination (Noncontrolled)
                    npcdx[nn]=int(npcx[nn]); npcdy[nn]=int(npcy[nn])
                    npcdist=0
                    nextTurn()
                else:
                    npcwalkspeedc[nn]=1.0; delay2=100
                    if (npcwalk[nn]==0): npcwalk[nn]=1.0
        if (npcwalkdir[nn]==0): npcy[nn]-=npcwalkspeed[nn]; npcwalkspeedc[nn]-=npcwalkspeed[nn] #Different dir x y changes
        if (npcwalkdir[nn]==1): npcx[nn]-=npcwalkspeed[nn]; npcwalkspeedc[nn]-=npcwalkspeed[nn]
        if (npcwalkdir[nn]==2): npcy[nn]+=npcwalkspeed[nn]; npcwalkspeedc[nn]-=npcwalkspeed[nn]
        if (npcwalkdir[nn]==3): npcx[nn]+=npcwalkspeed[nn]; npcwalkspeedc[nn]-=npcwalkspeed[nn]
        if (npcwalkdir[nn]>-1 and npcx[nn]>=npcdx[nn]-npcwalkspeed[nn] and npcx[nn]<=npcdx[nn]+npcwalkspeed[nn]):
            if (npcy[nn]>=npcdy[nn]-npcwalkspeed[nn] and npcy[nn]<=npcdy[nn]+npcwalkspeed[nn]): #Found, int x and y
                npcdist=0; e=0
                '''if (doored==1):
                    a=int(npcx[nn])+int(npcy[nn])*lvlW #Open/Close Doors not in a Cutscene
                    if (wallx[a]==6): wally[a]=1-wally[a]
                    if (wallx[a+1]==6 and walldir[a+1]==0): wally[a+1]=1-wally[a+1]
                    if (wallx[a-1]==6 and walldir[a-1]==3): wally[a-1]=1-wally[a-1]
                    if (wallx[a+lvlW]==6 and walldir[a+lvlW]==1): wally[a+lvlW]=1-wally[a+lvlW]
                    if (wallx[a-lvlW]==6 and walldir[a-lvlW]==2): wally[a-lvlW]=1-wally[a-lvlW]'''
                if (npccontrol[nn]==1 and movedalready==1 and actionalready==1): showDist2=-1
                if (npccontrol[nn]==0 and controlChar==part and npcani[nn]==""): showDist2=-1; nextTurn(); e=1
                if (estop==0):
                    if (npcwalkdir[nn]==0 or npcwalkdir[nn]==3): npcdir[nn]=0 #Change Facing Dir
                    if (npcwalkdir[nn]==1 or npcwalkdir[nn]==2): npcdir[nn]=1
                npcx[nn]=npcdx[nn]; npcy[nn]=npcdy[nn]; npcwalk[nn]=0; npcwalkdir[nn]=-1; delay2=0; moved=1; 
                if (part==controlChar and npccontrol[nn]==1): #Show the Possible Movable Tiles/Reopen Menu after Moving
                    if (movedchar==0 and actionalready==0): showDist2=nn
                    if (actionalready==1 and e==0 and whogoes==nn): nextTurn()
    if (lagging==0 or updating>0):
        updatefix=1
        for n in range(lvlH*lvlW): #Display Tiles
            if (pressed==1 and part==controlChar and showDist>=0 and tilefill[int(selectx+selecty*lvlW)]>0 and (npcx[int(showDist)]!=int(selectx) or npcy[int(showDist)]!=int(selecty))): #Pressed Enter over Tile to Move NPC
                if (npcx[showDist]==selectx and npcy[showDist]==selecty): None
                else: npcdx[showDist]=selectx; npcdy[showDist]=selecty; showDist=-1; showPaths=0; movedalready=1
            a=0; z=tilez[n]
            if (tilex[n]==0 and tiley[n]==0): a=1
            if ((tilex[n]==6 and tiley[n]==0) or (tilex[n]==6 and tiley[n]==1)): z=(sin((-waterWave+n%lvlW-(n/lvlW)*.35))*waterWaveMax+sin(3.14/2)*waterWaveMax+10); updating=1; tilez[n]=z #Water Tile
            if (a==0):
                screen.blit(tileset,((n%lvlW)*.5*si-int(camerax*si*.5-cameray*si*.5)-int(n/lvlW)*18+380-mmx  ,  int(n/lvlW)*.25*si-int(camerax*si*.25+cameray*si*.25)+(n%lvlW)*9+290+z-mmy)  ,  (tilex[n]*si,tiley[n]*si,si,si))
            b=0
            if (tilex[n]!=6):
                if (tilez[n]<=0.0): zz=.1; tilez[n]=tilez[n]*.97+zz
                if (tilez[n]>=0.0): zz=-.1; tilez[n]=tilez[n]*.97+zz
            #if (abs(tilez[n-1])<maxz*.9 or n==0): tilez[n]=tilez[n]*.97+zz; b=1 #Tile Z change, phase in
            #if (abs(tilez[n-lvlW])<maxz*.9 and b==0):  tilez[n]=tilez[n]*.97+zz
            if (abs(tilez[n])<=.1): tilez[n]=0
            if (tilefill[n]>0 and showDist>=0):
                if (level=="Ambush" or level=="Brawl" or (day>=43 and day<50)): screen.blit(selectpath2img,((n%lvlW)*.5*si-int(camerax*si*.5-cameray*si*.5)-int(n/lvlW)*18+380  ,  int(n/lvlW)*.25*si-int(camerax*si*.25+cameray*si*.25)+(n%lvlW)*9+290+z))  
                else: screen.blit(selectpathimg,((n%lvlW)*.5*si-int(camerax*si*.5-cameray*si*.5)-int(n/lvlW)*18+380  ,  int(n/lvlW)*.25*si-int(camerax*si*.25+cameray*si*.25)+(n%lvlW)*9+290+z))            
            if (n%lvlW==selectx and int(n/lvlW)==selecty and (movie==0 or level=="" or level=="LevelMenu") and thrown=="" and (gainparty=="" or level!="LevelMenu") and lmselect==0 and zooming==0 and lmquit==0): #Yellow Selector
                screen.blit(selectimg,((n%lvlW)*.5*si-int(camerax*si*.5-cameray*si*.5)-int(n/lvlW)*18+380-mmx  ,  int(n/lvlW)*.25*si-int(camerax*si*.25+cameray*si*.25)+(n%lvlW)*9+290+z-mmy))
        for n in range(lvlH*lvlW): #Display Walls
            z=tilez[n]
            if (True):
                if (walldir[n]==2 or walldir[n]==3):
                    #displayItems(n,z)
                    for nn in range(19):
                        if (item[nn]!="" and itemx[nn]==int(n%lvlW) and itemy[nn]==int(n/lvlW) and (tilex[itemx[nn]+itemy[nn]*lvlW]!=0 or tiley[itemx[nn]+itemy[nn]*lvlW]!=0)):
                            itemspark2=pygame.transform.scale(itemspark,(int(itemsparksize),int(itemsparksize)))
                            screen.blit(itemspark,((itemx[nn]+2)*.5*si-int(camerax*si*.5-cameray*si*.5)-(itemy[nn]+1)*18+380-11  ,  (itemy[nn]+1)*.25*si-int(camerax*si*.25+cameray*si*.25)+(itemx[nn]+2)*9+290+npcz[nn]+z-17))
                            screen.blit(itemspark2,((itemx[nn]+2)*.5*si-int(camerax*si*.5-cameray*si*.5)-(itemy[nn]+1)*18+380-itemsparksize/2  ,  (itemy[nn]+1)*.25*si-int(camerax*si*.25+cameray*si*.25)+(itemx[nn]+2)*9+290+npcz[nn]+z-itemsparksize/2-6))

                    #BloodLines(n,z)
                    for nn in range(11):
                        if (bloodlen[nn]>0 and int(bloodlx[nn])==int(n%lvlW) and int(bloodly[nn])==int(n/lvlW)):
                            screen.blit(bloodline,(bloodlx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-bloodly[nn]*18+380+bloodvarx[nn] ,  bloodly[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+bloodlx[nn]*9+290+z+bloodvary[nn]-10), (0,0,2,int(bloodlen[nn]))) 
                            if (bloodlen[nn]<bloodmax[nn]):
                                bloodlen[nn]+=.02
                                if (lagging==0): updating=2
                    #displayNPCs(n,z)
                    for nn in range(11): #Display NPCs
                        if (nextLevelMenu==2):
                            if (partyselect[nn]==1):
                                tilez[int(npcx[nn]+npcy[nn]*lvlW)]=-5
                            if (partyselect[nn]==0):
                                tilez[int(npcx[nn]+npcy[nn]*lvlW)]=0
                        if (npc[nn]!=0 and int(npcx[nn])==int(n%lvlW) and int(npcy[nn])==int(n/lvlW)):
                            ny=0; b=0
                            if (npcdead[nn]==1 and (npcbleeding[nn]>=3 or npcblood[nn]<90)):
                                displayBlood(nn,z)
                            if (level=="Choose" and ((tilex[int(npcx[nn]+npcy[nn]*lvlW)]==1 and tiley[int(npcx[nn]+npcy[nn]*lvlW)]==1) or npcy[nn]>=13)):
                                fallz=fallz+.5
                                fallz=fallz*1.05
                                updating=2
                                z=int(fallz)
                                if (fallz>=20000):
                                    fallz=0; npc[nn]=0
                            if (level=="Choose" and part==42 and npcside[nn]=="Adam"):
                                npcani[nn]=""; npcstrangle[nn]=0; twins=3
                                changelevelpart=56; changelevelto="LevelMenu"; chapter+=1
                            if (level=="Choose" and part==102 and npcside[nn]=="Evelyn"):
                                npcani[nn]=""; npcstrangle[nn]=0; twins=4
                                changelevelpart=117; changelevelto="LevelMenu"; chapter+=1
                            if (npcani[nn]=="Attack"): #Ani's of NPCs
                                npcaniframe[nn]+=.25; updating=2
                                if (npcaniframe[nn]>=4):
                                    npcaniframe[nn]=3.8; npcani[nn]="End Attack"
                                    npcx[hit]=int(npcx[hit]); npcy[hit]=int(npcy[hit])
                                    if (thrown=="" and selectx==npcx[nn] and selecty==npcy[nn] and throwdist<=0 and npccontrol[nn]==1): Attack()
                                    if (npcstrangle[npclist[actionselect]]==0 and npcani[npclist[actionselect]]!="Fall" and npccontrol[nn]==1): npcdir[npclist[actionselect]]=1-npcdir[showDist2]
                            if (npcani[nn]=="End Attack"):
                                updating=2
                                if (npcaniframe[nn]>3): npcaniframe[nn]-=.025
                                else: npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<.1):
                                    npcaniframe[nn]=0; npcani[nn]=""
                                    if (npccontrol[nn]==0): nextTurn()
                            if (npcani[nn]=="Hurt"):
                                npcaniframe[nn]+=.5; updating=2
                                if (npcaniframe[nn]>=4): npcaniframe[nn]=3.8; npcani[nn]="Get Up"
                            if (npcani[nn]=="Get Up"):
                                npcaniframe[nn]-=.1; updating=2
                                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""
                            if (npcani[nn]=="HurtBad"):
                                npcaniframe[nn]+=.1; updating=2
                                if (npcaniframe[nn]>=4 and npcfainted[nn]<=0 and npcdead[nn]==0): npcaniframe[nn]=3.8; npcani[nn]="UpSlow"; npcdir[nn]=1-npcdir[nn]
                                if (npcdead[nn]==1): npcani[nn]="Fall"; npcdir[nn]=1-npcdir[nn]
                            if (npcani[nn]=="Fall"):
                                if (npcdead[nn]==0 or npcaniframe[nn]<3.8): npcaniframe[nn]+=.075; updating=2
                                if (npcaniframe[nn]>=4 and npcdead[nn]==0): npcaniframe[nn]=3.8; npcani[nn]="Up"
                            if (npcani[nn]=="Up"):
                                npcaniframe[nn]-=.1; updating=2
                                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""
                            if (npcani[nn]=="UpSlow"):
                                updating=2
                                if (npcaniframe[nn]>3): npcaniframe[nn]-=.01
                                else: npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""; npcdir[nn]=1-npcdir[nn]
                            if (npcani[nn]=="Strangling"):
                                npcaniframe[nn]+=.1
                                if (npcaniframe[nn]>=2.5): npcaniframe[nn]=2.5; npcani[nn]="StranglingBack"
                            if (npcani[nn]=="StranglingBack"):
                                npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<=.5): npcaniframe[nn]=.5; npcani[nn]="Strangling"
                            if (npcani[nn]=="Strangled"):
                                npcaniframe[nn]+=.1
                                if (npcaniframe[nn]>=1.9): npcaniframe[nn]=1.9; npcani[nn]="StrangledBack"
                            if (npcani[nn]=="StrangledBack"):
                                npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<=.1): npcaniframe[nn]=.1; npcani[nn]="Strangled"
                            if (npcani[nn]=="Hanging"):
                                npcaniframe[nn]=3
                            if (npcwalkdir[nn]>-1): #Walk Dir
                                if (npcwalkdir[nn]==0 or npcwalkdir[nn]==3): ny=0
                                if (npcwalkdir[nn]==1 or npcwalkdir[nn]==2): ny=si
                            bered=0; #Flash Red from Hurt
                            if ((npcpain[nn]>0 or npcbleeding[nn]>0) and showhurt<=5): bered=1
                            if ((npcpain[nn]>4 or npcbleeding[nn]>4) and showhurt<=60 and showhurt>55): bered=1
                            if ((npcpain[nn]>8 or npcbleeding[nn]>8) and showhurt<=30 and showhurt>25): bered=1
                            if ((npcpain[nn]>12 or npcbleeding[nn]>12) and showhurt<=85 and showhurt>80): bered=1
                            if (npcside[nn]=="Winston"): #Different Chars
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]=="Lenna"):
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]=="Lucas"):
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]=="Floyd"):
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]!="" and b==0):
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npccontrol[nn]==1 and npcside[nn]!="Floyd" and npcside[nn]!="Winston" and npcside[nn]!="Lucas" and npcside[nn]!="Lenna"):
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))                
                            if (bered==1 or npcdead[nn]==1):
                                if (npcside[nn]!="" and npcside[nn]!="Lenna" and npcside[nn]!="Floyd"):
                                    b=1
                                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="HurtBad"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                                if (npcside[nn]=="Lenna"):
                                    b=1
                                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="HurtBad"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                                if (npcside[nn]=="Floyd"):
                                    b=1
                                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="HurtBad"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (nn==whogoes and part==controlChar): #Cursor over NPC if is their turn
                                screen.blit(message_ready,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380+12  ,  -12-arrowyy+npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10))
                                arrowyy=arrowyy-arrowdyy*fpsfix
                                arrowdyy=arrowdyy+0.05*fpsfix
                                if (arrowyy<0): arrowyy=0; arrowdyy=-1
                            if (npcdead[nn]==1):
                                a=int(npcx[nn])+int(npcy[nn])*lvlW #Dead will force open doors
                                if (wallx[a]>=5): wally[a]=1
                                if (wallx[a+1]>=5 and walldir[a+1]==0): wally[a+1]=1
                                if (wallx[a-1]>=5 and walldir[a-1]==3): wally[a-1]=1
                                if (wallx[a+lvlW]>=5 and walldir[a+lvlW]==1): wally[a+lvlW]=1
                                if (wallx[a-lvlW]>=5 and walldir[a-lvlW]==2): wally[a-lvlW]=1



                                
                if (wallx[n]!=0 or wally[n]!=0):
                    tn=0; tx=0
                    if (walldir[n]==0): tn=int(si*.5); ty=0 #left
                    if (walldir[n]==1): tn=0; ty=0 #up
                    if (walldir[n]==2): tn=0; ty=si*.25; tx=int(si*.5) #down
                    if (walldir[n]==3): tn=int(si*.5); ty=si*.25; tx=-int(si*.5) #right
                    screen.blit(tilewall,((n%lvlW)*.5*si-int(camerax*si*.5-cameray*si*.5)-int(n/lvlW)*18+380-tn-tx+si*.5  ,  int(n/lvlW)*.25*si-int(camerax*si*.25+cameray*si*.25)+(n%lvlW)*9+290+z-15+ty),  (wallx[n]*si+tn,wally[n]*si,int(si*.5),si))
                    if (level=="Brawl" and wallx[n]==1 and wally[n]==3 and part>=14): #Change certain Walls
                        wally[n]=4
                        if (part==14): updating=1
                    a=0
                    if (wallx[n]==2 and wally[n]==2 and a==0 and flashdelay<=0): wallx[n]=3; a=1 #Flashing Light Walls
                    if (wallx[n]==3 and wally[n]==2 and a==0 and flashdelay<=0): wallx[n]=2; a=1
                if (walldir[n]<2):
                    #displayItems(n,z)
                    for nn in range(19):
                        if (item[nn]!="" and itemx[nn]==int(n%lvlW) and itemy[nn]==int(n/lvlW) and (tilex[itemx[nn]+itemy[nn]*lvlW]!=0 or tiley[itemx[nn]+itemy[nn]*lvlW]!=0)):
                            itemspark2=pygame.transform.scale(itemspark,(int(itemsparksize),int(itemsparksize)))
                            screen.blit(itemspark,((itemx[nn]+2)*.5*si-int(camerax*si*.5-cameray*si*.5)-(itemy[nn]+1)*18+380-11  ,  (itemy[nn]+1)*.25*si-int(camerax*si*.25+cameray*si*.25)+(itemx[nn]+2)*9+290+npcz[nn]+z-17))
                            screen.blit(itemspark2,((itemx[nn]+2)*.5*si-int(camerax*si*.5-cameray*si*.5)-(itemy[nn]+1)*18+380-itemsparksize/2  ,  (itemy[nn]+1)*.25*si-int(camerax*si*.25+cameray*si*.25)+(itemx[nn]+2)*9+290+npcz[nn]+z-itemsparksize/2-6))

                    #BloodLines(n,z)
                    for nn in range(11):
                        if (bloodlen[nn]>0 and int(bloodlx[nn])==int(n%lvlW) and int(bloodly[nn])==int(n/lvlW)):
                            screen.blit(bloodline,(bloodlx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-bloodly[nn]*18+380+bloodvarx[nn] ,  bloodly[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+bloodlx[nn]*9+290+z+bloodvary[nn]-10), (0,0,2,int(bloodlen[nn]))) 
                            if (bloodlen[nn]<bloodmax[nn]):
                                bloodlen[nn]+=.02
                                if (lagging==0): updating=2
                    #displayNPCs(n,z)
                    for nn in range(11): #Display NPCs
                        if (nextLevelMenu==2):
                            if (partyselect[nn]==1):
                                tilez[int(npcx[nn]+npcy[nn]*lvlW)]=-5
                            if (partyselect[nn]==0):
                                tilez[int(npcx[nn]+npcy[nn]*lvlW)]=0
                        if (npc[nn]!=0 and int(npcx[nn])==int(n%lvlW) and int(npcy[nn])==int(n/lvlW)):
                            ny=0; b=0
                            if (npcdead[nn]==1 and (npcbleeding[nn]>=3 or npcblood[nn]<90)):
                                displayBlood(nn,z)
                            if (level=="Choose" and ((tilex[int(npcx[nn]+npcy[nn]*lvlW)]==1 and tiley[int(npcx[nn]+npcy[nn]*lvlW)]==1) or npcy[nn]>=13)):
                                fallz=fallz+.5
                                fallz=fallz*1.05
                                updating=2
                                z=int(fallz)
                                if (fallz>=20000):
                                    fallz=0; npc[nn]=0
                            if (level=="Choose" and part==42 and npcside[nn]=="Adam"):
                                npcani[nn]=""; npcstrangle[nn]=0; twins=3
                                changelevelpart=56; changelevelto="LevelMenu"; chapter+=1
                            if (level=="Choose" and part==102 and npcside[nn]=="Evelyn"):
                                npcani[nn]=""; npcstrangle[nn]=0; twins=4
                                changelevelpart=117; changelevelto="LevelMenu"; chapter+=1
                            if (npcani[nn]=="Attack"): #Ani's of NPCs
                                npcaniframe[nn]+=.25; updating=2
                                if (npcaniframe[nn]>=4):
                                    npcaniframe[nn]=3.8; npcani[nn]="End Attack"
                                    npcx[hit]=int(npcx[hit]); npcy[hit]=int(npcy[hit])
                                    if (thrown=="" and selectx==npcx[nn] and selecty==npcy[nn] and throwdist<=0 and npccontrol[nn]==1): Attack()
                                    if (npcstrangle[npclist[actionselect]]==0 and npcani[npclist[actionselect]]!="Fall" and npccontrol[nn]==1): npcdir[npclist[actionselect]]=1-npcdir[showDist2]
                            if (npcani[nn]=="End Attack"):
                                updating=2
                                if (npcaniframe[nn]>3): npcaniframe[nn]-=.025
                                else: npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<.1):
                                    npcaniframe[nn]=0; npcani[nn]=""
                                    if (npccontrol[nn]==0): nextTurn()
                            if (npcani[nn]=="Hurt"):
                                npcaniframe[nn]+=.5; updating=2
                                if (npcaniframe[nn]>=4): npcaniframe[nn]=3.8; npcani[nn]="Get Up"
                            if (npcani[nn]=="Get Up"):
                                npcaniframe[nn]-=.1; updating=2
                                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""
                            if (npcani[nn]=="HurtBad"):
                                npcaniframe[nn]+=.1; updating=2
                                if (npcaniframe[nn]>=4 and npcfainted[nn]<=0 and npcdead[nn]==0): npcaniframe[nn]=3.8; npcani[nn]="UpSlow"; npcdir[nn]=1-npcdir[nn]
                                if (npcdead[nn]==1): npcani[nn]="Fall"; npcdir[nn]=1-npcdir[nn]
                            if (npcani[nn]=="Fall"):
                                if (npcdead[nn]==0 or npcaniframe[nn]<3.8): npcaniframe[nn]+=.075; updating=2
                                if (npcaniframe[nn]>=4 and npcdead[nn]==0): npcaniframe[nn]=3.8; npcani[nn]="Up"
                            if (npcani[nn]=="Up"):
                                npcaniframe[nn]-=.1; updating=2
                                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""
                            if (npcani[nn]=="UpSlow"):
                                updating=2
                                if (npcaniframe[nn]>3): npcaniframe[nn]-=.01
                                else: npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""; npcdir[nn]=1-npcdir[nn]
                            if (npcani[nn]=="Strangling"):
                                npcaniframe[nn]+=.1
                                if (npcaniframe[nn]>=2.5): npcaniframe[nn]=2.5; npcani[nn]="StranglingBack"
                            if (npcani[nn]=="StranglingBack"):
                                npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<=.5): npcaniframe[nn]=.5; npcani[nn]="Strangling"
                            if (npcani[nn]=="Strangled"):
                                npcaniframe[nn]+=.1
                                if (npcaniframe[nn]>=1.9): npcaniframe[nn]=1.9; npcani[nn]="StrangledBack"
                            if (npcani[nn]=="StrangledBack"):
                                npcaniframe[nn]-=.1
                                if (npcaniframe[nn]<=.1): npcaniframe[nn]=.1; npcani[nn]="Strangled"
                            if (npcani[nn]=="Hanging"):
                                npcaniframe[nn]=3
                            if (npcwalkdir[nn]>-1): #Walk Dir
                                if (npcwalkdir[nn]==0 or npcwalkdir[nn]==3): ny=0
                                if (npcwalkdir[nn]==1 or npcwalkdir[nn]==2): ny=si
                            bered=0; #Flash Red from Hurt
                            if ((npcpain[nn]>0 or npcbleeding[nn]>0) and showhurt<=5): bered=1
                            if ((npcpain[nn]>4 or npcbleeding[nn]>4) and showhurt<=60 and showhurt>55): bered=1
                            if ((npcpain[nn]>8 or npcbleeding[nn]>8) and showhurt<=30 and showhurt>25): bered=1
                            if ((npcpain[nn]>12 or npcbleeding[nn]>12) and showhurt<=85 and showhurt>80): bered=1
                            if (npcside[nn]=="Winston"): #Different Chars
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]=="Lenna"):
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]=="Lucas"):
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]=="Floyd"):
                                b=1
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npcside[nn]!="" and b==0):
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (npccontrol[nn]==1 and npcside[nn]!="Floyd" and npcside[nn]!="Winston" and npcside[nn]!="Lucas" and npcside[nn]!="Lenna"):
                                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                if (npcani[nn]=="HurtBad"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))                
                            if (bered==1 or npcdead[nn]==1):
                                if (npcside[nn]!="" and npcside[nn]!="Lenna" and npcside[nn]!="Floyd"):
                                    b=1
                                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="HurtBad"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                                if (npcside[nn]=="Lenna"):
                                    b=1
                                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="HurtBad"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                                if (npcside[nn]=="Floyd"):
                                    b=1
                                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                                    if (npcani[nn]=="HurtBad"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                            if (nn==whogoes and part==controlChar): #Cursor over NPC if is their turn
                                screen.blit(message_ready,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380+12  ,  -12-arrowyy+npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10))
                                arrowyy=arrowyy-arrowdyy*fpsfix
                                arrowdyy=arrowdyy+0.05*fpsfix
                                if (arrowyy<0): arrowyy=0; arrowdyy=-1
                            if (npcdead[nn]==1):
                                a=int(npcx[nn])+int(npcy[nn])*lvlW #Dead will force open doors
                                if (wallx[a]>=5): wally[a]=1
                                if (wallx[a+1]>=5 and walldir[a+1]==0): wally[a+1]=1
                                if (wallx[a-1]>=5 and walldir[a-1]==3): wally[a-1]=1
                                if (wallx[a+lvlW]>=5 and walldir[a+lvlW]==1): wally[a+lvlW]=1
                                if (wallx[a-lvlW]>=5 and walldir[a-lvlW]==2): wally[a-lvlW]=1

    for nn in range(19): #New DisplayItems
        if (selectx==itemx[nn] and selecty==itemy[nn] and controlChar==part and item[nn]!=""):
            a=1
            screen.blit(message_item,(WIDTH/2-100,HEIGHT-165))
            text=font2.render("On Ground: ",1,GRAY)
            screen.blit(text,(WIDTH/2-90,HEIGHT-155));# n+=1
            b=0
            for m in range(19):
                if (item[m]!="" and itemx[m]==selectx and itemy[m]==selecty):
                    b+=1
                    text=font2.render(item[m],1,WHITE)
                    screen.blit(text,(WIDTH/2-90+23+b*40,HEIGHT-155));# n+=1
    if (flashdelay<=0):
        flashdelay=30
        updating=2
    flashdelay-=1
    itemsparksize+=2 #Item Spark Size Change
    if (itemsparksize>30): itemsparksize=0

updatefix=0
flashdelay=30
npcdist=0
def pathFinding(nn):
    global moved, event00, npcdist, updating, selectx, selecty
    for n in range(lvlW*lvlH): #Reset Floodfill
        tilefill[n]=0
    tilefill[int(npcx[nn])+int(npcy[nn])*lvlW]=1
    timess=lvlW*lvlH
    if (showPaths==1): # or npccontrol[nn]==1
        timess=5
        if (npcrightleg[nn]>2 or npcleftleg[nn]>2): timess=3
        if (shortmove==1): timess=2
        if (npcrightleg[nn]>2 and npcleftleg[nn]>2): timess=1
        if (npcpara[nn]==1): timess=1
        if (npcdead[nn]==1): timess=0
    if (npccontrol[nn]==0 and nn==whogoes): timess=12
    if (npccontrol[nn]==0 and part!=controlChar): timess=lvlW*lvlH
    for times in range(timess):
        for n in range(lvlW*lvlH-lvlW):
            a=1
            for m in range(11): #Check if NPC occupies tile
                if ((npc[m]>0) and npcx[m]==n%lvlW and npcy[m]==int(n/lvlW) and (npcdead[m]==0 or npccontrol[whogoes]==0)): a=0
                if (npccontrol[whogoes]==0 and npcx[m]==npcdx[whogoes] and npcy[m]==npcdy[whogoes]): a=1
                if (a==0): break
            if (tilefill[n]==0 and n%lvlW>0 and n%lvlW<lvlW and (tilex[n]>0 or (tiley[n]!=0 and tiley[n]!=2 and tiley[n]!=3)) and a==1 and tilex[n]!=6):
                a=0
                if (tilefill[n+1]==times+1 and ((wallx[n+1]==0 and wally[n+1]==0 and wallx[n]==0 and wally[n]==0) or (wallx[n+1]>=5 and wally[n+1]==1) or (wallx[n]>=5 and wally[n]==1) or ((walldir[n]!=3 or (wallx[n]==0 and wally[n]==0)) and (walldir[n+1]!=0 or (wallx[n+1]==0 and wally[n+1]==0))))): tilefill[n]=times+2
                if (tilefill[n-1]==times+1 and ((wallx[n-1]==0 and wally[n-1]==0 and wallx[n]==0 and wally[n]==0) or (wallx[n-1]>=5 and wally[n-1]==1) or (wallx[n]>=5 and wally[n]==1) or ((walldir[n]!=0 or (wallx[n]==0 and wally[n]==0)) and (walldir[n-1]!=3 or (wallx[n-1]==0 and wally[n-1]==0))))): tilefill[n]=times+2
                if (tilefill[n+lvlW]==times+1 and ((wallx[n+lvlW]==0 and wally[n+lvlW]==0 and wallx[n]==0 and wally[n]==0) or (wallx[n+lvlW]>=5 and wally[n+lvlW]==1) or (wallx[n]>=5 and wally[n]==1) or ((walldir[n]!=2 or (wallx[n]==0 and wally[n]==0)) and (walldir[n+lvlW]!=1 or (wallx[n+lvlW]==0 and wally[n+lvlW]==0))))): tilefill[n]=times+2
                if (tilefill[n-lvlW]==times+1 and ((wallx[n-lvlW]==0 and wally[n-lvlW]==0 and wallx[n]==0 and wally[n]==0) or (wallx[n-lvlW]>=5 and wally[n-lvlW]==1) or (wallx[n]>=5 and wally[n]==1) or ((walldir[n]!=1 or (wallx[n]==0 and wally[n]==0)) and (walldir[n-lvlW]!=2 or (wallx[n-lvlW]==0 and wally[n-lvlW]==0))))): tilefill[n]=times+2
        if (tilefill[int(npcdx[nn])+int(npcdy[nn])*lvlW]>=1 and showPaths==0):
            nb=int(npcdx[nn])+int(npcdy[nn])*lvlW
            back=tilefill[int(npcdx[nn])+int(npcdy[nn])*lvlW]
            for m in range(lvlW*lvlH-lvlW):
                if (tilefill[nb]==back):
                    if (tilefill[nb+1]==back-1 and back>2 and ((wallx[nb+1]==0 and wally[nb+1]==0 and wallx[nb]==0 and wally[nb]==0) or (wallx[nb+1]>=5 and wally[nb+1]==1) or (wallx[nb]>=5 and wally[nb]==1) or ((walldir[nb]!=3 or (wallx[nb]==0 and wally[nb]==0)) and (walldir[nb+1]!=0 or (wallx[nb+1]==0 and wally[nb+1]==0))))): nb=nb+1; back-=1
                    if (tilefill[nb-1]==back-1 and back>2 and ((wallx[nb-1]==0 and wally[nb-1]==0 and wallx[nb]==0 and wally[nb]==0) or (wallx[nb-1]>=5 and wally[nb-1]==1) or (wallx[nb]>=5 and wally[nb]==1) or ((walldir[nb]!=0 or (wallx[nb]==0 and wally[nb]==0)) and (walldir[nb-1]!=3 or (wallx[nb-1]==0 and wally[nb-1]==0))))): nb=nb-1; back-=1
                    if (tilefill[nb+lvlW]==back-1 and back>2 and ((wallx[nb+lvlW]==0 and wally[nb+lvlW]==0 and wallx[nb]==0 and wally[nb]==0) or (wallx[nb+lvlW]>=5 and wally[nb+lvlW]==1) or (wallx[nb]>=5 and wally[nb]==1) or ((walldir[nb]!=2 or (wallx[nb]==0 and wally[nb]==0)) and (walldir[nb+lvlW]!=1 or (wallx[nb+lvlW]==0 and wally[nb+lvlW]==0))))): nb=nb+lvlW; back-=1
                    if (tilefill[nb-lvlW]==back-1 and back>2 and ((wallx[nb-lvlW]==0 and wally[nb-lvlW]==0 and wallx[nb]==0 and wally[nb]==0) or (wallx[nb-lvlW]>=5 and wally[nb-lvlW]==1) or (wallx[nb]>=5 and wally[nb]==1) or ((walldir[nb]!=1 or (wallx[nb]==0 and wally[nb]==0)) and (walldir[nb-lvlW]!=2 or (wallx[nb-lvlW]==0 and wally[nb-lvlW]==0))))): nb=nb-lvlW; back-=1
                if (back==2):
                    if (npcdizzy[nn]>0 and npcwalkdir[nn]>-1 and npcside[nn]!="Host" and controlChar==part): #Falling if Dizzy
                        diz=random.randint(1,3)
                        if (diz==1): npcdx[nn]=npcx[nn]; npcdy[nn]=npcy[nn]; npcani[nn]="Fall"; npcwalk[nn]=0; moved=1; event00=npcside[nn]+" fell over from disorientation."; selectx=npcx[whogoes]; selecty=npcy[whogoes]
                        if (diz==1 and npccontrol[whogoes]==0): nextTurn()
                    if (npcrightleg[nn]>4 or npcleftleg[nn]>4 and npcside[nn]!="Host" and controlChar==part):
                        diz=random.randint(1,4)
                        if (diz==1): npcdx[nn]=npcx[nn]; npcdy[nn]=npcy[nn]; npcani[nn]="Fall"; npcwalk[nn]=0; moved=1; event00=npcside[nn]+" tripped."; selectx=npcx[whogoes]; selecty=npcy[whogoes]
                        if (diz==1 and npccontrol[whogoes]==0): nextTurn()
                    if (tilefill[nb+1]==1): npcwalkdir[nn]=1
                    if (tilefill[nb-1]==1): npcwalkdir[nn]=3
                    if (tilefill[nb+lvlW]==1): npcwalkdir[nn]=0
                    if (tilefill[nb-lvlW]==1): npcwalkdir[nn]=2
                    npcdist+=1
                    return



itemsparksize=0
def displayItems(n,z):
    global updating, itemsparksize
    a=0
    for nn in range(19):
        if (item[nn]!="" and itemx[nn]==int(n%lvlW) and itemy[nn]==int(n/lvlW) and (tilex[itemx[nn]+itemy[nn]*lvlW]!=0 or tiley[itemx[nn]+itemy[nn]*lvlW]!=0)):
            itemspark2=pygame.transform.scale(itemspark,(int(itemsparksize),int(itemsparksize)))
            screen.blit(itemspark,((itemx[nn]+2)*.5*si-int(camerax*si*.5-cameray*si*.5)-(itemy[nn]+1)*18+380-11  ,  (itemy[nn]+1)*.25*si-int(camerax*si*.25+cameray*si*.25)+(itemx[nn]+2)*9+290+npcz[nn]+z-17))
            screen.blit(itemspark2,((itemx[nn]+2)*.5*si-int(camerax*si*.5-cameray*si*.5)-(itemy[nn]+1)*18+380-itemsparksize/2  ,  (itemy[nn]+1)*.25*si-int(camerax*si*.25+cameray*si*.25)+(itemx[nn]+2)*9+290+npcz[nn]+z-itemsparksize/2-6))
            if (selectx==itemx[nn] and selecty==itemy[nn] and a==0 and  controlChar==part):
                a=1
                screen.blit(message_item,(WIDTH/2-100,HEIGHT-165))
                text=font2.render("On Ground: ",1,GRAY)
                screen.blit(text,(WIDTH/2-90,HEIGHT-155)); n+=1
                b=0
                for m in range(19):
                    if (item[m]!="" and itemx[m]==selectx and itemy[m]==selecty):
                        b+=1
                        text=font2.render(item[m],1,WHITE)
                        screen.blit(text,(WIDTH/2-90+23+b*40,HEIGHT-155)); n+=1
          
def randomizeItems():
    count=0
    for n in range(lvlW*lvlH):
        if (tilex[n]!=0 and tilex[n]!=6):
            count+=1
    count2=random.randint(0,count)
    count3=random.randint(0,count)
    count=0
    for n in range(lvlW*lvlH):
        if (tilex[n]!=0 and tilex[n]!=6):
            count+=1
            if (count==count2 or count==count3):
                for m in range(19):
                    if (item[m]==""):
                        if (count==count2): item[m]="Shiv"
                        if (count==count3): item[m]="Hammer"
                        itemx[m]=int(n%lvlW); itemy[m]=int(n/lvlW)
                        break
                    
            
def displayBlood(nn,z):
    screen.blit(bloodimg,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10+12),  (si,bloodsize[nn]*si-si,si,si))
    if (showhurt>=100 and bloodsize[nn]<3 and npcani[nn]=="Fall"):
        bloodsize[nn]+=1

whichblood=0
def BloodLines(n,z):
    global updating
    for nn in range(11):
        if (bloodlen[nn]>0 and int(bloodlx[nn])==int(n%lvlW) and int(bloodly[nn])==int(n/lvlW)):
            screen.blit(bloodline,(bloodlx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-bloodly[nn]*18+380+bloodvarx[nn] ,  bloodly[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+bloodlx[nn]*9+290+z+bloodvary[nn]-10), (0,0,2,int(bloodlen[nn]))) 
            if (bloodlen[nn]<bloodmax[nn]):
                bloodlen[nn]+=.02
                if (lagging==0): updating=2

showDist=-1
showDist2=-1
showPaths=0
arrowyy=0; arrowdyy=0
showhurt=0
fallz=0.0
def displayNPCs(n,z):
    global npcframetick, pressed, showDist, showPaths
    global arrowyy, arrowdyy, showhurt, fallz, updating, twins, changelevelpart, changelevelto, chapter
    for nn in range(11): #Display NPCs
        if (nextLevelMenu==2):
            if (partyselect[nn]==1):
                tilez[int(npcx[nn]+npcy[nn]*lvlW)]=-5
            if (partyselect[nn]==0):
                tilez[int(npcx[nn]+npcy[nn]*lvlW)]=0
        if (npc[nn]!=0 and int(npcx[nn])==int(n%lvlW) and int(npcy[nn])==int(n/lvlW)):
            ny=0; b=0
            if (npcdead[nn]==1 and (npcbleeding[nn]>=3 or npcblood[nn]<90)):
                displayBlood(nn,z)
            if (level=="Choose" and ((tilex[int(npcx[nn]+npcy[nn]*lvlW)]==1 and tiley[int(npcx[nn]+npcy[nn]*lvlW)]==1) or npcy[nn]>=13)):
                fallz=fallz+.5
                fallz=fallz*1.05
                updating=2
                z=int(fallz)
                if (fallz>=20000):
                    fallz=0; npc[nn]=0
            if (level=="Choose" and part==42 and npcside[nn]=="Adam"):
                npcani[nn]=""; npcstrangle[nn]=0; twins=3
                changelevelpart=56; changelevelto="LevelMenu"; chapter+=1
            if (level=="Choose" and part==102 and npcside[nn]=="Evelyn"):
                npcani[nn]=""; npcstrangle[nn]=0; twins=4
                changelevelpart=117; changelevelto="LevelMenu"; chapter+=1
            #if (npcdead[nn]==1):
            #    z-=1
            if (npcani[nn]=="Attack"): #Ani's of NPCs
                npcaniframe[nn]+=.25; updating=2
                if (npcaniframe[nn]>=4):
                    npcaniframe[nn]=3.8; npcani[nn]="End Attack"
                    npcx[hit]=int(npcx[hit]); npcy[hit]=int(npcy[hit])
                    if (thrown=="" and selectx==npcx[nn] and selecty==npcy[nn] and throwdist<=0 and npccontrol[nn]==1): Attack()
                    if (npcstrangle[npclist[actionselect]]==0 and npcani[npclist[actionselect]]!="Fall" and npccontrol[nn]==1): npcdir[npclist[actionselect]]=1-npcdir[showDist2]
            if (npcani[nn]=="End Attack"):
                updating=2
                if (npcaniframe[nn]>3): npcaniframe[nn]-=.025
                else: npcaniframe[nn]-=.1
                if (npcaniframe[nn]<.1):
                    npcaniframe[nn]=0; npcani[nn]=""
                    if (npccontrol[nn]==0): nextTurn()
            if (npcani[nn]=="Hurt"):
                npcaniframe[nn]+=.5; updating=2
                if (npcaniframe[nn]>=4): npcaniframe[nn]=3.8; npcani[nn]="Get Up"
            if (npcani[nn]=="Get Up"):
                npcaniframe[nn]-=.1; updating=2
                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""
            if (npcani[nn]=="HurtBad"):
                npcaniframe[nn]+=.1; updating=2
                if (npcaniframe[nn]>=4 and npcfainted[nn]<=0 and npcdead[nn]==0): npcaniframe[nn]=3.8; npcani[nn]="UpSlow"; npcdir[nn]=1-npcdir[nn]
                if (npcdead[nn]==1): npcani[nn]="Fall"; npcdir[nn]=1-npcdir[nn]
            if (npcani[nn]=="Fall"):
                if (npcdead[nn]==0 or npcaniframe[nn]<3.8): npcaniframe[nn]+=.075; updating=2
                if (npcaniframe[nn]>=4 and npcdead[nn]==0): npcaniframe[nn]=3.8; npcani[nn]="Up"
            if (npcani[nn]=="Up"):
                npcaniframe[nn]-=.1; updating=2
                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""
            if (npcani[nn]=="UpSlow"):
                updating=2
                if (npcaniframe[nn]>3): npcaniframe[nn]-=.01
                else: npcaniframe[nn]-=.1
                if (npcaniframe[nn]<.1): npcaniframe[nn]=0; npcani[nn]=""; npcdir[nn]=1-npcdir[nn]
            if (npcani[nn]=="Strangling"):
                npcaniframe[nn]+=.1
                if (npcaniframe[nn]>=2.5): npcaniframe[nn]=2.5; npcani[nn]="StranglingBack"
            if (npcani[nn]=="StranglingBack"):
                npcaniframe[nn]-=.1
                if (npcaniframe[nn]<=.5): npcaniframe[nn]=.5; npcani[nn]="Strangling"
            if (npcani[nn]=="Strangled"):
                npcaniframe[nn]+=.1
                if (npcaniframe[nn]>=1.9): npcaniframe[nn]=1.9; npcani[nn]="StrangledBack"
            if (npcani[nn]=="StrangledBack"):
                npcaniframe[nn]-=.1
                if (npcaniframe[nn]<=.1): npcaniframe[nn]=.1; npcani[nn]="Strangled"
            if (npcani[nn]=="Hanging"):
                npcaniframe[nn]=3
            if (npcwalkdir[nn]>-1): #Walk Dir
                if (npcwalkdir[nn]==0 or npcwalkdir[nn]==3): ny=0
                if (npcwalkdir[nn]==1 or npcwalkdir[nn]==2): ny=si
            bered=0; #Flash Red from Hurt
            if ((npcpain[nn]>0 or npcbleeding[nn]>0) and showhurt<=5): bered=1
            if ((npcpain[nn]>4 or npcbleeding[nn]>4) and showhurt<=60 and showhurt>55): bered=1
            if ((npcpain[nn]>8 or npcbleeding[nn]>8) and showhurt<=30 and showhurt>25): bered=1
            if ((npcpain[nn]>12 or npcbleeding[nn]>12) and showhurt<=85 and showhurt>80): bered=1
            if (npcside[nn]=="Winston"): #Different Chars
                b=1
                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="HurtBad"): screen.blit(charwinston,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
            if (npcside[nn]=="Lenna"):
                b=1
                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="HurtBad"): screen.blit(charlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
            if (npcside[nn]=="Lucas"):
                b=1
                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="HurtBad"): screen.blit(charLucas,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
            if (npcside[nn]=="Floyd"):
                b=1
                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="HurtBad"): screen.blit(charfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
            if (npcside[nn]!="" and b==0):
                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="HurtBad"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
            if (npccontrol[nn]==1 and npcside[nn]!="Floyd" and npcside[nn]!="Winston" and npcside[nn]!="Lucas" and npcside[nn]!="Lenna"):
                if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charally,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                if (npcani[nn]=="HurtBad"): screen.blit(charelse,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))                
            if (bered==1 or npcdead[nn]==1):
                if (npcside[nn]!="" and npcside[nn]!="Lenna" and npcside[nn]!="Floyd"):
                    b=1
                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="HurtBad"): screen.blit(charhurt,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                if (npcside[nn]=="Lenna"):
                    b=1
                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="HurtBad"): screen.blit(hurtlenna,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
                if (npcside[nn]=="Floyd"):
                    b=1
                    if (npcwalk[nn]==0 and npcani[nn]==""): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), ((npcdir[nn]+1)*si,npcframe*si,si,si))
                    if (npcwalk[nn]>=1.0 and npcani[nn]==""): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380-mmx  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-mmy), (2*si+int(npcwalk[nn])*si,ny,si,si))
                    if (npcani[nn]=="Attack" or npcani[nn]=="End Attack"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*8,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Hurt" or npcani[nn]=="Get Up"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*10,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Fall" or npcani[nn]=="Up" or npcani[nn]=="UpSlow"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*12,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Strangling" or npcani[nn]=="StranglingBack" or npcani[nn]=="Hanging"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*14,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="Strangled" or npcani[nn]=="StrangledBack"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*16,int(npcaniframe[nn])*si,si,si))
                    if (npcani[nn]=="HurtBad"): screen.blit(hurtfloyd,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10), ((npcdir[nn])*si+si*18,int(npcaniframe[nn])*si,si,si))
            if (nn==whogoes and part==controlChar): #Cursor over NPC if is their turn
                screen.blit(message_ready,(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380+12  ,  -12-arrowyy+npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10))
                arrowyy=arrowyy-arrowdyy*fpsfix
                arrowdyy=arrowdyy+0.05*fpsfix
                if (arrowyy<0): arrowyy=0; arrowdyy=-1


whiteflash=0
whitedir=0
def Flash():
    global whiteflash, whitedir, part, selectx, selecty, waterWaveMax, updating, sky, fade, mlucas
    if (level=="Escape"):
        if (part!=15 and part!=38 and part!=45 and part!=46 and part!=47 and part!=49 and part!=50):
            if (whitedir==1): whitedir=0; whiteflash=0; waterWaveMax=5.0
        if (part==15):
            updating=1
            if (whitedir==0): whiteflash=whiteflash+10
            if (whitedir==1): whiteflash=whiteflash-5
            if (whiteflash>255):
                whiteflash=255; whitedir=1
                for n in range(lvlW*lvlH):
                    if (n%lvlW>2 and n%lvlW<18 and int(n/lvlW)>2 and int(n/lvlW)<28):
                        wallx[n]=0; wally[n]=0
                        tilex[n]=6; tiley[n]=0
                        selectx=12; selecty=17
                for n in range(11):
                    if (npcside[n]!="Winston" and npcside[n]!="Lucas"):
                        npc[n]=0
                for n in range(11):
                    bloodlen[n]=0
                for n in range(19):
                    item[n]=""
                waterWaveMax=100.0
            if (whiteflash<0): whiteflash=0
            if (waterWaveMax>5): waterWaveMax=waterWaveMax*.98
            if (waterWaveMax<5): waterWaveMax=5.0
            miscwhite.set_alpha(int(whiteflash))
            screen.blit(miscwhite,(0,0))
        if (part==38):
            updating=1
            if (whitedir==0): whiteflash=whiteflash+255
            if (whitedir==1): whiteflash=whiteflash-5
            if (whiteflash>255): whiteflash=255; whitedir=1
            miscwhite.set_alpha(int(whiteflash))
            screen.blit(miscwhite,(0,0))
            if (whiteflash<0): whiteflash=0
        if (part==45 or part==46 or part==47):
            updating=1
            if (whitedir==0): whiteflash=whiteflash+5; waterWaveMax=waterWaveMax*1.05+.01
            if (whitedir==1): whiteflash=whiteflash-2; waterWaveMax=waterWaveMax*.99-.2
            if (whiteflash>255):
                whiteflash=255; whitedir=1
                for n in range(lvlW*lvlH):
                    if (n%lvlW>2 and n%lvlW<18 and int(n/lvlW)>2 and int(n/lvlW)<28):
                        wallx[n]=0; wally[n]=0
                        tilex[n]=6; tiley[n]=1
                        selectx=12; selecty=17
                sky=pygame.image.load("Images/skyorange.png").convert_alpha()
            if (whiteflash<0): whiteflash=0
            if (waterWaveMax<5 and whitedir==1): waterWaveMax=5.0
            miscwhite.set_alpha(int(whiteflash))
            screen.blit(miscwhite,(0,0))
        if (part==49 or part==50):
            fade=fade+6*fpsfix
    if (level=="Summit"):
        if (part!=42 and part!=44 and part!=46 and part!=47):
            if (whitedir==1): whitedir=0; whiteflash=0
        if (part==42 or part==44):
            updating=1
            if (whitedir==0): whiteflash=whiteflash+10
            if (whitedir==1): whiteflash=whiteflash-5
            if (whiteflash>255):
                whiteflash=255; whitedir=1
                selectx=9
                selecty=9
                for n in range(11):
                    bloodlen[n]=0
            if (whiteflash<0): whiteflash=0
            miscwhite.set_alpha(int(whiteflash))
            screen.blit(miscwhite,(0,0))
        if (part==46 or part==47):
            updating=1
            if (whitedir==0): whiteflash=whiteflash+10
            if (whitedir==1): None
            if (whiteflash>255):
                whiteflash=255; whitedir=1
                selectx=9
                selecty=9
                for n in range(11):
                    bloodlen[n]=0
            if (whiteflash<0): whiteflash=0
            miscwhite.set_alpha(int(whiteflash))
            screen.blit(miscwhite,(0,0))
    if (level=="Device"):
        if (part!=32 and part!=33):
            if (whitedir==1): whitedir=0; whiteflash=0
        if (part==32 or part==33):
            updating=1
            if (whitedir==0): whiteflash=whiteflash+10
            if (whitedir==1): None
            if (whiteflash>255):
                whiteflash=255; whitedir=1
                selectx=8
                selecty=8
                for n in range(11):
                    bloodlen[n]=0
            if (whiteflash<0): whiteflash=0
            miscwhite.set_alpha(int(whiteflash))
            screen.blit(miscwhite,(0,0))    

endreset=0
def EndGame():
    global updating, mlucas, fade, endreset, mfloyd, mlenna, mend
    if (day==33):
        if (part==49 or part==50 or part==51):
            updating=2; endreset=1
            if (zooming==0): mlucas1=mlucas.copy(); mlucas1.fill((255,255,255,fade), None, pygame.BLEND_RGBA_MULT)
            if (zooming!=0): mlucas1=mlucas.copy(); mlucas1.fill((255,255,255,255), None, pygame.BLEND_RGBA_MULT)
            screen.blit(mlucas1,(WIDTH*.35,HEIGHT*.45))
    if (day==46):
        if (part==28 or part==29 or part==30):
            updating=2; endreset=1
            if (zooming==0): mfloyd1=mfloyd.copy(); mfloyd1.fill((255,255,255,fade), None, pygame.BLEND_RGBA_MULT)
            if (zooming!=0): mfloyd1=mfloyd.copy(); mfloyd1.fill((255,255,255,255), None, pygame.BLEND_RGBA_MULT)
            screen.blit(mfloyd1,(WIDTH*.35,HEIGHT*.45))
            fade=fade+6*fpsfix
    if (day==54):
        if (part==13 or part==14 or part==15):
            updating=2; endreset=1
            if (zooming==0): mlenna1=mlenna.copy(); mlenna1.fill((255,255,255,fade), None, pygame.BLEND_RGBA_MULT)
            if (zooming!=0): mlenna1=mlenna.copy(); mlenna1.fill((255,255,255,255), None, pygame.BLEND_RGBA_MULT)
            screen.blit(mlenna1,(WIDTH*.35,HEIGHT*.45))
            fade=fade+6*fpsfix
    if (day==62):
        if (part==37 or part==38 or part==39):
            updating=2; endreset=1
            if (zooming==0): mend1=mend.copy(); mend1.fill((255,255,255,fade), None, pygame.BLEND_RGBA_MULT)
            if (zooming!=0): mend1=mend.copy(); mend1.fill((255,255,255,255), None, pygame.BLEND_RGBA_MULT)
            screen.blit(mend1,(WIDTH*.35+50,HEIGHT*.45))
            fade=fade+6*fpsfix

def displayFade():
    global fade
    if (fade>0):
        if (level!="TrueEnd" or part>=10):
            fade-=5.0*fpsfix
        if (fade<0): fade=0
        misc.set_alpha(int(fade))
        screen.blit(misc,(0,0))
    if (fade>255): fade=255

delaycam=0
def selectCamera():
    global camerax, cameray, selectx, selecty, delay2, delay2b, delaycam, updating
    if (movie==0 and delaycam<=0 and actionmenu==0 and lvlingup==0 and lmquit==0):
        b=0
        if (up==1): selecty-=1; b=1
        if (down==1): selecty+=1; b=1
        if (left==1): selectx-=1; b=1
        if (right==1): selectx+=1; b=1
        if (b==1 and delay2b==1): delaycam=2
        if (b==1 and delay2b==0): delaycam=10; delay2b=1
    if (camerax!=selectx or cameray!=selecty):
        if (lagging==0):
            a=camerax-selectx
            b=cameray-selecty
            c=(a*a+b*b)**.5
            aa=math.acos(a/c)
            bb=math.asin(b/c)
            camerax=camerax-math.cos(aa)*c*1.5/20*fpsfix
            cameray=cameray-math.sin(bb)*c*1.5/20*fpsfix
            if (camerax<selectx+0.03 and camerax>selectx-0.03): camerax=selectx
            if (cameray<selecty+0.03 and cameray>selecty-0.03): cameray=selecty
        if (lagging!=0):
            camerax=selectx
            cameray=selecty
            updating=2
    if (lagging==0):
        if (selectx>lvlW-1): selectx=lvlW-1
        if (selecty>lvlH-1): selecty=lvlH-1
        if (selectx<0): selectx=0
        if (selecty<0): selecty=0
    if (lagging==1):
        if (selectx>lvlW): selectx=lvlW-1
        if (selecty>lvlH): selecty=lvlH-1
        if (selectx<1): selectx=0
        if (selecty<1): selecty=0
    if (delaycam>0): delaycam-=1

def displayTutorial():
    global tutorialmove, tutorialhurt, tutorialpick, tutorialthrow, tutorialarms
    if (tutorialmove==1):
        chat="Press [Enter] over a character on his or her turn"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+10+1)) #Display Text
        chat="to open the Action Menu. Move and Open the Door"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+30+1))
        chat="for the Guest."; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+50+1))
    if (tutorialhurt==1):
        chat="In the Action Menu, select Actions -> Attack ->"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+10+1)) #Display Text
        chat="Enemy to fight when near an enemy. [Enter] will"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+30+1))
        chat="also show a character's move radius."; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+50+1))
    if (tutorialpick==1):
        chat="Stand over a sparkling area and select [Pick Up]"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+10+1)) #Display Text
        chat="in the Action Menu to pick up items. Currently"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+30+1))
        chat="held items will be dropped automatically."; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+50+1))
    if (tutorialthrow==1):
        chat="Select [Throw] in the Action Menu to throw the"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+10+1)) #Display Text
        chat="currently held item. Try throwing the Bottle"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+30+1))
        chat="at a wall near Lenna to allow her to pick it up."; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+50+1))
    if (tutorialarms==1):
        chat="Attacking Hands or Arms may cause an enemy to"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+10+1)) #Display Text
        chat="drop his or her held weapon. Use this method"; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+30+1))
        chat="to aquire new weapons when needed."; text = font.render(chat, False, (255,255,255)); screen.blit(text, (150+12,480+50+1))
    screen.blit(message,(150,480))

event00=""
event0=""
event1=""
event2=""
event3=""
event4=""
eventclose=0
eventfade=160
def displayEvents():
    global event1, event2, event3, event4, tutorialmove, tutorialhurt, event0, event00, tutorialthrow, tutorialarms
    global eventfade
    #screen.blit(message,(150,480))
    if (event0!="" and tutorialthrow==1):
        tutorialthrow=0
    if (event0!="" or event00!="" and tutorialarms==1):
        tutorialarms=0
    if (event0=="" and event00!=""): event0=event00; event00=""
    if (event0!=""):
        tutorialmove=0; tutorialhurt=0
        event4=event3
        event3=event2
        event2=event1
        event1=event0
        event0=event00
        event00=""
    if (event1!="" and eventclose==0):
        if (eventfade>0): eventfade-=1
        screen.blit(menu_levelbottom2,(0,HEIGHT-160+eventfade))
        chat=event1; text = font.render(chat, False, (255,255,255)); screen.blit(text, (12,480+10+1)) #Display Text
        chat=event2; text = font.render(chat, False, (150,150,150)); screen.blit(text, (12,480+30+1))
        chat=event3; text = font.render(chat, False, (110,110,110)); screen.blit(text, (12,480+50+1))
        chat=event4; text = font.render(chat, False, (70,70,70)); screen.blit(text, (12,480+70+1))
    else:
        if (eventfade<160): eventfade+=1

choiceselect=0
def displayChat():
    global letters1, letters2, letters3, up, down, choiceselect
    global nextDialogue, textspeed, updating, pressed
    global arrowy, arrowdy, part, event1, event2, event3, event0, event4
    length1=len(chat1[part]); length2=len(chat2[part]); length3=len(chat3[part])
    if (letters1<length1): letters1=letters1+textspeed*fpsfix
    if (letters2<length2 and letters1>=length1): letters2=letters2+textspeed*fpsfix
    if (letters3<length3 and letters2>=length2): letters3=letters3+textspeed*fpsfix
    if (letters3>=length3-2 and letters2>=length2-2 and letters1>=length1-2):
        if (nextDialogue==0): nextDialogue=1
    else:
        if (letters1<length1 and letters1%4==0 and mute==0): dialogue.play()
        if (letters2<length2 and letters1>=length1 and letters2%4==0 and mute==0): dialogue.play()
        if (letters3<length3 and letters2>=length2 and letters3%4==0 and mute==0): dialogue.play()
    #else:
        #if (pressed==1): pressed=0; letters3=length3; letters2=length2; letters1=length1
    screen.blit(message,(150,480))
    chat=chat1[part]; text = font.render(chat[:int(letters1)], False, (255,255,255)); screen.blit(text, (150+12,480+10+1)) #Display Text
    chat=chat2[part]; text = font.render(chat[:int(letters2)], False, (255,255,255)); screen.blit(text, (150+12,480+30+1))
    chat=chat3[part]; text = font.render(chat[:int(letters3)], False, (255,255,255)); screen.blit(text, (150+12,480+50+1))
    event1=""; event2=""; event3=""; event0=""; event4=""
    if (speaker[part]!=""): #Display speakerer Name
        am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1
        if (speaker[part]!=" "): screen.blit(message_name,(150,480-35))
        chat=speaker[part]; text = font.render(chat, False, (255,255,255));
        if (speaker[part]=="Commander" or speaker[part]=="Experiment"): screen.blit(text, (150+12-6,480-35+7+1))
        else: screen.blit(text, (150+12,480-35+7+1))
        ty=-1
        if (speaker[part]=="Lenna"): ty=0
        if (speaker[part]=="Floyd"): ty=1
        if (speaker[part]=="Winston"): ty=2
        if (speaker[part]=="Lucas" or speaker[part]=="Lucifer"): ty=3
        #if (speaker[part]=="???"): ty=4
        if (ty>=0):
            screen.blit(message_portrait,(150+4,480-35-48),(0,48*ty,92,48))
        
    if (nextDialogue==1 and delay2<=0 and choice1[part]==""): #Display End Arrow
        screen.blit(message_ready,(625,535-arrowy))
        arrowy=arrowy-arrowdy*fpsfix
        arrowdy=arrowdy+0.04*fpsfix
        if (arrowy<0): arrowy=0; arrowdy=-1

    '''
    if (choice1[part]!=""): #Display Options
        if (my>HEIGHT/2-120 and my<HEIGHT/2-120+30 and mx>WIDTH/2-200 and mx<WIDTH/2+200): screen.blit(option_boxlight,(WIDTH/2-200,HEIGHT/2-120))
        else: screen.blit(option_box,(WIDTH/2-200,HEIGHT/2-120))
        text = font.render(choice1[part], False, (255,255,255)); screen.blit(text, (WIDTH/2-200+12,HEIGHT/2+7-120+1)) #Display Option Text
    if (choice2[part]!=""):
        if (my>HEIGHT/2-60 and my<HEIGHT/2-60+30 and mx>WIDTH/2-200 and mx<WIDTH/2+200): screen.blit(option_boxlight,(WIDTH/2-200,HEIGHT/2-60))
        else: screen.blit(option_box,(WIDTH/2-200,HEIGHT/2-60))
        text = font.render(choice2[part], False, (255,255,255)); screen.blit(text, (WIDTH/2-200+12,HEIGHT/2+7-60+1)) 
    if (choice3[part]!=""):
        if (my>HEIGHT/2 and my<HEIGHT/2+30 and mx>WIDTH/2-200 and mx<WIDTH/2+200): screen.blit(option_boxlight,(WIDTH/2-200,HEIGHT/2))
        else: screen.blit(option_box,(WIDTH/2-200,HEIGHT/2))
        text = font.render(choice3[part], False, (255,255,255)); screen.blit(text, (WIDTH/2-200+12,HEIGHT/2+7+1))'''
    if (choice1[part]!=""): #Display Options
        if (choiceselect==1): screen.blit(option_boxlight,(WIDTH/2-200,HEIGHT/2-120))
        else: screen.blit(option_box,(WIDTH/2-200,HEIGHT/2-120))
        text = font.render(choice1[part], False, (255,255,255)); screen.blit(text, (WIDTH/2-200+12,HEIGHT/2+7-120+1)) #Display Option Text
    if (choice2[part]!=""):
        if (choiceselect==2): screen.blit(option_boxlight,(WIDTH/2-200,HEIGHT/2-60))
        else: screen.blit(option_box,(WIDTH/2-200,HEIGHT/2-60))
        text = font.render(choice2[part], False, (255,255,255)); screen.blit(text, (WIDTH/2-200+12,HEIGHT/2+7-60+1)) 
    if (choice3[part]!=""):
        if (choiceselect==3): screen.blit(option_boxlight,(WIDTH/2-200,HEIGHT/2))
        else: screen.blit(option_box,(WIDTH/2-200,HEIGHT/2))
        text = font.render(choice3[part], False, (255,255,255)); screen.blit(text, (WIDTH/2-200+12,HEIGHT/2+7+1))
    if (choice1[part]!=""):
        #if (choice1[part]!="" and my>HEIGHT/2-120 and my<HEIGHT/2-120+30 and mx>WIDTH/2-200 and mx<WIDTH/2+200): part=choice1go[part]-1; nextMessage()
        #if (choice2[part]!="" and my>HEIGHT/2-60 and my<HEIGHT/2-60+30 and mx>WIDTH/2-200 and mx<WIDTH/2+200): part=choice2go[part]-1; nextMessage()
        #if (choice3[part]!="" and my>HEIGHT/2 and my<HEIGHT/2+30 and mx>WIDTH/2-200 and mx<WIDTH/2+200): part=choice3go[part]-1; nextMessage()
        if (pressed==1):
            if (choice1[part]!="" and choiceselect==1): part=choice1go[part]-1; choiceselect=0; nextMessage()
            if (choice2[part]!="" and choiceselect==2): part=choice2go[part]-1; choiceselect=0; nextMessage()
            if (choice3[part]!="" and choiceselect==3): part=choice3go[part]-1; choiceselect=0; nextMessage()
        if (choiceselect==0):
            if (up==1 and choiceselect==0 and choice3[part]==""): up=0; choiceselect=2
            if (up==1 and choiceselect==0 and choice3[part]!=""): up=0; choiceselect=3
            if (down==1 and choiceselect==0): down=0; choiceselect=1
        if (choiceselect!=0):
            if (up==1 and choiceselect>1): choiceselect-=1
            if (down==1 and choice3[part]=="" and choiceselect<2): choiceselect+=1
            if (down==1 and choice3[part]!="" and choiceselect<3): choiceselect+=1
        if (up==1): up=0
        if (down==1): down=0
    if (lagging!=0): updating=2
        
def nextMessage():
    global letters1, letters2, letters3
    global nextDialogue, textspeed, sky, moved, day, cansave
    global arrowy, arrowdy, part, level, zooming, nextLevelMenu, updating, delay2, loadedparty
    if (letters1<len(chat1[part]) or letters2<len(chat2[part]) or letters3<len(chat3[part])):
        return
    if (npcx[movenpc[part]]!=npcdx[movenpc[part]] or npcy[movenpc[part]]!=npcdy[movenpc[part]]):
        return
    letters1=0; letters2=0; letters3=0
    part+=1
    nextDialogue=0
    updating=2
    #if (level=="Ten" and part==40): day=4
    if (partdelay[part]>0): delay2=partdelay[part]
    if (gotopart[part]>-1): part=gotopart[part]
    if (part==changelevelpart and zooming==0): zooming=1; level=changelevelto; loadedparty=0
    if (part==changelevelpart and changelevelto=="LevelMenu"):
        zooming=1; level=""; nextLevelMenu=1; cansave=1
    if (musicplay[part]!=""):
        if (musicplay[part]=="threefour" and mute==0): threefour.play(-1)
        if (musicplay[part]=="action" and mute==0): action.play(-1)
        if (musicplay[part]=="ambient" and mute==0): ambient.play(-1)
        if (musicplay[part]=="calm" and mute==0): calm.play(-1)
        if (musicplay[part]=="guitar" and mute==0): guitar.play(-1)
        if (musicplay[part]=="mystery" and mute==0): mystery.play(-1)
        if (musicplay[part]=="ominous" and mute==0): ominous.play(-1)
        if (musicplay[part]=="scary" and mute==0): scary.play(-1)
        if (musicplay[part]=="standby" and mute==0): standby.play(-1)
        if (musicplay[part]=="crowd" and mute==0): crowd.play(-1)
        if (musicplay[part]=="water" and mute==0): water.play(-1)
        if (musicplay[part]=="rain" and mute==0): rain.play(-1)
        if (musicplay[part]=="None" and mute==0): pygame.mixer.fadeout(2200)
        musicplay[part]=""
        

sund=3.14; skyfade=0.0; skydir=0; loadinggame=0; mute=0
def displayMainMenu():
    global menuselect, mainmenu, menuy, pressed, mainLoop, fade, updating, updatefix, sund, fade, skyfade, skydir
    global up,down,left,right, zooming, level, nextLevelMenu, endreset, day, loadinggame, mute
    global kurt, frederick, ruth, twins, matthew, Dinah, gamble, extra, lucas, floyd, lenna, lucas2, floyd2, lenna2
    dist=200
    a=abs(menuy-menuselect*dist)**.7
    if (menuy>menuselect*dist-1 and menuy<menuselect*dist+1): menuy=menuselect*dist
    if (menuy<menuselect*dist): menuy+=a
    if (menuy>menuselect*dist): menuy-=a
    if (down==1 and menuselect<3 and menuy%dist==0): menuselect+=1
    if (up==1 and menuselect>0 and menuy%dist==0): menuselect-=1
    if (menuselect==0 and os.path.exists("Images/Save.txt")==False): menuselect=1
    if (pressed==1 and menuy==menuselect*dist): #Enter Pressed on Menu
        pressed=0
        if (menuselect==0): zooming=1; mainmenu=0; nextLevelMenu=1; loadinggame=1; pygame.mixer.fadeout(2200); loadGame()
        if (menuselect==1):
            kurt=0; frederick=0; ruth=0; twins=0; matthew=0; Dinah=0; gamble=0; extra=0
            lucas=0; floyd=0; lenna=0; lucas2=0; floyd2=0; lenna2=0
            zooming=1; mainmenu=0; nextLevelMenu=1; day=-2; day=1; pygame.mixer.fadeout(2200) #day=22 (The Decision)
            endreset=1; resetNPCs(); endreset=0 #New
        if (menuselect==3): mainLoop=False #Quit
        if (menuselect==2):
            mute=1-mute #Mute
            if (mute==0): ambient.play(-1)
            if (mute==1): pygame.mixer.fadeout(2200)
        #if (menuselect==3): return #Options
        #if (menuselect==4): mainLoop=False #Quit
    for n in range(3):
        if (goingColor[n]==gotoColor[n]): gotoColor[n]=random.randint(0,255)
        if (goingColor[n]<gotoColor[n]): goingColor[n]+=1
        if (goingColor[n]>gotoColor[n]): goingColor[n]-=1
        
    if (sund>=3.14): #Moving Sun
        skyora.set_alpha(skyfade)
        screen.blit(skyora,(0,0))
        screen.blit(sun,(WIDTH/2.0+sin(sund+3.14/2*3)*500-100,HEIGHT/2.0+cos(sund+3.14/2*3)*300-100+100))
    else:
        skyblu.set_alpha(skyfade)
        screen.blit(skyblu,(0,0))
        screen.blit(moon,(WIDTH/2.0+sin(sund+3.14/2*3+3.14)*500-100,HEIGHT/2.0+cos(sund+3.14/2*3+3.14)*300-100+100))
    #screen.blit(titlefinal,(0,0))
    sund=sund+.0123*.5
    if (skydir==0): skyfade+=1
    if (skydir==1): skyfade-=1
    if (skyfade>=255 and skydir==0): skydir=1
    if (skyfade<=0 and skydir==1): skydir=0
    if (sund>=3.1415*2): sund=0.0; skyfade=0.0; skydir


    
    sx=255; sy=60
    menuyy=-menuy #Display Menu Text
    screen.blit(mcontinue,(WIDTH*.2,menuyy+HEIGHT*.45)); menuyy+=dist
    screen.blit(mnew,(WIDTH*.2,menuyy+HEIGHT*.45)); menuyy+=dist
    #screen.blit(mfreebattle,(WIDTH*.2,menuyy+HEIGHT*.45)); menuyy+=dist
    #screen.blit(moptions,(WIDTH*.2,menuyy+HEIGHT*.45)); menuyy+=dist
    screen.blit(mmute,(WIDTH*.2,menuyy+HEIGHT*.45)); menuyy+=dist
    screen.blit(mquit,(WIDTH*.2,menuyy+HEIGHT*.45)); menuyy+=dist

    mline11=mline1.copy(); mline11.fill((goingColor[0],goingColor[1],goingColor[2],255), None, pygame.BLEND_RGBA_MULT)
    mline22=mline2.copy(); mline22.fill((goingColor[0],goingColor[1],goingColor[2],255), None, pygame.BLEND_RGBA_MULT)
    for n in range(5): #Display Menu Lines
        screen.blit(mline11,(n*225,HEIGHT*.45))
        screen.blit(mline22,(n*225,HEIGHT*.45+45))

    if (mute==0): screen.blit(speakeri,(10,10)) #Speaker Image
    else: screen.blit(speakerx,(10,10))
    
    if (endreset==1):
        resetNPCs()
        endreset=0

alphafail=0
def Failure():
    global updating, alphafail, pressed, zooming, mainmenu, menuselect, level, day, oldchapter, onface, gainparty, matthew, gamble, loadedparty
    global actionalready, movedalready, lucastwo, jerry
    global lenna2, floyd2, lucas2,gainparty
    if (alphafail<255): alphafail+=1
    updating=2; gainparty=""
    for n in range(3):
        if (goingColor[n]==gotoColor[n]): gotoColor[n]=random.randint(0,255)
        if (goingColor[n]<gotoColor[n]): goingColor[n]+=1
        if (goingColor[n]>gotoColor[n]): goingColor[n]-=1
    mfailure1=mfailure.copy(); mfailure1.fill((255,255,255,alphafail), None, pygame.BLEND_RGBA_MULT) #Failure Text
    screen.blit(mfailure1,(WIDTH*.2,0+HEIGHT*.45))
    mline11=mline1.copy(); mline11.fill((goingColor[0],goingColor[1],goingColor[2],alphafail), None, pygame.BLEND_RGBA_MULT)
    mline22=mline2.copy(); mline22.fill((goingColor[0],goingColor[1],goingColor[2],alphafail), None, pygame.BLEND_RGBA_MULT)
    for n in range(5): 
        screen.blit(mline11,(n*225,HEIGHT*.45))
        screen.blit(mline22,(n*225,HEIGHT*.45+45))
    if (pressed==1 and alphafail>250): #Failure Text to Menu
        onface=0
        if (level!="Matthew" and level!="Gamble" and level!="Jerry2" and level!="Speechless" and level!="Confusion" and level!="Robot"): day-=1
        if ((level=="Confusion" or level=="Speechless") and floyd2==1 and lucas2==1 and lenna2==1): day-=1
        if (level=="Matthew"): gainparty=""; matthew=0
        if (level=="Gamble"): gainparty=""; gamble=0
        if (level=="Jerry2"): gainparty=""; jerry=0
        if (level=="Speechless"): lenna2=0
        if (level=="Confusion"): lucas2=0
        if (level=="Robot"): twins=2
        pressed=0; alphafail=1; chapter=oldchapter
        zooming=1
        resetNPCs()
        level="LevelMenu"
        mainmenu=1; menuselect=0; loadedparty=0; actionalready=0; movedalready=0; lucastwo=0
        

def optionOpen():
    if (level=="Truth"): return
    a=int(npcx[showDist2])+int(npcy[showDist2])*lvlW #Open/Close Doors
    if (wallx[a]>=5): wally[a]=1-wally[a]
    if (wallx[a+1]>=5 and walldir[a+1]==0): wally[a+1]=1-wally[a+1]
    if (wallx[a-1]>=5 and walldir[a-1]==3): wally[a-1]=1-wally[a-1]
    if (wallx[a+lvlW]>=5 and walldir[a+lvlW]==1): wally[a+lvlW]=1-wally[a+lvlW]
    if (wallx[a-lvlW]>=5 and walldir[a-lvlW]==2): wally[a-lvlW]=1-wally[a-lvlW]
    if (mute==0): door.play()

def npcEffects():
    global event0, event00, skipped
    for n in range(11):
        if (npcknocked[n]==1 and npcpain[n]>=8 and npcfainted[n]<=0 and npcdead[n]==0): event00=npcside[n]+" was knocked out!"; npcknocked[n]=0; npcfainted[n]+=3; npcpain[n]=9
        if (npcknocked[n]==1): npcknocked[n]=0
        if (npcfainted[n]>0 and npcstrangle[n]==0 and npcani[n]!="Hanging"): npcani[n]="Fall"; npcstrangle[npcstrangling[n]]=0
        if (npcfainted[n]>0 and npcstrangle[n]==2 and npcani[n]!="Fall"): npcani[n]="Fall"; npcstrangle[npcstrangling[n]]=0
        if (npcfainted[n]>0 and npcstrangle[n]==1): npcani[n]="Hanging"
        if (npcani[n]=="Hanging" and npcstrangle[n]!=1): npcani[n]="Fall"; npcaniframe[n]=0
        if (npcfainted[n]<=0):
            if (npcstrangle[n]==1 and npcani[n]!="StranglingBack"): npcani[n]="Strangling" #Being Strangled
            if (npcstrangle[n]==2 and npcani[n]!="StrangledBack"): npcani[n]="Strangled" #Strangling
        if (npcstrangle[n]==0 and (npcani[n]=="Strangling" or npcani[n]=="Strangled")): npcani[n]=""
        if (npcstrangle[n]==1 and npccontrol[n]==0 and delay2<=0 and whogoes==n): skipped=0; nextTurn()
        if (npcstrangle[n]==2 and (npcfainted[n]>0 or npcdead[n]==1) and (npcani[n]=="Strangled" or npcani[n]=="StrangledBack")): npcstrangle[n]=0; npcstrangle[npcstrangling[n]]=0
        if (npcstrangle[n]==2 and npcstrangle[npcstrangling[n]]==0): npcstrangle[n]=0
        if (npcstrangle[n]==2 and npccontrol[n]==0 and n==whogoes and selectx==camerax and selecty==cameray): skipped=0; nextTurn()
        if (npcani[n]=="" and npcdead[n]==1): npcani[n]="Fall"
        if (npcbrain[n]==2): npcdead[n]=1 #Brain
        if (npcneck[n]==3): npcdead[n]=1 #Neck
        if (npclungs[n]==2): npcinternal[n]=2; npclungs[n]=3; event00=npcside[n]+" can't breathe!"
        if (npcheart[n]==2): npcinternal[n]=2; npcheart[n]=3; event00=npcside[n]+"'s heart is failing!"
        if (npcheart[n]>=2): npcbleeding[n]=12

skipped=0
def nextTurn():
    global movedalready, actionalready, turn, whogoes, selectx, selecty, actionmenu, showskillsgoes, delay4
    global delay2, am_action, showDist, showDist2, event0, event00, throwdist, npcdist, doored, lvlingup, skipped, npcdist, shortmove
    if (npcexp[whogoes]>=100): lvlingup=1; return
    if (skipped==1): return
    #if (npccontrol[whogoes]==0 and (camerax!=selectx or cameray!=selecty)): return
    skipped=1;
    if (npccontrol[whogoes]==0): delay4=60
    movedalready=0; actionalready=0; actionmenu=0; delay2=60; am_action=0; showDist=-1; showDist2=-1; shortmove=0
    n=whogoes #Stat Changes at End of Turn
    b=0
    for nn in range(lvlW*lvlH):
        tilefill[nn]=0
    if (npcdead[n]==0):
        if (npcbreath[n]==1 or npcstrangle[n]==1 or npcthroat[n]==2 or npclungs[n]>=2): npcoxygen[n]-=40
        if (npcbreath[n]==0 and npcstrangle[n]!=1 and npcthroat[n]!=2 and npclungs[n]<=1): npcoxygen[n]+=40-npclungs[n]*20
        if (npcoxygen[n]>100): npcoxygen[n]=100
        if (npcoxygen[n]<=20): npcdizzy[n]+=2
        if (npcoxygen[n]<=0):
            npcfainted[n]+=3; npcbreath[n]=0; event00=npcside[n]+" faints from a lack of oxygen." #Pain
            npcdx[n]=npcx[n]; npcdy[n]=npcy[n]
        if (npcoxygen[n]<=-40): npcdead[n]=1; event00=npcside[n]+" suffocates."
        if (npcdizzy[n]>0): npcdizzy[n]-=1
        if (npcpain[n]>0): npcpain[n]-=1
        if (npcfainted[n]>0): npcpain[n]-=1
        if (npcbleeding[n]>5): npcblood[n]-=npcbleeding[n]
        if (npcbleeding[n]>0): npcbleeding[n]-=2
        if (npcblood[n]<70 and npcblood[n]>=60): npcdizzy[n]+=1
        #if (npcblood[n]<60 and npcblood[n]>=30 and npcfainted[n]>0 and selectx==camerax and selecty==cameray): nextTurn()
        if (npcblood[n]<30): npcdead[n]=1; event00=npcside[n]+" bleeds out."
        if (npcrunaway[n]>0):
            npcrunaway[n]-=1
            if (npcrunaway[n]==0): npcrunaway[n]=-1
    npcturn[whogoes]+=10; turn+=1
    if (npcdead[whogoes]==1): npcturn[whogoes]+=10; turn+=1
    low=10000
    for nn in range(11):
        if (npcturn[nn]<low and npc[nn]==1 and npcdead[nn]==0): low=npcturn[nn]
    for nn in range(11):
        if (npcturn[nn]==low and npc[nn]==1 and npcdead[nn]==0):
            whogoes=nn;
            selectx=npcx[nn]; selecty=npcy[nn]
            break
    #New NPC now going
    n=whogoes; throwdist=0; doored=0; showskillsgoes=0 
    if (npcfainted[n]>0): npcfainted[n]-=1
    if (npcfainted[n]>0 and npccontrol[n]==0): skipped=0; nextTurn()
    if (npcstun[n]>0): npcstun[n]-=1; event00=npcside[n]+" is stunned!"; npcani[n]="Fall"; skipped=0; nextTurn()
    if (npcblood[n]<60 and npcblood[n]>=30 and npcfainted[n]<=0 and npcani[n]==""):
        npcfainted[n]=2; npcbreath[n]=0; event00=npcside[n]+" faints from a loss of blood!"
        if (npccontrol[n]==0): skipped=0; nextTurn() #Pain
    if (npcpain[n]>=10 and npcfainted[n]<=0 and npcdead[n]==0):
        npcfainted[n]=2; npcbreath[n]=0; event00=npcside[n]+" faints from the pain!" #Pain
        if (npccontrol[n]==0): skipped=0; nextTurn()

BLUE=(0,160,230)
DARKBLUE=(80,90,220)
YELLOW=(255,240,0)
ORANGE=(255,110,20)
RED=(255,0,0)
PINK=(255,140,200)
GREEN=(20,205,20)
showskills=1
showskillsgoes=0
def displayStatsMenu():
    global actionmenu, showDist2, showDist, showskills
    n=0; mcy=0
    if (mmx!=0 or mmy!=0): mcy=50
    screen.blit(menu_stats,(230+230,220-45-mcy))
    text=font.render(npcside[showDist2]+" ",1,WHITE) #Npc name
    screen.blit(text,(230+238,220-40+20*n-mcy))
    text=font2.render("Lvl "+str(npclvl[showDist2]),1,WHITE) #Lvl Show
    screen.blit(text,(230+238+160-5,220-40+20*n-mcy+3+1)); n+=1
    text=font2.render("Holding: "+str(npcheld[showDist2]),1,WHITE)
    screen.blit(text,(230+238,220-34+12*n-mcy)); n+=1
    if (whogoes!=showDist2 and (showskills==1 or lvlingup>=1)): showLvls()
    if (whogoes==showDist2 and showskillsgoes==1): showLvls()
    if (lvlingup==0 and whogoes!=showDist2):
        if (showskills==1):
            text=font2.render("Hide(s)",1,WHITE) #Show/Hide
            screen.blit(text,(80+5+205,220-45+5+5))
        if (showskills==0):
            text=font2.render("Show(s)",1,WHITE) #Show/Hide
            screen.blit(text,(230+238+140+2,220-34+12*(n-1)-mcy))
    if (lvlingup==0 and whogoes==showDist2):
        if (showskillsgoes==1):
            text=font2.render("Hide(s)",1,WHITE) #Show/Hide
            screen.blit(text,(80+5+205,220-45+5+5))
        if (showskillsgoes==0):
            text=font2.render("Show(s)",1,WHITE) #Show/Hide
            screen.blit(text,(230+238+140+2,220-34+12*(n-1)-mcy))
    n+=1; sd=showDist2
    if (mmx!=0 or mmy!=0): n=n-5
    if (npcbleeding[sd]>0 and npcbleeding[sd]<6): #Bleeding
        text=font2.render("Some Bleeding",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcbleeding[sd]>=6 and npcbleeding[sd]<12):
        text=font2.render("Moderate Bleeding",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcbleeding[sd]>=12):
        text=font2.render("Heavy Bleeding",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcblood[sd]<95 and npcblood[sd]>85):
        text=font2.render("Some Blood Loss",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcblood[sd]<=85 and npcblood[sd]>60):
        text=font2.render("Moderate Blood Loss",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcblood[sd]<=60):
        text=font2.render("Heavy Blood Loss",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcartery[sd]==1): #Internal
        text=font2.render("Severed Artery",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcartery[sd]>=2):
        text=font2.render("Severed Arteries",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcinternal[sd]>=1):
        text=font2.render("Internal Bleeding",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcdead[sd]==0):
        if (npcpain[sd]>0 and npcpain[sd]<4): #Pain
            text=font2.render("Some Pain",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcpain[sd]>=4 and npcpain[sd]<7):
            text=font2.render("Moderate Pain",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcpain[sd]>=7):
            text=font2.render("Intense Pain",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npceyes[sd]==3): #Blindness 
            text=font2.render("Partially Blind",1,BLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1     
        if (npceyes[sd]==4):
            text=font2.render("Blind",1,BLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1            
        if (npcstrangle[sd]==1): #Strangle
            text=font2.render("Being Strangled",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcstrangle[sd]==2):
            text=font2.render("Strangling",1,BLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcbreath[sd]==1): #Breath
            text=font2.render("Holding Breath",1,BLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcthroat[sd]==2 or npclungs[sd]>=2):
            text=font2.render("Unable to Breathe",1,BLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcdizzy[sd]>0): #Dizzy
            text=font2.render("Dizzy",1,DARKBLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcoxygen[sd]<100 and npcoxygen[sd]>50): #Oxygen
            text=font2.render("Low Oxygen",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcoxygen[sd]<=50 and npcoxygen[sd]>0):
            text=font2.render("Very Low Oxygen",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcoxygen[sd]<=0):
            text=font2.render("No Oxygen",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcgut[sd]>1 or npcgut2[sd]>1): #Nauseous
            text=font2.render("Nauseated",1,GREEN); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcpara[sd]>0): #Paralyzed
            text=font2.render("Paralyzed",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcfainted[sd]>0): #Fainted
            text=font2.render("Fainted",1,PINK); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcstun[sd]>0): #Stunned
            text=font2.render("Stunned",1,BLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcdead[sd]==1):
        text=font2.render("Dead",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
        if (npcoxygen[sd]<=0): #Strangled and Dead
            text=font2.render("Suffocated",1,BLUE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    n+=1; maxn=18
    if (npcforehead[sd]==1 and n<maxn): #Forehead and Skull and Brain
        text=font2.render("Bruised Forehead",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcforehead[sd]==2 and n<maxn):
        text=font2.render("Cut Forehead",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcskull[sd]==1 and n<maxn):
        text=font2.render("Cracked Skull",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcskull[sd]==2 and n<maxn):
        text=font2.render("Shattered Skull",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcbrain[sd]==1 and n<maxn):
        text=font2.render("Hurt Brain",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcbrain[sd]==2 and n<maxn):
        text=font2.render("Torn Brain",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcneck[sd]==1 and n<maxn): #Neck
        text=font2.render("Bruised Neck",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcneck[sd]==2 and n<maxn):
        text=font2.render("Chipped Neck",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcneck[sd]==3 and n<maxn):
        text=font2.render("Snapped Neck",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcneck[sd]==4 and n<maxn):
        text=font2.render("Fractured Neck",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1   
    if (npceyes[sd]==1 and n<maxn): #Eyes
        text=font2.render("Bruised Eyes",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npceyes[sd]==2 and n<maxn):
        text=font2.render("Cut Eyes",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcnose[sd]==1 and n<maxn): #Nose
        text=font2.render("Bruised Nose",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcnose[sd]==2 and n<maxn):
        text=font2.render("Battered Nose",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcnose[sd]==3 and n<maxn):
        text=font2.render("Shattered Nose",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcnose2[sd]==1 and n<maxn):
        text=font2.render("Cut Nose",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcnose2[sd]==2 and n<maxn):
        text=font2.render("Cut Nose",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcnose2[sd]==3 and n<maxn):
        text=font2.render("Cut Nose",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcmouth[sd]==1 and n<maxn): #Mouth
        text=font2.render("Cut Mouth",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcmouth[sd]==2 and n<maxn):
        text=font2.render("Cut Mouth",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcmouth[sd]==3 and n<maxn):
        text=font2.render("Torn Mouth",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcjaw[sd]==1 and n<maxn):
        text=font2.render("Bruised Mouth",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcjaw[sd]==2 and n<maxn):
        text=font2.render("Chipped Jaw",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcjaw[sd]==3 and n<maxn):
        text=font2.render("Shattered Jaw",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npctemple[sd]==1 and n<maxn): #Temple
        text=font2.render("Bruised Temple",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npctemple[sd]==2 and n<maxn):
        text=font2.render("Cut Temple",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npctemple[sd]==3 and n<maxn):
        text=font2.render("Torn Temple",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcthroat[sd]==1 and n<maxn): #Throat
        text=font2.render("Cut Throat",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcthroat[sd]==2 and n<maxn):
        text=font2.render("Severed Throat",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if ((npceyes[sd]==3 or npceyes[sd]==4) and n<maxn):
        text=font2.render("Torn Eyes",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcchest[sd]==1 and n<maxn): #Chest
        text=font2.render("Bruised Chest",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcchest[sd]==2 and n<maxn):
        text=font2.render("Bruised Ribs",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcchest[sd]==3 and n<maxn):
        text=font2.render("Broken Ribs",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcchest2[sd]==1 and n<maxn):
        text=font2.render("Cut Chest",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcchest2[sd]==2 and n<maxn):
        text=font2.render("Cut Chest",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcchest2[sd]==3 and n<maxn):
        text=font2.render("Gashed Chest",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclungs[sd]==1 and n<maxn): #Lungs
        text=font2.render("Punctured Lung",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclungs[sd]>=2 and n<maxn):
        text=font2.render("Mortally Wounded Lungs",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcheart[sd]==1 and n<maxn): #Heart
        text=font2.render("Pierced Heart",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcheart[sd]>=2 and n<maxn):
        text=font2.render("Mortally Wounded Heart",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcgut[sd]==1 and n<maxn): #Gut
        text=font2.render("Bruised Gut",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcgut[sd]==2 and n<maxn):
        text=font2.render("Battered Gut",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcgut[sd]==3 and n<maxn):
        text=font2.render("Battered Gut",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcgut2[sd]==1 and n<maxn):
        text=font2.render("Cut Gut",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcgut2[sd]==2 and n<maxn):
        text=font2.render("Gashed Gut",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcgut2[sd]==3 and n<maxn):
        text=font2.render("Torn Gut",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcback[sd]==1 and n<maxn): #Back/Spine
        text=font2.render("Bruised Back",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcback[sd]==2 and n<maxn):
        text=font2.render("Cut Back",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcback[sd]==3 and n<maxn):
        text=font2.render("Battered Back",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcback[sd]==4 and n<maxn):
        text=font2.render("Gashed Back",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcback[sd]==5 and n<maxn):
        text=font2.render("Battered Back",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcback[sd]==6 and n<maxn):
        text=font2.render("Gashed Back",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcspine[sd]==1 and n<maxn):
        text=font2.render("Fractured Spine",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcspine[sd]==2 and n<maxn):
        text=font2.render("Severed Spine",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightarm[sd]==1 and n<maxn): #Right Arm
        text=font2.render("Bruised Right Arm",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightarm[sd]==2 and n<maxn):
        text=font2.render("Cut Right Arm",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightarm[sd]==3 and n<maxn):
        text=font2.render("Battered Right Arm",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightarm[sd]==4 and n<maxn):
        text=font2.render("Gashed Right Arm",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightarm[sd]==5 and n<maxn):
        text=font2.render("Broken Right Arm",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightarm[sd]==6 and n<maxn):
        text=font2.render("Severed Right Arm",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrighthand[sd]==1 and n<maxn): #Right Hand
        text=font2.render("Bruised Right Hand",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrighthand[sd]==2 and n<maxn):
        text=font2.render("Cut Right Hand",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrighthand[sd]==3 and n<maxn):
        text=font2.render("Battered Right Hand",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrighthand[sd]==4 and n<maxn):
        text=font2.render("Gashed Right Hand",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrighthand[sd]==5 and n<maxn):
        text=font2.render("Broken Right Hand",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrighthand[sd]==6 and n<maxn):
        text=font2.render("Severed Right Hand",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftarm[sd]==1 and n<maxn): #Left Arm
        text=font2.render("Bruised Left Arm",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftarm[sd]==2 and n<maxn):
        text=font2.render("Cut Left Arm",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftarm[sd]==3 and n<maxn):
        text=font2.render("Battered Left Arm",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftarm[sd]==4 and n<maxn):
        text=font2.render("Gashed Left Arm",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftarm[sd]==5 and n<maxn):
        text=font2.render("Broken Left Arm",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftarm[sd]==6 and n<maxn):
        text=font2.render("Severed Left Arm",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclefthand[sd]==1 and n<maxn): #Left Hand
        text=font2.render("Bruised Left Hand",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclefthand[sd]==2 and n<maxn):
        text=font2.render("Cut Left Hand",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclefthand[sd]==3 and n<maxn):
        text=font2.render("Battered Left Hand",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclefthand[sd]==4 and n<maxn):
        text=font2.render("Gashed Left Hand",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclefthand[sd]==5 and n<maxn):
        text=font2.render("Broken Left Hand",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npclefthand[sd]==6 and n<maxn):
        text=font2.render("Severed Left Hand",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightleg[sd]==1 and n<maxn): #Legs
        text=font2.render("Bruised Right Leg",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightleg[sd]==2 and n<maxn):
        text=font2.render("Cut Right Leg",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightleg[sd]==3 and n<maxn):
        text=font2.render("Battered Right Leg",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightleg[sd]==4 and n<maxn):
        text=font2.render("Gashed Right Leg",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightleg[sd]==5 and n<maxn):
        text=font2.render("Broken Right Leg",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcrightleg[sd]==6 and n<maxn):
        text=font2.render("Severed Right Leg",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftleg[sd]==1 and n<maxn):
        text=font2.render("Bruised Left Leg",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftleg[sd]==2 and n<maxn):
        text=font2.render("Cut Left Leg",1,YELLOW); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftleg[sd]==3 and n<maxn):
        text=font2.render("Battered Left Leg",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftleg[sd]==4 and n<maxn):
        text=font2.render("Gashed Left Leg",1,ORANGE); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftleg[sd]==5 and n<maxn):
        text=font2.render("Broken Left Leg",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (npcleftleg[sd]==6 and n<maxn):
        text=font2.render("Severed Left Leg",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (n>=maxn):
        text=font2.render("And More",1,RED); screen.blit(text,(230+238,220-34+12*n)); n+=1
    if (selectx!=npcx[showDist2] or selecty!=npcy[showDist2]):
        actionmenu=0; showDist2=-1; showDist=-1

bp1=0
bp2=0
hit=0
def AttSave(bp1a,bp2a,hita):
    global bp1, bp2, hit
    bp1=bp1a; bp2=bp2a; hit=hita
    if (hit<0): hit=whogoes
    if (actionselect==0 and npccontrol[whogoes]==1 and thrown==""):
        npcani[whogoes]="Hurt"
        if (thrown==""): Attack()
    else: npcani[whogoes]="Attack"


def Attack():
    global bp1, bp2, hit
    global actionalready, bodymenu, showDist, showDist2, updating, am_actions, showPaths, actionselect, bodyselect, openbody, bodymenu
    global event0, event00, whichblood, throwdam, thrown
    dam=0
    if (thrown!=""): npcheld[whogoes]=thrown
    if (npcheld[whogoes]==""):
        dam=random.randint(1,2); damtype="Hit";
        if (mute==0): fist.play() #Weapon Damage
    if (npcheld[whogoes]=="Hammer"):
        dam=random.randint(5,10); damtype="Hit";
        if (mute==0):thud.play()
    if (npcheld[whogoes]=="Wrench"):
        dam=random.randint(4,8); damtype="Hit";
        if (mute==0):thud.play()
    if (npcheld[whogoes]=="Baton"):
        dam=random.randint(3,6); damtype="Hit";
        if (mute==0):punch.play()
    if (npcheld[whogoes]=="Bottle"):
        dam=10; damtype="Hit";
        if (mute==0):shatter.play()
    if (npcheld[whogoes]=="Dice"):
        dam=random.randint(1,10); damtype="Hit";
        if (mute==0):punch.play()
    if (npcheld[whogoes]=="Cards"):
        dam=random.randint(2,4); damtype="Pierce";
        if (mute==0):slash.play()
    if (npcheld[whogoes]=="Med Kit"):
        dam=random.randint(1,2); damtype="Hit";
        if (mute==0):punch.play()
    if (npcheld[whogoes]=="Glass"):
        dam=random.randint(3,7); damtype="Pierce";
        if (mute==0):slash.play()
    if (npcheld[whogoes]=="Shiv"):
        dam=random.randint(4,8); damtype="Pierce";
        if (mute==0):slash.play()
    if (npcheld[whogoes]=="Pencil"):
        dam=random.randint(1,2); damtype="Pierce";
        if (mute==0):slash.play()
    if (npcheld[whogoes]=="Scissors"):
        dam=random.randint(3,5); damtype="Pierce";
        if (mute==0):slash.play()
    if (npcheld[whogoes]=="Knife"):
        dam=random.randint(5,10); damtype="Pierce";
        if (mute==0):slash.play()
    if (thrown!="" and npcheld[whogoes]=="Cards"): dam=random.randint(3,4); damtype="Pierce"; slash.play()
    if ((npcrighthand[whogoes]<=4 and npcrightarm[whogoes]<=4) or (npclefthand[whogoes]<=4 and npcleftarm[whogoes]<=4)): None
    else: dam=int(dam/2)
    hap=""; strong=0
    damc=random.randint(0,10)
    dam=int(dam+.3*(npcpain[hit]+npcbleeding[hit]))
    if (bp1==2 and bp2==4 and npcheld[whogoes]==""): dam=dam+4
    if (damtype=="Pierce"): #Pierce Skill
        dam=int(dam+npcpierces[whogoes]/4.0+npclvl[whogoes]/8.0)
    if (damtype=="Hit" and npcheld[whogoes]!=""): #Blunt Skill
        dam=int(dam+npcblunt[whogoes]/4.0+npclvl[whogoes]/8.0)
    if (npcheld[whogoes]==""): #Unarmed Skill
        dam=dam+int(npcunarmed[whogoes]/4.0+npclvl[whogoes]/8.0)
    if (throwdam==1): #Throw Skill
        dam=dam+int(npcthrowsk[whogoes]/4.0+npclvl[whogoes]/8.0)
    if (True): #Defense Skill
        if (npccontrol[hit]==1): dam=dam-int(npcdefense[hit]/4.0+npclvl[hit]/8.0)
        if (npccontrol[hit]==0): dam=dam-int(npcdefense[hit]/4.0+npclvl[hit]/8.0)
    if (npcrighthand[whogoes]>4 or npcrightarm[whogoes]>4 or npclefthand[whogoes]>4 or npcleftarm[whogoes]>4): #Broken Arms
        dam=int(dam/2)
    if ((npcrighthand[whogoes]>4 or npcrightarm[whogoes]>4) and (npclefthand[whogoes]>4 or npcleftarm[whogoes]>4)):
        dam=1
    if (throwdam==1): dam=dam+int(throwdist)*.3
    if (npcfainted[hit]>0): dam=dam+5
    if (dam>10): dam=10
    if (damc<dam): strong=1
    if ((damc==dam or (damc==dam+1 and dam>7) or (damc==dam+2 and dam>9)) and dam>5): strong=2
    if (bp1==2 and dam>8): strong=2
    if (dam>=10): strong=2
    miss=10; b=0; drop=0
    if (npceyes[whogoes]==1 or npceyes[whogoes]==2): miss=random.randint(4,10)
    if (npceyes[whogoes]==3): miss=random.randint(3,10)
    if (npceyes[whogoes]==4): miss=random.randint(2,10)
    if (throwdist>0): miss=10
        
    if (miss>=5):
        if (bp1==0):
            if (bp2==1):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=2; hap="bruising it."
                    if (strong==0 and npcforehead[hit]==0): npcforehead[hit]=1
                    if (strong==1):
                        npcpain[hit]+=5; hap="cracking the skull!"
                        aa=random.randint(0,2)
                        if (aa==0): npcknocked[hit]=1; npcpain[hit]=10
                    if (strong==1 and npcskull[hit]==0): npcforehead[hit]=1; npcskull[hit]=1
                    if (strong==2): npcpain[hit]+=10; hap="shattering the skull and brain!"; event00=npcside[hit]+" is killed."
                    if (strong==2): npcforehead[hit]=2; npcskull[hit]=2; npcbrain[hit]=2
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0): npcforehead[hit]=2
                    if (strong==1): npcpain[hit]+=4; hap="chipping the skull!"
                    if (strong==1 and npcskull[hit]==0): npcforehead[hit]=2; npcskull[hit]=1
                    if (strong==2): npcpain[hit]+=7; hap="piercing the skull and brain!"; event00=npcside[hit]+" is killed."; b=1
                    if (strong==2): npcforehead[hit]=2; npcskull[hit]=2; npcbrain[hit]=2
                evbody="Forehead"
            if (bp2==2):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising them."
                    if (strong==0 and npceyes[hit]==0): npceyes[hit]=1
                    if (strong==1):
                        npcpain[hit]+=5; hap="instead cracking the skull!"
                        aa=random.randint(0,2)
                        if (aa==0): npcknocked[hit]=1; npcpain[hit]=10
                    if (strong==1 and npcskull[hit]==0): npcskull[hit]=1
                    if (strong==2): npcpain[hit]+=10; hap="instead shattering the skull!"; npcknocked[hit]=1
                    if (strong==2): npcskull[hit]=2; npcbrain[hit]=1
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting them."
                    if (strong==0 and npceyes[hit]<=1): npceyes[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="partially blinding them."
                    if (strong==1 and npceyes[hit]<=2): npceyes[hit]=3
                    if (strong==2): npcpain[hit]+=4; hap="blinding them!"; b=1
                    if (strong==2): npceyes[hit]=4
                evbody="Eyes"
            if (bp2==3):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcnose[hit]==0): npcnose[hit]=1
                    if (strong==1): npcpain[hit]+=5; hap="battering it."
                    if (strong==1 and npcnose[hit]<=1): npcnose[hit]=2
                    if (strong==2): npcpain[hit]+=8; hap="shattering it!"; npcknocked[hit]=1
                    if (strong==2): npcnose[hit]=3
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcnose2[hit]==0): npcnose2[hit]=1
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."
                    if (strong==1 and npcnose2[hit]<=1): npcnose2[hit]=2
                    if (strong==2): npcpain[hit]+=4; hap="cutting off a piece!"; b=1
                    if (strong==2): npcnose2[hit]=3
                evbody="Nose"
            if (bp2==4):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcjaw[hit]==0): npcjaw[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping the jaw."
                    if (strong==1 and npcjaw[hit]<=1): npcjaw[hit]=2
                    if (strong==2): npcpain[hit]+=8; hap="shattering the jaw!"; npcknocked[hit]=1
                    if (strong==2): npcjaw[hit]=3
                if (damtype=="Pierce"):
                    if (strong==0):
                        npcpain[hit]+=1
                        aa=random.randint(0,1)
                        if (aa==0): hap="cutting the cheek."
                        if (aa==1): hap="cutting the lips."
                    if (strong==0 and npcmouth[hit]==0): npcmouth[hit]=1
                    if (strong==1): npcpain[hit]+=2; hap="cutting open the mouth."
                    if (strong==1 and npcmouth[hit]<=1): npcmouth[hit]=2
                    if (strong==2): npcpain[hit]+=4; hap="tearing the mouth apart!"
                    if (strong==2): npcmouth[hit]=3
                evbody="Mouth"
            if (bp2==5):
                if (damtype=="Hit"):
                    if (strong==0): hap=npcside[whogoes]+"'s attack glances off "+npcside[hit]+"..."
                    if (strong==1): npcpain[hit]+=2; hap="bruising the temple."
                    if (strong==1 and npctemple[hit]==0): npctemple[hit]=1
                    if (strong==2):
                        npcpain[hit]+=5; hap="chipping the skull."
                        aa=random.randint(0,2)
                        if (aa==0): npcknocked[hit]=1; npcpain[hit]=10
                    if (strong==2): npcskull[hit]=2; npcbrain[hit]=1
                if (damtype=="Pierce"):
                    if (strong==0): hap=npcside[whogoes]+"'s attack glances off "+npcside[hit]+"..."; npcbleeding[hit]-=dam
                    if (strong==1): npcpain[hit]+=1; hap="cutting the temple."
                    if (strong==1 and npctemple[hit]<=1): npctemple[hit]=2
                    if (strong==2): npcpain[hit]+=5; hap="tearing the brain!"; event00=npcside[hit]+" is killed instantly!"; b=1
                    if (strong==2): npctemple[hit]=3; npcbrain[hit]=2
                evbody="Temple"
            if (bp2==6):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcneck[hit]==0): npcneck[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping the neck!"
                    if (strong==1 and npcneck[hit]<=1): npcneck[hit]=2
                    if (strong==2 and npcfainted[hit]<=0): npcpain[hit]+=5; hap="fracturing the neck!"; event00=npcside[hit]+" is paralyzed!"; npcneck[hit]=4; npcpara[hit]+=1
                    if (strong==2 and npcfainted[hit]>0): npcpain[hit]+=10; hap="snapping the neck!"; event00=npcside[hit]+" is killed instantly!"; npcneck[hit]=3
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcthroat[hit]==0): npcthroat[hit]=1
                    if (strong==1): npcpain[hit]+=2; hap="severing an artery!"
                    if (strong==1): npcartery[hit]+=1; npcinternal[hit]+=1
                    if (strong==1 and npcthroat[hit]==0): npcthroat[hit]=1
                    if (strong==2): npcpain[hit]+=4; hap="severing the throat!"; event00=npcside[hit]+" can't breathe!"; b=1
                    if (strong==2): npcthroat[hit]=2
                evbody="Throat"
        if (bp1==1): #----------------------------Body
            if (bp2==2):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcchest[hit]==0): npcchest[hit]=1
                    if (strong==1): npcpain[hit]+=5; hap="badly hurting it."
                    if (strong==1 and npcchest[hit]<=1): npcchest[hit]=2
                    if (strong==2): npcpain[hit]+=9; hap="breaking ribs!"
                    if (strong==2):
                        npcchest[hit]=3
                        aa=random.randint(0,3)
                        if (aa==0): npcheart[hit]+=1; event00=npcside[hit]+"'s heart is pierced by a broken rib."
                        if (aa==1): npclungs[hit]+=1; event00=npcside[hit]+"'s lungs are pierced by a broken rib."
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcchest2[hit]==0): npcchest2[hit]=1
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."
                    if (strong==1 and npcchest2[hit]<=1): npcchest2[hit]=2
                    if (strong==1):
                        aa=random.randint(0,3)
                        if (aa==0): npcheart[hit]+=1; npcinternal[hit]+=1; event00=npcside[hit]+"'s heart is pierced by the "+npcheld[whogoes]+"."
                        if (aa==1): npclungs[hit]+=1; npcinternal[hit]+=1; event00=npcside[hit]+"'s lungs are pierced by the "+npcheld[whogoes]+"."                        
                    if (strong==2): npcpain[hit]+=4; hap="tearing internal organs!"
                    if (strong==2):
                        npcchest2[hit]=3; npcinternal[hit]+=1; b=1
                        aa=random.randint(0,1)
                        if (aa==0): npcheart[hit]+=2; event00=npcside[hit]+"'s heart is pierced by the "+npcheld[whogoes]+"."
                        if (aa==1): npclungs[hit]+=2; event00=npcside[hit]+"'s lungs are pierced by the "+npcheld[whogoes]+"."
                evbody="Chest"
            if (bp2==3):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcgut[hit]==0): npcgut[hit]=1
                    if (strong==1):
                        npcpain[hit]+=5; hap="battering it."
                        npcstun[hit]+=1
                    if (strong==1 and npcgut[hit]<=1): npcgut[hit]=2
                    if (strong==2):
                        npcpain[hit]+=8; hap="knocking the air out of them!"; npcknocked[hit]=1
                        if (npcoxygen[hit]>0): npcoxygen[hit]=0
                    if (strong==2): npcgut[hit]=3
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcgut2[hit]==0): npcgut2[hit]=1
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."; event00=npcside[hit]+" is feeling sick."
                    if (strong==1 and npcgut2[hit]<=1): npcgut2[hit]=2
                    if (strong==2): npcpain[hit]+=4; hap="tearing the gut!"; b=1; npcinternal[hit]+=1; npcstun[hit]+=1; event00=npcside[hit]+" is feeling sick."
                    if (strong==2): npcgut2[hit]=3
                evbody="Gut"
            if (bp2==4):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcback[hit]==0): npcback[hit]=1
                    if (strong==1): npcpain[hit]+=4; hap="battering it."
                    if (strong==1 and npcback[hit]<=2): npcback[hit]=3
                    if (strong==2): npcpain[hit]+=6; hap="fracturing the spine!"; event00=npcside[hit]+" is paralyzed!"; npcpara[hit]+=1
                    if (strong==2): npcback[hit]=5; npcspine[hit]=1
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcback[hit]<=1): npcback[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."
                    if (strong==1 and npcback[hit]<=3): npcback[hit]=4
                    if (strong==2): npcpain[hit]+=4; hap="severing the spine!"; event00=npcside[hit]+" is paralyzed!"; npcpara[hit]+=1
                    if (strong==2): npcback[hit]=6; npcspine[hit]=2
                evbody="Back"
        if (bp1==2): #----------------------------------Arms
            if (bp2==3):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcrightarm[hit]==0): npcrightarm[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping it."; drop=1
                    if (strong==1 and npcrightarm[hit]<=2): npcrightarm[hit]=3
                    if (strong==2): npcpain[hit]+=4; hap="breaking it!"; drop=2; event00=npcside[hit]+" can't use their right arm."
                    if (strong==2 and npcrightarm[hit]!=6): npcrightarm[hit]=5
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcrightarm[hit]<=1): npcrightarm[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."; drop=1; npcartery[hit]+=1; event00="An artery is torn."
                    if (strong==1 and npcrightarm[hit]<=3): npcrightarm[hit]=4
                    if (strong==2): npcpain[hit]+=3; hap="severing vital muscles!"; b=1; drop=2; npcartery[hit]+=1; event00=npcside[hit]+" can't use their right arm."
                    if (strong==2): npcrightarm[hit]=6
                evbody="Right Arm"
            if (bp2==4):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcrighthand[hit]==0): npcrighthand[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping it."; drop=1
                    if (strong==1 and npcrighthand[hit]<=2): npcrighthand[hit]=3
                    if (strong==2): npcpain[hit]+=4; hap="breaking it!"; drop=2; event00=npcside[hit]+" can't use their right arm."
                    if (strong==2 and npcrighthand[hit]!=6): npcrighthand[hit]=5
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcrighthand[hit]<=1): npcrighthand[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."; drop=1; npcartery[hit]+=1; event00="An artery is torn."
                    if (strong==1 and npcrighthand[hit]<=3): npcrighthand[hit]=4
                    if (strong==2): npcpain[hit]+=3; hap="severing vital muscles!"; b=1; drop=2; npcartery[hit]+=1; event00=npcside[hit]+" can't use their right hand."
                    if (strong==2): npcrighthand[hit]=6
                evbody="Right Arm"
            if (bp2==5):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcleftarm[hit]==0): npcleftarm[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping it."; drop=1
                    if (strong==1 and npcleftarm[hit]<=2): npcleftarm[hit]=3
                    if (strong==2): npcpain[hit]+=4; hap="breaking it!"; drop=2; event00=npcside[hit]+" can't use their left arm."
                    if (strong==2 and npcleftarm[hit]!=6): npcleftarm[hit]=5
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcleftarm[hit]<=1): npcleftarm[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."; drop=1; npcartery[hit]+=1; event00="An artery is torn."
                    if (strong==1 and npcleftarm[hit]<=3): npcleftarm[hit]=4
                    if (strong==2): npcpain[hit]+=3; hap="severing vital muscles!"; b=1; drop=2; npcartery[hit]+=1; event00=npcside[hit]+" can't use their left arm."
                    if (strong==2): npcleftarm[hit]=6
                evbody="Left Arm"
            if (bp2==6):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npclefthand[hit]==0): npclefthand[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping it."; drop=1
                    if (strong==1 and npclefthand[hit]<=2): npclefthand[hit]=3
                    if (strong==2): npcpain[hit]+=4; hap="breaking it!"; drop=2; event00=npcside[hit]+" can't use their left arm."
                    if (strong==2 and npclefthand[hit]!=6): npclefthand[hit]=5
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npclefthand[hit]<=1): npclefthand[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."; drop=1; npcartery[hit]+=1; event00="An artery is torn."
                    if (strong==1 and npclefthand[hit]<=3): npclefthand[hit]=4
                    if (strong==2): npcpain[hit]+=3; hap="severing vital muscles!"; b=1; drop=2; npcartery[hit]+=1; event00=npcside[hit]+" can't use their left hand."
                    if (strong==2): npclefthand[hit]=6
                evbody="Left Arm"  
        if (bp1==3): #----------------------------------Legs
            if (bp2==4):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcrightleg[hit]==0): npcrightleg[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping it."
                    if (strong==1 and npcrightleg[hit]<=2): npcrightleg[hit]=3
                    if (strong==2): npcpain[hit]+=4; hap="breaking it!"; event00=npcside[hit]+" is having trouble moving."
                    if (strong==2 and npcrightleg[hit]!=6): npcrightleg[hit]=5
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcrightleg[hit]<=1): npcrightleg[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."; npcartery[hit]+=1; event00="An artery is torn."
                    if (strong==1 and npcrightleg[hit]<=3): npcrightleg[hit]=4
                    if (strong==2): npcpain[hit]+=3; hap="severing vital muscles!"; b=1; npcartery[hit]+=1; event00=npcside[hit]+" is having trouble moving."
                    if (strong==2): npcrightleg[hit]=6
                evbody="Right Leg"
            if (bp2==5):
                if (damtype=="Hit"):
                    if (strong==0): npcpain[hit]+=1; hap="bruising it."
                    if (strong==0 and npcleftleg[hit]==0): npcleftleg[hit]=1
                    if (strong==1): npcpain[hit]+=3; hap="chipping it."
                    if (strong==1 and npcleftleg[hit]<=2): npcleftleg[hit]=3
                    if (strong==2): npcpain[hit]+=4; hap="breaking it!"; event00=npcside[hit]+" is having trouble moving."
                    if (strong==2 and npcleftleg[hit]!=6): npcleftleg[hit]=5
                if (damtype=="Pierce"):
                    if (strong==0): npcpain[hit]+=1; hap="cutting it."
                    if (strong==0 and npcleftleg[hit]<=1): npcleftleg[hit]=2
                    if (strong==1): npcpain[hit]+=2; hap="cutting deep."; npcartery[hit]+=1; event00="An artery is torn."
                    if (strong==1 and npcleftleg[hit]<=3): npcleftleg[hit]=4
                    if (strong==2): npcpain[hit]+=3; hap="severing vital muscles!"; b=1; npcartery[hit]+=1; event00=npcside[hit]+" is having trouble moving."
                    if (strong==2): npcleftleg[hit]=6
                evbody="Left Leg"
        if (damtype=="Pierce"): #If a Pierce Weapon is Used
            npcbleeding[hit]+=int(dam/1.2); a=0
            if (bp1==1): npcbleeding[hit]+=int(dam/2.0)
            if (bp1==2): npcbleeding[hit]-=int(dam/2.0)
            if (bp1==3): npcbleeding[hit]-=int(dam/1.5)
            if (b==1): whichblood=0
            if ((wallx[npcx[hit]+npcy[hit]*lvlW-1]!=0 or wally[npcx[hit]+npcy[hit]*lvlW-1]!=0) and walldir[npcx[hit]+npcy[hit]*lvlW-1]==3): a=1
            if ((wallx[npcx[hit]+npcy[hit]*lvlW]!=0 or wally[npcx[hit]+npcy[hit]*lvlW]!=0) and walldir[npcx[hit]+npcy[hit]*lvlW]==0): a=1
            if ((wallx[npcx[hit]+npcy[hit]*lvlW-lvlW]!=0 or wally[npcx[hit]+npcy[hit]*lvlW-lvlW]!=0) and walldir[npcx[hit]+npcy[hit]*lvlW-lvlW]==2): a=2
            if ((wallx[npcx[hit]+npcy[hit]*lvlW]!=0 or wally[npcx[hit]+npcy[hit]*lvlW]!=0) and walldir[npcx[hit]+npcy[hit]*lvlW]==1): a=2
            if (a>=1):
                bup=3.0; bsi=0.0
                c=random.randint(0,1)
                d=random.randint(0,1)
                if (b==0): d=0
                if (a==2): bup=int(si)/2+3
                for m in range(11):
                    if (m==whichblood):
                        whichblood+=1
                        if (whichblood>=11): whichblood=0; break
                        bloodlx[m]=npcx[hit]; bloodly[m]=npcy[hit]
                        if (b==1):
                            bloodvarx[m]=int(bup)
                            bloodvary[m]=int(bsi)
                            if (d==1): bloodvary[m]=int(bsi)+10
                            bup+=1
                            if (c==0): bsi=bsi*1.4+.1
                            if (c==1): bsi=bsi*1.4-.1
                            if (d==0): bloodlen[m]=1; bloodmax[m]=random.randint(1,25-bloodvary[m])
                            if (d==1): bloodlen[m]=1; bloodmax[m]=random.randint(1,15)
                        if (b==0):
                            if (a==1): bloodvarx[m]=random.randint(3,int(si/2)-3)
                            if (a==2): bloodvarx[m]=random.randint(int(si/2)+3,si-3)
                            bloodvary[m]=random.randint(0,10)
                            if (d==0): bloodlen[m]=1; bloodmax[m]=random.randint(1,25-bloodvary[m])
                            if (d==1): bloodlen[m]=1; bloodmax[m]=random.randint(1,15)
                            break
        if (npcdead[hit]==1):
            event00=""
        if (npcstrangle[hit]==2 and (npcdead[hit]==1 or npcfainted[hit]>0)):
            npcstrangle[hit]=0
            npcstrangle[npcstrangling[hit]]=0
            npcrunaway[hit]=2
        if (drop>0 and npcheld[hit]!=""):
            a=0
            aa=random.randint(0,1)
            xx=npcx[hit]; yy=npcy[hit]
            if (aa==0 or drop==2):
                if (walldir[npcx[hit]+npcy[hit]*lvlW]!=1 and walldir[npcx[hit]+npcy[hit]*lvlW-lvlW]==2 and wallx[npcx[hit]+npcy[hit]*lvlW-lvlW]!=0): a+=1
                if (walldir[npcx[hit]+npcy[hit]*lvlW]!=2 and walldir[npcx[hit]+npcy[hit]*lvlW+lvlW]==1 and wallx[npcx[hit]+npcy[hit]*lvlW+lvlW]!=0): a+=1
                if (walldir[npcx[hit]+npcy[hit]*lvlW]!=0 and walldir[npcx[hit]+npcy[hit]*lvlW-1]==3 and wallx[npcx[hit]+npcy[hit]*lvlW-1]!=0): a+=1
                if (walldir[npcx[hit]+npcy[hit]*lvlW]!=3 and walldir[npcx[hit]+npcy[hit]*lvlW+1]==0 and wallx[npcx[hit]+npcy[hit]*lvlW+1]!=0): a+=1
                if (a==0):
                    xx=npcx[whogoes]; yy=npcy[whogoes]
                    if (thrown!=""): xx=npcx[hit]; yy=npcy[hit]
                else:
                    aa=random.randint(0,a); a=0
                    if (walldir[npcx[hit]+npcy[hit]*lvlW]!=1 and walldir[npcx[hit]+npcy[hit]*lvlW-lvlW]==2 and wallx[npcx[hit]+npcy[hit]*lvlW-lvlW]!=0): a+=1
                    if (aa==a): xx=npcx[hit]; yy=npcy[hit]-1
                    if (walldir[npcx[hit]+npcy[hit]*lvlW]!=2 and walldir[npcx[hit]+npcy[hit]*lvlW+lvlW]==1 and wallx[npcx[hit]+npcy[hit]*lvlW+lvlW]!=0): a+=1
                    if (aa==a): xx=npcx[hit]; yy=npcy[hit]+1
                    if (walldir[npcx[hit]+npcy[hit]*lvlW]!=0 and walldir[npcx[hit]+npcy[hit]*lvlW-1]==3 and wallx[npcx[hit]+npcy[hit]*lvlW-1]!=0): a+=1
                    if (aa==a): xx=npcx[hit]-1; yy=npcy[hit]
                    if (walldir[npcx[hit]+npcy[hit]*lvlW]!=3 and walldir[npcx[hit]+npcy[hit]*lvlW+1]==0 and wallx[npcx[hit]+npcy[hit]*lvlW+1]!=0): a+=1
                    if (aa==a): xx=npcx[hit]+1; yy=npcy[hit]
                for nn in range(19):
                    if (item[nn]==""):
                        item[nn]=npcheld[hit]; itemx[nn]=int(xx); itemy[nn]=int(yy)
                        break
                event00=npcside[hit]+" dropped their "+npcheld[hit]+"."
                npcheld[hit]=""

    if (npcheld[whogoes]==""): wep="Fist"
    else: wep=npcheld[whogoes]
    if (npcheld[whogoes]=="Bottle" and (throwdam==0 or npccontrol[whogoes]==0 or npccontrol[whogoes]==1)): npcheld[whogoes]="Glass"; event00=npcside[whogoes]+"'s Bottle shattered and became Glass!"
    if (thrown=="Bottle"): thrown="Glass"; event00=npcside[whogoes]+"'s Bottle shattered and became Glass!"
    if (miss>=5):
        event0=npcside[whogoes]+" "+damtype+"s "+npcside[hit]+" in the "+evbody+" with their "+wep+", "+hap
        if (actionselect==0 and npccontrol[whogoes]==1 and thrown==""): event0=npcside[whogoes]+" "+damtype+"s "+"themselves"+" in the "+evbody+" with their "+wep+", "+hap
        if (npcdead[hit]==0 and hit!=whogoes and npcani[hit]!="Fall"): #End Animations
            if (npcani[hit]!="Strangling" and npcani[hit]!="Strangled" and npcani[hit]!="StranglingBack" and npcani[hit]!="StrangledBack"):
                if (dam>5): npcani[hit]="HurtBad"
                if (dam<=5): npcani[hit]="Hurt"
        if (npccontrol[whogoes]==1 and actionselect!=0 and npclvl[whogoes]<20 and npcdead[hit]==0):
            if (npccontrol[whogoes]==1):
                #if (npclvl[whogoes]<10): exp=dam*(15.0-npclvl[whogoes])#+(npclvl[hit]-npclvl[whogoes])*10.0
                #if (npclvl[whogoes]>=10): exp=dam*(5.0)#+(npclvl[hit]-npclvl[whogoes])*10.0
                if (npclvl[whogoes]<=npclvl[hit]): exp=dam*(15.0-npclvl[whogoes])+(npclvl[hit]-npclvl[whogoes])*3.0
                if (npclvl[whogoes]>npclvl[hit]): exp=dam*(15.0-npclvl[whogoes])+(npclvl[hit]-npclvl[whogoes])*5.0
                if (npcfainted[hit]>0): exp=int(exp*.8)
                if ((npcbleeding[hit]+npcpain[hit]>=40 and npcfainted[hit]>0) or npcdead[hit]==1): exp=int(exp*.3)
                if (exp<=0 or npclvl[whogoes]>=20): exp=0
                exp=int(exp*.9)
                #print exp
                if (npccontrol[hit]==1): npcexp[hit]+=int(exp)
                npcexp[whogoes]+=int(exp) #Experience Gain for Attacking 
    else:
        event0=npcside[whogoes]+" misses "+npcside[hit]+"..."
    if (throwdam==1 and npcheld[whogoes]!="Cards" and thrown!=""): throwdam=0; npcheld[whogoes]=""
    actionalready=1
    updating=2; am_actions=0; showPaths=0; actionselect=1; bodyselect=0; openbody=-1; bodymenu=-1


openbody=-1
bodyselect=0
def displayBodyMenu():
    global openbody, updating, bodyselect
    global delay2, bodymenu, pressed
    screen.blit(menu_body,(30,30))
    screen.blit(actionselectimg,(30+5,30+5+20*bodyselect))
    n=0; a=0
    text=font.render("Head",1,WHITE)
    screen.blit(text,(30+10,30+7+20*n+1)); n+=1
    if (openbody==n-1):
        text=font.render("  Forehead",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Eyes",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Nose",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Mouth",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Temple",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Throat",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        a=6
    text=font.render("Torso",1,WHITE)
    screen.blit(text,(30+10,30+7+20*n+1)); n+=1
    if (openbody==n-1):
        text=font.render("  Chest",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Gut",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Back",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        a=3
    text=font.render("Arms",1,WHITE)
    screen.blit(text,(30+10,30+7+20*n+1)); n+=1
    if (openbody==n-1):
        text=font.render("  Right Arm",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Right Hand",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Left Arm",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Left Hand",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        a=4
    text=font.render("Legs",1,WHITE)
    screen.blit(text,(30+10,30+7+20*n+1)); n+=1
    if (openbody==n-1):
        text=font.render("  Right Leg",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        #text=font.render("  Right Foot",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        text=font.render("  Left Leg",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        #text=font.render("  Left Foot",1,WHITE); screen.blit(text,(30+10,30+7+20*n+1)); n+=1
        a=4
    text=font.render("Cancel",1,GRAY)
    screen.blit(text,(30+10,30+7+20*n+1)); n+=1
    if (down==1 and bodyselect<n-1 and delay2<=0):
        bodyselect+=1; delay2=10; updating=2;
        if (mute==0): select.play()
    if (up==1 and bodyselect>0 and delay2<=0):
        bodyselect-=1; delay2=10; updating=2;
        if (mute==0): select.play()
    if (pressed==1 and delay2<=0): #Nested Body
        if (bodyselect<n-1):
            updating=2; delay2=10; b=0
            if (openbody==-1 and b==0):
                openbody=bodyselect; b=1
            if (openbody==0 and b==0):
                if (bodyselect==1): AttSave(openbody,bodyselect,npclist[actionselect]) #Forehead
                if (bodyselect==2): AttSave(openbody,bodyselect,npclist[actionselect]) #Eyes
                if (bodyselect==3): AttSave(openbody,bodyselect,npclist[actionselect]) #Nose
                if (bodyselect==4): AttSave(openbody,bodyselect,npclist[actionselect]) #Mouth
                if (bodyselect==5): AttSave(openbody,bodyselect,npclist[actionselect]) #Temple
                if (bodyselect==6): AttSave(openbody,bodyselect,npclist[actionselect]) #Throat
                if (bodyselect==a+1): openbody=1; bodyselect=1; b=1
                if (bodyselect==a+2): openbody=2; bodyselect=2; b=1
                if (bodyselect==a+3): openbody=3; bodyselect=3; b=1
            if (openbody==1 and b==0):
                if (bodyselect==2): AttSave(openbody,bodyselect,npclist[actionselect]) #Chest
                if (bodyselect==3): AttSave(openbody,bodyselect,npclist[actionselect]) #Gut
                if (bodyselect==4): AttSave(openbody,bodyselect,npclist[actionselect]) #Back
                if (bodyselect==0): openbody=0; bodyselect=0; b=1
                if (bodyselect==a+2): openbody=2; bodyselect=2; b=1
                if (bodyselect==a+3): openbody=3; bodyselect=3; b=1
            if (openbody==2 and b==0):
                if (bodyselect==3): AttSave(openbody,bodyselect,npclist[actionselect]) #Right Arm
                if (bodyselect==4): AttSave(openbody,bodyselect,npclist[actionselect]) #Right Hand
                if (bodyselect==5): AttSave(openbody,bodyselect,npclist[actionselect]) #Left Arm
                if (bodyselect==6): AttSave(openbody,bodyselect,npclist[actionselect]) #Left Hand
                if (bodyselect==0): openbody=0; bodyselect=0; b=1
                if (bodyselect==1): openbody=1; bodyselect=1; b=1
                if (bodyselect==a+3): openbody=3; bodyselect=3; b=1
            if (openbody==3 and b==0):
                if (bodyselect==4): AttSave(openbody,bodyselect,npclist[actionselect]) #Right Leg
                if (bodyselect==5): AttSave(openbody,bodyselect,npclist[actionselect]) #Left Leg
                if (bodyselect==0): openbody=0; bodyselect=0; b=1
                if (bodyselect==1): openbody=1; bodyselect=1; b=1
                if (bodyselect==2): openbody=2; bodyselect=2; b=1
        if (bodyselect==n-1): #Cancel
            bodymenu=-1; bodyselect=0; updating=2; delay2=10; pressed=0; openbody=-1

check=""
bodymenu=-1
delay3=0
shortmove=0
def displayActionMenu():
    global actionselect, delay2, showDist, showDist2, updating, pressed, selectx, selecty, up, down
    global am_actions, turn, movedalready, actionalready, showPaths, whogoes, check, delay3, tutorialthrow, shortmove, endlevel
    global bodymenu, event00, actionmenu
    if (movedalready==1 and actionalready==1 and thrown=="" and (npcani[whogoes]!="Attack" and npcani[whogoes]!="End Attack") and npccontrol[whogoes]==1): #Turn Over
        nextTurn()
        return
    if (showskillsgoes==1):
        pressed=0; up=0; down=0
    screen.blit(menu_action,(200,220)) #Panel
    screen.blit(menu_actiontop,(200,220))
    screen.blit(actionselectimg,(200+5,220+5+20*actionselect))
    n=0
    if (am_actions==0):
        if (movedalready==0):
            if (npcfainted[whogoes]<=0): text=font.render("Move",1,WHITE) 
            if (npcfainted[whogoes]>0): text=font.render("Move",1,PINK)  #List of Options
            if (npcstrangle[whogoes]>0): text=font.render("Move",1,BLUE)
            if (npcdead[whogoes]==1): text=font.render("Move",1,RED)
            screen.blit(text,(200+10,220+7+20*n+1))
        n+=1
        if (actionalready==0):
            if (npcfainted[whogoes]<=0): text=font.render("Action",1,WHITE)
            if (npcfainted[whogoes]>0): text=font.render("Action",1,PINK)
            #if (npcstrangle[whogoes]==1): text=font.render("Action",1,BLUE)
            if (npcdead[whogoes]==1): text=font.render("Action",1,RED) 
            screen.blit(text,(200+10,220+7+20*n+1))
        n+=1
        text=font.render("End Turn",1,WHITE)
        screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        if (endlevel>0):
            text=font.render("End Chapter",1,TAN)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
    if (am_actions==1):
        if (npcstrangle[whogoes]<=1):
            text=font.render("Attack",1,WHITE)
            if (npcheld[whogoes]=="Med Kit"): text=font.render("Heal",1,WHITE)
            if (npcstrangle[whogoes]==1): text=font.render("Struggle",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
            if (npcstrangle[whogoes]==0):
                text=font.render("Open/Close",1,WHITE)
                screen.blit(text,(200+10,220+7+20*n+1)); n+=1
                if ((npcrighthand[whogoes]<=4 and npcrightarm[whogoes]<=4) or (npclefthand[whogoes]<=4 and npcleftarm[whogoes]<=4)):
                    text=font.render("Pick Up/Drop",1,WHITE)
                else:
                    text=font.render("Pick Up/Drop",1,RED)
                screen.blit(text,(200+10,220+7+20*n+1)); n+=1
                if ((npcrighthand[whogoes]<=4 and npcrightarm[whogoes]<=4) or (npclefthand[whogoes]<=4 and npcleftarm[whogoes]<=4)):
                    text=font.render("Throw",1,WHITE)
                else:
                    text=font.render("Throw",1,RED)
                screen.blit(text,(200+10,220+7+20*n+1)); n+=1
            else: n+=2
        else: n+=3
        if (npcstrangle[whogoes]==0):
            if ((npcrighthand[whogoes]<=4 and npcrightarm[whogoes]<=4) or (npclefthand[whogoes]<=4 and npcleftarm[whogoes]<=4)):
                text=font.render("Strangle",1,WHITE)
            else:
                text=font.render("Strangle",1,RED)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        if (npcstrangle[whogoes]==1):
            n+=1
            text=font.render(" ",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        if (npcstrangle[whogoes]==2):
            n+=1
            text=font.render("Let Go",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        text=font.render("Breath",1,WHITE)
        screen.blit(text,(200+10,220+7+20*n+1)); n+=1
    if (am_actions==2 or bodymenu>=0):
        for nn in range(11):
            npclist[nn]=-1
            npclist2[nn]=""
        if (check=="Attack"):
            text=font.render("Self",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
            for nn in range(11):
                if (npc[nn]==1):
                    if (npcx[nn]==npcx[showDist2] and npcy[nn]==npcy[showDist2]-1): npclist[n]=nn; npclist2[n]="(Up)"
                    if (npcx[nn]==npcx[showDist2] and npcy[nn]==npcy[showDist2]+1): npclist[n]=nn; npclist2[n]="(Dn)"
                    if (npcx[nn]==npcx[showDist2]-1 and npcy[nn]==npcy[showDist2]): npclist[n]=nn; npclist2[n]="(Lt)"
                    if (npcx[nn]==npcx[showDist2]+1 and npcy[nn]==npcy[showDist2]): npclist[n]=nn; npclist2[n]="(Rt)"
                    if (npclist[n]!=-1):
                        text=font.render(npcside[nn]+" "+npclist2[n],1,WHITE)
                        screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        if (check=="Open/Close"):
            a=int(npcx[whogoes])+int(npcy[whogoes])*lvlW
            if (wallx[a]>=5 and walldir[a]==0): npclist2[n]="(Lt)"
            if (wallx[a]>=5 and walldir[a]==1): npclist2[n]="(Up)"
            if (wallx[a]>=5 and walldir[a]==2): npclist2[n]="(Dn)"
            if (wallx[a]>=5 and walldir[a]==3): npclist2[n]="(Rt)"
            if (wallx[a+1]>=5 and walldir[a+1]==0): npclist[n]=a+1; npclist2[n]="(Rt)"
            if (wallx[a-1]>=5 and walldir[a-1]==3): npclist[n]=a-1; npclist2[n]="(Lt)"
            if (wallx[a+lvlW]>=5 and walldir[a+lvlW]==1): npclist[n]=a+lvlW; npclist2[n]="(Dn)"
            if (wallx[a-lvlW]>=5 and walldir[a-lvlW]==2): npclist[n]=a-lvlW; npclist2[n]="(Up)"
            if (npclist2[n]!=""):
                text=font.render("Door"+" "+npclist2[n],1,WHITE)
                screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        if (check=="Strangle"):
            for nn in range(11):
                if (npc[nn]==1 and npcside[nn]!="Commander" and (npcside[nn]!="Floyd" or level!="Friends") and (npcside[nn]!="Lenna" or level!="Speechless") and (npcside[nn]!="Sanders" or level!="Unity") and ((npcani[nn]=="" and npcstrangle[nn]==0) or (npcstrangle[nn]==1 and npcstrangle[whogoes]==2))):
                    a=0
                    if (npcstrangle[showDist2]==2 and npcstrangle[nn]==1): a=1
                    if (npcstrangle[showDist2]==0 and npcstrangle[nn]==0): a=1
                    if (a==1):
                        if (npcx[nn]==npcx[showDist2] and npcy[nn]==npcy[showDist2]-1): npclist[n]=nn; npclist2[n]="(Up)"
                        if (npcx[nn]==npcx[showDist2] and npcy[nn]==npcy[showDist2]+1): npclist[n]=nn; npclist2[n]="(Dn)"
                        if (npcx[nn]==npcx[showDist2]-1 and npcy[nn]==npcy[showDist2]): npclist[n]=nn; npclist2[n]="(Lt)"
                        if (npcx[nn]==npcx[showDist2]+1 and npcy[nn]==npcy[showDist2]): npclist[n]=nn; npclist2[n]="(Rt)"
                        if (npclist[n]!=-1):
                            text=font.render(npcside[nn]+" "+npclist2[n],1,WHITE)
                            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        if (check=="Pick Up"):
            dropping=0
            for nn in range(19):
                if (item[nn]!="" and itemx[nn]==npcx[whogoes] and itemy[nn]==npcy[whogoes]):
                    npclist[n]=nn
                    #item[nn]=""
                    text=font.render(item[nn],1,WHITE)
                    screen.blit(text,(200+10,220+7+20*n+1)); n+=1
            if (n==0):
                dropping=1
                text=font.render(npcheld[whogoes],1,WHITE)
                screen.blit(text,(200+10,220+7+20*n+1)); n+=1
        if (check=="Throw"):
            text=font.render("Up",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
            text=font.render("Left",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
            text=font.render("Right",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
            text=font.render("Down",1,WHITE)
            screen.blit(text,(200+10,220+7+20*n+1)); n+=1
    text=font.render("Cancel",1,GRAY)
    screen.blit(text,(200+10,220+7+20*n+1)); n+=1
    if (delay3>0): delay3-=1
    if (delay3<=0 and bodymenu<0):
        if (down==1 and actionselect<n-1): actionselect+=1; delay3=10; updating=2; select.play()
        if (up==1 and actionselect>0): actionselect-=1; delay3=10; updating=2; select.play()
    if (pressed==1 and delay3<=0 and am_actions==0): #First Menu
        if (actionselect==0 and movedalready==0 and npcfainted[whogoes]<=0 and npcstrangle[whogoes]<=0 and npcdead[whogoes]==0): #Move
            showDist=showDist2; showDist2=-1; updating=2; actionmenu=0; pressed=0; delay2=10
        if (actionselect==1 and actionalready==0 and npcfainted[whogoes]<=0 and npcdead[whogoes]==0): am_actions=1; delay2=10; actionselect=0 #To Actions Menu
        if (actionselect==2 and npcani[whogoes]!="Attack" and npcani[whogoes]!="End Attack"): #End Turn
            actionalready=1; movedalready=1
            showDist2=-1; updating=2; actionmenu=0; pressed=0; delay2=10; am_actions=0
        if (actionselect==3 and endlevel==0): showDist=-1; showDist2=-1; updating=2; actionmenu=0; pressed=0; delay2=10; am_actions=0; showPaths=0; actionselect=0 #Cancel
        if (actionselect==4 and endlevel>0): showDist=-1; showDist2=-1; updating=2; actionmenu=0; pressed=0; delay2=10; am_actions=0; showPaths=0; actionselect=0 #Cancel
        if (actionselect==3 and endlevel>0): endlevel=2 #end chapter
    if (pressed==1 and delay2<=0 and am_actions==1): #Actions Menu
        if (actionselect==0 and npcstrangle[whogoes]==0):
            check="Attack"; am_actions=2; updating=2; delay2=10; actionselect=0
        if (actionselect==0 and npcstrangle[whogoes]==1):
            check="Struggle"; updating=2; delay2=10; actionselect=0; showDist=-1; showDist2=-1; actionmenu=0; pressed=0; am_actions=0; actionalready=1; showPaths=0
            event00=npcside[whogoes]+" struggles to get free!"
        if (actionselect==1 and npcstrangle[whogoes]==0):
            check="Open/Close"; am_actions=2; updating=2; delay2=10; actionselect=0
        if (actionselect==2 and npcstrangle[whogoes]==0):
            if ((npcrighthand[whogoes]<=4 and npcrightarm[whogoes]<=4) or (npclefthand[whogoes]<=4 and npcleftarm[whogoes]<=4)):
                check="Pick Up"; am_actions=2; updating=2; delay2=10; actionselect=0
        if (actionselect==3 and npcstrangle[whogoes]==0):
            if ((npcrighthand[whogoes]<=4 and npcrightarm[whogoes]<=4) or (npclefthand[whogoes]<=4 and npcleftarm[whogoes]<=4)):
                check="Throw"; am_actions=2; updating=2; delay2=10; actionselect=0
        if (actionselect==4 and npcstrangle[whogoes]!=1):
            if ((npcrighthand[whogoes]<=4 and npcrightarm[whogoes]<=4) or (npclefthand[whogoes]<=4 and npcleftarm[whogoes]<=4)):
                check="Strangle"; am_actions=2; updating=2; delay2=10; actionselect=0
        if (actionselect==5):
            check="Breath"; updating=2; delay2=10; actionselect=0; showDist=-1; showDist2=-1; actionmenu=0; pressed=0; am_actions=0; actionalready=1; showPaths=0
            npcbreath[whogoes]=1-npcbreath[whogoes]
            if (npcbreath[whogoes]==1): event00=npcside[whogoes]+" held their breath."
            if (npcbreath[whogoes]==0): event00=npcside[whogoes]+" began to breathe again."
        if (actionselect==n-1):
            showPaths=0; updating=2; pressed=0; delay2=10; am_actions=0; actionselect=0 #Cancel
    if (pressed==1 and delay2<=0 and am_actions==2): #Object/Char Select Menu
        if (actionselect<n-1):
            if (check=="Attack"):
                if (npcheld[whogoes]!="Med Kit"):
                    if (actionselect==0): #Self Attack
                        bodymenu=whogoes; updating=2; delay2=10; pressed=0
                    else:
                        bodymenu=npclist[actionselect]; updating=2; delay2=10; pressed=0
                        if (npcstrangle[npclist[actionselect]]==0 or npcani[npclist[actionselect]]=="Strangled" or npcani[npclist[actionselect]]=="StrangledBack"):
                            if (npclist2[actionselect]=="(Rt)" or npclist2[actionselect]=="(Up)"): npcdir[whogoes]=0
                            if (npclist2[actionselect]=="(Dn)" or npclist2[actionselect]=="(Lt)"): npcdir[whogoes]=1
                if (npcheld[whogoes]=="Med Kit"): #Heal Ability
                    if (actionselect==0):
                        updating=2; delay2=10; pressed=0; npcbleeding[whogoes]=0; npcblood[whogoes]=100; npcpain[whogoes]=0
                        event00=npcside[whogoes]+" heals themselves with a Medical Kit."
                    else:
                        updating=2; delay2=10; pressed=0; npcbleeding[npclist[actionselect]]=0; npcpain[npclist[actionselect]]=0
                        event00=npcside[whogoes]+" heals "+npcside[npclist[actionselect]]+" with a Medical Kit."
                    actionalready=1; am_actions=0
            if (check=="Open/Close"):
                optionOpen(); showDist=-1; showDist2=-1; updating=2; actionmenu=0; pressed=0; delay2=10; am_actions=0; actionalready=1; showPaths=0; storyTriggers() #Open/Close
                if (movedalready==1): movedalready=0; shortmove=1
            if (check=="Strangle" and npcunarmed[whogoes]>=15):
                if (npcstrangle[whogoes]==2):
                    npcstrangle[whogoes]=0
                    npcstrangle[npclist[actionselect]]=0
                    npcstrangling[whogoes]=-1
                else:
                    npcstrangle[whogoes]=2
                    npcstrangle[npclist[actionselect]]=1
                    npcstrangling[whogoes]=npclist[actionselect]
                updating=2; delay2=10; pressed=0; showDist=-1; showDist2=-1; actionmenu=0; am_actions=0; actionalready=1; showPaths=0
                if (npclist2[actionselect]=="(Rt)" or npclist2[actionselect]=="(Up)"): npcdir[whogoes]=0
                if (npclist2[actionselect]=="(Dn)" or npclist2[actionselect]=="(Lt)"): npcdir[whogoes]=1
            if (check=="Strangle" and npcunarmed[whogoes]<15 and tutorialmove==0 and tutorialhurt==0 and tutorialpick==0 and tutorialthrow==0 and tutorialarms==0):
                event00="Your [Unarmed] skill must be 15 or higher to use the [Strangle] command."
                check==""
                pressed=0
            if (check=="Pick Up"):
                if (dropping==0):
                    g=npcheld[whogoes]
                    npcheld[whogoes]=item[npclist[actionselect]]; item[npclist[actionselect]]=g
                    actionalready=1; showPaths=0; updating=2; pressed=0; delay2=10; am_actions=0; actionselect=0 #Cancel
                if (dropping==1):
                    for nn in range(19):
                        if (item[nn]==""):
                            item[nn]=npcheld[whogoes]; itemx[nn]=npcx[whogoes]; itemy[nn]=npcy[whogoes]
                            npcheld[whogoes]=""
                            actionalready=1; showPaths=0; updating=2; pressed=0; delay2=10; am_actions=0; actionselect=0
                            break
            if (check=="Throw" and npcheld[whogoes]!=""):
                if (actionselect==0): throwHeld("up") #up
                if (actionselect==1): throwHeld("left") #left
                if (actionselect==2): throwHeld("right") #right
                if (actionselect==3): throwHeld("down") #down
                if (tutorialthrow==1): tutorialthrow=0
        if (actionselect==n-1):
            showPaths=0; updating=2; pressed=0; delay2=10; am_actions=1; actionselect=0 #Cancel
    if (movedalready==1 and actionalready==1 and thrown=="" and (npcani[whogoes]!="Attack" and npcani[whogoes]!="End Attack") and npccontrol[whogoes]==1): #Turn Over
        nextTurn()

def throwHeld(direc):
    global throwndir, thrown, throwx, throwy, throwdist, updating, delay2, pressed, showDist, showDist2, actionmenu, am_actions, actionalready, showPaths
    a=0
    for n in range(lvlW*lvlH):
        if (n==npcx[whogoes]+npcy[whogoes]*lvlW):
            if (direc=="up"):
                if (wallx[n]>0 and walldir[n]==1): a=1
                if (wallx[n-lvlW]>0 and walldir[n-lvlW]==2): a=1
            if (direc=="down"):
                if (wallx[n]>0 and walldir[n]==2): a=1
                if (wallx[n+lvlW]>0 and walldir[n+lvlW]==1): a=1
            if (direc=="left"):
                if (wallx[n]>0 and walldir[n]==0): a=1
                if (wallx[n-1]>0 and walldir[n-1]==3): a=1
            if (direc=="right"):
                if (wallx[n]>0 and walldir[n]==3): a=1
                if (wallx[n+1]>0 and walldir[n+1]==0): a=1
            break
    for n in range(11):
        if (npcx[n]==npcx[whogoes] and npcy[n]==npcy[whogoes]-1 and direc=="up"): a=1
        if (npcx[n]==npcx[whogoes] and npcy[n]==npcy[whogoes]+1 and direc=="down"): a=1
        if (npcx[n]==npcx[whogoes]-1 and npcy[n]==npcy[whogoes] and direc=="left"): a=1
        if (npcx[n]==npcx[whogoes]+1 and npcy[n]==npcy[whogoes] and direc=="right"): a=1
    if (a==1): return
    thrown=npcheld[whogoes]
    if (npcheld[whogoes]!="Cards"): npcheld[whogoes]=""
    throwndir=direc
    throwdist=0.0
    throwx=npcx[whogoes]; throwy=npcy[whogoes]
    if (throwndir=="right"): throwx=npcx[whogoes]+1; throwy=npcy[whogoes]
    if (throwndir=="down"): throwx=npcx[whogoes]; throwy=npcy[whogoes]+1
    if (throwndir=="up"): throwx=npcx[whogoes]; throwy=npcy[whogoes]-1
    if (throwndir=="left"): throwx=npcx[whogoes]-1; throwy=npcy[whogoes]
    npcani[whogoes]="Attack"
    updating=2; delay2=10; pressed=0; showDist=-1; showDist2=-1; actionmenu=0; am_actions=0; actionalready=1; showPaths=0

throwdam=0
throwdist=0.0
def thrownAlready():
    global updating, throwndir, thrown, selectx, selecty, throwx, throwy, throwdam, throwdist
    global selectx, selecty
    updating=2
    npcani[whogoes]="Attack"
    selectx=throwx; selecty=throwy
    z=tilez[int(throwx)+int(throwy)*lvlW]
    screen.blit(itemspark,((throwx+2)*.5*si-int(camerax*si*.5-cameray*si*.5)-(throwy+1)*18+380-11  ,  (throwy+1)*.25*si-int(camerax*si*.25+cameray*si*.25)+(throwx+2)*9+290+z-17-10))
    for nn in range(11): #Thrown item hits NPC
        a=0
        if (int(throwx)==npcx[nn] and int(throwy)==npcy[nn] and nn!=whogoes and npcdead[nn]==0 and npc[nn]==1): a=1
        if ((int(throwx)==npcx[nn] and int(throwy)==npcy[nn] and nn!=whogoes and npcdead[nn]==0 and npc[nn]==1) or a==1):
            bp1a=random.randint(0,3)
            if (bp1a==0): bp2a=random.randint(1,6)
            if (bp1a==1): bp2a=random.randint(2,4)
            if (bp1a==2): bp2a=random.randint(3,6)
            if (bp1a==3): bp2a=random.randint(4,5)
            throwdam=1
            npcx[nn]=int(npcx[nn]); npcy[nn]=int(npcy[nn])
            AttSave(bp1a,bp2a,nn)
            Attack()
            for nn in range(19):
                if (item[nn]=="" and thrown!="Cards"):
                    item[nn]=thrown; itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="up"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="right"): itemx[nn]=int(throwx-1); itemy[nn]=int(throwy); selectx=int(throwx-1); selecty=int(throwy)
                    if (throwndir=="left"): itemx[nn]=int(throwx+1); itemy[nn]=int(throwy); selectx=int(throwx+1); selecty=int(throwy)
                    if (throwndir=="down"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    break
            thrown=""; selectx=int(selectx); selecty=int(selecty)
            break
    if (throwx<lvlW-1 and throwy<lvlH-1 and throwx>0 and throwy>0): #Thrown Item hits a wall
        a=0
        if (throwndir=="up" and ((walldir[int(throwx)+int(throwy)*lvlW]==1 and wallx[int(throwx)+int(throwy)*lvlW]!=0 and (wally[int(throwx)+int(throwy)*lvlW]==0 or wallx[int(throwx)+int(throwy)*lvlW]<=4)))): a=1
        if (throwndir=="left" and ((walldir[int(throwx)+int(throwy)*lvlW]==0 and wallx[int(throwx)+int(throwy)*lvlW]!=0 and (wally[int(throwx)+int(throwy)*lvlW]==0 or wallx[int(throwx)+int(throwy)*lvlW]<=4)))): a=1
        if (throwndir=="right" and ((walldir[int(throwx)+int(throwy)*lvlW]==3 and wallx[int(throwx)+int(throwy)*lvlW]!=0 and (wally[int(throwx)+int(throwy)*lvlW]==0 or wallx[int(throwx)+int(throwy)*lvlW]<=4)))): a=1
        if (throwndir=="down" and ((walldir[int(throwx)+int(throwy)*lvlW]==2 and wallx[int(throwx)+int(throwy)*lvlW]!=0 and (wally[int(throwx)+int(throwy)*lvlW]==0 or wallx[int(throwx)+int(throwy)*lvlW]<=4)))): a=1
        if (a==1):
            for nn in range(19):
                if (item[nn]=="" and thrown!="Cards"):
                    item[nn]=thrown; itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="up"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="down"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="right"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="left"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    break
            thrown=""; npcani[whogoes]="End Attack"
            selectx=int(selectx); selecty=int(selecty)
    if (throwx<lvlW-1 and throwy<lvlH-1 and throwx>0 and throwy>0): #Thrown Item hits a wall
        a=0
        if (throwndir=="up" and ((walldir[int(throwx)+int(throwy-1)*lvlW]==2 and wallx[int(throwx)+int(throwy-1)*lvlW]!=0 and (wally[int(throwx)+int(throwy-1)*lvlW]==0 or wallx[int(throwx)+int(throwy-1)*lvlW]<=4)))): a=1
        if (throwndir=="left" and ((walldir[int(throwx-1)+int(throwy)*lvlW]==3 and wallx[int(throwx-1)+int(throwy)*lvlW]!=0 and (wally[int(throwx-1)+int(throwy)*lvlW]==0 or wallx[int(throwx-1)+int(throwy)*lvlW]<=4)))): a=1
        if (throwndir=="right" and ((walldir[int(throwx+1)+int(throwy)*lvlW]==0 and wallx[int(throwx+1)+int(throwy)*lvlW]!=0 and (wally[int(throwx+1)+int(throwy)*lvlW]==0 or wallx[int(throwx+1)+int(throwy)*lvlW]<=4)))): a=1
        if (throwndir=="down" and ((walldir[int(throwx)+int(throwy+1)*lvlW]==1 and wallx[int(throwx)+int(throwy+1)*lvlW]!=0 and (wally[int(throwx)+int(throwy+1)*lvlW]==0 or wallx[int(throwx)+int(throwy+1)*lvlW]<=4)))): a=1
        if (a==1):
            for nn in range(19):
                if (item[nn]=="" and thrown!="Cards"):
                    item[nn]=thrown; itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="up"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="down"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="right"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    if (throwndir=="left"): itemx[nn]=int(throwx); itemy[nn]=int(throwy); selectx=int(throwx); selecty=int(throwy)
                    break
            thrown=""; npcani[whogoes]="End Attack"
            selectx=int(selectx); selecty=int(selecty)
        
    else:
        thrown=""; npcani[whogoes]="End Attack"; selectx=round(throwx); selecty=round(throwy)
    if (thrown!=""): #Moving thrown item
        if (throwndir=="up"): throwy-=.25; npcdir[whogoes]=0
        if (throwndir=="left"): throwx-=.25; npcdir[whogoes]=1
        if (throwndir=="right"): throwx+=.25; npcdir[whogoes]=0
        if (throwndir=="down"): throwy+=.25; npcdir[whogoes]=1
        throwdist+=.25


def showLvls():
    global showDist2
    screen.blit(menu_stats2,(80+5,220-45))
    n=0; mm=-1
    for m in range(11):
        if (npcx[m]==selectx and npcy[m]==selecty):
            mm=m
            if (lvlingup>=1): showDist2=m
            break
    if (mm==-1 or mm!=showDist2): return
    if (lvlingup>=1):
        text=font.render(str(npcside[mm])+" Lvl "+str(npclvl[mm])+" -> "+str(npclvl[mm]+1),1,WHITE)
        screen.blit(text,(80+12,220-45-5+9+20*n)); n+=1
    if (lvlingup==0):
        text=font.render(("Statistics"),1,WHITE)
        screen.blit(text,(80+12,220-45-5+9+20*n)); n+=1
    n+=1 #Stat Increase Options
    text=font2.render("Pierce",1,WHITE)
    screen.blit(text,(80+12,220-55-5+9+22*n)); n+=1
    text=font2.render("Blunt",1,WHITE)
    screen.blit(text,(80+12,220-55-5+9+22*n)); n+=1
    text=font2.render("Unarmed",1,WHITE)
    screen.blit(text,(80+12,220-55-5+9+22*n)); n+=1
    text=font2.render("Throw",1,WHITE)
    screen.blit(text,(80+12,220-55-5+9+22*n)); n+=1
    text=font2.render("Defense",1,WHITE)
    screen.blit(text,(80+12,220-55-5+9+22*n)); n+=1
    for yy in range(0,5): #Stat Icons
        for xx in range(0,20):
            if (yy==0): skill=npcpierces[mm]+skillpierces
            if (yy==1): skill=npcblunt[mm]+skillblunt
            if (yy==2): skill=npcunarmed[mm]+skillunarmed
            if (yy==4): skill=npcdefense[mm]+skilldefense
            if (yy==3): skill=npcthrowsk[mm]+skillthrowsk
            if (skill>xx): #Color of Icon
                screen.blit(staticonyel,(150+8*xx,220-5-15+9+22*yy))
            if (skill<xx):
                screen.blit(staticongray,(150+8*xx,220-5-15+9+22*yy))
            if (lvlingup>=1):
                if (skill==xx):
                    if (skillselect==yy): screen.blit(staticonblue,(150+8*xx,220-5-15+9+22*yy))
                    if (skillselect!=yy): screen.blit(staticongray,(150+8*xx,220-5-15+9+22*yy))
            else:
                if (skill==xx):
                    screen.blit(staticongray,(150+8*xx,220-5-15+9+22*yy))
    if (npcpierces[mm]+skillpierces>0):
        text=font2.render(str(npcpierces[mm]+skillpierces),1,WHITE); screen.blit(text,(80+14+220,220-55-5+32+22*1-1)) #How many points on skill
    if (npcblunt[mm]+skillblunt>0):
        text=font2.render(str(npcblunt[mm]+skillblunt),1,WHITE); screen.blit(text,(80+14+220,220-55-5+32+22*2-1))
    if (npcunarmed[mm]+skillunarmed>0):
        text=font2.render(str(npcunarmed[mm]+skillunarmed),1,WHITE); screen.blit(text,(80+14+220,220-55-5+32+22*3-1))
    if (npcdefense[mm]+skilldefense>0):
        text=font2.render(str(npcdefense[mm]+skilldefense),1,WHITE); screen.blit(text,(80+14+220,220-55-5+32+22*5-1))
    if (npcthrowsk[mm]+skillthrowsk>0):
        text=font2.render(str(npcthrowsk[mm]+skillthrowsk),1,WHITE); screen.blit(text,(80+14+220,220-55-5+32+22*4-1))

lvlingup=0
skillselect=0
skillpierces=0
skillblunt=0
skillunarmed=0
skilldefense=0
skillthrowsk=0
skillamount=0
def lvlUp():
    global selectx, selecty, updating, pressed, skillselect, up, down, lvlingup
    global skillpierces, skillblunt, skillunarmed, skilldefense, skillthrowsk, skillamount
    global levelup, levelup2, levelupdelay
    updating=2
    selectx=npcx[whogoes]; selecty=npcy[whogoes]
    
    sl=0
    if (up==1 and skillselect>0): skillselect-=1; up=0
    if (down==1 and skillselect<4): skillselect+=1; down=0
    if (npclvl[whogoes]<=4 or True): skam=3
    if (npclvl[whogoes]>7 and npclvl[whogoes]<=10): skam=2
    if (npclvl[whogoes]>10): skam=1
    if (pressed==1 and skillamount<skam): #Add a point to the Stat
        pressed=0
        if (skillselect==0 and npcpierces[whogoes]+skillpierces<20): skillpierces+=1; skillamount+=1
        if (skillselect==1 and npcblunt[whogoes]+skillblunt<20): skillblunt+=1; skillamount+=1
        if (skillselect==2 and npcunarmed[whogoes]+skillunarmed<20): skillunarmed+=1; skillamount+=1
        if (skillselect==4 and npcdefense[whogoes]+skilldefense<20): skilldefense+=1; skillamount+=1
        if (skillselect==3 and npcthrowsk[whogoes]+skillthrowsk<20): skillthrowsk+=1; skillamount+=1
    showLvls()
    if (skillamount>=skam): #Finished Adding Points to Stats
        lvlUpSure()

lmsurepp=0
def lvlUpSure():
    global lmsurepp, right, left, pressed, lmselect, skillamount, lvlingup, levelup, levelup2, levelupdelay
    global skillselect, skillpierces, skillblunt, skillunarmed, skilldefense, skillthrowsk, skillamount, updating
    screen.blit(message_name,(int(WIDTH)/2-240-2,int(HEIGHT)/2+80))
    text=font.render("Are You Sure?",1,WHITE)
    screen.blit(text,(int(WIDTH)/2-245-4,int(HEIGHT)/2+60+1))
    if (lmsurepp==0):
        text=font.render("No",1,YELLOW)
        screen.blit(text,(int(WIDTH)/2-180,int(HEIGHT)/2+6+80+1))
        text=font.render("Yes",1,WHITE)
        screen.blit(text,(int(WIDTH)/2-230,int(HEIGHT)/2+6+80+1))
    else:
        text=font.render("No",1,WHITE)
        screen.blit(text,(int(WIDTH)/2-180,int(HEIGHT)/2+6+80+1))
        text=font.render("Yes",1,YELLOW)
        screen.blit(text,(int(WIDTH)/2-230,int(HEIGHT)/2+6+80+1))
    if (right==1 or left==1):
        right=0; left=0
        lmsurepp=1-lmsurepp
    if (pressed==1):
        pressed=0
        select.play()
        if (lmsurepp==0): #Choose Stats Again
            skillpierces=0
            skillblunt=0
            skillunarmed=0
            skilldefense=0
            skillthrowsk=0
            skillamount=0
        if (lmsurepp==1): #Finish Leveling Up
            lvlingup=0
            npcpierces[whogoes]=npcpierces[whogoes]+skillpierces; skillpierces=0
            npcblunt[whogoes]=npcblunt[whogoes]+skillblunt; skillblunt=0
            npcunarmed[whogoes]=npcunarmed[whogoes]+skillunarmed; skillunarmed=0
            npcdefense[whogoes]=npcdefense[whogoes]+skilldefense; skilldefense=0
            npcthrowsk[whogoes]=npcthrowsk[whogoes]+skillthrowsk; skillthrowsk=0
            npclvl[whogoes]+=1
            npcexp[whogoes]=0
            skillamount=0; skillselect=0
            levelup=-60.0; levelup2=0.0; levelupdelay=0
            updating=5
        lmsurepp=0
        


levelup=-60.0
levelup2=0.0
levelupdelay=0
def lvlUpText():
    global selectx, selecty, updating, pressed, skillselect, up, down, lvlingup
    global levelup, levelup2, levelupdelay
    updating=2
    selectx=npcx[whogoes]; selecty=npcy[whogoes]
    n=0
    b=levelup
    for m in range(3):
        if (goingColor[m]==gotoColor[m]): gotoColor[m]=random.randint(0,255)
        if (goingColor[m]<gotoColor[m]): goingColor[m]+=1
        if (goingColor[m]>gotoColor[m]): goingColor[m]-=1
    for nn in range(8): #Text LEVEL UP
        if (nn*10<=levelup2):
            if (nn==0): letter="L"
            if (nn==1): letter="E"
            if (nn==2): letter="V"
            if (nn==3): letter="E"
            if (nn==4): letter="L"
            if (nn==5): letter=""
            if (nn==6): letter="U"
            if (nn==7): letter="P"
            text=font3.render((letter),1,WHITE)
            text1=text.copy(); text1.fill((goingColor[0],goingColor[1],goingColor[2],255), None, pygame.BLEND_RGBA_MULT)
            
            if (abs((levelup-nn*10))<=40):
                screen.blit(text1,(int(WIDTH/2)-50+12*n,int(HEIGHT/2)-50-30+(((levelup-nn*10)/12.0)**2.0))); n+=1
            else:
                screen.blit(text1,(int(WIDTH/2)-50+12*n,int(HEIGHT/2)-50-30+((40.0/12.0)**2.0))); n+=1
        
    levelup+=2 #Bounce the Text
    if (levelup+60>levelup2): levelup2=levelup+60; levelupdelay=2
    if (levelup>=175): levelup=-60
    if (levelupdelay>0): levelupdelay-=1
    if (levelupdelay<=0): lvlingup=2


day=-1
day=1
oldchapter=0
chapter=day
onface=0; onface2=0; onfacedist=200 
level="LevelMenu"
difficulty=0
endlevel=0
once=0
lmselect=0
lmsure=0
lmsurep=0
pescape=0
lmquit=0
doneparty=0
bottomfade=0
kurt=0; frederick=0; ruth=0; twins=0; matthew=0; Dinah=0; gamble=0; extra=0; jerry=0
#kurt=0; frederick=1; ruth=4; twins=2; matthew=2; Dinah=1; gamble=1; extra=1; jerry=0
lucas=0
floyd=0
lenna=0
lucas2=0; floyd2=0; lenna2=0
def displayLevelMenu():
    global leftMouse, nextLevelMenu, selectx, selecty, controlChar, lmselect, lmsure, lmsurep, bottomfade
    global level, zooming, onface, onface2, gainparty, fakegainparty, pressed, movie, showDist2, endlevel
    global mainmenu, menuselect, loadedparty, actionalready, movedalready, lucastwo, onface, alphafail, chapter
    global up, down, left, right, once, loadedparty, oldchapter, whogoes, pescape, lmquit, endreset, difficulty
    global kurt, frederick, ruth, twins, matthew, Dinah, extra, gamble, jerry
    global lucas2, floyd2, lenna2
    screen.blit(sky,(0,0))
    displayTiles() #Show Level and Party NPCs
    movie=0; controlChar=-1; a=0; mc=0; sc=0; whogoes=-1
    if (day==11): #Remove Main Characters for Story
        for n in range(11):
            if (party[n]=="Lenna" or party[n]=="Floyd"):
                party[n]=""; partyselect[n]=0
    if (day==16): #Remove Main Characters for Story
        for n in range(11):
            if (party[n]=="Lucas"):
                party[n]=""; partyselect[n]=0
    if (day==17): #Remove Main Characters for Story
        for n in range(11):
            if (party[n]=="Adam" and twins==4): party[n]=""; twins=2; partyselect[n]=0
            if (party[n]=="Evelyn" and twins==3): party[n]=""; twins=2; partyselect[n]=0
    if (day==20): #Remove Main Characters for Story
        for n in range(11):
            if (party[n]=="Floyd"): party[n]=""; partyselect[n]=0
    if (day==30 or day==40 or day==60): #Remove Main Characters for Story
        for n in range(11):
            if (party[n]=="Lenna"): party[n]=""; partyselect[n]=0
        if (day==60): partyheld[0]="Knife"
    if (day==42): #Remove Main Characters for Story
        for n in range(11):
            if (party[n]=="Floyd"): party[n]=""; partyselect[n]=0
    if (day==53 and party[1]!=""): #Remove Main Characters for Story
        endreset=1; resetNPCs(); endreset=0
    if (day==61 and party[0]!="Lenna"): #Remove Main Characters for Story
        endreset=1; resetNPCs(); endreset=0
        party[0]="Lenna"; party[1]="Floyd"; party[2]="Lucas"
    if (matthew==1): #Heal all Party
        healParty()
        matthew=2
    sy=3
    for n in range(11): #Add in the NPCs for the Menu
        if (party[n]!=""):
            npcside[n]=party[n]; npc[n]=1
            if (npcside[n]=="Winston" or npcside[n]=="Lenna" or npcside[n]=="Floyd" or npcside[n]=="Lucas"):
                npcx[n]=mc+1; npcy[n]=1; mc+=1
            else:
                if (sc>6): sc=0; sy=5
                npcx[n]=sc+1; npcy[n]=sy; sc+=1
            if (npcy[n]==1): partyselect[n]=1
            if (npcside[n]=="Ruth" and npcdead[n]==1 and ruth!=-1): ruth=-1; extra=1 #Certain Characters
            if (npcside[n]=="Adam" and npcdead[n]==1 and twins!=-1): twins=-1; extra=1 #Certain Characters
            if (npcside[n]=="Evelyn" and npcdead[n]==1 and twins!=-1): twins=-1; extra=1 #Certain Characters
            if (npcside[n]=="Kurt" and npcdead[n]==1 and extra==0): extra=1 #Certain Characters
            if (npcside[n]=="Frederick" and npcdead[n]==1 and extra==0): extra=1 #Certain Characters
            if (npcside[n]=="Matthew" and npcdead[n]==1 and extra==0): extra=1 #Certain Characters
            if (npcside[n]=="Gambler" and npcdead[n]==1 and extra==0): twins=-1 #Certain Characters
    for n in range(11): #Show stats of Party NPCs
        if (selectx==npcx[n] and selecty==npcy[n] and selectx!=0 and selecty!=0):
            loadParty(n)
            showDist2=n; a=1
            if (npcwalk[n]<=0): npcwalk[n]=1
            if (pressed==1):
                ps=0
                for m in range(11):
                    if (partyselect[m]==1 and party[m]!="Winston" and party[m]!="Lenna" and party[m]!="Floyd" and party[m]!="Lucas"): ps+=1
                if (npcy[n]!=1 and (ps<3 or partyselect[n]==1)):
                    partyselect[n]=1-partyselect[n]
                    if (kurt==1): kurt=2
                pressed=0
            if (kurt!=1 and day!=1): displayStatsMenu()
        else:
            npcwalk[n]=0
        if (a==0): 
            showDist2=-1
    if (showDist2==-1 and gainparty=="" and kurt!=1):
        if (lmselect==0 and pressed==1 and pescape==0 and lmsure==0 and lmquit==0): pressed=0; lmsure=1; lmselect=1
        if (lmselect==0 and pescape==1 and pressed==0 and lmsure==0 and lmsure==0 and bottomfade<=0): pescape=0; lmquit=1
    if (lmsure==1 and day>1): #Finished? Prompt
        screen.blit(message_name,(int(WIDTH)/2+100,int(HEIGHT)/2-60))
        text=font.render("Finished?",1,WHITE)
        screen.blit(text,(int(WIDTH)/2+110,int(HEIGHT)/2-80+1))
        if (lmsurep==0):
            text=font.render("No",1,YELLOW)
            screen.blit(text,(int(WIDTH)/2+110,int(HEIGHT)/2-60+6+1))
            text=font.render("Yes",1,WHITE)
            screen.blit(text,(int(WIDTH)/2+160,int(HEIGHT)/2-60+6+1))
        else:
            text=font.render("No",1,WHITE)
            screen.blit(text,(int(WIDTH)/2+110,int(HEIGHT)/2-60+6+1))
            text=font.render("Yes",1,YELLOW)
            screen.blit(text,(int(WIDTH)/2+160,int(HEIGHT)/2-60+6+1))
        if (right==1 or left==1):
            right=0; left=0
            lmsurep=1-lmsurep
        if (pressed==1):
            pressed=0; lmsure=0
            if (lmsurep==0): lmselect=0
            if (lmsurep==1): lmselect=1
            lmsurep=0
    if (lmsure==1 and day==1): #Difficulty
        screen.blit(message_name,(int(WIDTH)/2+100,int(HEIGHT)/2-60))
        text=font.render("Choose a Difficult",1,WHITE)
        screen.blit(text,(int(WIDTH)/2+110-40,int(HEIGHT)/2-80-15+1))
        text=font.render("This Cannot be Changed",1,WHITE)
        screen.blit(text,(int(WIDTH)/2+110-60,int(HEIGHT)/2-80+1))
        if (lmsurep==0):
            text=font.render("Easy",1,YELLOW)
            screen.blit(text,(int(WIDTH)/2+110-3,int(HEIGHT)/2-60+6+1))
            text=font.render("Hard",1,WHITE)
            screen.blit(text,(int(WIDTH)/2+160-3,int(HEIGHT)/2-60+6+1))
            text=font.render("Main Characters will be Healed",1,WHITE)
            screen.blit(text,(int(WIDTH)/2+110-85,int(HEIGHT)/2-80+50+1))
        else:
            text=font.render("Easy",1,WHITE)
            screen.blit(text,(int(WIDTH)/2+110-3,int(HEIGHT)/2-60+6+1))
            text=font.render("Hard",1,YELLOW)
            screen.blit(text,(int(WIDTH)/2+160-3,int(HEIGHT)/2-60+6+1))
            text=font.render("All Damage is Permanent",1,WHITE)
            screen.blit(text,(int(WIDTH)/2+120-70,int(HEIGHT)/2-80+50+1))
        if (right==1 or left==1):
            right=0; left=0
            lmsurep=1-lmsurep
        if (pressed==1):
            pressed=0; lmsure=0
            if (lmsurep==0): difficulty=0; lmselect=1
            if (lmsurep==1): difficulty=1; lmselect=1
            lmsurep=0
    if (lmquit==1): #Quit? Prompt
        screen.blit(message_name,(int(WIDTH)/2-100-70,int(HEIGHT)/2-60))
        text=font.render("Quit?",1,WHITE)
        screen.blit(text,(int(WIDTH)/2-110-32,int(HEIGHT)/2-80+1))
        if (lmsurep==0):
            text=font.render("No",1,YELLOW)
            screen.blit(text,(int(WIDTH)/2-160,int(HEIGHT)/2-60+6+1))
            text=font.render("Yes",1,WHITE)
            screen.blit(text,(int(WIDTH)/2-110,int(HEIGHT)/2-60+6+1))
        else:
            text=font.render("No",1,WHITE)
            screen.blit(text,(int(WIDTH)/2-160,int(HEIGHT)/2-60+6+1))
            text=font.render("Yes",1,YELLOW)
            screen.blit(text,(int(WIDTH)/2-110,int(HEIGHT)/2-60+6+1))
        if (right==1 or left==1):
            right=0; left=0
            lmsurep=1-lmsurep
        if (pressed==1):
            pressed=0; lmsure=0
            if (lmsurep==0): lmquit=0
            if (lmsurep==1): #Exit to Main Menu
                lmquit=0
                onface=0
                pressed=0; alphafail=1; chapter=oldchapter
                zooming=1
                resetNPCs()
                level="LevelMenu"
                mainmenu=1; menuselect=0; loadedparty=0; actionalready=0; movedalready=0; lucastwo=0
                if (mute==0): ambient.play(-1)
            lmsurep=0
    if (pescape==1): pescape=0
        
    if (day==1 or day==3): #Show Bottom Events and Faces *0=Lenna *1=Floyd *2=Winston *3=Lucas *4=Mystery *5=Green *6=Red
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
    if (day==2):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48)) 
    if (day==4):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48))
    if (day==5):
        a=2
        for n in range(a):
            if (n==0 and kurt==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and kurt>=1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
    if (day==6 or day==7):
        a=3
        for n in range(a):
            if (n==0 and frederick==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and frederick>=1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1 and ruth==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==1 and ruth>=1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==2 and day==6): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
            if (n==2 and day==7): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
    if (day==8):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==9):
        a=2
        for n in range(a):
            if (n==0 and ruth==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==0 and ruth==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and ruth==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==0 and (ruth==-1 or ruth==0)): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==10):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
    if (day==11):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==12):
        a=3
        for n in range(a):
            if (n==0 and twins==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and twins==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1 and matthew==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==1 and matthew>=1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==13):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==14):
        a=2
        for n in range(a):
            if (n==0 and ruth==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and ruth==3): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==0 and (ruth==-1 or ruth==0 or ruth==1)): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
    if (day==15):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==16):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))  
    if (day==17 or day==18):
        a=3
        for n in range(a):
            if (n==0 and twins==0 or matthew==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==0 and twins==1 and matthew==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))  
            if (n==0 and twins>=2 and matthew==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1 and Dinah==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==1 and Dinah==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==2 and day==17): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
            if (n==2 and day==18): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48))
    if (day==19):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))        
    if (day==20):
        a=2
        for n in range(a):
            if (n==0 and ruth<3): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==0 and ruth==3): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and ruth==4): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48)) 
    if (day==21):
        a=3
        for n in range(a):
            if (n==0 and gamble==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and gamble==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1 and extra==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==1 and extra==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==1 and extra==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48)) 
    if (day==22):
        a=2
        for n in range(a):
            if (n==0 and extra==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==0 and extra==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and extra==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48))
    if (day==23):
        a=5
        for n in range(a):
            if (n==0 and ruth<4): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and ruth==4): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and ruth==5): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1 and lucas>=2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
            if (n==1 and lucas<2):  screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*(3+7),92,48))
            if (n==2 and floyd>=2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
            if (n==2 and floyd<2):  screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*(1+7),92,48))
            if (n==3 and lenna>=2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48))
            if (n==3 and lenna<2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*(0+7),92,48))
            if (n==4 and lucas<2 and floyd<2 and lenna<2):    screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
            if (n==4 and (lucas>=2 or floyd>=2 or lenna>=2)): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*(2+7),92,48))
    if (day==30):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==31):
        a=2
        for n in range(a):
            if (n==0 and twins<2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==0 and twins==2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and twins>2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48)) 
    if (day==32):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
    if (day==40):
        a=2
        for n in range(a):
            if (n==0 and jerry==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            #if (n==0 and jerry==0 and twins!=2): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==0 and jerry!=0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
    if (day==41):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
    if (day==42):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
    if (day==43):
        a=3
        for n in range(a):
            if (n==0 and lenna2==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48))
            if (n==1 and floyd2==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
            if (n==2 and lucas2==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*3,92,48))
            if (n==0 and lenna2==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*7,92,48))
            if (n==1 and floyd2==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*11,92,48))
            if (n==2 and lucas2==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*10,92,48))
    if (day==44):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
    if (day==45):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*1,92,48))
    if (day==50):
        a=2
        for n in range(a):
            if (n==0 and twins<2 or gamble==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*6,92,48))
            if (n==0 and twins==2 and gamble==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
            if (n==0 and twins>2 and gamble==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*5,92,48))
            if (n==1): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48))
    if (day==51):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*4,92,48))
    if (day==52):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*0,92,48))
    if (day==53):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
    if (day==60):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
    if (day==61):
        a=1
        for n in range(a):
            if (n==0): screen.blit(message_portrait,(WIDTH/2-40+n*onfacedist-onface2,HEIGHT-100),(0,48*2,92,48))
    if (gainparty==""):
        if (pressed==1 and lmselect==1 and lmsure==0): #Entered over a Face
            for n in range(11): #Load Up Party Stats
                loadParty(n)
            if (day==1 and onface==0): zooming=1; level="Floor" #Winston
            if (day==2 and onface==0): zooming=1; level="Murder" #???
            if (day==3 and onface==0): zooming=1; level="Accused"; gainparty="Lenna" #Winston
            if (day==4 and onface==0): zooming=1; level="Fight" #Lenna
            if (day==5 and onface==1): zooming=1; level="Outside"; gainparty="Floyd" #Floyd
            if (day==5 and onface==0 and kurt==0): zooming=1; level="Kurt"; gainparty="Kurt"; kurt=1 #Kurt
            if ((day==6 or day==7) and onface==0 and frederick==0): zooming=1; level="Frederick"; gainparty="Frederick"; frederick=1 #Frederick
            if ((day==6 or day==7) and onface==1 and ruth==0): zooming=1; level="Ruth"; gainparty="Ruth"; ruth=1 #Ruth
            if (day==6 and onface==2): zooming=1; level="Lucas" #Lucas
            if (day==7 and onface==2): zooming=1; level="Ambush"; gainparty="Lucas" #Winston
            if (day==8 and onface==0): zooming=1; level="Blackmail" #Lucas
            if (day==9 and onface==0 and ruth==1): zooming=1; level="Ruth1"; ruth=2 #Ruth
            if (day==9 and onface==1): zooming=1; level="Break" #Lucas
            if (day==10 and onface==0): zooming=1; level="Split" #Winston
            if (day==11 and onface==0): zooming=1; level="Main" #Lucas
            if (day==12 and onface==0 and twins==0): zooming=1; level="Twins"; gainparty="Adam and Evelyn"; twins=1 #Twins
            if (day==12 and onface==1 and matthew==0): zooming=1; level="Matthew"; gainparty="Matthew"; matthew=1 #Matthew
            if (day==12 and onface==2): zooming=1; level="Jerry" #Lucas
            if (day==13 and onface==0): zooming=1; level="Questions" #Lucas
            if (day==14 and onface==0 and ruth==2): zooming=1; level="Ruth2"; ruth=3 #Ruth
            if (day==14 and onface==1): zooming=1; level="Save"; gainparty="Floyd" #Floyd
            if (day==15 and onface==0): zooming=1; level="Gone" #Lucas
            if (day==16 and onface==0): zooming=1; level="Weapons"; loseItems() #Floyd
            if ((day==17 or day==18) and onface==0 and twins==1 and matthew==2): zooming=1; level="Choose"; twins=2 #Twins
            if ((day==17 or day==18) and onface==1): zooming=1; level="Dinah"; gainparty="Dinah"; Dinah=1 #Dinah
            if (day==17 and onface==2): zooming=1; level="Brawl" #Floyd
            if (day==18 and onface==2): zooming=1; level="Report" #Lenna
            if (day==19 and onface==0): zooming=1; level="Idea"; gainparty="Lenna" #Floyd
            if (day==20 and onface==0 and ruth==3): zooming=1; level="Ruth3"; ruth=4 #Ruth
            if (day==20 and onface==1): zooming=1; level="Memory" #Lenna
            if (day==21 and onface==0 and gamble==0): zooming=1; level="Gamble"; gainparty="Gambler"; gamble=1 #Gambler
            if (day==21 and onface==1 and extra==1): zooming=1; level="Extra"; gainparty="David"; extra=2 #David
            if (day==21 and onface==2): zooming=1; level="Lab" #Lenna
            if (day==22 and onface==0 and extra==1): zooming=1; level="Extra"; gainparty="David"; extra=2 #David
            if (day==22 and onface==1): zooming=1; level="Talk" #Lenna
            if (day==23 and onface==0 and ruth<4): zooming=1; level="NoRuth"; ruth=5 #Winston
            if (day==23 and onface==0 and ruth==4): zooming=1; level="Ruth4"; ruth=5 #Ruth
            if (day==23 and onface==1 and lucas>=2): zooming=1; level="LucasChoice"; gainparty="Lucas" #Lucas
            if (day==23 and onface==2 and floyd>=2): zooming=1; level="FloydChoice"; gainparty="Floyd" #Floyd
            if (day==23 and onface==3 and lenna>=2): zooming=1; level="LennaChoice" #Lenna
            if (day==23 and onface==4 and lenna<2 and lucas<2 and floyd<2): zooming=1; level="WinstonChoice" #Winston
            #LucasChoice
            if (day==30 and onface==0): zooming=1; level="Lobby" #Lucas
            if (day==31 and onface==0 and twins==2): zooming=1; level="Sanders"; gainparty="Sanders"; twins=3 #Sanders
            if (day==31 and onface==1): zooming=1; level="Friends" #Lucas
            if (day==32 and onface==0): zooming=1; level="Escape" #Lucas
            #FloydChoice
            if (day==40 and onface==0 and jerry==0): zooming=1; level="Jerry2"; gainparty="Jerry"; jerry=1 #Jerry
            if (day==40 and onface==1): zooming=1; level="Climb" #Floyd
            if (day==41 and onface==0): zooming=1; level="Summit" #Floyd
            if (day==42 and onface==0): zooming=1; level="Wake" #Floyd
            if (day==43 and onface==0 and lenna2==0): zooming=1; level="Speechless"; lenna2=1 #Lenna
            if (day==43 and onface==1 and floyd2==0): zooming=1; level="World"; gainparty="Floyd"; floyd2=1 #Floyd
            if (day==43 and onface==2 and lucas2==0): zooming=1; level="Confusion"; lucas2=1 #Lucas
            if (day==44 and onface==0): zooming=1; level="Unity" #Lucas
            if (day==45 and onface==0): zooming=1; level="Watchers" #Lucas
            #LennaChoice
            if (day==50 and onface==0 and twins==2 and gamble==1): zooming=1; level="Robot"; twins=3; gainparty="Madison and Robot" #Lenna
            if (day==50 and onface==1): zooming=1; level="Experiment" #Lenna
            if (day==51 and onface==0): zooming=1; level="Science" #Scientist
            if (day==52 and onface==0): zooming=1; level="Device" #Lenna
            if (day==53 and onface==0): zooming=1; level="Reset" #Winston
            #WinstonChoice
            if (day==60 and onface==0): zooming=1; level="Truth" #Winston
            if (day==61 and onface==0): zooming=1; level="TrueEnd" #Everyone
            if (zooming==1): oldchapter=chapter
            lmselect=0; pressed=0; endlevel=0
        if (right==1 and onface<a-1 and onface*onfacedist==onface2 and lmselect==1 and lmsure==0): onface+=1
        if (left==1 and onface>0 and onface*onfacedist==onface2 and lmselect==1 and lmsure==0): onface-=1

        if (kurt==1 and gainparty==""): #Sent Party Members into Battle
            screen.blit(message,(WIDTH/2-250,HEIGHT/2-100-100))
            text=font.render("Press [Enter] over party members to set them",1,WHITE)
            screen.blit(text,(WIDTH/2-250+20,HEIGHT/2-100+10-100+1))
            text=font.render("as Active for battles. Certain characters",1,WHITE)
            screen.blit(text,(WIDTH/2-250+20,HEIGHT/2-100+30-100+1))
            text=font.render("cannot be unselected.",1,WHITE)
            screen.blit(text,(WIDTH/2-250+20,HEIGHT/2-100+50-100+1))
        if (day==1): #Sent Party Members into Battle
            screen.blit(message,(WIDTH/2-250,HEIGHT/2-100-100))
            text=font.render("Press [Enter] over a blank space to select a",1,WHITE)
            screen.blit(text,(WIDTH/2-250+20,HEIGHT/2-100+10-100+1))
            text=font.render("chapter to advance to.",1,WHITE)
            screen.blit(text,(WIDTH/2-250+20,HEIGHT/2-100+30-100+1))
            text=font.render("",1,WHITE)
            screen.blit(text,(WIDTH/2-250+20,HEIGHT/2-100+50-100+1))
        if (lmselect==1 and lmsure==0): #Bottom Fade
            if (bottomfade<200): bottomfade+=10
        else:
            if (bottomfade>0): bottomfade-=10
                
    else: #Show who has entered the party
        if (level=="LevelMenu" or level==""):
            screen.blit(message,(WIDTH/2-250,HEIGHT/2-100))
            text=font.render("The following character(s) have joined your party:",1,WHITE)
            screen.blit(text,(WIDTH/2-250+20,HEIGHT/2-100+10+1))
            if (gainparty!=""):
                text=font.render(str(gainparty),1,YELLOW)
                screen.blit(text,(WIDTH/2-len(gainparty)*5,HEIGHT/2-100+20+20+1))
        if (pressed==1):
            pressed=0; gainparty=""
    if (onface*onfacedist>onface2): onface2+=20
    if (onface*onfacedist<onface2): onface2-=20
    screen.blit(menu_levelbottom,(0,HEIGHT-160))
    screen.blit(menu_levelbottom2,(0,HEIGHT-160+bottomfade))
    if (day<30 and day!=23):
        text=font.render("Chapter "+str(day),1,WHITE)
        screen.blit(text,(WIDTH/2-36,50))
    if (day==23):
        text=font.render("The Choice",1,WHITE)
        screen.blit(text,(WIDTH/2-36,50))        
    if (day>=30 and day<40):
        text=font.render("Lucas Route",1,WHITE)
        screen.blit(text,(WIDTH/2-36-10,50))
    if (day>=40 and day<50):
        text=font.render("Floyd Route",1,WHITE)
        screen.blit(text,(WIDTH/2-36-10,50))
    if (day>=50 and day<60 and day!=53):
        text=font.render("Lenna Route",1,WHITE)
        screen.blit(text,(WIDTH/2-36-10,50))
    if (day>=60 and day<70):
        text=font.render("Winston Route",1,WHITE)
        screen.blit(text,(WIDTH/2-36-25,50))
    if (day==53):
        text=font.render("Chapter 1",1,WHITE)
        screen.blit(text,(WIDTH/2-36-10,50))
    if (lmselect==1 or gainparty!=""): up=0; down=0; left=0; right=0
    selectCamera()




def displayZoom():
    global mapArea, zooming, mainmenu, menuselect, loadedparty, actionalready, movedalready, lucastwo, alphafail
    global zoom, fade, rotDir, event00, level, pressed, chapter, day, menuselect, whiteflash, shortmove, loadinggame
    global nextLevelMenu, sky, updating, dorandomizeItems, tileset, tilewall, once, onface, onface2, lagging
    global cansave
    if (zooming==1):
        lagging=0; endreset=0
        if (whiteflash==255):
            miscwhite.set_alpha(int(255))
            screen.blit(miscwhite,(0,0))
            whiteflash=0
        if (day==33): #Escape
            fade=0; screen.blit(misc,(0,0)); EndGame(); endreset=1; menuselect=1
            pressed=0; alphafail=1; chapter=oldchapter
            zooming=1
            #resetNPCs()
            level="LevelMenu"; day=1
            mainmenu=1; menuselect=1; loadedparty=0; actionalready=0; movedalready=0; lucastwo=0
        if (day==46): #Watchers
            fade=0; screen.blit(misc,(0,0)); EndGame(); endreset=1; menuselect=1
            pressed=0; alphafail=1; chapter=oldchapter
            zooming=1
            #resetNPCs()
            level="LevelMenu"; day=1
            mainmenu=1; menuselect=1; loadedparty=0; actionalready=0; movedalready=0; lucastwo=0
        if (day==54): #Reset
            fade=0; screen.blit(misc,(0,0)); EndGame(); endreset=1; menuselect=1
            pressed=0; alphafail=1; chapter=oldchapter
            zooming=1
            #resetNPCs()
            level="LevelMenu"; day=1
            mainmenu=1; menuselect=1; loadedparty=0; actionalready=0; movedalready=0; lucastwo=0
        if (day==62): #Reset
            fade=0; screen.blit(misc,(0,0)); EndGame(); endreset=1; menuselect=1
            pressed=0; alphafail=1; chapter=oldchapter
            zooming=1
            #resetNPCs()
            level="LevelMenu"; day=1
            mainmenu=1; menuselect=1; loadedparty=0; actionalready=0; movedalready=0; lucastwo=0
        pygame.image.save(screen,"Images/trash.jpeg") #Screenshot for Zooming
        zoom=pygame.image.load("Images/trash.jpeg").convert_alpha()
        rotDir=random.randint(0,1)
        once=1; onface=0; onface2=0; shortmove=0; movedalready=0; actionalready=0
        for n in range(11):
            npc[n]=0
        resetDialogue()
        zooming=2; dorandomizeItems=0
        for n in range(19):
            if (item[n]!=""): item[n]=""
        if (level==""):
            level="LevelMenu"
            #cansave=0
            #saveGame()
        loadLevel()
        if (loadinggame==1): loadGame(); loadinggame=0
        if (dorandomizeItems==1): randomizeItems()
    if (WIDTH-zooming*4>0 and HEIGHT-zooming*4>0): #Rotate and Scale
        zoom2=pygame.transform.scale(zoom,(int(WIDTH+zooming*4),int(HEIGHT-zooming*4)))
        oldCenter=zoom2.get_size()
        if (rotDir==0): zoomRot=pygame.transform.rotate(zoom2,zooming/12)
        if (rotDir==1): zoomRot=pygame.transform.rotate(zoom2,-zooming/12)
        rect=zoomRot.get_rect()
        rect.center=oldCenter
        screen.blit(zoomRot,(rect[0]-oldCenter[0]/2,rect[1]-oldCenter[1]/2),(oldCenter[0]/2-WIDTH/2,oldCenter[1]/2-HEIGHT/2,oldCenter[0]/2+WIDTH,oldCenter[1]/2+HEIGHT))
    zooming+=3.0
    fade+=8.0
    if (fade>=255): #Reset level after Zoom
        event00=""
        zooming=0
        if (nextLevelMenu==2):
            nextLevelMenu=0
        if (nextLevelMenu==0):
            b=random.randint(0,3)
            for n in range(lvlW*lvlH):
                a=random.randint(0,1)
                tilez[n]=random.randint(HEIGHT,maxz)
                if (b==2): tilez[n]=maxz
                if (a==0): tilez[n]=-tilez[n]
                if (b==0): tilez[n]=maxz
                if (b==1): tilez[n]=-maxz
                if (zoominlevel==0): tilez[n]=0
                tilez[n]=0 #Nevermind...
                if (level=="Floor21"): tilez[n]=-maxz
                if (level=="Floor85"): tilez[n]=maxz
        if (nextLevelMenu==1):
            if (day>=42 and day<50):
                sky=pygame.image.load("Images/skyorange.png").convert_alpha()
                tileset=pygame.image.load("Images/isotileset.png").convert_alpha()
                tilewall=pygame.image.load("Images/isowall.png").convert_alpha()
            else:
                sky=pygame.image.load("Images/skyblue.png").convert_alpha()
            nextLevelMenu=2
            if (mainmenu==1): nextLevelMenu=0


def saveGame():
    global kurt, frederick, ruth, twins, matthew, Dinah, gamble, extra, lucas, floyd, lenna
    save = open("Images/Save.txt", "w") #Erases old file and writes new
    save.write(str(day)+"\n")
    save.write(str(kurt)+"\n")
    save.write(str(frederick)+"\n")
    save.write(str(ruth)+"\n")
    save.write(str(twins)+"\n")
    save.write(str(matthew)+"\n")
    save.write(str(Dinah)+"\n")
    save.write(str(gamble)+"\n")
    save.write(str(extra)+"\n")
    save.write(str(jerry)+"\n")
    save.write(str(lucas)+"\n")
    save.write(str(floyd)+"\n")
    save.write(str(lenna)+"\n")
    save.write(str(lucas2)+"\n")
    save.write(str(floyd2)+"\n")
    save.write(str(lenna2)+"\n")
    for n in range(21):
        save.write(str(party[n])+"%"+str(int(partyblood[n]))+"%"+str(partyartery[n])+"%"+str(partypara[n])+"%"+str(partyforehead[n])+"%"+str(partyeyes[n])+"%"+str(partynose[n])+"%"+str(partymouth[n])+"%"+str(partyjaw[n])+"%"+str(partytemple[n])+"%"+str(partyneck[n])+"%"+str(partybrain[n])+"%"+str(partyskull[n])+"%"+str(partychest[n])+"%"+str(partychest2[n])+"%"+str(partylungs[n])+"%"+str(partyheart[n])+"%"+str(partyspine[n])+"%"+str(partyback[n])+"%"+str(partygut[n])+"%"+str(partygut2[n])+"%"+str(partyrightarm[n])+"%"+str(partyrighthand[n])+"%"+str(partyleftarm[n])+"%"+str(partylefthand[n])+"%"+str(partyrightleg[n])+"%"+str(partyleftleg[n])+"%"+str(partyexp[n])+"%"+str(partylvl[n])+"%"+str(partypierces[n])+"%"+str(partyblunt[n])+"%"+str(partyunarmed[n])+"%"+str(partydefense[n])+"%"+str(partythrowsk[n])+"%"+str(partyheld[n])+"%")
    save.close()
    return

def loadGame():
    global kurt, frederick, ruth, twins, matthew, Dinah, gamble, extra, jerry, lucas, floyd, lenna
    global day
    global lucas2, floyd2, lenna2
    load = open("Images/Save.txt", "r")
    day=int(load.readline())
    kurt=int(load.readline())
    frederick=int(load.readline())
    ruth=int(load.readline())
    twins=int(load.readline())
    matthew=int(load.readline())
    Dinah=int(load.readline())
    gamble=int(load.readline())
    extra=int(load.readline())
    jerry=int(load.readline())
    lucas=int(load.readline())
    floyd=int(load.readline())
    lenna=int(load.readline())
    lucas2=int(load.readline())
    floyd2=int(load.readline())
    lenna2=int(load.readline())
    chars=load.readline()
    for n in range(21):
        for times in range(0,35):
            t=0
            for nn in chars:
                t=t+1
                if (nn=="%"):
                    cut=chars[:t-1]
                    if (times==0): party[n]=str(cut)
                    if (times==1): partyblood[n]=int(cut)
                    if (times==2): partyartery[n]=int(cut)
                    if (times==3): partypara[n]=int(cut)
                    if (times==4): partyforehead[n]=int(cut)
                    if (times==5): partyeyes[n]=int(cut)
                    if (times==6): partynose[n]=int(cut)
                    if (times==7): partymouth[n]=int(cut)
                    if (times==8): partyjaw[n]=int(cut)
                    if (times==9): partytemple[n]=int(cut)
                    if (times==10): partyneck[n]=int(cut)
                    if (times==11): partybrain[n]=int(cut)
                    if (times==12): partyskull[n]=int(cut)
                    if (times==13): partychest[n]=int(cut)
                    if (times==14): partychest2[n]=int(cut)
                    if (times==15): partylungs[n]=int(cut)
                    if (times==16): partyheart[n]=int(cut)
                    if (times==17): partyspine[n]=int(cut)
                    if (times==18): partyback[n]=int(cut)
                    if (times==19): partygut[n]=int(cut)
                    if (times==20): partygut2[n]=int(cut)
                    if (times==21): partyrightarm[n]=int(cut)
                    if (times==22): partyrighthand[n]=int(cut)
                    if (times==23): partyleftarm[n]=int(cut)
                    if (times==24): partylefthand[n]=int(cut)
                    if (times==25): partyrightleg[n]=int(cut)
                    if (times==26): partyleftleg[n]=int(cut)
                    if (times==27): partyexp[n]=int(cut)
                    if (times==28): partylvl[n]=int(cut)
                    if (times==29): partypierces[n]=int(cut)
                    if (times==30): partyblunt[n]=int(cut)
                    if (times==31): partyunarmed[n]=int(cut)
                    if (times==32): partydefense[n]=int(cut)
                    if (times==33): partythrowsk[n]=int(cut)
                    if (times==34): partyheld[n]=str(cut)
                    chars=chars[t:]
                    break
    return


def blurZoom():
    global zoom
    scale = 1.0/1
    surf_size = screen.get_size()
    scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
    zoom = pygame.transform.smoothscale(screen, scale_size)
    zoom = pygame.transform.smoothscale(zoom, surf_size)

updating=1
lagging=0
laggingcount=0
def updateScreen():
    global updating, lagging, updatefix, laggingcount
    a=0
    if (int(Clock.get_fps())<45 and part>1 and lagging==0): laggingcount+=1
    if (laggingcount>60): laggingcount=0 #lagging
    
    if (camerax!=selectx*1.0 or cameray!=selecty*1.0 or mainmenu==1 or nextLevelMenu>0 or fade>0 or pressed==1): a=1
    if (choice1[part]!="" or choice2[part]!="" or choice3[part]!=""): a=1
    if (a==0):
        if (updating>=1):
            updating-=1
            a=2
    if (a>=1 and (updatefix==1 or lagging==0)): #Update Screen
        if (a==1): updating=2
        pygame.display.update()
    if (a==0 and (lagging==0 or (updating>0 and updatefix==1))):
        for nn in range(11): #NPC Update
            if (npc[nn]>0):
                z=tilez[int(npcx[nn]+npcy[nn]*lvlW)]
                pygame.display.update(pygame.Rect(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10,si,si))
            if (nn==whogoes and npc[nn]>0):
                z=tilez[int(npcx[nn]+npcy[nn]*lvlW)]
                pygame.display.update(pygame.Rect(npcx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-npcy[nn]*18+380  ,  npcy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+npcx[nn]*9+290+npcz[nn]+z-10-50,si,50))                
        for nn in range(19): #Item Update
            if (item[nn]!=""):
                z=tilez[int(itemx[nn]+itemy[nn]*lvlW)]
                pygame.display.update(pygame.Rect(itemx[nn]*.5*si-int(camerax*si*.5-cameray*si*.5)-itemy[nn]*18+380  ,  itemy[nn]*.25*si-int(camerax*si*.25+cameray*si*.25)+itemx[nn]*9+290+npcz[nn]+z-10,si,si))                
        if (showDist>-1): #Pathfinder Tiles
            for n in range(lvlW*lvlH):
                if (tilefill[n]>0):
                    pygame.display.update(pygame.Rect((n%lvlW)*.5*si-int(camerax*si*.5-cameray*si*.5)-int(n/lvlW)*18+380  ,  int(n/lvlW)*.25*si-int(camerax*si*.25+cameray*si*.25)+(n%lvlW)*9+290+z,si,si))
        z=tilez[int(selectx+selecty*lvlW)] #Selector Update
        n=selectx+selecty*lvlW
        pygame.display.update(pygame.Rect((n%lvlW)*.5*si-int(camerax*si*.5-cameray*si*.5)-int(n/lvlW)*18+380  ,  int(n/lvlW)*.25*si-int(camerax*si*.25+cameray*si*.25)+(n%lvlW)*9+290+z,36,36))
        if (chat1[part]!="" or chat2[part]!="" or chat3[part]!=""): #Update Chat
            pygame.display.update(pygame.Rect(0,395,WIDTH,HEIGHT-395))
        if (actionmenu==1): #Update Action Menu
            pygame.display.update(pygame.Rect(200,220,150,150))
        if (showDist2>-1): #Update Stats Menu
            pygame.display.update(pygame.Rect(230+230,220-45,200,250))
    if (updatefix==1): updatefix=0

gameintro=1
intropart=0
introdel=120
covery=0
ambient.play(-1)
def gameIntro():
    global fade, intropart, gameintro, introdel
    if (intropart==0):
        text = font.render("Created by Alex Elson", True, (255,255,255)); screen.blit(text, (WIDTH/2-80,HEIGHT/2)) #Display Text
        screen.blit(cover,(-60,HEIGHT-370-introdel))
        screen.blit(introblack,(0,0-int(introdel)*1.5))
        introdel+=4
        if (introdel>=HEIGHT): intropart=1; introdel=0
    if (intropart==1):
        if (introdel<WIDTH*.2):
            text = font.render("Created by Alex Elson", True, (255,255,255)); screen.blit(text, (WIDTH/2-80,HEIGHT/2)) #Display Text
        if (introdel>WIDTH*.4):
            text = font.render("Music by Josh Jacobs", True, (255,255,255)); screen.blit(text, (WIDTH/2-80,HEIGHT/2)) #Display Text
        screen.blit(cover,(int(introdel)*.4,HEIGHT/2-185))
        if (introdel<WIDTH*.4):
            text = font.render("Created by Alex Elson", True, (255,255,255)); screen.blit(text, (WIDTH/2-80,HEIGHT/2)) #Display Text
        screen.blit(cover,(WIDTH-int(introdel)*2,HEIGHT/2-185))
        screen.blit(introblack,(WIDTH-int(introdel)*1.5,0))
        screen.blit(introblack,(int(introdel)*4,0))
        screen.blit(introblack,(WIDTH/2+100,-HEIGHT*3+introdel))
        introdel+=5
        if (introdel>=WIDTH*2.25): intropart=2; introdel=0
    if (intropart==2):
        text = font.render("Music by Josh Jacobs", True, (255,255,255)); screen.blit(text, (WIDTH/2-80,HEIGHT/2)) #Display Text
        screen.blit(cover2,(0,-100-int(introdel/4)))
        screen.blit(introblack,(0,-HEIGHT/2-introdel))
        screen.blit(introblack,(0,HEIGHT/2+introdel))
        screen.blit(introblack,(WIDTH*4-introdel*4,0))
        introdel+=2
        if (introdel>=WIDTH): intropart=3; introdel=0
    if (intropart==3):
        fade=fade+8
        if (fade>=255): fade=255; intropart=0; introdel=0; gameintro=0

    
mainLoop=True
while mainLoop:
    Clock.tick(fps)
    screen.fill((0,0,0))
    mx,my=pygame.mouse.get_pos()
    fpsfix=60.0/fps

    if (gameintro==1):
        gameIntro()
    else:
        if (zooming<=1):
            if (nextLevelMenu==2):
                displayLevelMenu()
            if (nextLevelMenu<=1):
                if (mainmenu==0 and zooming<=1):
                    displaySky()
                    displayTiles()
                    if (level=="Summit" or level=="TrueEnd"): displayRain()
                    if (day>=43 and day<50 and level!="" and level!="LevelMenu" and level!="Watchers"): displayDust()
                    npcEffects()
                    if (level!="Floor" and level!="Accused" and lvlingup==0): storyTriggers()
                    if (bodymenu>=0): displayBodyMenu()
                    if (actionmenu==1 and lvlingup==0 and showskillsgoes==0): displayActionMenu()
                    if (showDist2>-1): displayStatsMenu()
                    if (thrown!=""): thrownAlready()
                    selectCamera()
                    if (speaker[part]!="" and delay<=0 and (level!="TrueEnd" or part>=10)): displayChat()
                    if ((tutorialmove==1 or tutorialhurt==1 or tutorialpick==1 or tutorialthrow==1 or tutorialarms==1) and part==controlChar): displayTutorial()
                    if (part==controlChar): displayEvents()
                    waterWave+=.05
                    if (waterWave>1000000.0): waterWave=0.0
                    if (delay>0): delay-=1
                    if (delay2>0): delay2-=1
                    if (delay4>0): delay4-=1            
                    if (part==0): nextMessage()
                    if (delay2<=0 and partdelay[part]>0): nextMessage()
                    if (part==failurepart): Failure()
                    if (level=="Escape"): Flash()
                    if (level=="Summit"): Flash()
                    if (level=="Device"): Flash()
                if (mainmenu==1 and alphafail!=1):
                    displayMainMenu()
                if (mainmenu==1 and alphafail==1):
                    alphafail=0
                if (lvlingup==1): lvlUpText()
                if (lvlingup==2): lvlUp()
                if (skipped==1): skipped=0
        if (zooming>0):
            displayZoom()
        
    displayFade()
    if (level=="TrueEnd" and part<10 and speaker[part]!="" and delay<=0): displayChat()
    if (day==33 and level=="Escape"): EndGame()
    if (day==46 and level=="Watchers"): EndGame()
    if (day==54 and level=="Reset"): EndGame()
    if (day==62 and level=="TrueEnd"): EndGame()
    if (day!=33 and day!=46 and day!=54 and day!=62 and level!="Escape" and level!="Watchers" and level!="Reset" and level!="TrueEnd"): endreset=0
    
    leftMouse=0

    for event in pygame.event.get():
        
        if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1): #Left Mouse Click
            leftMouse=1
        elif (event.type==pygame.MOUSEBUTTONUP and event.button==1): #Left Mouse Up
            None
        elif (event.type==KEYDOWN): #Pressing Keys
            if (event.key==K_UP): up=1; delaycam=0
            if (event.key==K_DOWN): down=1; delaycam=0
            if (event.key==K_LEFT): left=1; delaycam=0
            if (event.key==K_RIGHT): right=1; delaycam=0
            if (event.key==K_RETURN): pressed=1; delaycam=0; updating=2; textspeed=10.5
        elif (event.type==KEYUP): #Lifting Keys
            if (event.key==K_UP): up=0; delay2b=0
            if (event.key==K_DOWN): down=0; delay2b=0
            if (event.key==K_LEFT): left=0; delay2b=0
            if (event.key==K_RIGHT): right=0; delay2b=0
            if (event.key==K_RETURN):
                pressed=0; textspeed=10.5
                if (nextDialogue==1 and mainmenu==0 and moved==0 and choice1[part]==""): nextMessage()
                if (zooming<=0 and fade<=0):
                    None
            if (event.key==K_BACKSPACE and lmsure==0): showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1; lmselect=0; lmsure=0
            if (event.key==K_ESCAPE and lmsure==0): showDist=-1; showDist2=-1; updating=2; am_actions=0; showPaths=0; actionselect=0; bodyselect=0; openbody=-1; bodymenu=-1; lmselect=0; lmsure=0
            if (event.key==K_ESCAPE and gameintro==0 and level=="LevelMenu"): pescape=1
            if (event.key==K_ESCAPE and gameintro==1 and intropart!=3): intropart=3
            if (event.key==K_s):
                if (showDist2==whogoes):
                    showskillsgoes=1-showskillsgoes; updating=2
                else:
                    showskills=1-showskills; updating=2
                
            
        elif (event.type==QUIT): #Quitting
            mainLoop=False
            
    pygame.display.set_caption("FPS: "+str(int(Clock.get_fps())))

    updateScreen()
    #pygame.display.update()
    
pygame.quit()
