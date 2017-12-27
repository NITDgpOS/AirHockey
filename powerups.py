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
        
        """
        dx = self.x - paddle.x
        dy = self.y - paddle.y

        # distance between powerup and paddle
        distance = math.hypot(dx, dy)

        # no collison takes place.
        if distance > paddle.radius :
            return False

        return True
        """
        return self.collision(self.x,self.y,10,50,paddle.x,paddle.y,paddle.radius)

    def collision(self,rleft, rtop, width, height,   # rectangle definition
              center_x, center_y, radius):  # circle definition
        """ Detect collision between a rectangle and circle. """

        # complete boundbox of the rectangle
        rright, rbottom = rleft + width/2, rtop + height/2

        # bounding box of the circle
        cleft, ctop     = center_x-radius, center_y-radius
        cright, cbottom = center_x+radius, center_y+radius

        # trivial reject if bounding boxes do not intersect
        if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
            return False  # no collision possible

        # check whether any point of rectangle is inside circle's radius
        for x in (rleft, rleft+width):
            for y in (rtop, rtop+height):
                # compare distance between circle's center point and each point of
                # the rectangle with the circle's radius
                if math.hypot(x-center_x, y-center_y) <= radius:
                    return True  # collision detected

        # check if center of circle is inside rectangle
        if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
            return True  # overlaid

        return False  # no collision detected