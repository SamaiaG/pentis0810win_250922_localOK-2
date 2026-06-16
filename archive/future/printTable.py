import pygame

import os 
from pathlib import Path


os.chdir(Path(__file__).parent)

pygame.font.init()
screen_width = 320
screen_height = 240
screen = pygame.display.set_mode((screen_width, screen_height))
# Define the colors to use for the table
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the font to use for the table
FONT = pygame.font.SysFont("Arial", 20)

# Define the list of data to display in the table
data = [    ["Name", "Score"],
    ["Player 1", "100"],
    ["Player 2", "90"],
    ["Player 3", "80"]
]

# Define the dimensions and position of the table
table_x = 50
table_y = 50
global cell_rect
cell_width = 150
cell_height = 30
padding = 5

# Set up the loop variables
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Draw the table onto the screen surface
                for i, row in enumerate(data):
                    for j, cell in enumerate(row):
                        cell_text = FONT.render(cell, True, BLACK)
                        cell_rect = cell_text.get_rect()
                        cell_rect.x = table_x + (cell_width + padding) * j
                        cell_rect.y = table_y + (cell_height + padding) * i
                        pygame.draw.rect(screen, WHITE, (cell_rect.x, cell_rect.y, cell_width, cell_height))
                        screen.blit(cell_text, cell_rect)


    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, WHITE, (cell_rect.x, cell_rect.y, cell_width, cell_height))
    screen.blit(cell_text, cell_rect)
    pygame.display.update()
    
    # Limit the frame rate
    clock.tick(30)