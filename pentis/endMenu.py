import pygame as pg
import sys
import inoutput as io
from utils import START_MENU
from utils import monitor_size90, monitor_size30, grid, clock, ost01 #toggleMusic #username

def clearGrid(grid):
    for n, farbe in enumerate(grid): # nicht merh self , weil es ist ja schon die Instanz
        if farbe > 0:
            grid[n] = 0

#*****************************************************************************************************************************
    #******************************************************************endLoop************************************************

def endLoop(current_state, bool1, score, imageEnd):
    #imageEnd = pg.image.load("graphics\\gameOver.png")
    screen = pg.display.set_mode(monitor_size90)
    screen_width, screen_height = screen.get_size()
    imageEnd = pg.transform.scale(imageEnd, (monitor_size30))
    imageE_width, imageE_height = imageEnd.get_size()
    if pg.mixer.music.get_busy():
        pg.mixer.music.stop()
            
    pg.key.set_repeat()  
      
    while bool1:
        clock.tick(80)      # variable clock durhläuft nur WhileSchleife, wenn best Zeit 80 vergangen ist -> ergibt 20 Bilder/sec
                            # wegen set_timer 500ms ist die framerate 80 egal
        
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
            
            if event.type == pg.KEYDOWN:        #    
                if event.key == pg.K_RETURN:
                    #pg.mixer.music.load(ost01)
                    # pg.mixer.music.play(-1,0.0,0)
                    current_state = START_MENU
                    bool1 = False
                    
                if event.key == pg.K_ESCAPE:
                    bool1 = False

        clearGrid(grid)

        textSurface_username    = io.get_font(42).render(f'{io.dataJS[io.KEY_USERNAME]}', False, (231,151,4))
        textSurface_username_bg = io.get_font(42).render(f'{io.dataJS[io.KEY_USERNAME]}', False, (100,100,100))
        textSurface_score       = io.get_font(42).render(f'{io.t("eM", "highscore")}  {score:,}', False, (231,151,4))
        textSurface_score_bg    = io.get_font(42).render(f'{io.t("eM", "highscore")}  {score:,}', False, (100,100,100))
        textSurface_enter       = io.get_font(38).render(io.t("eM", "enter"), False, (196,44,39))
        textSurface_enter_bg    = io.get_font(38).render(io.t("eM", "enter"), False, (110,110,110))
        textSurface_esc         = io.get_font(34).render(io.t("eM", "esc"), False, (126,26,52))
        textSurface_esc_bg      = io.get_font(34).render(io.t("eM", "esc"), False, (80,80,80))

        screen.blit(textSurface_username_bg,((screen_width - textSurface_username_bg.get_width())//2, screen_height//2+1))
        screen.blit(textSurface_username,((screen_width - textSurface_username.get_width()) //2, screen_height//2))
        screen.blit(textSurface_score_bg,((screen_width - textSurface_score_bg.get_width())//2, screen_height//2+41))
        screen.blit(textSurface_score,((screen_width - textSurface_score.get_width()) //2, screen_height//2+40))
        screen.blit(textSurface_enter_bg,((screen_width - textSurface_enter_bg.get_width()) //2, screen_height//2 +81))
        screen.blit(textSurface_enter,((screen_width - textSurface_enter.get_width()) //2, screen_height//2 +80))
        screen.blit(textSurface_esc_bg,((screen_width - textSurface_esc_bg.get_width()) //2, screen_height//2 +121))
        screen.blit(textSurface_esc,((screen_width - textSurface_esc.get_width()) //2, screen_height//2 +120))
        screen.blit(imageEnd, ((screen_width - imageE_width)//2, screen_height//5))
        pg.display.flip()
    
    return current_state, score


