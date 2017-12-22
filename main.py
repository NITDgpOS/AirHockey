import os
import sys
import time
import pygame
from pygame.locals import *
from paddle import Paddle
from puck import Puck
from startScreen import airHockeyStart
from themeScreen import themeScreen
import constants as const
from globals import *
from endScreen import GameEnd
import time

# Globals, initialized in method `init()`

# Create game objects.
paddle1 = Paddle(const.PADDLE1X, const.PADDLE1Y)
paddle2 = Paddle(const.PADDLE2X, const.PADDLE2Y)
puck = Puck(width / 2, height / 2)


def init():
    global paddleHit, goal_whistle, clock, screen, smallfont
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()
    
    gamelogo = pygame.image.load(os.path.join(auxDirectory, 'AHlogo.png'))
    pygame.display.set_icon(gamelogo)
    pygame.display.set_caption('Air Hockey')
    screen = pygame.display.set_mode((width, height))

    paddleHit = pygame.mixer.Sound(os.path.join(auxDirectory, 'hit.wav'))
    goal_whistle = pygame.mixer.Sound(os.path.join(auxDirectory, 'goal.wav'))

    smallfont = pygame.font.SysFont("comicsans", 35)

    clock = pygame.time.Clock()


def score(score1, score2):
    text1 = smallfont.render("Score 1: " + str(score1), True, const.BLACK)
    text2 = smallfont.render("Score 2: " + str(score2), True, const.BLACK)

    screen.blit(text1, [40, 0])
    screen.blit(text2, [width - 150, 0])


def rounds(rounds_p1, rounds_p2, round_no):
    text = smallfont.render("Round "+str(round_no), True, const.BLACK)
    screen.blit(text, [width / 2 - 40, 0])
    text = smallfont.render(str(rounds_p1) + " : " + str(rounds_p2), True, const.BLACK)
    screen.blit(text, [width / 2 - 16, 20])


def end(option, speed):
    global rounds_p1, rounds_p2, round_no, score1, score2

    # reset game with everything else same
    if option == 1:
        puck.end_reset(speed)
        paddle1.reset(22, height / 2)
        paddle2.reset(width - 20, height / 2)
        score1, score2 = 0, 0
        rounds_p1, rounds_p2 = 0, 0
        round_no = 1
        return False  # Tells that game should continue with reset

    # goes to menu
    elif option == 2:
        return True  # Game should restart at startScreen

    # Quit game
    else:
        sys.exit()


def showPauseScreen():
    global mute, music_paused
    """ 
        Shows the pause screen,
        This function will return,
        2 if the game is to be restarted, 
        1 if the game is to be continued
        and exit here itself if exit is pressed
    """

    while True:
        text_pause = smallfont.render("PAUSED", True, const.BLACK)
        screen.blit(text_pause, [width / 2 - 44, 200])
        screen.blit(play_image, (width / 2 - 32, height - 70))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #RESET       
        if mouse[0] > width / 4 and mouse[0] < width / 4 + 150 and mouse[1] > height - 200 and mouse[1] < height - 160:
            pygame.draw.rect(screen, colors[4][0], (width / 4, height - 200, 150, 40))
            if click[0] == 1:
                return 2
        else:
            pygame.draw.rect(screen, colors[4][1], (width / 4, height - 200, 150, 40))
        text_restart = smallfont.render("RESET", True, const.WHITE)
        screen.blit(text_restart, [width / 4 + 30, height - 195])

        #CONTINUE
        if mouse[0] > width / 2 - 70 and mouse[0] < width / 2 + 80 and mouse[1] > height - 200 and mouse[1] < height - 160:
            pygame.draw.rect(screen, colors[0][0], (width / 2 - 70, height - 200, 150, 40))
            if click[0] == 1:
                return 1
        else:
            pygame.draw.rect(screen, colors[0][1], (width / 2 - 70, height - 200, 150, 40))
        text_cont = smallfont.render("CONTINUE", True, const.WHITE)
        screen.blit(text_cont, [width / 2 - 60, height - 195])

        #EXIT
        if mouse[0] > width / 2 + 150 and mouse[0] < width / 2 + 300 and mouse[1] > height - 200 and mouse[1] < height -160:
            pygame.draw.rect(screen, colors[1][0], (width / 2 + 150, height - 200, 150, 40))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, colors[1][1], (width / 2 + 150, height - 200, 150, 40))
        text_exit = smallfont.render("EXIT", True, const.WHITE)
        screen.blit(text_exit, [width / 2 + 190, height -195])

        # Look for mouse press events.
        events = pygame.event.get()
        for event in events:
            # removing pause using space
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return 1

            # continue by pressing play button as well
            if event.type == pygame.MOUSEBUTTONUP:
                if hitsPauseArea(mouse):
                    return 1

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # checking if mute button clicked

        if abs(mouse[0] - (width - 100 + 32)) < const.MUTE_BUTTON_RADIUS and abs(mouse[1] - (height / 2 - 250)) < const.MUTE_BUTTON_RADIUS and click[0] == 1:
            mute = not mute

        # mute and unmute audio code
        if mute and (not music_paused):
            pygame.mixer.music.pause()
            music_paused = True
        elif (not mute) and music_paused:
            pygame.mixer.music.unpause()
            music_paused = False

        # displaying mute and unmute button
        if mute:
            screen.blit(mute_image, (width - 100, height / 2 - 250 - 32))
        else:
            screen.blit(unmute_image, (width - 100, height / 2 - 250 - 32))
                
        pygame.display.flip()
        clock.tick(10)

