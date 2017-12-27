import pygame
import sys
import os
import random
from globals import *
from constants import MUTE_BUTTON_RADIUS

x=squareSide+30
positionGrid = [145,145+x,145+2*x,145+3*x+250,145+4*x+250, 145+5*x+250]

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


#funtion to display text
def dispText(screen, text, center, fontAndSize, color):
    TextSurf, TextRect = textObj(text, fontAndSize, color)
    TextRect.center = center
    screen.blit(TextSurf, TextRect)

class selBox:
    def __init__(self):
        self.playerId=1
        self.gridPos=0
        self.length=squareSide + 10
        self.breadth=squareSide + 10

    def moveLeft(self):
        if self.gridPos>0:
            self.gridPos-=1

        if self.gridPos > 2:
            self.playerId=2
        else:
            self.playerId=1

    def moveRight(self):
        if self.gridPos<5:
            self.gridPos+=1

        if self.gridPos > 2:
            self.playerId=2
        else:
            self.playerId=1

    def draw(self,screen,x,y):
        pygame.draw.rect(screen, (255, 255, 255),(x,y,self.length,self.breadth))

# function for creating a start screen


def airHockeyStart(screen, clock, Scrwidth, Scrheight, mute):

    global powerEnable , clickflag

    pygame.mixer.music.load(os.path.join(auxDirectory, 'StartScreenBack.mp3'))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.1)


    # Variables set to none initially
    player1Color = colors[1][1]
    player2Color = colors[1][1]
    colorFlag1 = False
    colorFlag2 = False
    sel=selBox()

    music_paused = False  # to check if music is playing or paused

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # print("key q is pressed ")
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_a:
                    # print("key a is pressed ")
                    sel.moveLeft()
                elif event.key == pygame.K_d:
                    # print("key d is pressed ")
                    sel.moveRight()
                elif event.key == pygame.K_RETURN:
                    # print("key RETURN is pressed ")
                    if sel.playerId == 1:
                        flagLeft = 1
                        player1Color = colors[(sel.gridPos % 3) + 1][1]
                    else:
                        flagRight = 2
                        player2Color = colors[(sel.gridPos % 3) + 1][1]
                elif event.key == pygame.K_e:
                    #print("key e is pressed ")
                    if player1Color == None or player2Color == None:
                        if player1Color == None:
                            colorFlag1 = True
                        if player2Color == None:
                            colorFlag2 = True
                    else:
                        return (1, player1Color, player2Color,mute)
                elif event.key == pygame.K_h:
                    #print("key h is pressed ")
                    if player1Color == None or player2Color == None:
                        if player1Color == None:
                            colorFlag1 = True
                        if player2Color == None:
                            colorFlag2 = True
                    else:
                        return (2, player1Color, player2Color,mute)

        screen.fill((60, 90, 100))
        celebText = pygame.font.Font(os.path.join(auxDirectory,'Jelly Crazies.ttf'), 70)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        smallText = pygame.font.Font('freesansbold.ttf', 30)
        smallerText=pygame.font.Font('freesansbold.ttf', 20)
        color_x = random.randint(0,4)
        color_y = random.randint(0,1)
        dispText(screen, "AIRHOCKEY", (Scrwidth / 2, 100), celebText, colors[color_x][color_y])

        # mute and unmute audio code
        if mute and (not music_paused):
            pygame.mixer.music.pause()
            music_paused = True
        elif (not mute) and music_paused:
            pygame.mixer.music.unpause()
            music_paused = False


        # mouse data
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #choose colors for paddle

        xposRectLeft = 150 
        yposRectLeft = Scrheight/2 - 70

        xposRectRight = Scrwidth - 150 - 320
        yposRectRight = Scrheight/2 - 70

        dispText(screen, "Player 1", (Scrwidth / 2 - 290, Scrheight / 2 - 100), smallText, (255, 255, 255))
        dispText(screen, "Player 2", (Scrwidth / 2 + 290, Scrheight / 2 - 100), smallText, (255, 255, 255))
        
        #Color picking pallete for player 1 (Left)

        #white border line
        pygame.draw.rect(screen, (255,255,255),(xposRectLeft - 10, yposRectLeft - 10, 320 , 100), 1)
        # Draw selection box
        sel.draw(screen, positionGrid[sel.gridPos], yposRectLeft - 5)

        #using only three color options back
        for x in range(1,4):
            if mouse[0] > xposRectLeft and mouse[0] < (xposRectLeft + squareSide) and mouse[1] > yposRectLeft and mouse[1] < (yposRectLeft +squareSide) :
                pygame.draw.rect(screen, colors[x][0], (xposRectLeft, yposRectLeft, squareSide, squareSide))
                if click[0] == 1:
                    player1Color = colors[x][1]

                    #updating sel.gridPos to draw after display update
                    sel.gridPos = x-1
            else:
                pygame.draw.rect(screen, colors[x][1], (xposRectLeft, yposRectLeft, squareSide, squareSide))
            xposRectLeft  = xposRectLeft + squareSide + 30



        #color picking pallete for player 2(Right)

        #white border Line
        pygame.draw.rect(screen, (255,255,255),(xposRectRight -10, yposRectRight -10,320 , 100),1)
        
        #using only three color options
        for x in range(1,4):
            if mouse[0] > xposRectRight and mouse[0] < (xposRectRight + squareSide) and mouse[1] > yposRectRight and mouse[1] < (yposRectRight +squareSide) :
                pygame.draw.rect(screen, colors[x][0], (xposRectRight, yposRectRight, squareSide, squareSide))
                if click[0] == 1 :
                    player2Color = colors[x][1]

                    #updating sel.gridPos to draw after display update
                    sel.gridPos = x-1 + 3
            else:
                pygame.draw.rect(screen, colors[x][1], (xposRectRight, yposRectRight, squareSide, squareSide))
            xposRectRight = xposRectRight + squareSide + 30

        # displaying the color selected

        dispText(screen, "Color Selected", (Scrwidth / 4, yposRectLeft + 120), smallText, player1Color)
        dispText(screen, "Color selected", (Scrwidth - Scrwidth/4 - 20, yposRectLeft + 120), smallText, player2Color)


        # difficulty button 'Easy'
        if abs(mouse[0] - 200) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[0][0], (200, 470), "Easy", largeText, (255, 255, 255),
                         (Scrwidth / 2 - 400, Scrheight / 2 + 170))
            if click[0] == 1:
                if music_paused:
                    pygame.mixer.music.unpause()
                pygame.mixer.music.stop()
                return (1, player1Color, player2Color, mute , powerEnable)

        else:
            buttonCircle(screen, colors[0][0], (200, 470), "Easy", smallText, (255, 255, 255),
                         (Scrwidth / 2 -400, Scrheight / 2 + 170))

        # difficulty button 'Hard'
        if abs(mouse[0] - 450) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[4][1], (450, 470), "Hard", largeText, (255, 255, 255),
                         (Scrwidth / 2 -150, Scrheight / 2 + 170))
            if click[0] == 1:
                if music_paused:
                    pygame.mixer.music.unpause()
                pygame.mixer.music.stop()
                return (2 ,player1Color, player2Color, mute,powerEnable)
        
        else:
            buttonCircle(screen, colors[4][1], (450, 470), "Hard", smallText, (255, 255, 255),
                         (Scrwidth / 2-150, Scrheight / 2 + 170))

        #Button to enable or disable powerups
        
        if abs(mouse[0] - 700) < buttonRadius and abs(mouse[1] - 470) < buttonRadius and click[0] == 1:
            if clickflag == 1:
                buttonCircle(screen, colors[4][1], (700, 470), "Power OFF", smallerText, (255, 255, 255),
                         (Scrwidth / 2+100 , Scrheight / 2 + 170))
                clickflag=0
                powerEnable=0     
            else:
                buttonCircle(screen, colors[4][1], (700, 470), "Power ON", smallerText, (255, 255, 255),
                         (Scrwidth / 2+100, Scrheight / 2 + 170))      
                clickflag=1
                powerEnable = 1
        elif powerEnable == 1:
            buttonCircle(screen, colors[4][1], (700, 470), "Power ON", smallerText, (255, 255, 255),
                         (Scrwidth / 2+100 , Scrheight / 2 + 170))

        
        elif powerEnable == 0:
            buttonCircle(screen, colors[4][1], (700, 470), "Power OFF", smallerText, (255, 255, 255),
                         (Scrwidth / 2+100, Scrheight / 2 + 170))

        # quit button
        if abs(mouse[0] - 1000) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[1][1], (1000, 470), "Quit", largeText, (255, 255, 255),
                         (Scrwidth / 2 + 400, Scrheight / 2 + 170))
            if click[0] == 1:
                pygame.quit()
                sys.exit()                
        else:
            buttonCircle(screen, colors[1][0], (1000, 470), "Quit", smallText, (255, 255, 255),
                         (Scrwidth / 2 + 400, Scrheight / 2 + 170))

        # mute status toggle using mouse
        if abs(mouse[0] - (width - 100 + 32)) < MUTE_BUTTON_RADIUS and abs(mouse[1] - (height / 2 - 250)) < MUTE_BUTTON_RADIUS and click[0] == 1:
            mute = not mute


        # displaying mute and unmute button
        if mute:
            screen.blit(mute_image, (width - 100, Scrheight / 2 -250 - 32))
        else:
            screen.blit(unmute_image, (width - 100, Scrheight / 2 -250 - 32))

        pygame.display.update()
        clock.tick(10)
