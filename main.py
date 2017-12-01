import pygame, sys
from pygame.locals import *
from gameObjects import *
from random import randint
pygame.init()
clock= pygame.time.Clock()
screen= pygame.display.set_mode((800,600))
pygame.time.set_timer(USEREVENT + 1, 1000) # Used to correctly implement seconds
  
#Create Game Objects
initht=80
paddleVelocity= 10
paddle1= Paddle(10, screen.get_height()/2 -40 , 10, 80, paddleVelocity)
paddle2= Paddle(screen.get_width()-20, screen.get_height()/2 -40, 10, 80, paddleVelocity)

puckVelocity= [8,4]
puck= Puck(screen.get_width()/2, screen.get_height()/2, 20, 20, puckVelocity)

divider= pygame.Rect(screen.get_width()/2,0,3,screen.get_height())
powerup1 = powerup1(screen.get_width()/2, screen.get_height()/2, 8, 25)


#Score
score1,score2=0,0
collideflag=0
seconds = 0
randomflag=1
time2 =0
time1 =0
#Game Loop
while True:
    # timer for making the powerups disappear

    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type == USEREVENT + 1:
                seconds+=1
                time2+=1
    #generating random x and y coordinates for the powerup
    if powerup1.active == True and randomflag == 1:
        powerup1.x=randint(0,screen.get_width())
        powerup1.y=randint(0,screen.get_height())
        randomflag=0
        

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
    puck.x+=puck.velocity[0]
    puck.y+=puck.velocity[1]
    if puck.x<0:
        score2+=1
        puck.serveDirection=-1
        puck.reset()
    elif puck.x>screen.get_width()-puck.width:
        score1+=1
        puck.serveDirection=1
        puck.reset()
    if puck.y<0 or puck.y>screen.get_height()-puck.height:
        puck.velocity[1]*=-1
    if puck.getPuck().colliderect(paddle1.getPaddle()) or puck.getPuck().colliderect(paddle2.getPaddle()):
        puck.velocity[0]*=-1
    if powerup1.getpowerup1().colliderect(paddle1.getPaddle()) and powerup1.active==True :
        paddle1.height*=2
        collideflag=1
        
    if powerup1.getpowerup1().colliderect(paddle2.getPaddle()) and powerup1.active==True :
        paddle2.height*=2
        collideflag=1
    
    if collideflag==1:
        powerup1.kill() #powerup1.active = False
        time1 = seconds
        collideflag = 0
        randomflag = 1 
    
   # print("time1="+str(time1))
   # print("seconds="+str(seconds))
    #making powerup pop up every 10 seconds 
    if powerup1.active == False and seconds > time1+15:
        time2=0 
        powerup1.active = True
    #reducing the length of paddles after taking the powerup after 10seconds
    if paddle1.height>80 and seconds > time1 +15:
            paddle1.height/=2
    if paddle2.height>80 and seconds>time1+15:   #reverting it after  15 seconds
            paddle2.height/=2
    if time2>5 :
        
        powerup1.active = False
        randomflag =1


    #Render Logic
    screen.fill((0,40,40))

    pygame.draw.rect(screen, (255,0, 0), paddle1.getPaddle())
    pygame.draw.rect(screen, (255,255,0), paddle2.getPaddle())        
    pygame.draw.circle(screen, (255,255,255), (int(puck.x), int(puck.y)), int(puck.width/2))
    pygame.draw.rect(screen, (255,255,255), divider)
    if powerup1.active==True:
        time1=seconds        
        pygame.draw.rect(screen,(255,255,0),powerup1.getpowerup1(),2)
        
    pygame.display.flip()
    clock.tick(60)
  















    
