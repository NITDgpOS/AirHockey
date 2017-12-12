import pygame
import sys


#colours
#(dimgreen,green) , (dimred,red) , (dimblue,blue ) , (yellow,dimyellow), (orange, dimorange) 
colors = [ [(46, 120, 50),(66, 152, 60)] , [(200, 72, 72),(255, 92, 92)] ,
           [(0, 158, 239),(100, 189, 219)] , [(221, 229, 2),(252, 255, 59)],
           [(232, 114, 46),(244, 133, 51)]] 


buttonRadius = 60
squareSide = 80

flagLeft = 0
flagRight = 0

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



# function for creating a start screen
def airHockeyStart(screen, clock, Scrwidth, Scrheight):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((60, 90, 100))
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        smallText = pygame.font.Font('freesansbold.ttf', 30)
        dispText(screen, "AirHockey", (Scrwidth / 2, Scrheight / 2 -250), largeText, (255, 255, 255))

        # mouse data
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #choose colors for paddle

        xposRectLeft = 150 
        yposRectLeft = Scrheight/2 - 90

        xposRectRight = Scrwidth - 150 - 320
        yposRectRight = Scrheight/2 - 90

        dispText(screen, "Player 1", ( Scrwidth / 2 - 290, Scrheight / 2 - 120), smallText, (255,255,255))
        dispText(screen, "Player 2", ( Scrwidth / 2 + 290, Scrheight / 2 - 120), smallText, (255,255,255))

        
        #Color picking pallete for player 1 (Left)

        #white border line
        pygame.draw.rect(screen, (255,255,255),(xposRectLeft - 10, yposRectLeft -10, 320 , 100), 1)

        #using only three color options 
        for x in range(1,4):
            if mouse[0] > xposRectLeft and mouse[0] < (xposRectLeft + squareSide) and mouse[1] > yposRectLeft and mouse[1] < (yposRectLeft +squareSide) :
                pygame.draw.rect(screen, colors[x][0], (xposRectLeft, yposRectLeft, squareSide, squareSide))
                if click[0] == 1:
                    player1Color = colors[x][1]
                    global flagLeft
                    flagLeft = 1
            else:
                pygame.draw.rect(screen, colors[x][1], (xposRectLeft, yposRectLeft, squareSide, squareSide))
            xposRectLeft  = xposRectLeft + squareSide + 30
            x = x + 1



        #color picking pallete for player 2(Right)

        #white border Line
        pygame.draw.rect(screen, (255,255,255),(xposRectRight -10, yposRectRight -10,320 , 100),1)
        
        #using only three color options
        for x in range(1,4):
            if mouse[0] > xposRectRight and mouse[0] < (xposRectRight + squareSide) and mouse[1] > yposRectRight and mouse[1] < (yposRectRight +squareSide) :
                pygame.draw.rect(screen, colors[x][0], (xposRectRight, yposRectRight, squareSide, squareSide))
                if click[0] == 1 :
                    player2Color = colors[x][1]
                    global flagRight
                    flagRight = 2
            else:
                pygame.draw.rect(screen, colors[x][1], (xposRectRight, yposRectRight, squareSide, squareSide))
            xposRectRight = xposRectRight + squareSide + 30
        if flagLeft == 1:
            dispText(screen, "selected", (Scrwidth / 4  , yposRectLeft + 120), smallText, (255,255,255))
        if flagRight == 2:
            dispText(screen, "selected", (Scrwidth - Scrwidth/4, yposRectLeft + 120), smallText, (255,255,255))

        # difficulty button 'Hard'
        if abs(mouse[0] - 200) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[4][1], (200, 470), "Hard", largeText, (255, 255, 255),
                         (Scrwidth / 2 -400 , Scrheight / 2 + 170))
            if click[0] == 1:
                return (2, player1Color, player2Color)

        else:
            buttonCircle(screen, colors[4][0], (200, 470), "Hard", smallText, (255, 255, 255),
                         (Scrwidth / 2 -400, Scrheight / 2 + 170))

        # difficulty button 'Easy'
        if abs(mouse[0] - 600) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[0][1], (600, 470), "Easy", largeText, (255, 255, 255),
                         (Scrwidth / 2 , Scrheight / 2 + 170))
            if click[0] == 1:
                return (1, player1Color, player2Color)
        
        else:
            buttonCircle(screen, colors[0][0], (600, 470), "Easy", smallText, (255, 255, 255),
                         (Scrwidth / 2, Scrheight / 2 + 170))

        # quit button
        if abs(mouse[0] - 1000) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, colors[1][1], (1000, 470), "Quit", largeText, (255, 255, 255),
                         (Scrwidth / 2 + 400, Scrheight / 2 + 170))
            if click[0] == 1:
                return (0, 0, 0)   
        else:
            buttonCircle(screen, colors[1][0], (1000, 470), "Quit", smallText, (255, 255, 255),
                         (Scrwidth / 2 + 400, Scrheight / 2 + 170))

        pygame.display.update()
        clock.tick(10)
