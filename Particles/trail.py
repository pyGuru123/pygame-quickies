import pygame
import random

class Trail(pygame.sprite.Sprite):
	def __init__(self, player, color, win):
		super(Trail, self).__init__()
		self.p = player
		self.color = color
		self.win = win

		self.x, self.y = self.p.rect.center
		self.y += 10
		self.dx = random.randint(0,20) / 10 - 1
		self.dy = -2
		self.size = random.randint(4,7)

		self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), self.size)

	def update(self):
		self.x -= self.dx
		self.y -= self.dy
		self.size -= 0.1

		if self.size <= 0:
			self.kill()

		self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), self.size)