def hitsPauseArea(mouseXY):
    """ Returns True if the mouse is clicked within the pause area"""

    return (abs(mouseXY[0] - width / 2) < const.PAUSE_BUTTON_RADIUS) and (abs(mouseXY[1] - (height - 70 + 32)) < const.PAUSE_BUTTON_RADIUS)


def renderPlayingArea(backgroundColor):
    # Render Logic
    screen.fill(backgroundColor)
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
    screen.blit(pause_image, (width / 2 - 32, height - 70))


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
def gameLoop(screen, speed, player1Color, player2Color, backgroundColor):
    global rounds_p1, rounds_p2, round_no, music_paused
    rounds_p1, rounds_p2, round_no = 0, 0, 1

    pygame.mixer.music.load(os.path.join(auxDirectory, 'back.mp3'))  # background music
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(.2)

    music_paused = False  # to check if music is playing or paused

    # mute if start screen was mute
    if mute and (not music_paused):
        pygame.mixer.music.pause()
        music_paused = True

    while True:
        global score1, score2

        for event in pygame.event.get():

            # check for space bar
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    showPauseScreen()
                    
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                         
            # check mouse click events
            if event.type == pygame.MOUSEBUTTONUP:
                mouseXY = pygame.mouse.get_pos()

                # check if the mouse is clicked within the pause area.
                if hitsPauseArea(mouseXY):
                    ch= showPauseScreen()
                    #if the return value is 2 reset everything
                    if ch == 2:
                        score1 = 0
                        score2 = 0
                        rounds_p1 = 0
                        rounds_p2 = 0
                        round_no = 1
                        resetGame(speed, 1)
                        resetGame(speed, 2)

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
            pygame.mixer.Sound.play(goal_whistle)  # Added sound for goal
            score2 += 1
            resetGame(speed, 1)

        # Hits the right goal!
        if insideGoal(1):
            pygame.mixer.Sound.play(goal_whistle)  # Added sound for goal
            score1 += 1
            resetGame(speed, 2)

        # check puck collisions and update if necessary.
        puck.checkBoundary(width, height)

        if puck.collidesWithPaddle(paddle1):
            pygame.mixer.Sound.play(paddleHit)  # Added sound for paddle hit

        if puck.collidesWithPaddle(paddle2):
            pygame.mixer.Sound.play(paddleHit)

        # Update round points
        if score1 == const.SCORELIMIT:
            round_no += 1
            rounds_p1 += 1
            score1, score2 = 0, 0
        if score2 == const.SCORELIMIT:
            round_no += 1
            rounds_p2 += 1
            score1, score2 = 0, 0

        # playing area should be drawn first
        renderPlayingArea(backgroundColor)

        # show score
        score(score1, score2)

        # display endscreen or rounds
        if rounds_p1 == const.ROUNDLIMIT:  # Player one denotes left player
            if end(GameEnd(screen, clock, 1, backgroundColor), speed):
                if music_paused:
                    pygame.mixer.music.unpause()
                pygame.mixer.stop()
                return
        elif rounds_p2 == const.ROUNDLIMIT:  # Player two denotes right player
            if end(GameEnd(screen, clock, 2, backgroundColor), speed):
                if music_paused:
                    pygame.mixer.music.unpause()
                pygame.mixer.stop()
                return

        else:
            rounds(rounds_p1, rounds_p2, round_no)

        # drawing the paddle and the puck
        paddle1.draw(screen, player1Color)
        paddle2.draw(screen, player2Color)
        puck.draw(screen)


        # refresh screen.
        pygame.display.flip()
        clock.tick(const.FPS)


if __name__ == "__main__":
    global mute
    mute = False  # to keep state of mute
    init()
    while True:
        gameChoice, player1Color, player2Color, mute = airHockeyStart(screen, clock, width, height, mute)
        backgroundColor = themeScreen(screen, clock, width, height, mute)
        init()
        if gameChoice == 1:
            puck.speed = const.EASY
            gameLoop(screen, const.EASY, player1Color, player2Color, backgroundColor)
        elif gameChoice == 2:
            puck.speed = const.HARD
            gameLoop(screen, const.HARD, player1Color, player2Color, backgroundColor)
        elif gameChoice == 0:
            sys.exit()
