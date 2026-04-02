import pygame as pg

# Initialize Pygame
pg.init()

# Set up window and font
window = pg.display.set_mode((400, 300))
font = pg.font.SysFont("Consolas", 40)

# Define menu options
options = ["Start Game", "Options", "Quit"]

# Set up menu variables
selected_option = 0
option_spacing = 50

# Main loop
while True:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                selected_option = (selected_option - 1) % len(options)
            elif event.key == pg.K_DOWN:
                selected_option = (selected_option + 1) % len(options)
            elif event.key == pg.K_RETURN:
                if selected_option == 0:
                    # Start game action
                    pass
                elif selected_option == 1:
                    # Options action
                    pass
                elif selected_option == 2:
                    # Quit action
                    pg.quit()
                    quit()

    # Clear screen
    window.fill((255, 255, 255))

    # Display menu options
    for i in range(len(options)):
        if i == selected_option:
            # Highlight selected option
            text = font.render(options[i], True, (255, 0, 0))
        else:
            text = font.render(options[i], True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (200, 100 + i * option_spacing)
        window.blit(text, text_rect)

    # Update screen
    pg.display.update()