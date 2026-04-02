import pygame

# Initialize Pygame
pygame.init()

# Set up window
window_size = (640, 480)
window = pygame.display.set_mode(window_size)

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get state of all keys
    keys = pygame.key.get_pressed()

    # Check if two keys are pressed simultaneously
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        print("Up and right keys pressed simultaneously")

    # Update screen
    pygame.display.update()
