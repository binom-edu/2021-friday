# Space Shooter (Redux, plus fonts and sounds) by Kenney Vleugels (www.kenney.nl)

import pygame, os, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20
        self.shoot_delay = 1000
        self.last_shoot = pygame.time.get_ticks()
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullet_snd.play()
            self.last_shoot = now

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(meteor_imgs)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, 100)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randint(-3, 3)
        all_sprites.add(self)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, 100)
            self.speedy = random.randrange(1, 10)

WIDTH = 400
HEIGHT = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Аркадный шутер')
clock = pygame.time.Clock()
img_dir = os.path.join(os.path.dirname(__file__), 'img')
snd_dir = os.path.join(os.path.dirname(__file__), 'snd')
player_img = pygame.image.load(os.path.join(img_dir, 'playerShip.png')).convert_alpha()
bullet_img = pygame.image.load(os.path.join(img_dir, 'laserBlue16.png')).convert_alpha()
meteor_imgs = []
meteors_list = os.listdir(os.path.join(img_dir, 'Meteors'))
for img in meteors_list:
    meteor_imgs.append(pygame.image.load(os.path.join(img_dir, 'Meteors', img)).convert_alpha())
bullet_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'sfx_laser2.ogg'))
pygame.mixer.music.load(os.path.join(snd_dir, 'bgmusic.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()

game_on = True
while game_on:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    all_sprites.update()
    # рендеринг
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()