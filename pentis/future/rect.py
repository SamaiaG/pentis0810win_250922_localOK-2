import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rectangle Drawing")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up rectangle parameters
rect_width = 200
rect_height = 100
rect_x = (width - rect_width) // 2
rect_y = (height - rect_height) // 2

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
