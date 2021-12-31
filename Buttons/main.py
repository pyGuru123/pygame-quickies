import pygame

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

class Button(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Button, self).__init__()

		self.image = img
		self.scale = scale
		self.image = pygame.transform.scale(self.image, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = pygame.transform.scale(img, self.scale)

	def draw(self, win):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		win.blit(self.image, self.rect)
		return action

home = pygame.image.load('homeBtn.png')
replay = pygame.image.load('replay.png')
on = pygame.image.load('soundOnBtn.png')
off = pygame.image.load('soundOffBtn.png')

home_btn = Button(home, (24, 24), WIDTH//2-100, HEIGHT//2)
replay_btn = Button(replay, (36, 36), WIDTH//2, HEIGHT//2 - 10)
sound_btn = Button(off, (24, 24), WIDTH//2 + 100, HEIGHT//2)

# button = Button(off, (100, 70), WIDTH//2-100, HEIGHT//2)
sound_on = False

running = True
while running:
	win.fill((32, 32, 32))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q or \
				event.key == pygame.K_ESCAPE:
				running = False

	if home_btn.draw(win):
		print('yes')

	if replay_btn.draw(win):
		running = False

	if sound_btn.draw(win):
		sound_on = not sound_on
		
		if sound_on:
			sound_btn.update_image(on)
		else:
			sound_btn.update_image(off)
	pygame.display.update()

pygame.quit()