# Звуки: https://opengameart.org/node/132358
# Спрайты и звуки: https://opengameart.org/content/snake-sprites-sound
# Фоновая музыка: https://opengameart.org/content/bossa-nova

import pygame, random
from os import path

SQUARE_SIZE = 10
WIDTH = 50
HEIGHT = 50
SNAKE_SIZE = 3
FPS = 10
SCORE_FIELD_HEIGTH = 2
font_name = pygame.font.match_font('arial')

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
        self.score = 0
    
    def update(self):
        global gameover
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
        # проверяем еду
        collide = pygame.sprite.spritecollide(newHead, foods, False)
        if collide:
            for food in collide:
                eat(food)
        else:
            tail = self.items.pop()
            tail.kill()
        # проверяем, не столкнулась ли голова с хвостом
        collide = pygame.sprite.spritecollide(newHead, snake_items, False)
        if collide:
            gameover = True
        # проверяем выход за границы поля
        if newHead.x < 0 or newHead.x == WIDTH or\
           newHead.y < 0 or newHead.y == HEIGHT:
            gameover = True
        snake_items.add(newHead)
        self.score += 1

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
    eat_sound.play()

def showGoScreen(gameover=False):
    screen.fill((30, 30, 30))
    if gameover:
        draw_text(screen, 'Игра окончена', 32, WIDTH // 2 * SQUARE_SIZE, 20 * SQUARE_SIZE)
    draw_text(screen, 'Нажмите ENTER, чтобы начать игру', 24, WIDTH // 2 * SQUARE_SIZE, HEIGHT // 2 * SQUARE_SIZE)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            waiting = False


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_score(surf, score):
    outline_rect = pygame.Rect(5, 5, (WIDTH - 1) * SQUARE_SIZE, SCORE_FIELD_HEIGTH * SQUARE_SIZE - 5)
    pygame.draw.rect(surf, (200, 200, 200), outline_rect, 2)
    draw_text(surf, f'Score: {score}', 10, 50, 5)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH * SQUARE_SIZE, HEIGHT * SQUARE_SIZE + SCORE_FIELD_HEIGTH * SQUARE_SIZE), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
sound_dir = path.join(path.dirname(__file__), 'sounds')
eat_sound = pygame.mixer.Sound(path.join(sound_dir, 'apple_bite.ogg'))
go_sound = pygame.mixer.Sound(path.join(sound_dir, 'die.ogg'))
pygame.mixer.music.load(path.join(sound_dir, 'bgm.mp3'))
pygame.mixer.music.set_volume(0.4)


all_sprites = pygame.sprite.Group()
foods = pygame.sprite.Group()
snake_items = pygame.sprite.Group()

snake = Snake(5)
food = Food()
gameOn = True
gameover = False

showGoScreen()
pygame.mixer.music.play(-1)

while gameOn:
    if gameover:
        go_sound.play()
        pygame.mixer.music.stop()
        showGoScreen(gameover)
        pygame.mixer.music.play(-1)
        gameover = False
        all_sprites = pygame.sprite.Group()
        foods = pygame.sprite.Group()
        snake_items = pygame.sprite.Group()
        snake = Snake(5)
        food = Food()
    
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
    draw_score(screen, snake.score)
    pygame.display.flip()

pygame.quit()