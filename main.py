import os
import sys
import time
import pygame
from pygame.locals import *
from paddle import *
from puck import *
from startScreen import airHockeyStart, buttonCircle
import constants as const
import time


# Globals, initialized in method `init()`
# TODO: Maybe introduce a class Global to keep track of all the global variables.

smallfont = None
score1, score2 = 0, 0

# Sound globals.
paddleHit = None
goalWhistle = None
backgroundMusic = None

# game globals.
clock = None
screen = None
screenColor = (224, 214, 141)

# width and height of the screen.
width, height = const.WIDTH, const.HEIGHT

# Create game objects.
paddle1 = Paddle(const.PADDLE1X, const.PADDLE1Y)
paddle2 = Paddle(const.PADDLE2X, const.PADDLE2Y)
puck = Puck(width / 2, height / 2)


def init():
    global paddleHit, goalWhistle, backgroundMusic, clock, screen, smallfont
    pygame.init()
    pygame.mixer.init()

    auxDirectory = os.path.join(os.path.dirname(__file__), 'aux')

    gamelogo = pygame.image.load(os.path.join(auxDirectory, 'AHlogo.png'))
    pygame.display.set_icon(gamelogo)
    pygame.display.set_caption('Air Hockey')
    screen = pygame.display.set_mode((width, height))

    paddleHit = pygame.mixer.Sound(os.path.join(auxDirectory, 'hit.wav'))
    goalWhistle = pygame.mixer.Sound(os.path.join(auxDirectory, 'goal.wav'))
    backgroundMusic = pygame.mixer.Sound(os.path.join(auxDirectory, 'back.wav'))

    smallfont = pygame.font.SysFont("comicsans", 35)

    clock = pygame.time.Clock()


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


def showPauseScreen():
    """ Shows the pause screen till the user un-pauses"""

    paused = True

    while paused:
        paddle1.draw(screen, (255, 0, 0))
        paddle2.draw(screen, (255, 255, 0))
        puck.draw(screen)

        score(score1, score2)
        rounds(rounds_p1, rounds_p2)

        pygame.draw.circle(screen, (0, 255, 0), (width / 2, height - 30), 20, 0)

        text1 = smallfont.render("Go", True, const.WHITE)
        screen.blit(text1, [width / 2 - 15, height - 42])

        text_pause = smallfont.render("Paused", True, const.BLACK)
        screen.blit(text_pause, [width / 2 - 40, height / 2 - 30])

        text_cont = smallfont.render("Click Anywhere to Continue", True, const.BLACK)
        screen.blit(text_cont, [width / 2 - 150, height / 2])

        # Look for mouse press events.
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.circle(screen, (255, 0, 0), (width / 2, height - 30), 20, 0)
                text1 = smallfont.render("||", True, const.WHITE)
                screen.blit(text1, [width / 2 - 7, height - 44])
                paused = False

            if event.type == QUIT:
                sys.exit()

        pygame.display.flip()
        clock.tick(const.FPS)


def hitsPauseArea(mouseXY):
    """ Returns True if the mouse is clicked within the pause area"""

    return mouseXY[1] < (height - 30 + 20) \
        and mouseXY[1] > (height - 30 - 20) \
        and mouseXY[0] < (width / 2 + 20) \
        and mouseXY[0] > (width / 2 - 20)


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

    # PAUSE
    pygame.draw.circle(screen, const.LIGHTRED, (width / 2, height - 30), 20, 0)
    text1 = smallfont.render("||", True, const.WHITE)
    screen.blit(text1, [width / 2 - 7, height - 44])


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
    global rounds_p1, rounds_p2
    rounds_p1, rounds_p2 = 0, 0

    pygame.mixer.Sound.play(backgroundMusic, -1)
    pygame.mixer.Sound.set_volume(backgroundMusic, 0.2)

    while True:
        global score1, score2

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            # check mouse click events
            if event.type == pygame.MOUSEBUTTONUP:
                mouseXY = pygame.mouse.get_pos()

                # check if the mouse is clicked withing the pause area.
                if hitsPauseArea(mouseXY):
                    showPauseScreen()

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

        # Hits the left goal!
        if insideGoal(0):
            pygame.mixer.Sound.play(goalWhistle)  # Added sound for goal
            score1 += 1
            resetGame(speed, 1)

        # Hits the right goal!
        if insideGoal(1):
            pygame.mixer.Sound.play(goalWhistle)  # Added sound for goal
            score2 += 1
            resetGame(speed, 2)

        # check puck collisions and update if necessary.
        puck.checkBoundary(width, height)

        if puck.collidesWithPaddle(paddle1):
            pygame.mixer.Sound.play(paddleHit)  # Added sound for paddle hit
            pass

        if puck.collidesWithPaddle(paddle2):
            pygame.mixer.Sound.play(paddleHit)
            pass

        # Update round points
        if score1 == const.SCORELIMIT:
            rounds_p1 += 1
            pygame.mixer.Sound.play(backgroundMusic, -1)
            score1, score2 = 0, 0
        if score2 == const.SCORELIMIT:
            rounds_p2 += 1
            pygame.mixer.Sound.play(backgroundMusic, -1)
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

        # refresh screen.
        pygame.display.flip()
        clock.tick(const.FPS)


if __name__ == "__main__":
    init()
    choice = airHockeyStart(screen, clock, width, height)
    if choice == 1:
        puck.speed = const.EASY
        gameLoop(const.EASY)
    elif choice == 2:
        puck.speed = const.HARD
        gameLoop(const.HARD)
    elif choice == 0:
        sys.exit()
