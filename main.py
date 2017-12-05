import os
import sys
import time
import pygame
from pygame.locals import *
from paddle import *
from puck import *
from startScreen import airHockeyStart
import constants as const

"""
setting logo, should be before setting display, some OS prevent
setting icon after the display has been set.
"""
gamelogo = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/AHlogo.png'))
pygame.display.set_icon(gamelogo)

pygame.init()
paddle_hit = pygame.mixer.Sound('sound/hit.wav')
goal_whistle = pygame.mixer.Sound('sound/goal.wav')
# Below is the code for playing sound after round change.
#round_change = pygame.mixer.Sound('round.wav')

clock = pygame.time.Clock()

width, height = const.WIDTH, const.HEIGHT
screen = pygame.display.set_mode((width, height))

# Window title and Caption
pygame.display.set_caption('Air Hockey')

# Create Game Objects
paddle1 = Paddle(const.PADDLE1X, const.PADDLE1Y)
paddle2 = Paddle(const.PADDLE2X, const.PADDLE2Y)
puck = Puck(width / 2, height / 2)

screenColor = (224, 214, 141)

# Score
score1, score2 = 0, 0

smallfont = pygame.font.SysFont("comicsans", 35)


def score(score1, score2):
    text1 = smallfont.render("Score 1: " + str(score1), True, const.BLACK)
    text2 = smallfont.render("Score 2: " + str(score2), True, const.BLACK)

    screen.blit(text1, [40, 0])
    screen.blit(text2, [width - 150, 0])


def rounds(rounds_p1, rounds_p2):
    if rounds_p1 == const.ROUNDLIMIT:
        print "Player 1 Wins"
        sys.exit()
    elif rounds_p2 == const.ROUNDLIMIT:
        print "Player 2 Wins"
        sys.exit()
    else:
        text = smallfont.render("Rounds", True, const.BLACK)
        screen.blit(text, [width / 2 - 40, 0])

        text = smallfont.render(str(rounds_p1) + " : " + str(rounds_p2), True, const.BLACK)
        screen.blit(text, [width / 2 - 16, 20])


def renderPlayingArea():
    # Render Logic
    screen.fill(screenColor)
    # center circle
    pygame.draw.circle(screen, const.WHITE, (width / 2, height / 2), 70, 5)
    # borders
    pygame.draw.rect(screen, const.WHITE, (0, 0, width, height), 5)
    # D-box
    pygame.draw.rect(screen, const.WHITE, (0, height / 2 - 150, 150, 300), 5)
    pygame.draw.rect(screen, const.WHITE, (width - 150, height / 2 - 150, 150, 300), 5)
    # goals
    pygame.draw.rect(screen, const.BLACK, (0, const.GOALY1, 5, const.GOALWIDTH))
    pygame.draw.rect(screen, const.BLACK, (width - 5, const.GOALY1, 5, const.GOALWIDTH))
    # Divider
    pygame.draw.rect(screen, const.WHITE, (width / 2, 0, 3, height))


def resetGame(speed, player):
    puck.reset(speed, player)
    paddle1.reset(22, height / 2)
    paddle2.reset(width - 20, height / 2)


def insideGoal(side):
    """ Returns true if puck is within goal boundary"""
    if side == 0:
        return puck.x - puck.radius <= 0 and puck.y >= const.GOALY1 and puck.y <= const.GOALY2

    if side == 1:
        return puck.x + puck.radius >= width and puck.y >= const.GOALY1 and puck.y <= const.GOALY2


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

        puck.move(time_delta)

        if insideGoal(0):
            pygame.mixer.Sound.play(goal_whistle)  # Added sound for goal
            score1 += 1
            resetGame(speed, 1)

        if insideGoal(1):
            pygame.mixer.Sound.play(goal_whistle)  # Added sound for goal
            score2 += 1
            resetGame(speed, 2)

        puck.checkBoundary(width, height)

        if puck.collidesWithPaddle(paddle1):
            pygame.mixer.Sound.play(paddle_hit)  # Added sound for paddle hit
            pass

        if puck.collidesWithPaddle(paddle2):
            pygame.mixer.Sound.play(paddle_hit)
            pass

        # Update round points
        if score1 == const.SCORELIMIT:
            rounds_p1 += 1
#            pygame.mixer.Sound.play(round_change)  # Added sound for round change
            score1, score2 = 0, 0
        if score2 == const.SCORELIMIT:
            rounds_p2 += 1
#            pygame.mixer.Sound.play(round_change)  # Added sound for round change
            score1, score2 = 0, 0

        # playing area should be drawn first
        renderPlayingArea()

        # show score
        score(score1, score2)
        rounds(rounds_p1, rounds_p2)

        # drawing the paddle and the puck
        paddle1.draw(screen, (255, 0, 0))
        paddle2.draw(screen, (255, 255, 0))
        puck.draw(screen)

        pygame.display.flip()
        clock.tick(const.FPS)


if __name__ == "__main__":
    choice = airHockeyStart(screen, clock, width, height)
    if choice == 1:
        puck.speed = const.EASY
        gameLoop(const.EASY)
    elif choice == 2:
        puck.speed = const.HARD
        gameLoop(const.HARD)
    elif choice == 0:
        sys.exit()