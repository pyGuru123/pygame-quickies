import pygame
import random

class Square(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(Square, self).__init__()

		self.win = win
		self.color = (128, 128, 128)
		self.speed = 3
		self.angle = 0

		self.side = random.randint(15, 40)

		self.surface = pygame.Surface((self.side, self.side), pygame.SRCALPHA)
		self.surface.set_colorkey((200,200,200))
		self.rect = self.surface.get_rect(center=(x, y))

	def update(self, win):
		center = self.rect.center
		self.angle = (self.angle + self.speed) % 360
		image = pygame.transform.rotate(self.surface , self.angle)
		self.rect = image.get_rect()
		self.rect.center = center

		self.rect.y += 1.5

		if self.rect.top >= HEIGHT:
			self.kill()

		pygame.draw.rect(self.surface, self.color, (0,0, self.side, self.side), 4)
		win.blit(image, self.rect)

if __name__ == '__main__':
	pygame.init()
	SCREEN = WIDTH, HEIGHT = 288, 512
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

	clock = pygame.time.Clock()
	FPS = 60
	count = 0

	square_group = pygame.sprite.Group()

	running = True
	while running:
		win.fill((200,200,200))

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		count += 1
		if count % 100 == 0:
			x = random.randint(40, WIDTH-40)
			y = 0
			square = Square(x, y)
			square_group.add(square)
			count = 0

		square_group.update(win)

		pygame.draw.rect(win, (30,30,30), (0, 0, WIDTH, HEIGHT), 8)
		clock.tick(FPS)
		pygame.display.update()
pygame.quit()