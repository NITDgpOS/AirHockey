import math
import pygame
import constants as const
import random as rand

from globals import *

class Powerup1():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.Active = True
        

    def checkTopBottomBounds(self, height):
        # top
        if self.y - self.height <= 0:
            self.y = self.height
        # bottom
        elif self.y + self.height > height:
            self.y = height - self.height

    
    def draw(self, screen):
        pygame.draw.rect(screen, (147,47,4), (self.x,self.y,10,50),2)
        
    def get_pos(self):
        return self.x,self.y

    def set_pos(self,a):
        self.x=a[0]
        self.y=a[1]

    def isActive(self):
        return self.Active
    
    def kill(self):
        self.Active=False

    def collidewithPaddle(self,paddle):
        dx = self.x - paddle.x
        dy = self.y - paddle.y

        # distance between the centers of the circle
        distance = math.hypot(dx, dy)

        # no collison takes place.
        if distance > paddle.radius:
            return False

        return True
 