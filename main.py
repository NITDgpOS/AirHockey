import pygame, sys
from pygame.locals import *
from gameObjects import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

#Adding the code for logo display -thealphadollar
gamelogo = pygame.image.load('img/logo.png')
pygame.display.set_icon(gamelogo)


# Create Game Objects

paddleVelocity = 10
paddle1 = Paddle(10, screen.get_height() / 2 - 40, 10, 80, paddleVelocity)
paddle2 = Paddle(screen.get_width() - 20, screen.get_height() / 2 - 40, 10, 80, paddleVelocity)

puckVelocity = [8, 4]
puck = Puck(screen.get_width() / 2, screen.get_height() / 2, 20, 20, puckVelocity)

divider = pygame.Rect(screen.get_width() / 2, 0, 3, screen.get_height())

# Score
score1, score2 = 0, 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    w, s, up, down, d, a, right, left = 0, 0, 0, 0, 0, 0, 0, 0
    # Process Player Input
    if pygame.key.get_pressed()[pygame.K_w] != 0:
        w = 1
    if pygame.key.get_pressed()[pygame.K_s] != 0:
        s = 1
    if pygame.key.get_pressed()[pygame.K_UP] != 0:
        up = 1
    if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
        down = 1
    if pygame.key.get_pressed()[pygame.K_d] != 0:
        d = 1
    if pygame.key.get_pressed()[pygame.K_a] != 0:
        a = 1
    if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        right = 1
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        left = 1

    # Update Logic

    # Update Paddle1
    paddle1.y += (s - w) * paddleVelocity
    paddle1.x += (d - a) * paddleVelocity
    if paddle1.y < 0:
        paddle1.y = 0
    elif paddle1.y > screen.get_height() - paddle1.height:
        paddle1.y = screen.get_height() - paddle1.height
    if paddle1.x < 0:
        paddle1.x = 0
    elif paddle1.x > screen.get_width() / 2 - paddle1.width:
        paddle1.x = screen.get_width() / 2 - paddle1.width

    # Update Paddle2
    paddle2.y += (down - up) * paddleVelocity
    paddle2.x += (right - left) * paddleVelocity
    if paddle2.y < 0:
        paddle2.y = 0
    elif paddle2.y > screen.get_height() - paddle2.height:
        paddle2.y = screen.get_height() - paddle2.height
    if paddle2.x > screen.get_width() - paddle1.width:
        paddle2.x = screen.get_width() - paddle1.width
    elif paddle2.x < screen.get_width() / 2:
        paddle2.x = screen.get_width() / 2

    # Update Puck
    puck.x += puck.velocity[0]
    puck.y += puck.velocity[1]
    if puck.x < 0:
        score2 += 1
        puck.serveDirection = -1
        puck.reset()
    elif puck.x > screen.get_width() - puck.width:
        score1 += 1
        puck.serveDirection = 1
        puck.reset()
    if puck.y < 0 or puck.y > screen.get_height() - puck.height:
        puck.velocity[1] *= -1
    if puck.getPuck().colliderect(paddle1.getPaddle()) or puck.getPuck().colliderect(paddle2.getPaddle()):
        puck.velocity[0] *= -1

    # Render Logic
    screen.fill((0, 40, 40))

    pygame.draw.rect(screen, (255, 0, 0), paddle1.getPaddle())
    pygame.draw.rect(screen, (255, 255, 0), paddle2.getPaddle())
    pygame.draw.circle(screen, (255, 255, 255), (puck.x, puck.y), int(puck.width / 2))
    pygame.draw.rect(screen, (255, 255, 255), divider)

    pygame.display.flip()
    clock.tick(60)
