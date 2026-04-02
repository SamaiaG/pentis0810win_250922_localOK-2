import pygame

# Initialize Pygame
pygame.init()

# Set up window
window_size = (640, 480)
window = pygame.display.set_mode(window_size)

# Import font file
font_path = "myfont.ttf"  # replace with your font file path
font_size = 24
my_font = pygame.font.Font(font_path, font_size)

# Render text
text = my_font.render("Hello, world!", True, (255, 255, 255))

# Display text on screen
text_rect = text.get_rect()
text_rect.center = (window_size[0] // 2, window_size[1] // 2)
window.blit(text, text_rect)

# Update screen
pygame.display.update()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()