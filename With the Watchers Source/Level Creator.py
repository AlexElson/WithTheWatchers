import pygame, sys
import time
import random
from pygame.locals import *
pygame.init()
fps=60

WIDTH=720+200
HEIGHT=480+200
screen=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()

#Load Files
tileset=pygame.image.load("Images/isotileset.png").convert_alpha()
tilewall=pygame.image.load("Images/isowall.png").convert_alpha()
misc=pygame.image.load("Images/misc.png").convert()

GRAY=(50,50,50)

#Variables
heldtilex=1
heldtiley=0
holding=0

right=0
left=0
up=0
down=0
camerax=0
cameray=0


#Tiles
lvlW=10
lvlH=10
tilex=[]
tiley=[]
wallx=[]
wally=[]
walldir=[]
si=36
wdir=-1

#NPCs
npc=[]
npcx=[]
npcy=[]
for n in range(18):
    npc.append(n); npc[n]=""
    npcx.append(n); npcx[n]=0
    npcy.append(n); npcy[n]=0

#Check if File Exists
a=0
try:
    with open('level.txt'): a=1
except IOError:
    a=0
    lvlW=int(raw_input("x-coor: "))
    lvlH=int(raw_input("y-coor: "))
    for n in range(lvlW*lvlH):
        tilex.append(n); tilex[n]=0
        tiley.append(n); tiley[n]=0
        wallx.append(n); wallx[n]=0
        wally.append(n); wally[n]=0
        walldir.append(n); walldir[n]=0

if (a==1): #Load level
    load=open("level.txt","r")
    lvlW=int(load.readline())
    lvlH=int(load.readline())
    for n in range(lvlW*lvlH):
        tilex.append(n); tilex[n]=0
        tiley.append(n); tiley[n]=0
        wallx.append(n); wallx[n]=0
        wally.append(n); wally[n]=0
        walldir.append(n); walldir[n]=0
    level=load.readline()
    w=0
    for n in range(lvlW*lvlH):
        for times in range(5):
            t=0
            for nn in level:
                t=t+1
                if (nn=="%"):
                    cut=level[:t-1]
                    if (times==0): tilex[n]=int(cut)
                    if (times==1): tiley[n]=int(cut)
                    if (times==2): wallx[n]=int(cut)
                    if (times==3): wally[n]=int(cut)
                    if (times==4): walldir[n]=int(cut)
                    level=level[t:]
                    break
    load.close()


def displayTiles():
    for n in range(lvlH*lvlW):
        screen.blit(tileset,((n%lvlW)*si-int(camerax*si),int(n/lvlW)*si-cameray*si),(tilex[n]*si,tiley[n]*si,si,si))

def displayWalls():
    for n in range(lvlW*lvlH):
        if (wallx[n]!=0 or wally[n]!=0):
            tn=0; tx=0
            if (walldir[n]==0): tn=int(si*.5); ty=0
            if (walldir[n]==1): tn=0; ty=0
            if (walldir[n]==2): tn=0; ty=si*.25; tx=int(si*.5)
            if (walldir[n]==3): tn=int(si*.5); ty=si*.25; tx=-int(si*.5)
            screen.blit(tilewall,((n%lvlW)*si-int(camerax*si)+si*.5-tn-tx,int(n/lvlW)*si-cameray*si-15+ty),(wallx[n]*si+tn,wally[n]*si,int(si*.5),si))
            

def changeTiles():
    global holding
    if (holding==1 and int(mx/si)<lvlW-camerax and int(my/si)<lvlH-cameray and wdir==-1):
        if (int(mx/si)>-camerax-1 and int(my/si)>-cameray-1 and my<HEIGHT-200):
            a=int(mx/si)
            b=int(my/si)
            q=a+b*lvlW+camerax+cameray*lvlW
            tilex[q]=heldtilex
            tiley[q]=heldtiley
    if (holding==1 and int(mx/si)<lvlW-camerax and int(my/si)<lvlH-cameray and wdir>=0):
        if (int(mx/si)>-camerax-1 and int(my/si)>-cameray-1 and my<HEIGHT-200):
            a=int(mx/si)
            b=int(my/si)
            q=a+b*lvlW+camerax+cameray*lvlW
            wallx[q]=heldtilex
            wally[q]=heldtiley
            walldir[q]=wdir

def displayBottom():
    if (wdir==-1):
        screen.blit(tileset,(0,HEIGHT-200))
    if (wdir>=0):
        screen.blit(tilewall,(0,HEIGHT-200))

def changeHold():
    global heldtilex, heldtiley
    if (my>=HEIGHT-200):
        heldtilex=int(mx/si)
        heldtiley=int((my-HEIGHT+200)/si)

def selectCamera():
    global camerax, cameray
    if (up==1): cameray-=1
    if (down==1): cameray+=1
    if (left==1): camerax-=1
    if (right==1): camerax+=1

    
        
mainLoop=True
while mainLoop:
    Clock.tick(fps)
    screen.fill(GRAY)
    mx,my=pygame.mouse.get_pos()

    displayTiles()
    displayWalls()
    changeTiles()
    selectCamera()
    displayBottom()

    for event in pygame.event.get():
        
        if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1): #Left Mouse Click
            holding=1
            changeHold()
        elif (event.type==pygame.MOUSEBUTTONUP and event.button==1): #Left Mouse Up
            holding=0  
        elif (event.type==KEYDOWN): #Pressing Keys
            if (event.key==K_UP): up=1
            if (event.key==K_DOWN): down=1
            if (event.key==K_LEFT): left=1
            if (event.key==K_RIGHT): right=1
        elif (event.type==KEYUP): #Lifting Keys
            if (event.key==K_UP): up=0
            if (event.key==K_DOWN): down=0
            if (event.key==K_LEFT): left=0
            if (event.key==K_RIGHT): right=0
            if (event.key==K_w): wdir=1
            if (event.key==K_a): wdir=0
            if (event.key==K_s): wdir=2
            if (event.key==K_d): wdir=3
            if (event.key==K_q): wdir=-1



        elif (event.type==QUIT): #Quitting
            mainLoop=False
            
    pygame.display.set_caption("FPS: "+str(int(Clock.get_fps()))+" "+str(wdir)+" "+str("w-up, a-left, s-down, d-right, q-none")+str(wallx[0]))
    pygame.display.flip()




save = open("level.txt", "w") #Erases old file and writes new
save.write(str(lvlW)+"\n")
save.write(str(lvlH)+"\n")
for n in range(lvlW*lvlH):
    save.write(str(tilex[n])+"%"+str(tiley[n])+"%"+str(wallx[n])+"%"+str(wally[n])+"%"+str(walldir[n])+"%")
save.close()

pygame.quit()
