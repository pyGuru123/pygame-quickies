# AABB Shower.

# Axis aligned bounding box - this means a collision detection between
# 2 rectangles whose axis are aligned. means their is no rotation.

import pygame
import random

pygame.init()
WIDTH, HEIGHT = 288, 512
win = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 30

rect1 = pygame.Rect(10, 250, 100, 20)
w, h = 100, 20

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def aabb(r1, r2, dx, dy):
	if ((r1.x + dx < r2.rect.x + r2.w) and (r1.x + w + dx > r2.rect.x) and
		(r1.y + dy < r2.rect.y + r2.h) and (r1.height + r1.y + dy > r2.rect.y)):
		return True
	return False

clicked = False
collision = False
pos = None
last = None

class Box(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(Box, self).__init__()
		self.w = self.h = 20
		self.rect = pygame.Rect(x, y, 20, 20)
		self.color = random.choice([RED, GREEN, BLUE])

	def update(self, dx=0, dy=0):
		self.rect.x += dx
		self.rect.y += dy
		if self.rect.y >= HEIGHT:
			self.kill()

		pygame.draw.rect(win, self.color, self.rect)

box_group = pygame.sprite.Group()
counter = 0
relx = rely = 0
dx, dy = 0, 5

running = True
while running:
	win.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos
			if rect1.collidepoint(pos):
				clicked = True
				last = pos

		if event.type == pygame.MOUSEMOTION:
			if clicked and not collision:
				new_pos = event.pos
				relx = new_pos[0] - last[0]
				rely = new_pos[1] - last[1]
				rect1.x += relx
				rect1.y += rely
				last = new_pos

				# rect1.x += event.rel[0]
				# rect1.y += event.rel[1]

		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
			last = None

	counter += 1
	if counter % 15 == 0:
		box = Box(random.randint(0, WIDTH-20), -20)
		box_group.add(box)

	for box in box_group:
		if aabb(rect1, box, relx, rely):
			dx, dy = -relx, -rely
		else:
			dx, dy = 0, 5

	box_group.update(dx, dy)
	pygame.draw.rect(win, WHITE, rect1)

	clock.tick(FPS)
	pygame.display.update()
pygame.quit()