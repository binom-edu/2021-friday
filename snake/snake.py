import pygame, random

SQUARE_SIZE = 10
WIDTH = 50
HEIGHT = 50
SNAKE_SIZE = 3
FPS = 10

class Item(pygame.sprite.Sprite):
    def __init__(self, x = WIDTH // 2, y = HEIGHT // 2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill((255, 255, 255))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x * SQUARE_SIZE, y * SQUARE_SIZE)
        all_sprites.add(self)

class Snake():
    def __init__(self, size = SNAKE_SIZE, x = WIDTH // 2, y = HEIGHT // 2):
        self.items = []
        for i in range(size):
            item = Item(x - i, y)
            self.items.append(item)
        self.direction = 'R'
        self.dirs = {
            'U': [0, -1],
            'R': [1, 0],
            'D': [0, 1],
            'L': [-1, 0]
        }
    
    def update(self):
        d = self.dirs[self.direction]
        head = self.items[0]
        newHead = Item(head.x + d[0], head.y + d[1])
        self.items.insert(0, newHead)


pygame.init()
screen = pygame.display.set_mode((WIDTH * SQUARE_SIZE, HEIGHT * SQUARE_SIZE), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

snake = Snake(5)

gameOn = True

while gameOn:
    clock.tick(FPS)
    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    # Обновление
    all_sprites.update()
    snake.update()
    # Рендеринг
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
# домашка
# попробовать разные направления движения