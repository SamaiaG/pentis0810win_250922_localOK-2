import pygame
import random
import os
from pathlib import Path


os.chdir(Path(__file__).parent)

class PixelStone:
    def __init__(self, width=532, height=532):
        self.width = width
        self.height = height
        self.image = self.create_stone()

    def create_stone(self):
        # Create a surface for the stone
        stone_surface = pygame.Surface((self.width, self.height))
        stone_surface.fill((0, 0, 0))  # Black background for transparency

        # Define stone color and shape
        stone_color = (100, 100, 100)  # A simple gray color
        stone_color2 = (133, 133, 22)
        stone_color3 = (155, 155, 155)
        for x in range(self.width):
            for y in range(self.height):

                if random.random() >= 0.2:  # Random pattern with 0.2 => 80% coverage
                    stone_surface.set_at((x, y), stone_color)
                elif random.random() >= 0.5:
                    stone_surface.set_at((x, y), stone_color2)
                elif random.random() >= 0.75:
                    stone_surface.set_at((x, y), stone_color3)                
       
        return stone_surface

    def draw(self, surface, x, y):
        # Draw the stone on the given surface at (x, y)
        surface.blit(self.image, (x, y))

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pixel Stone')
clock = pygame.time.Clock()

# Create a PixelStone instance
stone = PixelStone()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    stone.draw(screen, 50, 50)  # Draw the stone at position (50, 50)
    # Export the stone_surface as a JPG image
    pygame.image.save(stone.image, "stone_surface_1x1.jpg")    
   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()