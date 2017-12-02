#Adding line to make the program executable
#! /usr/bin/env python

import pygame
import sys
from pygame.locals import *
from gameObjects import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

# Create Game Objects

paddleVelocity = 10
paddle1 = Paddle(10, screen.get_height() / 2 - 40, 10, 80, paddleVelocity)
paddle2 = Paddle(screen.get_width() - 20, screen.get_height() / 2 - 40, 10, 80, paddleVelocity)

puckVelocity = [8, 4]
puck = Puck(screen.get_width() / 2, screen.get_height() / 2, 20, 20, puckVelocity)

divider = pygame.Rect(screen.get_width() / 2, 0, 3, screen.get_height())

# setting logo
gamelogo = pygame.image.load('img/logo.png')
pygame.display.set_icon(gamelogo)

# window title and caption
pygame.display.set_caption('Air Hockey')

# screen height and width
height = screen.get_height()
width = screen.get_width()

# Create Game Objects
paddleVelocity = 10
paddleSize = 26
puckSize = 20

paddle1 = Paddle(22, height / 2, paddleSize, paddleVelocity)
paddle2 = Paddle(width - 20, height / 2, paddleSize, paddleVelocity)

puckVelocity = [8, 4]
puck = Puck(width / 2, height / 2, puckSize, puckVelocity)

divider = pygame.Rect(width / 2, 0, 3, height)
screenColor = (224, 214, 141)
>>>>>>> 3386ee18a2b09b28bc8b3f2fa94ab284ab5c127a

# Score
score1, score2 = 0, 0

<<<<<<< HEAD
=======

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
    pygame.draw.rect(screen, (0, 0, 0), (width -
                                         5, height / 2 - 90, 5, 180))

    pygame.draw.rect(screen, (255, 255, 255), divider)


>>>>>>> 3386ee18a2b09b28bc8b3f2fa94ab284ab5c127a
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    w, s, up, down, d, a, right, left = 0, 0, 0, 0, 0, 0, 0, 0
<<<<<<< HEAD
    # Process Player Input
    if pygame.key.get_pressed()[pygame.K_w] != 0:
        w = 1
    if pygame.key.get_pressed()[pygame.K_s] != 0:
        s = 1
    if pygame.key.get_pressed()[pygame.K_UP] != 0:
        up = 1
    if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
        down = 1
    if pygame.key.get_pressed()[pygame.K_d] != 0:
        d = 1
    if pygame.key.get_pressed()[pygame.K_a] != 0:
        a = 1
    if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        right = 1
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        left = 1
=======
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
>>>>>>> 3386ee18a2b09b28bc8b3f2fa94ab284ab5c127a

    # Update Logic

    # Update Paddle1
    paddle1.y += (s - w) * paddleVelocity
    paddle1.x += (d - a) * paddleVelocity
<<<<<<< HEAD
    if paddle1.y < 0:
        paddle1.y = 0
    elif paddle1.y > screen.get_height() - paddle1.height:
        paddle1.y = screen.get_height() - paddle1.height
    if paddle1.x < 0:
        paddle1.x = 0
    elif paddle1.x > screen.get_width() / 2 - paddle1.width:
        paddle1.x = screen.get_width() / 2 - paddle1.width
=======
    paddle1.checkTopBottomBounds(height)
    paddle1.checkLeftBoundary(width)
>>>>>>> 3386ee18a2b09b28bc8b3f2fa94ab284ab5c127a

    # Update Paddle2
    paddle2.y += (down - up) * paddleVelocity
    paddle2.x += (right - left) * paddleVelocity
<<<<<<< HEAD
    if paddle2.y < 0:
        paddle2.y = 0
    elif paddle2.y > screen.get_height() - paddle2.height:
        paddle2.y = screen.get_height() - paddle2.height
    if paddle2.x > screen.get_width() - paddle1.width:
        paddle2.x = screen.get_width() - paddle1.width
    elif paddle2.x < screen.get_width() / 2:
        paddle2.x = screen.get_width() / 2
=======
    paddle2.checkTopBottomBounds(height)
    paddle2.checkRightBoundary(width)
>>>>>>> 3386ee18a2b09b28bc8b3f2fa94ab284ab5c127a

    # Update Puck
    puck.x += puck.velocity[0]
    puck.y += puck.velocity[1]
<<<<<<< HEAD
    if puck.x < 0:
        score2 += 1
        puck.serveDirection = -1
        puck.reset()
    elif puck.x > screen.get_width() - puck.width:
        score1 += 1
        puck.serveDirection = 1
        puck.reset()
    if puck.y < 0 or puck.y > screen.get_height() - puck.height:
        puck.velocity[1] *= -1
    if puck.getPuck().colliderect(paddle1.getPaddle()) or puck.getPuck().colliderect(paddle2.getPaddle()):
        puck.velocity[0] *= -1

    # Render Logic
    screen.fill((0, 40, 40))

    pygame.draw.rect(screen, (255, 0, 0), paddle1.getPaddle())
    pygame.draw.rect(screen, (255, 255, 0), paddle2.getPaddle())
    pygame.draw.circle(screen, (255, 255, 255), (puck.x, puck.y), int(puck.width / 2))
    pygame.draw.rect(screen, (255, 255, 255), divider)
=======
    if puck.x + puck.radius < 0:
        score2 += 1
        puck.serveDirection = -1
        puck.reset()
    elif puck.x - puck.radius > width:
        score1 += 1
        puck.serveDirection = 1
        puck.reset()
    if puck.collidesTopBottom(height):
        puck.velocity[1] *= -1
    if puck.collidesWithPaddle(paddle1):
        puck.x = paddle1.x + paddle1.radius + puck.radius
        puck.velocity[0] *= -1
    if puck.collidesWithPaddle(paddle2):
        puck.x = paddle2.x - paddle2.radius - puck.radius
        puck.velocity[0] *= -1

    # playing area should be drawn first
    renderPlayingArea()

    # drawing the paddle and the puck
    paddle1.draw(screen, (255, 0, 0))
    paddle2.draw(screen, (255, 255, 0))
    puck.draw(screen)
>>>>>>> 3386ee18a2b09b28bc8b3f2fa94ab284ab5c127a

    pygame.display.flip()
    clock.tick(60)
