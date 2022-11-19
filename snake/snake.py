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
        self.rect.topleft = (x * SQUARE_SIZE, y * SQUARE_SIZE)
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
        old_d = self.direction
        k = pygame.key.get_pressed()
        if k[pygame.K_UP] and old_d != 'D':
            self.direction = 'U'
        elif k[pygame.K_RIGHT] and old_d != 'L':
            self.direction = 'R'
        elif k[pygame.K_DOWN] and old_d != 'U':
            self.direction = 'D'
        elif k[pygame.K_LEFT] and old_d != 'R':
            self.direction = 'L'
        d = self.dirs[self.direction]
        head = self.items[0]
        newHead = Item(head.x + d[0], head.y + d[1])
        self.items.insert(0, newHead)
        collide = pygame.sprite.spritecollide(newHead, foods, False)
        if collide:
            for food in collide:
                eat(food)
        else:
            tail = self.items.pop()
            tail.kill()

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randrange(0, WIDTH) * SQUARE_SIZE, random.randrange(0, HEIGHT) * SQUARE_SIZE)
        all_sprites.add(self)
        foods.add(self)

def eat(food):
    food.kill()
    Food()

pygame.init()
screen = pygame.display.set_mode((WIDTH * SQUARE_SIZE, HEIGHT * SQUARE_SIZE), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
foods = pygame.sprite.Group()

snake = Snake(5)
food = Food()
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
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
# домашка
# сделать так, чтобы еда появлялась