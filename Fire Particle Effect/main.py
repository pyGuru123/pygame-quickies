import pygame
import random

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
win = pygame.display.set_mode(SCREEN)

clock = pygame.time.Clock()
FPS = 60

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super(Fire, self).__init__()
        self.x = x
        self.y = y
        self.radius = radius
        
        self.yvel = random.randint(1, 9)
        self.burn_rate = 0.1
        
        self.layers = 2
        self.glow = 2
        
        surf_size = 2 * self.radius * self.layers * self.layers * self.glow
        self.surf = pygame.Surface((surf_size, surf_size), pygame.SRCALPHA)
        
    def update(self, win):
        xvel = random.randint(-int(self.radius), int(self.radius))
        self.x += xvel
        self.y -= self.yvel
        
        self.radius -= self.burn_rate
        if self.radius <= 0:
            self.radius = 0.01
        
        surf_size = 2 * self.radius * self.layers * self.layers * self.glow
        self.surf = pygame.Surface((surf_size, surf_size), pygame.SRCALPHA)
        
        for i in range(self.layers, -1, -1):
            alpha = 255 - i * (255 // self.layers - 5)
            if alpha <= 0:
                alpha = 0
            radius = int(self.radius * self.glow * i * i)
             
            if self.radius >3.5:
                color = 255, 0, 0
            elif self.radius > 2.5:
                color = 255, 150, 0
            else:
                color = 50, 50, 50
            color = (*color, alpha)
        
            pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), radius)
        win.blit(self.surf, self.surf.get_rect(center=(self.x, self.y)))
        
fire_group = pygame.sprite.Group()
pygame.mouse.set_pos((WIDTH//2, HEIGHT//2))
torch = pygame.image.load('torch.png')
torch = pygame.transform.scale(torch, (60, 125))

show_torch = True

running = True
while running:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
            
    pos = pygame.mouse.get_pos()
    for i in range(2):
        x, y = pos
        r = random.randint(2, 5)
        f = Fire(x, y, r)
        fire_group.add(f)

    if show_torch:
        win.blit(torch, (x - 30, y))
    
    fire_group.update(win)
    for fire in fire_group:
        if fire.radius <= 0:
            fire.kill()
    
    clock.tick(FPS)
    pygame.display.update()
            
pygame.quit()