import pygame as pg

speed = 500
demtimeEvent = pg.USEREVENT+1


demclock = pg.time.Clock()
goon = True
while (goon):
    demclock.tick(0.2)    # Bildrefresh Rate x Bilder pro Sekunde
    print("timer")

    
