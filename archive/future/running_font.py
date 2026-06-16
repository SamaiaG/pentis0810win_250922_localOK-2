import pygame

pygame.init()

font = pygame.font.SysFont('Arial', 30)
text = font.render('Hello, world!', True, (111,111,111))
text_rect = text.get_rect()
text_rect.center = (640, 240)

screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update the position of the text rectangle
    text_rect.x -= 0.00001

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display the text on the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()
