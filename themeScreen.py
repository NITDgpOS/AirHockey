import sys
from globals import *
from startScreen import disp_text

selected_color = theme_colors[0][0]


def theme_screen(screen, clock, scr_width, scr_height, music_paused):

    # initialised font
    smallfont = pygame.font.SysFont("comicsans", 35)

    if not music_paused:
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.1)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((60, 90, 100))

        # using the global color which is initialized
        global selected_color

        # mouse data
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # positions of four boxes
        pos_of_boxes = [[200, 50], [scr_width-500, 50], [200, scr_height / 2 - 50], [scr_width - 500,
                                                                                     scr_height / 2 - 50]]

        # This loop will draw the four boxes
        i = 0
        for xy in pos_of_boxes:
            if (mouse[0] > xy[0]) and (mouse[0] < xy[0] + 300) and (mouse[1] > xy[1]) and (mouse[1] < xy[1] + 150):
                pygame.draw.rect(screen, theme_colors[i][0], (xy[0], xy[1], 300, 150), 0)  # rect fill
                if click[0] == 1:
                    selected_color = theme_colors[i][0]
            else:
                pygame.draw.rect(screen, theme_colors[i][1], (xy[0], xy[1], 300, 150), 0)   # rect fill
            pygame.draw.rect(screen, const.WHITE, (xy[0], xy[1], 300, 150), 2)  # rect border
            pygame.draw.circle(screen, const.WHITE, (xy[0] + 150, xy[1] + 75), 30, 2)   # middle circle
            pygame.draw.line(screen, const.WHITE, (xy[0] + 150, xy[1]), (xy[0] + 150, xy[1] + 150), 2)  # middle line
            pygame.draw.rect(screen, const.WHITE, (xy[0], xy[1] + 30, 50, 95), 2)   # left small rect
            pygame.draw.rect(screen, const.WHITE, (xy[0] + 300 - 50, xy[1] + 30, 50, 95), 2)    # right small rect
            i = i+1

        # displaying the selected color
        disp_text(screen, "SELECTED COLOR", (width / 2, 450), smallfont, selected_color)

        # start
        x, y = width / 2 - 50, 500
        if (mouse[0] > x) and (mouse[0] < x + 90) and (mouse[1] > 500) and (mouse[1] < 530):
            pygame.draw.rect(screen, colors[0][1], (width / 2 - 50, 500, 90, 30), 0)
            if click[0] == 1:
                return selected_color
        else:
            pygame.draw.rect(screen, colors[0][0], (width / 2 - 50, 500, 90, 30), 0)
        text_start = smallfont.render("START", True, const.BLACK)
        screen.blit(text_start, [width / 2 - 44, 500])

        pygame.display.update()
        clock.tick(10)
