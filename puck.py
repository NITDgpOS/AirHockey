import pygame
import math
import constants as const
class Puck():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = const.PUCKSIZE
        self.speed = const.PUCKSPEED
        self.mass = const.PUCKMASS
        self.angle = 0

    def move(self, time_delta):
        self.x += math.sin(self.angle) * self.speed * time_delta
        self.y -= math.cos(self.angle) * self.speed * time_delta

        self.speed *= const.FRICTION

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

    def addVectors(self, (angle1, length1), (angle2, length2)):
        x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
        y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

        length = math.hypot(x, y)
        angle = math.pi / 2 - math.atan2(y, x)
        return (angle, length)

    def collidesWithPaddle(self, paddle):
        """
        Checks collision between circles using the distance formula:
        distance = sqrt(dx**2 + dy**2)
        """
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        dx = self.x - paddle.x
        dy = self.y - paddle.y

        # distance between the centers of the circle
        distance = math.hypot(dx, dy)

        # no collison takes place.
        if distance > self.radius + paddle.radius:
            return False

        # calculates angle of projection.
        tangent = math.atan2(dy, dx)
        temp_angle = math.pi / 2 + tangent
        total_mass = self.mass + paddle.mass

        # The new vector for puck formed after collision.
        vecA = (self.angle, self.speed * (self.mass - paddle.mass) / total_mass)
        vecB = (temp_angle, 2 * paddle.speed * paddle.mass / total_mass)

        (self.angle, self.speed) = self.addVectors(vecA, vecB)

        # speed should never exceed a certain limit.
        if self.speed > const.MAXSPEED:
            self.speed = const.MAXSPEED

        # new vector for paddle without changing the speed.
        vecA = (paddle.angle, paddle.speed * (paddle.mass - self.mass) / total_mass)
        vecB = (temp_angle + math.pi, 2 * self.speed * self.mass / total_mass)

        temp_speed = paddle.speed
        (paddle.angle, paddle.speed) = self.addVectors(vecA, vecB)
        paddle.speed = temp_speed

        # To prevent puck and paddle from sticking.
        offset = 0.5 * (self.radius + paddle.radius - distance + 1)
        self.x += math.sin(temp_angle) * offset
        self.y -= math.cos(temp_angle) * offset
        paddle.x -= math.sin(temp_angle) * offset
        paddle.y += math.cos(temp_angle) * offset
        return True

    def reset(self, speed):
        self.angle = 0
        self.speed = speed
        self.x = const.WIDTH / 2
        self.y = const.HEIGHT / 2

    def draw(self, screen):
        pygame.draw.circle(screen, const.WHITE, (int(self.x), int(self.y)), self.radius)
