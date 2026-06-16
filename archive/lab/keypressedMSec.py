import pygame

# Initialize Pygame
pygame.init()

# Set the key repeat delay and interval
pygame.key.set_repeat(1, 1)

# Store the state of keys for timing
key_state = {}

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key press and release events
        if event.type == pygame.KEYDOWN:
            if event.key not in key_state:
                key_state[event.key] = pygame.time.get_ticks()
                print(f"Key {pygame.key.name(event.key)} pressed.")

        if event.type == pygame.KEYUP:
            if event.key in key_state:
                key_duration = pygame.time.get_ticks() - key_state[event.key]
                del key_state[event.key]
                print(f"Key {pygame.key.name(event.key)} released after {key_duration} ms.")

# Quit Pygame
pygame.quit()
