import pygame

pygame.init()


def inputBox():
    # Set up the screen
    screen_width = 320
    screen_height = 240
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Input Username")

    strOut = "Please type your online username for the highscore list"
    # Set up the font
    font = pygame.font.Font(None, 32)

    # Set up the text input box
    input_box = pygame.Rect(50, 50, 200, 32)
    input_text = ''

    # Set up the loop variables
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Store the user's input when they press enter
                    print(input_text)
                    input_text = ''
                    username = input_text
                    print(username)
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character when the user presses backspace
                    input_text = input_text[:-1]
                else:
                    # Add the character to the input text
                    input_text += event.unicode
        
        # Draw the screen
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.update()
        
        # Limit the frame rate
        clock.tick(30)

pygame.quit()
