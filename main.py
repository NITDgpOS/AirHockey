import pygame
import sys
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

puckVelocity = [8, 4]
puck = Puck(screen.get_width() / 2, screen.get_height() / 2, 20, 20, puckVelocity)

divider = pygame.Rect(screen.get_width() / 2, 0, 3, screen.get_height())
screenColor=(224,214,141)

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
        if event.type == QUIT:
            sys.exit()
        elif event.type == USEREVENT + 1:
                seconds+=1
                time2+=1
    #generating random x and y coordinates for the powerup
    if powerup1.active == True and randomflag == 1:
        powerup1.x=randint(0,screen.get_width())
        powerup1.y=randint(0,screen.get_height())
        randomflag=0
        


    w, s, up, down, d, a, right, left = 0, 0, 0, 0, 0, 0, 0, 0
    # Process Player 1 Input
    w = pygame.key.get_pressed()[pygame.K_w]
    s = pygame.key.get_pressed()[pygame.K_s]
    d = pygame.key.get_pressed()[pygame.K_d]
    a = pygame.key.get_pressed()[pygame.K_a]

    # Process Player 2 Input
    up = pygame.key.get_pressed()[pygame.K_UP]
    down = pygame.key.get_pressed()[pygame.K_DOWN]
    right = pygame.key.get_pressed()[pygame.K_RIGHT]
    left = pygame.key.get_pressed()[pygame.K_LEFT]

    # Update Logic

    # Update Paddle1
    paddle1.y += (s - w) * paddleVelocity
    paddle1.x += (d - a) * paddleVelocity
    paddle1.checkTopBottomBounds(screen.get_height())
    paddle1.checkLeftBoundary(screen.get_width())

    # Update Paddle2
    paddle2.y += (down - up) * paddleVelocity
    paddle2.x += (right - left) * paddleVelocity
    paddle2.checkTopBottomBounds(screen.get_height())
    paddle2.checkRightBoundary(screen.get_width())

    # Update Puck
    puck.x += puck.velocity[0]
    puck.y += puck.velocity[1]
    if puck.x < 0:
        score2 += 1
        puck.serveDirection = -1
        puck.reset()
    elif puck.x > screen.get_width():
        score1 += 1
        puck.serveDirection = 1
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