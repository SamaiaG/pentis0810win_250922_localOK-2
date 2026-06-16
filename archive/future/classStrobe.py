import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a custom class for the stroboscope effect
class Stroboscope:
    def __init__(self, frequency):
        self.frequency = frequency
        self.counter = 0
        
    def update(self, dt):
        self.counter += dt
        if self.counter > 1/self.frequency:
            self.counter -= 1/self.frequency
            return True
        else:
            return False

# Create a surface to draw on
test_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# Add a test object to the surface
test_circle = pygame.draw.rect(test_surface, RED, (300, 400), 50)
pygame.draw.rect()

# Create a stroboscope effect for the object
stroboscope = Stroboscope(5)

# Start the game loop
done = False
clock = pygame.time.Clock()

while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Update the stroboscope effect
    if stroboscope.update(clock.tick()/1000):
        # Draw the object if the stroboscope is on
        screen.blit(test_surface, (0, 0))
    
    # Update the display
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
