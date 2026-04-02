import pygame

# Initialize Pygame
pygame.init()

# Set the initial key repeat settings
key_repeat_settings = {
    pygame.K_x: (0, 0),  # Key X with no repeat
    pygame.K_y: (0, 0),  # Key Y with no repeat
    pygame.K_a: (0, 0),  # Key A with no repeat
    pygame.K_RIGHT: (200, 50),  # Key RIGHT with repeat delay of 200ms and interval of 50ms
    pygame.K_LEFT: (200, 50),  # Key LEFT with repeat delay of 200ms and interval of 50ms
    pygame.K_DOWN: (200, 50),  # Key DOWN with repeat delay of 200ms and interval of 50ms
}

# Enable key repeat globally
pygame.key.set_repeat(1, 1)

# Store the state of keys for repeat logic
key_state = {}


print(key_repeat_settings)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key press events
        if event.type == pygame.KEYDOWN:
            key = event.key

            # Switch key repeat settings based on the pressed key
            if key in key_repeat_settings:
                repeat_delay, repeat_interval = key_repeat_settings[key]
                pygame.key.set_repeat(repeat_delay, repeat_interval)
                key_state[key] = pygame.time.get_ticks() + repeat_delay

            # Handle key X press
            if key == pygame.K_x:
                print("Key X is pressed")
                # Perform actions specific to key X

            # Handle key Y press
            elif key == pygame.K_y:
                print("Key Y is pressed")
                # Perform actions specific to key Y

            # Handle key A press
            elif key == pygame.K_a:
                print("Key A is pressed")
                # Perform actions specific to key A

    # Check for key repeat events
    pressed_keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    for key, state in key_state.items():
        if pressed_keys[key]:
            if current_time >= state:
                print(f"Key {pygame.key.name(key)} is repeating")
                # Perform repeat actions for the key
                key_state[key] = current_time + repeat_interval

# Quit Pygame
pygame.quit()
