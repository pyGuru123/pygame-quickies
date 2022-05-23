# AABB collision detection.

# Axis aligned bounding box - this means a collision detection between
# 2 rectangles whose axis are aligned. means their is no rotation.

import pygame

pygame.init()
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))

rect1 = pygame.Rect(10, 10, 100, 100)
rect2 = pygame.Rect(WIDTH//2-50, HEIGHT//2-50, 100, 100)
w, h = 100, 100

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

clicked = False
collision = False
pos = None
last = None

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

	if (rect1.x < rect2.x + w and rect1.x + w > rect2.x and
		rect1.y < rect2.y + h and rect1.height + rect1.y > rect2.y):
		collision = True
	else:
		collision = False

	pygame.draw.rect(win, GREEN, rect1)
	pygame.draw.rect(win, WHITE, rect2)

	pygame.display.update()
pygame.quit()