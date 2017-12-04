#!/usr/bin/env python2
import time
import pygame
import sys
import os
from pygame.locals import *
from gameObjects import *
from startScreen import airHockeyStart
# setting logo should take place before setting the display on some OS
gamelogo = pygame.image.load(os.path.join(os.path.dirname(__file__),'img/AHlogo.png'))
pygame.display.set_icon(gamelogo)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))
# Window title and Caption
pygame.display.set_caption('Air Hockey')
# screen height and width
height = screen.get_height()
width = screen.get_width()

# Create Game Objects
paddleVelocity = 10
paddleSize = 40
puckSize = 35

paddle1 = Paddle(22, height / 2, paddleSize, paddleVelocity)
paddle2 = Paddle(width - 20, height / 2, paddleSize, paddleVelocity)

divider = pygame.Rect(width / 2, 0, 3, height)
screenColor = (224, 214, 141)

# Score
score1, score2 = 0, 0

smallfont=pygame.font.SysFont("comicsansms",35)
black =(0,0,0)
def score(score1,score2):
    text1 =smallfont.render("Score1: "+str(score1), True ,black)
    text2 =smallfont.render("Score2: "+str(score2), True ,black)

    screen.blit(text1, [40,0])
    screen.blit(text2,[ width-150,0])
def rounds(rounds_p1,rounds_p2):
	if(rounds_p1==2):
		print "Player 1 Wins"
		sys.exit()
	elif(rounds_p2==2):
		print "Player 2 Wins"
		sys.exit()	
	else:
		text=smallfont.render("Rounds",True,black)
		screen.blit(text,[width/2-40,0])
		text=smallfont.render(str(rounds_p1)+":"+str(rounds_p2),True,black)
		screen.blit(text,[width/2-16,20])
def renderPlayingArea():
    # Render Logic

    screen.fill(screenColor)

    # center circle
    pygame.draw.circle(screen, (255, 255, 255),
                       (width / 2, height / 2), 70, 5)

    # borders
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height), 5)

    # D-box
    pygame.draw.rect(screen, (255, 255, 255), (0, height / 2 - 150, 150, 300), 5)
    pygame.draw.rect(screen, (255, 255, 255), (width -
                                               150, height / 2 - 150, 150, 300), 5)
    # goals
    pygame.draw.rect(screen, (0, 0, 0), (0, height / 2 - 90, 5, 180))
    pygame.draw.rect(screen, (0, 0, 0), (width-5, height / 2 - 90, 5, 180))

    pygame.draw.rect(screen, (255, 255, 255), divider)

# Game Loop
def gameLoop(vel):
    res=0
    puckVelocity = [vel, vel]
    puck = Puck(width / 2, height / 2, puckSize, puckVelocity)
    global rounds_p1,rounds_p2
    rounds_p1=0
    rounds_p2=0
    while True:

    	#friction

    	puck.velocity[0]-=puck.velocity[0]*0.005#X dir friction
    	puck.velocity[1]-=puck.velocity[1]*0.001#Y dir friction
    

    	#sleep for 1 sec on reset
    	if res==1:
    		time.sleep(1)
    		res=0
        


        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        global score1, score2
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
        paddle1.checkTopBottomBounds(height)
        paddle1.checkLeftBoundary(width)

        # Update Paddle2
        paddle2.y += (down - up) * paddleVelocity
        paddle2.x += (right - left) * paddleVelocity
        paddle2.checkTopBottomBounds(height)
        paddle2.checkRightBoundary(width)

        # Update Puck
        puck.x += puck.velocity[0]
        puck.y += puck.velocity[1]
        if puck.x + puck.radius < 0 :
			print "1"
			score2 += 1
			puck.serveDirection = -1
			puck.reset(vel)
			paddle1.reset(22, height / 2)
			paddle2.reset(width - 20, height / 2)
			res=1#set reset to 1
            # paddle2.reset()
        elif puck.x - puck.radius > width:
            print "2"
            score1 += 1
            puck.serveDirection = 1
            puck.reset(vel)
            paddle1.reset(22, height / 2)
            paddle2.reset(width - 20, height / 2)
            res=1#set reset to 1
        elif puck.collidesTopBottom(height):
            puck.velocity[1] *= -1
        elif puck.collidesLeftRight(width):
            print "4"
            if(puck.y<((height / 2) - 90) or puck.y>((height / 2) + 90) ):
                puck.velocity[0] *= -1
        elif puck.collidesWithPaddle(paddle1):
            puck.x = paddle1.x + paddle1.radius + puck.radius
            puck.velocity[0] = -1*(puckVelocity[0])+(d-a)*paddleVelocity
        elif puck.collidesWithPaddle(paddle2):
            puck.x = paddle2.x - paddle2.radius - puck.radius
            puck.velocity[0] = -1*(puckVelocity[0])+(right-left)*paddleVelocity
        # playing area should be drawn first
        renderPlayingArea()
        # drawing the paddle and the puck
        paddle1.draw(screen, (255, 0, 0))
        paddle2.draw(screen, (255, 255, 0))
        puck.draw(screen)
        

        #ROUNDS 
        if(score1==5):
        	rounds_p1+=1
        	score1=0
        	score2=0
        if(score2==5):
        	rounds_p2+=1
        	score1=0
        	score2=0
        


        score(score1,score2)
        rounds(rounds_p1,rounds_p2)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
        choice = airHockeyStart(screen, clock, width, height)
        if choice == 1:
            gameLoop(7.00)
        elif choice == 2:
            gameLoop(12.00)
        elif choice == 0:
            sys.exit()
