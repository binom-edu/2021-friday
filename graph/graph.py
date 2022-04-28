import pygame

WIDTH = 480
HEIGTH = 360
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH), 0, 32)
pygame.display.set_caption("Hello world")
clock = pygame.time.Clock()

gameOn = True
while gameOn:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    # обновление
    # рендеринг
    pygame.display.flip()

pygame.quit()