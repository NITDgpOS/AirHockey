import pygame
import math


class Paddle():
    def __init__(self, x, y, radius, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity

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

    def draw(self, screen, color):
        position = (self.x, self.y)

        pygame.draw.circle(screen, color, position, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 5, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 10, 2)


class Puck():
    def __init__(self, x, y, radius, velocity):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.radius = radius
        self.velocity = velocity
        self.serveDirection = 1

    def collidesTopBottom(self, height):
        return self.y - self.radius < 0 or self.y + self.radius > height

    def collidesLeftRight(self,width):
        return self.x - self.radius < 0 or self.x + self.radius > width



    def collidesWithPaddle(self, paddle):
        """
        Checks collision between circles using the distance formula:
        dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)

        returns true if the distance is less than or equal to sum of
        radius of the puck and the paddle
        """
        centerDistance = (paddle.x - self.x)**2 + (paddle.y - self.y)**2
        centerDistance = math.ceil(math.sqrt(centerDistance))

        if centerDistance <= self.radius + paddle.radius:
            return True

        return False

    def reset(self):
        self.velocity[0] = 5 * self.serveDirection
        self.velocity[1] = 5 * self.serveDirection
        self.x = self.init_x
        self.y = self.init_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
