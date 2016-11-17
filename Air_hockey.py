import pygame, sys
from pygame.locals import *

pygame.init()
clock= pygame.time.Clock()
screen= pygame.display.set_mode((800,600))

#Create Game Objects
paddle1= pygame.Rect(20,0,10,80)
paddle2= pygame.Rect(screen.get_width()-20,0,10,80)
paddleVelocity= 10
puck= pygame.Rect(screen.get_width()/2,screen.get_height()/2,15,15)
divider= pygame.Rect(screen.get_width()/2,0,3,screen.get_height())
puckVelocity= [8,4]

#Score
score1,score2=0,0
serveDirection=1

def resetPuck():
    puckVelocity[0]=10*serveDirection
    puckVelocity[1]=4*serveDirection
    print(score1,score2)
    puck.x= screen.get_width()/2
    puck.y= screen.get_height()/2


#Game Loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()

    w,s,up,down,d,a,right,left=0,0,0,0,0,0,0,0
    #Process Player Input
    if pygame.key.get_pressed()[pygame.K_w]!=0:
        w=1
    if pygame.key.get_pressed()[pygame.K_s]!=0:
        s=1
    if pygame.key.get_pressed()[pygame.K_UP]!=0:
        up=1
    if pygame.key.get_pressed()[pygame.K_DOWN]!=0:
        down=1
    if pygame.key.get_pressed()[pygame.K_d]!=0:
        d=1
    if pygame.key.get_pressed()[pygame.K_a]!=0:
        a=1
    if pygame.key.get_pressed()[pygame.K_RIGHT]!=0:
        right=1
    if pygame.key.get_pressed()[pygame.K_LEFT]!=0:
        left=1

    #Update Logic

    #Update Paddle1
    paddle1.y+= (s-w)*paddleVelocity
    paddle1.x+= (d-a)*paddleVelocity
    if paddle1.y<0:
        paddle1.y=0
    elif paddle1.y>screen.get_height()-  paddle1.height:
        paddle1.y=screen.get_height()-  paddle1.height
    if paddle1.x<0:
        paddle1.x=0
    elif paddle1.x>screen.get_width()/2- paddle1.width:
        paddle1.x= screen.get_width()/2- paddle1.width

    #Update Paddle2
    paddle2.y+= (down-up)*paddleVelocity
    paddle2.x+= (right-left)*paddleVelocity
    if paddle2.y<0:
        paddle2.y=0
    elif paddle2.y>screen.get_height()-  paddle2.height:
        paddle2.y=screen.get_height()-  paddle2.height
    if paddle2.x>screen.get_width()- paddle1.width:
        paddle2.x= screen.get_width()- paddle1.width
    elif paddle2.x<screen.get_width()/2:
        paddle2.x= screen.get_width()/2

    #Update Puck
    puck.x+=puckVelocity[0]
    puck.y+=puckVelocity[1]
    if puck.x<0:
        score2+=1
        serveDirection=-1
        resetPuck()
    elif puck.x>screen.get_width()-puck.width:
        score1+=1
        serveDirection=1
        resetPuck()
    if puck.y<0 or puck.y>screen.get_height()-puck.height:
        puckVelocity[1]*=-1
    if puck.colliderect(paddle1) or puck.colliderect(paddle2):
        puckVelocity[0]*=-1


    #Render Logic
    screen.fill((0,40,40))

    pygame.draw.rect(screen, (255,0, 0), paddle1)
    pygame.draw.rect(screen, (255,255,0), paddle2)        
    pygame.draw.rect(screen, (200,200,200), puck)
    pygame.draw.rect(screen, (255,255,255), divider)

    pygame.display.flip()
    clock.tick(60)















    
