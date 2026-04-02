import pygame as pg
#print("BoF - utils")
#import inoutput as io
import os
from pathlib import Path
os.chdir(Path(__file__).parent)

pg.init()

monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
monitor_size90 = [monitor_size[0]*0.8, monitor_size[1]*0.8]
monitor_size30 = [monitor_size[0]*0.6, monitor_size[1]*0.2]
print(monitor_size) 

screen = pg.display.set_mode(monitor_size90)
screen_width, screen_height = screen.get_size()

#print("in utils.py - NO import: monitor_size90, screen, screen_width, screen_height, NO imageStart:",  monitor_size90, screen, screen_width, screen_height)

pg.display.set_caption("Pentis 0.8.1 beta")

abstand = 30        # 1 Block zum Quadrat - Blockbreite = Blockhoehe = abstand
abstand = monitor_size90[1] // 32
#print("abstand//monitor_size90[1]", abstand)
spalten = 16
zeilen = 32
breite = abstand * spalten
hoehe = abstand * zeilen
grid = [0] * spalten * zeilen

bilder = []
bilder2 = []
# imageStart udn pg.transform.scale wurde io vershcoben wegen display quit suface error

if os.name == 'nt':  # Windows
    for n in range(14):     #13 hier + 0 - 0.png ist aber nur dummy - wird zu sw gemacht
        bilder.append(pg.transform.scale(pg.image.load(f'graphics\\block0{n}.png'),(abstand,abstand)))
    for n in range(14):     #13
        bilder2.append(pg.transform.scale(pg.image.load(f'graphics\\block0{n}.png'),(abstand,abstand)))

    font = pg.font.Font("graphics\\Prototype.ttf", 36) # Russo_One --> Scoreboard anders

    ost01 = 'sound\Pentis_v02.flac'
    ost02 = 'sound\Pentis_v02.flac'
    icon = pg.image.load('graphics\\block08.png')
    imageEnd = pg.image.load("graphics\\gameOver.png")


else: #Linux
    for n in range(14):     #13 hier + 0 - 0.png ist aber nur dummy - wird zu sw gemacht
        bilder.append(pg.transform.scale(pg.image.load(f'graphics/block0{n}.png'),(abstand,abstand)))
    for n in range(14):     #13
        bilder2.append(pg.transform.scale(pg.image.load(f'graphics/block0{n}.png'),(abstand,abstand)))

    font = pg.font.Font("graphics/Prototype.ttf", 36) # Russo_One --> Scoreboard anders
    ost01 = 'sound/Pentis_v02.flac'
    ost02 = 'sound/Pentis_v02.flac'
    icon = pg.image.load('graphics/block08.png')
    imageEnd = pg.image.load("graphics/gameOver.png")


pg.display.set_icon(icon)

clock = pg.time.Clock()     #clock von pygame


GAME = "start_game"
USERNAME = "Username"
SCOREBOARD = "Scoreboard"
OPTIONS = "Options"
START_MENU = "start_menu"
END_SCREEN = "end_screen"

#global goon, goonOptions, goonEnd#, goonStart       # ergibt tatsächlich global sinn  weil sie überall verwendet werden?? NEIN !! => chatGPT !!
goon, goonOptions, goonEnd = True, True, True

displayInit = pg.display.get_init

displaySurface = pg.display.get_surface
#print("utils: displayInit, displaySurface ", displayInit, displaySurface )

#pg.quit()
#print("EoF - utils")