import pygame

pygame.init()

# Fenstergröße und -titel festlegen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame screen")

keyVar = pygame.K_DOWN
print("keyVar:", keyVar)

keyVar2 = pygame.K_ESCAPE
print("keyVar:", keyVar2)

keyVar3 = pygame.K_SPACE
print("keyVar:", keyVar3)

game_keys = {
    (0,0):"Right",(0,1): "Right Arrow",
    (1,0):"Left",(1,1): "Left Arrow",
    (2,0):"Down",(2,1): "Down Arrow",
    (3,0):"Rotate CCW",(3,1): "y",
    (4,0):"Rotate CW",(4,1): "x",
    (5,0):"Rotate 180°",(5,1): "a",
    (6,0):"Smash",(6,1): pygame.K_SPACE,
    }
item_6_1 = game_keys[(6, 1)]

print(game_keys[(6, 1)])

# Hauptprogrammschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hier erfolgt die Spiellogik und Aktualisierung

    # Zeichnen
    screen.fill((0, 0, 0))  # Hintergrund löschen
    # Hier erfolgt das Zeichnen von Sprites oder anderen Elementen auf das Surface

    pygame.display.flip()  # Bildschirm aktualisieren

pygame.quit()
