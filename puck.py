import pygame
import math


class Puck():
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.angle = 0
        self.init_x = x
        self.init_y = y

    def move(self, time_delta, friction=1):
        self.x += math.sin(self.angle) * self.speed * time_delta
        self.y -= math.cos(self.angle) * self.speed * time_delta

        self.speed *= friction

    def checkBoundary(self, width, height):
        # right side
        if self.x + self.radius > width:
            self.x = 2 * (width - self.radius) - self.x
            self.angle = -self.angle

        # left side
        elif self.x - self.radius < 0:
            self.x = 2 * self.radius - self.x
            self.angle = -self.angle

        # bottom
        if self.y + self.radius > height:
            self.y = 2 * (height - self.radius) - self.y
            self.angle = math.pi - self.angle

        # top
        elif self.y - self.radius < 0:
            self.y = 2 * self.radius - self.y
            self.angle = math.pi - self.angle


    def collidesWithPaddle(self, paddle):
        """
        Checks collision between circles using the distance formula:
        distance = sqrt(dx**2 + dy**2)
        """

        dx = self.x - paddle.x
        dy = self.y - paddle.y

        # distance between the centers of the circle
        distance = math.hypot(dx, dy)

        # no collison takes place.
        if distance > self.radius + paddle.radius:
            return False

        # calculates angle of projection.
        tangent = math.atan2(dy, dx)
        self.angle = 2 * tangent - self.angle

        temp_angle = math.pi / 2 + tangent

        # experimental value to prevent the puck from sticking.
        offset = 10

        self.x += math.sin(temp_angle) * offset
        self.y -= math.cos(temp_angle) * offset

        return True

    def reset(self, speed):
        self.angle = 0
        self.speed = speed
        self.x = self.init_x
        self.y = self.init_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
