import constants as const
import pygame
import os

auxDirectory = os.path.join(os.path.dirname(__file__), 'assets')

smallfont = None
score1, score2 = 0, 0

# Sound globals.
paddleHit = None
goal_whistle = None
backgroundMusic = None

# image for mute and unmute
mute_image = pygame.image.load(os.path.join(auxDirectory, 'mute.png'))
unmute_image = pygame.image.load(os.path.join(auxDirectory, 'unmute.png'))

play_image = pygame.image.load(os.path.join(auxDirectory, 'play.png'))
pause_image = pygame.image.load(os.path.join(auxDirectory, 'pause.png'))

info_image = pygame.image.load(os.path.join(auxDirectory, "info.png"))


# game globals.
clock = None
screen = None

# width and height of the screen.
width, height = const.WIDTH, const.HEIGHT

# button constants
buttonRadius = 60
squareSide = 80

# color globals
# (dimgreen, green) , (dimred, red) , (dimblue, blue ) , (yellow, dimyellow), (orange, dimorange)
colors = [[(46, 120, 50), (66, 152, 60)], [(200, 72, 72), (255, 92, 92)],
          [(0, 158, 239), (100, 189, 219)], [(221, 229, 2), (252, 255, 59)],
          [(232, 114, 46), (244, 133, 51)]]

theme_colors = [[(255, 169, 119), (255, 161, 107)], [(230, 232, 104), (217, 219, 92)],
                [(125, 216, 201), (103, 178, 166)], [(164, 229, 121), (117, 168, 84)]]
