import pygame
<<<<<<< HEAD
import math
import constants as const


class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = const.PADDLESIZE
        self.speed = const.PADDLESPEED
        self.mass = const.PADDLEMASS
        self.angle = 0
=======


class Paddle():
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
>>>>>>> upstream/master

    def checkTopBottomBounds(self, height):
        # top
        if self.y - self.radius <= 0:
            self.y = self.radius
        # bottom
        elif self.y + self.radius > height:
            self.y = height - self.radius

    def checkLeftBoundary(self, width):
        if self.x - self.radius <= 0:
            self.x = self.radius
        elif self.x + self.radius > int(width / 2):
            self.x = int(width / 2) - self.radius

    def checkRightBoundary(self, width):
        if self.x + self.radius > width:
            self.x = width - self.radius
        elif self.x - self.radius < int(width / 2):
            self.x = int(width / 2) + self.radius

<<<<<<< HEAD
    def move(self, up, down, left, right, time_delta):
        dx, dy = self.x, self.y
        self.x += (right - left) * self.speed * time_delta
        self.y +=  (down - up) * self.speed * time_delta

        dx = self.x - dx
        dy = self.y - dy

        self.angle = math.atan2(dy, dx)
=======

    def move(self, up, down, left, right, time_delta):
        self.x += (right - left) * self.speed * time_delta
        self.y += (down - up) * self.speed * time_delta
>>>>>>> upstream/master

    def draw(self, screen, color):
        position = (int(self.x), int(self.y))

        pygame.draw.circle(screen, color, position, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 5, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 10, 2)

    def reset(self, startX, startY):
        self.x = startX
        self.y = startY
