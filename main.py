import os
import sys
import time
import pygame
from pygame.locals import *
from paddle import *
from puck import *
from startScreen import airHockeyStart

"""
setting logo, should be before setting display, some OS prevent
setting icon after the display has been set.
"""
gamelogo = pygame.image.load(os.path.join(os.path.dirname(__file__),'img/AHlogo.png'))
pygame.display.set_icon(gamelogo)

pygame.init()
clock = pygame.time.Clock()

width, height = 1200, 600
screen = pygame.display.set_mode((width, height))


# Window title and Caption
pygame.display.set_caption('Air Hockey')

# Create Game Objects
paddleSpeed = 400
puckSpeed = 450

paddleSize = 35
puckSize =25

paddle1 = Paddle(22, height / 2, paddleSize, paddleSpeed)
paddle2 = Paddle(width - 20, height / 2, paddleSize, paddleSpeed)

puck = Puck(width / 2, height / 2, puckSize, puckSpeed)

screenColor = (224, 214, 141)

# Score
score1, score2 = 0, 0

smallfont = pygame.font.SysFont("comicsansms",35)

BLACK = (0, 0, 0)
GOALXY = (height / 2 - 90, height / 2 + 90)

def score(score1,score2):
    text1 = smallfont.render("Score 1: " + str(score1), True ,BLACK)
    text2 = smallfont.render("Score 2: " + str(score2), True ,BLACK)

    screen.blit(text1, [40, 0])
    screen.blit(text2, [width - 150, 0])

def rounds(rounds_p1, rounds_p2):
    if(rounds_p1 == 2):
        print "Player 1 Wins"
        sys.exit()
    elif(rounds_p2 == 2):
        print "Player 2 Wins"
        sys.exit()
    else:
        text = smallfont.render("Rounds",True,BLACK)
        screen.blit(text,[width / 2 - 40, 0])
        text = smallfont.render(str(rounds_p1)+ ":" +str(rounds_p2), True, BLACK)
        screen.blit(text,[width / 2 - 16, 20])

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
    pygame.draw.rect(screen, (0, 0, 0), (0, GOALXY[0], 5, 180))
    pygame.draw.rect(screen, (0, 0, 0), (width - 5, GOALXY[0], 5, 180))
    # Divider
    pygame.draw.rect(screen, (255, 255, 255), (width / 2, 0, 3, height))


def resetGame(speed):
    puck.reset(speed)
    paddle1.reset(22, height / 2)
    paddle2.reset(width - 20, height / 2)

def insideGoal(side):
    """ Returns true if puck is within goal boundary"""
    if side == 0:
        return puck.x - puck.radius <= 0 and puck.y >= GOALXY[0] and puck.y <= GOALXY[1]

    if side == 1:
        return puck.x + puck.radius >= width and puck.y >= GOALXY[0] and puck.y <= GOALXY[1]

# Game Loop
def gameLoop(speed):
    rounds_p1, rounds_p2 = 0, 0

    while True:
        global score1, score2
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        keyPresses = pygame.key.get_pressed()

        # Process Player 1 Input
        w = keyPresses[pygame.K_w]
        s = keyPresses[pygame.K_s]
        d = keyPresses[pygame.K_d]
        a = keyPresses[pygame.K_a]

        # Process Player 2 Input
        up = keyPresses[pygame.K_UP]
        down = keyPresses[pygame.K_DOWN]
        right = keyPresses[pygame.K_RIGHT]
        left = keyPresses[pygame.K_LEFT]
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

        if insideGoal(0):
            # TODO: add goal sound.

            print "2 scores"
            score1 += 1
            resetGame(speed)

        if insideGoal(1):
            # TODO: add goal sound.

            print "1 scores"
            score2 += 1
            resetGame(speed)

        puck.checkBoundary(width, height)

        if puck.collidesWithPaddle(paddle1):
            # play collision sound
            pass

        if puck.collidesWithPaddle(paddle2):
            # play collision sound
            pass

        # Update round points
        if(score1 == 5):
            rounds_p1 += 1
            score1, score2 = 0, 0
        if(score2 == 5):
            rounds_p2 += 1
            score1, score2 = 0, 0

        score(score1,score2)
        rounds(rounds_p1,rounds_p2)

        # playing area should be drawn first
        renderPlayingArea()

        # drawing the paddle and the puck
        paddle1.draw(screen, (255, 0, 0))
        paddle2.draw(screen, (255, 255, 0))
        puck.draw(screen)
        rounds(rounds_p1,rounds_p2)
        score(score1,score2)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
        choice = airHockeyStart(screen, clock, width, height)
        if choice == 1:
            puck.speed = 450
            gameLoop(450)
        elif choice == 2:
            puck.speed = 850
            gameLoop(850)
        elif choice == 0:
            sys.exit()
