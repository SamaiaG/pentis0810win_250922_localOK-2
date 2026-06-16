import pygame as pg

pg.init()
width = 640
height = 480
screen = pg.display.set_mode([width, height])

demclock = pg.time.Clock()

blue = (0,255,255)
blue2 = (0,0,100)
pos = (100, 120)
def drawCircle(color):
    pg.draw.circle(screen, color, pos , 11)
goon = True
while (goon):
    demclock.tick(0.4)    # Bildrefresh Rate x Bilder pro Sekunde


    for event in pg.event.get(): # welche Events liegen momentan an
        if event.type == pg.QUIT:       # X - event vom Typ pg quit
            print("quit -> goon = false")
            goon = False

    drawCircle(blue)
    drawCircle(blue2)
    print("timer")
    pg.display.update()
    


pg.quit() # <-> pg.init
    
