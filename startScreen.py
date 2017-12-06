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
def color_change(screen,Color,x,y,width,height,player):
    pygame.draw.rect(screen, Color, (x, y, width, height),0)
    pygame.draw.circle(screen,(255,255,255),(x-20,y+35),15)
    smallText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf,TextRect=textObj("<",smallText,(0,0,0))
    TextRect.center=(x-20,y+33)
    player_color = smallText.render("Player "+player, True, (0,0,0))
    screen.blit(player_color,[x+(width/2)-55,y+height+25])
    screen.blit(TextSurf,TextRect)
    pygame.draw.circle(screen,(255,255,255),(x+width+20,y+35),15)
    TextSurf2,TextRect2=textObj(">",smallText,(0,0,0))
    TextRect2.center=(x+21+width,y+33)
    screen.blit(TextSurf2,TextRect2)
def get_color(num,color,Type):
    if(num==1):
        color=(255,0,0)
        if Type=="Dec":
            num=6
    elif(num==2):
        color=(0,0,255)
    elif(num==3):
        color=(255,255,0)
    elif(num==4):
        color=(255,0,255)
    elif(num==5):
        if Type=="Inc":
            num=0
        color=(0,255,255)
    if(Type=="Inc"):
        return color,num
    else:
        return color,6-num
# function for creating a start screen
def airHockeyStart(screen, clock, Scrwidth, Scrheight):
    num_p1=1
    num_p2=1
    color_p1=(255,0,0)
    color_p2=(255,255,0)
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
        color_change(screen,color_p1,120,110,150,80,"1")
        color_change(screen,color_p2,920,110,150,80,"2")
        if((mouse[0]>85 and mouse[0]<115) and (mouse[1]>130 and mouse[1]<160)):
            # pygame.draw.circle(screen,(255,200,255),(100,145),15)
            if pygame.mouse.get_pressed()[0]==1:
                num_p1+=1
                color_p1,num_p1=get_color(num_p1,color_p1,"Inc")
        elif((mouse[0]>275 and mouse[0]<305) and (mouse[1]>130 and mouse[1]<160)):
            if pygame.mouse.get_pressed()[0]==1:
                num_p1+=1
                color_p1,num_p1=get_color(5-num_p1+1,color_p1,"Dec")
            # pygame.draw.circle(screen,(255,200,255),(100,145),15)
        if((mouse[0]>885 and mouse[0]<915) and (mouse[1]>130 and mouse[1]<160)):
            # pygame.draw.circle(screen,(255,200,255),(100,145),15)
            if pygame.mouse.get_pressed()[0]==1:
                num_p2+=1
                color_p2,num_p2=get_color(num_p2,color_p2,"Inc")
        elif((mouse[0]>1075 and mouse[0]<1105) and (mouse[1]>130 and mouse[1]<160)):
            # pygame.draw.circle(screen,(255,200,255),(100,145),15)
            if pygame.mouse.get_pressed()[0]==1:
                num_p2+=1
                color_p2,num_p2=get_color(5-num_p2+1,color_p2,"Dec")
        





        # difficulty button 'Hard'
        if abs(mouse[0] - 200) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, green, (200, 470), "Hard", largeText, (255, 255, 255),
                (Scrwidth / 2 -400 , Scrheight / 2 + 170))
            if click[0] == 1:
                return 2,color_p1,color_p2

        else:
            buttonCircle(screen, dimgreen, (200, 470), "Hard", smallText, (255, 255, 255),
                (Scrwidth / 2 -400, Scrheight / 2 + 170))
        
        # difficulty button 'Easy'
        if abs(mouse[0] - 600) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            buttonCircle(screen, green, (600, 470), "Easy", largeText, (255, 255, 255),
                (Scrwidth / 2 , Scrheight / 2 + 170))
            if click[0] == 1:
                return 1,color_p1,color_p2
        
        else:
            buttonCircle(screen, dimgreen, (600, 470), "Easy", smallText, (255, 255, 255),
                (Scrwidth / 2, Scrheight / 2 + 170))

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
