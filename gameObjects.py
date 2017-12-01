import pygame


class Paddle():
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def getPaddle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def checkTopBottomBounds(self, height):
        if self.y < 22:
            self.y = 22
        elif self.y > height - self.height:
            self.y = height - self.height

    def checkLeftBoundary(self, width):
        if self.x < 22:
            self.x = 22
        elif self.x > width / 2 - self.width:
            self.x = width / 2 - self.width

    def checkRightBoundary(self, width):
        if self.x > width - self.width:
            self.x = width - self.width
        elif self.x < width / 2+22:
            self.x = width / 2+22


class Puck():
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.serveDirection = 1

    def getPuck(self):
        return pygame.Rect(self.x - int(self.width) / 2, self.y - int(self.height / 2), self.width, self.height)

    def reset(self):
        self.velocity[0] = 10 * self.serveDirection
        self.velocity[1] = 4 * self.serveDirection
        self.x = self.init_x
        self.y = self.init_y
