import pygame
import sys
import random as rand
import os
from startScreen import *
from globals import *

def GameEnd(screen, clock, player, backgroundColor):

    first_time = True
    auxDirectory = os.path.join(os.path.dirname(__file__), 'assets')
    celebText = pygame.font.Font(os.path.join(auxDirectory,'Jelly Crazies.ttf'), 70)
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    smallText = pygame.font.Font('freesansbold.ttf', 30)

    while True:

        # to smoothly shine winning message
        delay = 0

        screen.fill(backgroundColor)

        # set flashing colors
        color_x = rand.randint(0,4)
        color_y = rand.randint(0,1)

        # Get inputs
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            # Press R to reset game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return 1
            # Press M to go to menu
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                return 2
            # Press esc or Q to quit
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # print which player won
        if player == 1 and delay == 0:
            dispText(screen, "PLAYER 1 WINS", (width / 2, height / 2 - 150), celebText, colors[color_x][color_y])
        elif player == 2 and delay == 0:
            dispText(screen, "PLAYER 2 WINS", (width / 2, height / 2 - 150), celebText, colors[color_x][color_y])

        # Drawing buttons for reset, menu and exit.
        # Reset button
        if abs(mouse_pos[0] - 200) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[0][0], (200, 470), "Reset", largeText, (255, 255, 255),
                         (width / 2 - 400, height / 2 + 170))
            if mouse_press[0] == 1:
                return 1

        else:
            buttonCircle(screen, colors[0][0], (200, 470), "Reset", smallText, (255, 255, 255),
                         (width / 2 - 400, height / 2 + 170))

        # Menu button
        if abs(mouse_pos[0] - 600) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[4][1], (600, 470), "Menu", largeText, (255, 255, 255),
                         (width / 2, height / 2 + 170))
            if mouse_press[0] == 1:
                return 2

        else:
            buttonCircle(screen, colors[4][1], (600, 470), "Menu", smallText, (255, 255, 255),
                         (width / 2, height / 2 + 170))

        # quit button
        if abs(mouse_pos[0] - 1000) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[1][1], (1000, 470), "Quit", largeText, (255, 255, 255),
                         (width / 2 + 400, height / 2 + 170))
            if mouse_press[0] == 1:
                pygame.quit()        
                return 3
        else:
            buttonCircle(screen, colors[1][0], (1000, 470), "Quit", smallText, (255, 255, 255),
                         (width / 2 + 400, height / 2 + 170))

        delay = (delay + 1) % 300
        first_time = False
        pygame.display.update()
        clock.tick(10)

