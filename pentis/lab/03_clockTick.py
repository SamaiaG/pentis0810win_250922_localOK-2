

import pygame
import sys

pygame.init()
Myscreen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    print(clock)
    clock.tick(1) # <Clock(fps=1.00)> - 60 => 60 fps 
