#Adding line to make the program executable
#! /usr/bin/env python

import pygame
import sys
from pygame.locals import *
from gameObjects import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

#setting logo
gamelogo = pygame.image.load('img/logo.png')
pygame.display.set_icon(gamelogo)

#Window title and Caption
pygame.display.set_caption('Air Hockey')

# Create Game Objects
paddleVelocity = 10
paddle1 = Paddle(10, screen.get_height() / 2 - 40, 10, 80, paddleVelocity)
paddle2 = Paddle(screen.get_width() - 20, screen.get_height() / 2 - 40, 10, 80, paddleVelocity)

puckVelocity = [8, 4]
puck = Puck(screen.get_width() / 2, screen.get_height() / 2, 20, 20, puckVelocity)

divider = pygame.Rect(screen.get_width() / 2, 0, 3, screen.get_height())
screenColor=(224,214,141)

# Score
score1, score2 = 0, 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()


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
    if puck.y < 0 or puck.y > screen.get_height() - puck.height:
        puck.velocity[1] *= -1
    if puck.getPuck().colliderect(paddle1.getPaddle()):
        # offset to prevent repeated collision.
        puck.x = paddle1.x + paddle1.width + int(puck.width / 2)
        puck.velocity[0] *= -1
    if puck.getPuck().colliderect(paddle2.getPaddle()):
        # offset to prevent repeated collision.
        puck.x = paddle2.x - int(puck.width / 2) - 1
        puck.velocity[0] *= -1

   #Render Logic
    screen.fill(screenColor)

    pygame.draw.circle(screen,(255,255,255), (screen.get_width()/2,screen.get_height()/2) ,70 ,5)        # center circle
    pygame.draw.rect(screen,(255,255,255), (0,0,screen.get_width(),screen.get_height()) ,5)        # borders
    pygame.draw.rect(screen,(255,255,255), (0,screen.get_height()/2-150,150,300) ,5)        # D-box
    pygame.draw.rect(screen,(255,255,255), (screen.get_width()-150,screen.get_height()/2-150,150,300) ,5)        # D-box


    pygame.draw.rect(screen,(0,0,0), (0,screen.get_height()/2-90,5,180) )        # goals
    pygame.draw.rect(screen,(0,0,0), (screen.get_width()-5,screen.get_height()/2-90,5,180) )        # goals


    pygame.draw.rect(screen, (255,0, 0), paddle1.getPaddle())
    pygame.draw.rect(screen, (255,255,0), paddle2.getPaddle())
    pygame.draw.circle(screen, (255,255,255), (puck.x, puck.y), int(puck.width/2))
    pygame.draw.rect(screen, (255,255,255), divider)

    pygame.display.flip()
    clock.tick(60)
