import pygame
from pygame.locals import *

class Paddle():
	def __init__(self, x, y, width, height, velocity):
		self.x= x
		self.y= y
		self.width= width
		self.height= height
		self.velocity= velocity

	def getPaddle(self):
		return pygame.Rect(self.x,self.y,self.width,self.height)

class Puck():
	def __init__(self, x, y, width, height, velocity):
		self.x= x
		self.y= y
		self.init_x= x
		self.init_y= y
		self.width= width
		self.height= height
		self.velocity= velocity
		self.serveDirection= 1

	def getPuck(self):
		return pygame.Rect(self.x,self.y,self.width,self.height)

	def reset(self):
	    self.velocity[0]=10*self.serveDirection
	    self.velocity[1]=4*self.serveDirection
	    self.x= self.init_x
	    self.y= self.init_y


