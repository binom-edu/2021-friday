# Space Shooter (Redux, plus fonts and sounds) by Kenney Vleugels (www.kenney.nl)

import pygame, os, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
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
            bullets.add(bullet)
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
        self.image_orig = random.choice(meteor_imgs)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.65 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, 100)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randint(-3, 3)
        self.rot = 0
        self.rot_speed = random.randint(-10, 10)
        self.last_update = pygame.time.get_ticks()
        all_sprites.add(self)
        mobs.add(self)

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 20 or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, 100)
            self.speedy = random.randrange(1, 10)
            self.speedx = random.randint(-3, 3)
    
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

class Explosion(pygame.sprite.Sprite):
    def __init__(self, coord, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[size][0]
        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                self.image = explosion_anim[self.size][self.frame]

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text('Используйте стрелки для перемещения, пробел для стрельбы', screen, WIDTH / 2, HEIGHT / 2, 12)
    draw_text('Для начала нажмите любую клавишу', screen, WIDTH / 2, HEIGHT * 3 / 5, 18)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYUP:
                waiting = False

def draw_text(text, surf, x, y, size):
    font = pygame.font.Font(font_name, size)
    font_surf = font.render(text, True, (255, 255, 255))
    text_rect = font_surf.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(font_surf, text_rect)

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
background = pygame.image.load(os.path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
meteor_imgs = []
meteors_list = os.listdir(os.path.join(img_dir, 'Meteors'))
for img in meteors_list:
    meteor_imgs.append(pygame.image.load(os.path.join(img_dir, 'Meteors', img)).convert_alpha())
explosion_anim = {'sm': [], 'lg': [], 'player': []}
for i in range(9):
    filename = f'regularExplosion0{i}.png'
    img = pygame.image.load(os.path.join(img_dir, 'explosions', filename)).convert_alpha()
    img_lg = pygame.transform.scale(img, (75, 75))
    img_sm = pygame.transform.scale(img, (30, 30))
    explosion_anim['lg'].append(img_lg)
    explosion_anim['sm'].append(img_sm)
    filename = f'sonicExplosion0{i}.png'
    img = pygame.image.load(os.path.join(img_dir, 'player_expl', filename)).convert_alpha()
    explosion_anim['player'].append(img)

bullet_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'sfx_laser2.ogg'))
expl_snd = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_snd.append(pygame.mixer.Sound(os.path.join(snd_dir, snd)))
pygame.mixer.music.load(os.path.join(snd_dir, 'bgmusic.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

font_name = pygame.font.match_font('arial')

game_on = True
game_over = True
while game_on:
    if game_over:
        show_go_screen()
        score = 0
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            m = Mob()

    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    all_sprites.update()

    # встреча пули и метеора
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 40 - hit.radius
        random.choice(expl_snd).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        Mob()
    
    # встреча игрока и метеора
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    if hits:
        game_over = True

    # рендеринг
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(str(score), screen, WIDTH / 2, 10, 18)
    pygame.display.flip()
pygame.quit()