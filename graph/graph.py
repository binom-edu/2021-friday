# starship sprite: https://www.freepng.ru/png-h8gseh/download.html

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.surface.Surface((50, 50))
        # self.image.fill((0, 255, 0))
        self.image_big = pygame.image.load('1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_big, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGTH / 2)
        self.direction = {'x': 5, 'y': 1}
    
    def update(self):
        self.rect.x += self.direction['x']
        self.rect.y += self.direction['y']
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.direction['x'] *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGTH:
            self.direction['y'] *= -1

WIDTH = 480
HEIGTH = 360
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH), 0, 32)
pygame.display.set_caption("Hello world")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

gameOn = True
while gameOn:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.direction['x'] = 0
                player.direction['y'] = -5
            elif event.key == pygame.K_DOWN:
                player.direction['x'] = 0
                player.direction['y'] = 5
            elif event.key == pygame.K_LEFT:
                player.direction['x'] = -5
                player.direction['y'] = 0
            elif event.key == pygame.K_RIGHT:
                player.direction['x'] = 5
                player.direction['y'] = 0
    # обновление
    all_sprites.update()
    # рендеринг
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()