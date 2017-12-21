import pygame
import sys
import os
from globals import *

selected_color = (224, 214, 141)
selected_flag = 0

def themeScreen(screen, clock, Scrwidth, Scrheight, musicPaused):
    if musicPaused == False:
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.1)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((60,90,100))

        #using the global color which is initialized
        global selected_color 
        global selected_flag

        theme_colors = [ [(255, 169, 119), (255, 161, 107)], [(230, 232, 104), (217, 219, 92)],
                         [(125, 216, 201), (103, 178, 166)], [(164, 229, 121), (117, 168, 84)] ]
        
        #mouse data
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #FIRST
        x1, y1 = 200, 50
        if mouse[0] > x1 and mouse[0] < x1 + 300 and mouse[1] > y1 and mouse [1] < y1 +150:
            pygame.draw.rect(screen, theme_colors[0][0], (x1, y1, 300, 150), 0) #rect fill
            if click[0] == 1:
                selected_color = theme_colors[0][0]
                selected_flag = 1
        else:
            pygame.draw.rect(screen, theme_colors[0][1], (x1, y1, 300, 150), 0) #rect fill
        pygame.draw.rect(screen, const.WHITE, (x1, y1, 300, 150), 2) #rect border
        pygame.draw.circle(screen, const.WHITE, (x1 + 150, y1 + 75), 30, 2) #middle circle
        pygame.draw.line(screen, const.WHITE, (x1 + 150, y1), (x1 + 150, y1 + 150), 2) #middle line
        pygame.draw.rect(screen, const.WHITE, (x1, y1 + 30, 50, 95), 2) #left small rect
        pygame.draw.rect(screen, const.WHITE, (x1 + 300 - 50, y1 + 30, 50, 95), 2) #right small rect

        #second
        x2, y2 = Scrwidth - 500, 50  
        if mouse[0] > x2 and mouse[0] < x2 + 300 and mouse[1] > y2 and mouse[1] < y2 + 150:
            pygame.draw.rect(screen, theme_colors[1][0], (x2, y2, 300, 150), 0) #rect fill
            if click[0] == 1:
                selected_color = theme_colors[1][0]
                selected_flag = 1
        else:      
            pygame.draw.rect(screen, theme_colors[1][1], (x2, y2, 300, 150), 0) #rect fill
        pygame.draw.rect(screen, const.WHITE, (x2, y2, 300, 150), 2) #rect border
        pygame.draw.circle(screen, const.WHITE, (x2 + 150, y2 + 75), 30, 2) #middle circle
        pygame.draw.line(screen, const.WHITE, (x2 + 150, y2), (x2 + 150, y2 + 150), 2) #middle line
        pygame.draw.rect(screen, const.WHITE, (x2, y2 + 30, 50, 95), 2) #left small rect
        pygame.draw.rect(screen, const.WHITE, (x2 + 300 - 50, y2 + 30, 50, 95), 2) #right small rect

        #third
        x3, y3 = 200, Scrheight / 2 - 50
        if mouse[0] > x3 and mouse[0] < x3 + 300 and mouse[1] > y3 and mouse[1] < y3 +150:
            pygame.draw.rect(screen, theme_colors[2][0], (x3, y3, 300, 150), 0) #rect fill
            if click[0] == 1:
                selected_color = colors[2][0]
                selected_flag = 1
        else:
            pygame.draw.rect(screen, theme_colors[2][1], (x3, y3, 300, 150), 0) #rect fill
        pygame.draw.rect(screen, const.WHITE, (x3, y3, 300, 150), 2) #rect border
        pygame.draw.circle(screen, const.WHITE, (x3 + 150, y3 + 75), 30, 2) #middle circle
        pygame.draw.line(screen, const.WHITE, (x3 + 150, y3), (x3 + 150, y3 + 150), 2) #middle line
        pygame.draw.rect(screen, const.WHITE, (x3, y3 + 30, 50, 95), 2) #left small rect
        pygame.draw.rect(screen, const.WHITE, (x3 + 300 - 50, y3 + 30, 50, 95), 2) #right small rect

        #fourth
        x4, y4 = Scrwidth - 500, Scrheight / 2 - 50
        if mouse[0] > x4 and mouse[0] < x4 + 300 and mouse[1] > y4 and mouse[1] < y4 + 150:
            pygame.draw.rect(screen, theme_colors[3][0], (x4, y4, 300, 150), 0) #rect fill
            if click[0] == 1:
                selected_color = theme_colors[3][0]
                selected_flag = 1
        else:
            pygame.draw.rect(screen, theme_colors[3][1], (x4, y4, 300, 150), 0) #rect fill
        pygame.draw.rect(screen, const.WHITE, (x4, y4, 300, 150), 2) #rect border
        pygame.draw.circle(screen, const.WHITE, (x4 + 150, y4 + 75), 30, 2) #middle circle
        pygame.draw.line(screen, const.WHITE, (x4 + 150, y4), (x4 + 150, y4 + 150), 2) #middlw line
        pygame.draw.rect(screen, const.WHITE, (x4, y4 + 30, 50, 95), 2) #left small rect
        pygame.draw.rect(screen, const.WHITE, (x4 + 300 - 50, y4 + 30, 50, 95), 2) #right small rect


        #if theme is selected
        if selected_flag == 1:
            text_selected = smallfont.render("SELECTED", True, const.WHITE)
            screen.blit(text_selected, [width / 2 - 60, 450])

        #start
        x, y = width / 2 - 50, 500
        if mouse[0] > x and mouse[0] < x + 90 and mouse[1] > 500 and mouse[1] < 530:
            pygame.draw.rect(screen, colors[0][1], (width / 2 - 50, 500, 90, 30), 0)
            if click[0] == 1:
                return selected_color
        else:
            pygame.draw.rect(screen, colors[0][0], (width / 2 - 50, 500, 90, 30), 0)
        smallfont = pygame.font.SysFont("comicsans", 35)
        text_start = smallfont.render("START", True, const.BLACK)
        screen.blit(text_start, [width / 2 - 44, 500])

        pygame.display.update()
        clock.tick(10)