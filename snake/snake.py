import pygame, random

SQUARE_SIZE = 10
WIDTH = 50
HEIGHT = 50
FPS = 30

class Item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

pygame.init()
screen = pygame.display.set_mode((WIDTH * SQUARE_SIZE, HEIGHT * SQUARE_SIZE), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

item = Item()
item.rect.center = (WIDTH // 2, HEIGHT // 2)
all_sprites.add(item)

gameOn = True

while gameOn:
    clock.tick(FPS)
    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    # Обновление
    all_sprites.update()
    # Рендеринг
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
# домашка
# 1. Отрисовать квадрат по центру окна
# 2. Найти картинки для еды