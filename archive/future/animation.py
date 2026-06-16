import pygame
import os 
from pathlib import Path

os.chdir(Path(__file__).parent)

pygame.init()

width = 640
height = 480

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Animation")

sprite_1 = pygame.image.load("block01.png")
sprite_2 = pygame.image.load("block02.png")
sprite_3 = pygame.image.load("block03.png")

sprites = [sprite_1, sprite_2, sprite_3]

x = 100
y = 100

sprite_index = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(sprites[sprite_index], (x, y))

    sprite_index += 1

    if sprite_index >= len(sprites):
        sprite_index = 0

    pygame.time.delay(100)

    pygame.display.update()

pygame.quit()
