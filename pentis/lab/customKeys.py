import pygame as pg

# Define your menu options and initial selected option
options = ["Start Game", "Customize Controls", "Highscore", "Back"]
selected_option = 0

# Define your action keys dictionary with default values
action_keys = {
    "Right": "Right Arrow",
    "Left": "Left Arrow",
    "Down": "Down Arrow",
    "Rotate": "Up Arrow"
}

def menu():
    screen_width = 320
    screen_height = 240

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Main Menu")

    font = pg.font.Font(None, 32)
    option_spacing = 40

    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == pg.K_RETURN:
                    if selected_option == 0:  # Start Game
                        running = False
                    elif selected_option == 1:  # Customize Controls
                        action_keys = inputBox(action_keys)
                    elif selected_option == 2:  # Highscore
                        io.highscoreBox()
                    elif selected_option == 3:  # Back
                        running = False

        screen.fill((0, 0, 0))
        # Display menu options
        for i in range(len(options)):
            if i == selected_option:
                text = font.render(options[i], True, (255, 255, 255))
            else:
                text = font.render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (screen_width // 2, screen_height * 0.6 + i * option_spacing)
            screen.blit(text, text_rect)

        pg.display.update()
        clock.tick(30)

    return action_keys

def inputBox(action_keys):
    # Customize control keys similar to your previous code
    # ...

# Call the menu function to start your menu
new_action_keys = menu()

# You can use the new_action_keys dictionary with the updated control keys in your game
print("Updated control keys:", new_action_keys)
