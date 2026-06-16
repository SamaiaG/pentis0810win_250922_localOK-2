import pygame

# Initialize Pygame
pygame.init()

# Set up window
window_size = (640, 480)
window = pygame.display.set_mode(window_size)

# Set up variables
score = 0
level = 1

# Main loop
while True and score < 4000:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update score
    score += 7  # replace with your score update code

    # Check if level should be increased
    if score % 500 == 0:
        level += 1
        print(score, level)
        print("Level up!")

    # Update screen
    pygame.display.update()
