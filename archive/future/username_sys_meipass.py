import pygame
import os
import sys

# Get the path to the directory where the executable is running from
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    base_path = sys._MEIPASS
else:
    # If we are running in a normal Python environment, the
    # current directory is the base path.
    base_path = os.path.abspath(".")

# Define the path to the username text file
username_path = os.path.join(base_path, "username.txt")

class Timer:
    def __init__(self, fps):
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.username = ""

    def run(self):
        running = True
        while running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_RETURN:
                        self.save_username()
            
            # Draw test circle and update screen
            screen.fill((255, 255, 255))
            pygame.draw.circle(screen, (255, 0, 0), (300, 400), 50)
            pygame.display.update()

    def save_username(self):
        self.username = input_box.text
        with open(username_path, "w") as f:
            f.write(self.username)
