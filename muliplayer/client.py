import requests
import pygame, json

class User(pygame.sprite.Sprite):
    def __init__(self, name, color, x, y, score):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.score = score
        self.image = pygame.surface.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill(COLORS[color])
        self.rect = self.image.get_rect()
        self.rect.x = self.x * SQUARE_SIZE
        self.rect.y = self.y * SQUARE_SIZE
    def update(self):
        self.rect.x = self.x * SQUARE_SIZE
        self.rect.y = self.y * SQUARE_SIZE

FPS = 10
SIZE = 20
SQUARE_SIZE = 20
COLORS = [
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]

username = input('Имя пользователя: ')
res = requests.get('http://127.0.0.1:5000/register?name=' + username)

if not res:
    print('Сервер недоступен')
    exit(0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * SQUARE_SIZE, SIZE * SQUARE_SIZE), 0, 32)
pygame.display.set_caption('Сеть')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
users = {}

user_d = json.loads(res.text)
print(user_d)
user = User(
    user_d['name'], 
    user_d['color'],
    user_d['x'],
    user_d['y'],
    user_d['score']
    )
all_sprites.add(user)
users[username] = user

gameOn = True
while gameOn:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        elif event.type == pygame.KEYDOWN:
            direction = False
            if event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            if direction:
                params = {
                    'username': username,
                    'direction': direction
                }
                requests.get('http://127.0.0.1:5000/move', params=params)
    # обновление
    status = json.loads(requests.get('http://127.0.0.1:5000/status').text)
    for name in status:
        d = json.loads(status[name])
        if not name in users:
            newUser = User(d['name'], d['color'], d['x'], d['y'], d['score'])
            users[name] = newUser
            all_sprites.add(newUser)
        else:
            users[name].x = d['x']
            users[name].y = d['y']
            users[name].score = d['score']
    all_sprites.update()
    # рендеринг
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()