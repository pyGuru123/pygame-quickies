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

w, h = 150, 20
rect1 = pygame.Rect(10, 250, w, h)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def aabb(r1, r2, dx, dy):
	if ((r1.x + dx < r2.x + r2.w) and (r1.x + w + dx > r2.x) and
		(r1.y + dy < r2.y + r2.h) and (r1.y + h + dy > r2.y)):
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
		self.rect = pygame.Rect(x, y, self.w, self.h)
		self.color = random.choice([RED, GREEN, BLUE])

	def update(self, dx=0, dy=0):
		self.rect.x += dx
		self.rect.y += dy
		if self.rect.y >= HEIGHT:
			self.kill()

		pygame.draw.rect(win, (48, 48, 48), self.rect)
		pygame.draw.rect(win, WHITE, self.rect, 3)
		pygame.draw.rect(win, self.color, self.rect, 1)

def gradientRect( window, left_colour, right_colour, target_rect ):
	colour_rect = pygame.Surface((2, 2))
	pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))
	pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))
	colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))
	window.blit(colour_rect, target_rect)

box_group = pygame.sprite.Group()
counter = 0
relx = rely = 0
dx, dy = 0, 5

running = True
while running:
	win.fill((18, 18, 18))
	gradientRect(win, (18,18, 18), (4, 4, 4), pygame.Rect(0, 0, WIDTH, HEIGHT))
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

		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
			last = None

	counter += 1
	if counter % 5 == 0:
		box = Box(random.randint(0, WIDTH-20), -20)
		box_group.add(box)

	for box in box_group:
		dy = 5
		if aabb(rect1, box.rect, relx, rely):
			if box.rect.y <= rect1.y:
				dy = 0
			if rely:
				dy = rely

		box.update(0, dy)
		
	rely = 0
	gradientRect(win, (173, 6, 200), (255, 30, 0), rect1)
	pygame.draw.rect(win, WHITE, rect1, 2)

	clock.tick(FPS)
	pygame.display.update()
pygame.quit()