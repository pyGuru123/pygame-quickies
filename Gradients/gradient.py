import pygame

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def gradientRect( window, left_colour, right_colour, target_rect ):
	""" Draw a horizontal-gradient filled rectangle covering <target_rect> """
	colour_rect = pygame.Surface((2, 2))                                   # tiny! 2x2 bitmap
	pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))            # left colour line
	pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))            # right colour line
	colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
	window.blit(colour_rect, target_rect)

# GAME ************************************************************************

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False

	gradientRect(win, (18,18, 18), (6, 6, 6), pygame.Rect(0, 0, WIDTH, HEIGHT))
	gradientRect(win, RED, (100, 0, 0), pygame.Rect(30, 50, 100, 50))
	gradientRect(win, GREEN, (0, 100, 0), pygame.Rect(150, 50, 100, 50))
	gradientRect(win, BLUE, (0, 0, 100), pygame.Rect(30, 130, 100, 50))
	gradientRect(win, (255, 255, 0), (0, 0, 255), pygame.Rect(150, 130, 100, 50))
	gradientRect(win, (0, 249, 182), (252, 91, 122), pygame.Rect(30, 210, 220, 50))
	gradientRect(win, (173, 6, 200), (255, 30, 0), pygame.Rect(30, 280, 220, 50))
	gradientRect(win, (184, 15, 10), (19, 135, 8), pygame.Rect(30, 350, 220, 50))
	gradientRect(win, WHITE, BLACK, pygame.Rect(30, 420, 220, 50))

	pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 2)

	clock.tick(FPS)
	pygame.display.update()

pygame.quit()