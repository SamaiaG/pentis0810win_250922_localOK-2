import pygame

# Initialize Pygame
pygame.init()

# Define custom repeat settings for specific keys
key_repeat_settings = {
    pygame.K_a: (200, 50),  # Key A repeat delay of 200ms and interval of 50ms
    pygame.K_b: (300, 100),  # Key B repeat delay of 300ms and interval of 100ms
}

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key press events
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key in key_repeat_settings:
                repeat_delay, repeat_interval = key_repeat_settings[key]
                pygame.key.set_repeat(repeat_delay, repeat_interval)

            # Handle key A press
            if key == pygame.K_a:
                print("Key A is pressed")
                # Perform actions specific to key A

            # Handle key B press
            elif key == pygame.K_b:
                print("Key B is pressed")
                # Perform actions specific to key B

# Quit Pygame
pygame.quit()
