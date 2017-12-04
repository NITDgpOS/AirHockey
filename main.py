import sys
import pygame
from pygame.locals import *
from paddle import *
from puck import *

pygame.init()
clock = pygame.time.Clock()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# setting logo
gamelogo = pygame.image.load('img/logo.png')
pygame.display.set_icon(gamelogo)

# Window title and Caption
pygame.display.set_caption('Air Hockey')

# Create Game Objects
paddleSpeed = 380
puckSpeed = 450

paddleSize = 25
puckSize = 15

paddle1 = Paddle(22, height / 2, paddleSize, paddleSpeed)
paddle2 = Paddle(width - 20, height / 2, paddleSize, paddleSpeed)

puck = Puck(width / 2, height / 2, puckSize, puckSpeed)

screenColor = (224, 214, 141)

# Score
score1, score2 = 0, 0


def renderPlayingArea():
    # Render Logic

    screen.fill(screenColor)

    # center circle
    pygame.draw.circle(screen, (255, 255, 255), (width / 2, height / 2), 70, 5)

    # borders
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height), 5)

    # D-box
    pygame.draw.rect(screen, (255, 255, 255), (0, height / 2 - 150, 150, 300), 5)
    pygame.draw.rect(screen, (255, 255, 255), (width - 150, height / 2 - 150, 150, 300), 5)

    # goals
    pygame.draw.rect(screen, (0, 0, 0), (0, height / 2 - 90, 5, 180))
    pygame.draw.rect(screen, (0, 0, 0), (width - 5, height / 2 - 90, 5, 180))

    divider = pygame.Rect(width / 2, 0, 3, height)
    pygame.draw.rect(screen, (255, 255, 255), divider)


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

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

    # time period between two consecutive frames.
    time_delta = clock.get_time() / 1000.0

    # Update Paddle1
    paddle1.move(w, s, a, d, time_delta)
    paddle1.checkTopBottomBounds(height)
    paddle1.checkLeftBoundary(width)

    # Update Paddle2
    paddle2.move(up, down, left, right, time_delta)
    paddle2.checkTopBottomBounds(height)
    paddle2.checkRightBoundary(width)

    puck.move(time_delta, 1)
    # TODO: puck is within the goal boundary.

    puck.checkBoundary(width, height)

    if puck.collidesWithPaddle(paddle1):
        # play sound
        pass

    if puck.collidesWithPaddle(paddle2):
        # play sound
        pass

    # playing area should be drawn first
    renderPlayingArea()

    # drawing the paddle and the puck
    paddle1.draw(screen, (255, 0, 0))
    paddle2.draw(screen, (255, 255, 0))
    puck.draw(screen)

    pygame.display.flip()
    clock.tick(60)
