import pygame as pg



textSurface = pg.font.SysFont('OCR A Extended', 23).render("m - music on/off", False, (50,50,50))
screen.blit(textSurface,(screen_width*0.85, screen_height*0.9))

text = .render("some text")

text_rect = text.get_rect()
text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)      #  - textSurface_score.get_width()
screen.blit(text, text_rect) 