import pygame
import random

class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Explosion, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)
		
		self.color = 150
			
	def update (self):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:
			self.x += self.x_vel
			self.y += self.y_vel
			s = int(self.size)
			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:
			self.kill()