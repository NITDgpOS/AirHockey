import pygame
import sys
import os
import random
from globals import *
from constants import MUTE_BUTTON_RADIUS, INFO_BUTTON_RADIUS

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

class selBox():
    def __init__(self, PID, gridPosition):
        self.playerId=PID
        self.gridPos=gridPosition
        self.length=squareSide + 10
        self.breadth=squareSide + 10
        self.init_gridPos = gridPosition

    def moveLeft(self):
        if self.init_gridPos+2>=self.gridPos>self.init_gridPos:
            self.gridPos-=1

    def moveRight(self):
        if self.init_gridPos<=self.gridPos<self.init_gridPos+2:
            self.gridPos+=1

    def draw(self,screen,x,y):
        pygame.draw.rect(screen, (255, 255, 255),(x,y,self.length,self.breadth))


# INFO
# This functions renders a ingame help 
def showInfo(screen, scrWidth, scrHeight, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((60, 90, 100))
        mainText = pygame.font.Font('freesansbold.ttf', 35)
        otherText = pygame.font.Font('freesansbold.ttf', 25)

        gameplay = mainText.render('HELP', True, colors[0][1])
        screen.blit(gameplay, (550, 70))

        line = otherText.render("CONTROLS:-", True, const.WHITE)
        screen.blit(line, (130, 130))
        line = otherText.render("PLAYER 1 :- W,A,S,D     PLAYER 2 :- Arrow key's", True, const.WHITE)
        screen.blit(line, (290, 170))
        
        line = otherText.render("1. Choose each player's paddle color at the title screen.", True, const.WHITE)
        screen.blit(line, (100,  220))

        line = otherText.render("2. To start playing, click on the difficulty level.", True, const.WHITE)
        screen.blit(line, (100, 260))

        line = otherText.render("3. Each game comprises of three rounds, and the player who wins ", True, const.WHITE)
        screen.blit(line, (100, 300))
        line = otherText.render("two (or more) rounds is the winner.", True, const.WHITE)
        screen.blit(line, (130, 330))

        line = otherText.render("4. During playtime, game can be paused anytime by pressing SpaceBar ", True, const.WHITE)
        screen.blit(line, (100, 370))
        line = otherText.render("or clicking the pause icon on the screen.", True, const.WHITE)
        screen.blit(line, (130, 400))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Back Button
        if abs(mouse[0] - scrWidth / 2 - 50) < 120 and abs(mouse[1] - 470) < 40:
            pygame.draw.rect(screen, colors[2][1], (scrWidth / 2 - 50, 440, 90, 30))
            if click[0] == 1:
                return
        else:
            pygame.draw.rect(screen, colors[2][0], (scrWidth / 2 - 50, 440, 90, 30))

        back = otherText.render("BACK", True, const.BLACK)
        screen.blit(back, (scrWidth / 2 - 40, 445))
        pygame.display.flip()
        clock.tick(10)


# function for creating a start screen


def airHockeyStart(screen, clock, Scrwidth, Scrheight, mute):

    pygame.mixer.music.load(os.path.join(auxDirectory, 'StartScreenBack.mp3'))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.1)


    # Variables set to none initially
    player1Color = colors[1][1]
    player2Color = colors[1][1]
    colorFlag1 = False
    colorFlag2 = False
    sel_P1 = selBox(1, 0)
    sel_P2 = selBox(2, 3)

    music_paused = False  # to check if music is playing or paused

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    
                #player 1 controls: move highlight with a and d, select with s
                elif event.key == pygame.K_a:
                    sel_P1.moveLeft()
                elif event.key == pygame.K_d:
                    sel_P1.moveRight()
                elif event.key == pygame.K_s:
                    flagLeft = 1
                    player1Color = colors[(sel_P1.gridPos % 3) + 1][1]
                #player 2 controls: move highlight with left and right, select with down
                elif event.key == pygame.K_LEFT:
                    sel_P2.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    sel_P2.moveRight()                
                elif event.key == pygame.K_DOWN:
                    flagRight = 2
                    player2Color = colors[(sel_P2.gridPos % 3) + 1][1]

                elif event.key == pygame.K_e:
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
        sel_P1.draw(screen, positionGrid[sel_P1.gridPos], yposRectLeft - 5)
        sel_P2.draw(screen, positionGrid[sel_P2.gridPos], yposRectLeft - 5)

        #using only three color options back
        for x in range(1,4):
            if mouse[0] > xposRectLeft and mouse[0] < (xposRectLeft + squareSide) and mouse[1] > yposRectLeft and mouse[1] < (yposRectLeft +squareSide) :
                pygame.draw.rect(screen, colors[x][0], (xposRectLeft, yposRectLeft, squareSide, squareSide))
                if click[0] == 1:
                    player1Color = colors[x][1]

                    #updating sel_P1.gridPos to draw after display update
                    sel_P1.gridPos = x-1
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

                    #updating sel_P2.gridPos to draw after display update
                    sel_P2.gridPos = x-1 + 3
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
                return (1, player1Color, player2Color, mute)

        else:
            buttonCircle(screen, colors[0][0], (200, 470), "Easy", smallText, (255, 255, 255),
                         (Scrwidth / 2 -400, Scrheight / 2 + 170))

        # difficulty button 'Hard'
        if abs(mouse[0] - 600) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[4][1], (600, 470), "Hard", largeText, (255, 255, 255),
                         (Scrwidth / 2 , Scrheight / 2 + 170))
            if click[0] == 1:
                if music_paused:
                    pygame.mixer.music.unpause()
                pygame.mixer.music.stop()
                return (2 ,player1Color, player2Color, mute)
        
        else:
            buttonCircle(screen, colors[4][1], (600, 470), "Hard", smallText, (255, 255, 255),
                         (Scrwidth / 2, Scrheight / 2 + 170))

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

        # info button
        screen.blit(info_image , (40, 20))
        if abs(mouse[0] - (40 + 32)) < INFO_BUTTON_RADIUS and abs(mouse[1] - (20 + 32)) < INFO_BUTTON_RADIUS:
            if click[0] == 1:
                showInfo(screen, Scrwidth, Scrheight, clock)

        # mute status toggle using mouse
        if abs(mouse[0] - (width - 100 + 32)) < MUTE_BUTTON_RADIUS and abs(mouse[1] - (20 + 32)) < MUTE_BUTTON_RADIUS and click[0] == 1:
            mute = not mute


        # displaying mute and unmute button
        if mute:
            screen.blit(mute_image, (width - 100, 20))
        else:
            screen.blit(unmute_image, (width - 100, 20))

        pygame.display.update()
        clock.tick(10)
