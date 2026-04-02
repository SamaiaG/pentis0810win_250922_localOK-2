import pygame

class Timer:
    def __init__(self, delay):
        self.delay = delay
        self.last_trigger = 0

    def check(self):
        if pygame.time.get_ticks() - self.last_trigger > self.delay:
            self.last_trigger = pygame.time.get_ticks()
            return True
        else:
            return False

# Set up Pygame
pygame.init()

# Create a test surface
test_surface = pygame.display.set_mode((600, 800))

# Create a test circle object
test_circle = pygame.Surface((50, 50))
pygame.draw.circle(test_circle, (255, 0, 0), (25, 25), 25)

# Create a Timer object with a delay of 500 milliseconds
timer = Timer(500)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the Timer has triggered
    if timer.check():
        # Toggle the visibility of the test circle object
        if test_circle.get_alpha() == 255:
            test_circle.set_alpha(0)
        else:
            test_circle.set_alpha(255)

    # Draw the test circle object to the test surface
    test_surface.blit(test_circle, (275, 375))

    # Update the display
    pygame.display.update()

# Clean up Pygame
pygame.quit()
