import pygame
import sys

dimgreen = (46, 120, 50)
green = (56, 142, 60)

dimred = (200, 72, 72)
red = (255, 82, 82)

buttonRadius = 55


# funtion to render font
def textObj(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


# function to render interactive button
def buttonCircle(screen, buttColor, buttonPos, text, textSize, textColor, textPos):
    pygame.draw.circle(screen, buttColor, buttonPos, buttonRadius)
    TextSurf, TextRect = textObj(text, textSize, textColor)
    TextRect.center = textPos
    screen.blit(TextSurf, TextRect)


# function for creating a start screen
def airHockeyStart(screen, clock, Scrwidth, Scrheight):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((60, 90, 100))
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        smallText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = textObj("AirHockey", largeText, (255, 255, 255))
        TextRect.center = (Scrwidth / 2, Scrheight / 2 - 130)
        screen.blit(TextSurf, TextRect)

        # mouse data
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # play button
        if abs(mouse[0] - 200) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, green, (200, 470), "Play", largeText, (255, 255, 255),
                         (Scrwidth / 2 - 400, Scrheight / 2 + 170))
            if click[0] == 1:
                return 1

        else:
            buttonCircle(screen, dimgreen, (200, 470), "Play", smallText, (255, 255, 255),
                         (Scrwidth / 2 - 400, Scrheight / 2 + 170))

        # quit button
        if abs(mouse[0] - 1000) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, red, (1000, 470), "Quit", largeText, (255, 255, 255),
                         (Scrwidth / 2 + 400, Scrheight / 2 + 170))
            if click[0] == 1:
                return 0
        else:
            buttonCircle(screen, dimred, (1000, 470), "Quit", smallText, (255, 255, 255),
                         (Scrwidth / 2 + 400, Scrheight / 2 + 170))

        pygame.display.update()
        clock.tick(10)
