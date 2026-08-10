import pygame as pg
import sys
import inoutput as io
from footer import Footer
from utils import START_MENU
from utils import monitor_size90, monitor_size30, grid, clock

def clearGrid(grid):
    for n, farbe in enumerate(grid): # nicht merh self , weil es ist ja schon die Instanz
        if farbe > 0:
            grid[n] = 0

#*****************************************************************************************************************************
    #******************************************************************endLoop************************************************

def endLoop(current_state, bool1, score, imageEnd, is_new_highscore=False):
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

        _u            = io.dataJS[io.KEY_USERNAME]
        _u_set        = bool(_u and _u != io.DEFAULT_USERNAME)
        _not_practice = io.dataJS[io.KEY_MODE] != 0
        show_username = _u_set and _not_practice
        ROW_GAP       = 60
        GROUP_GAP     = ROW_GAP + 40   # extra space between user-info and nav-info groups
        score_offset  = 0 if show_username else -ROW_GAP

        highscore_label       = io.t("eM", "new_highscore") if is_new_highscore else io.t("eM", "highscore")
        textSurface_score    = io.get_font(io.FONT_LG).render(f'{highscore_label}  {score:,}', False, (231,151,4))
        textSurface_score_bg = io.get_font(io.FONT_LG).render(f'{highscore_label}  {score:,}', False, (100,100,100))
        textSurface_enter    = io.get_font(io.FONT_MD).render(io.t("eM", "enter"), False, (196,44,39))
        textSurface_enter_bg = io.get_font(io.FONT_MD).render(io.t("eM", "enter"), False, (110,110,110))
        textSurface_esc      = io.get_font(io.FONT_SM).render(io.t("eM", "esc"), False, (126,26,52))
        textSurface_esc_bg   = io.get_font(io.FONT_SM).render(io.t("eM", "esc"), False, (80,80,80))

        if show_username:
            textSurface_username    = io.get_font(io.FONT_LG).render(_u, False, (231,151,4))
            textSurface_username_bg = io.get_font(io.FONT_LG).render(_u, False, (100,100,100))
            screen.blit(textSurface_username_bg, ((screen_width - textSurface_username_bg.get_width())//2, screen_height//2+1))
            screen.blit(textSurface_username,    ((screen_width - textSurface_username.get_width())//2,    screen_height//2))

        y_score = screen_height//2 + ROW_GAP + score_offset
        y_enter = y_score + GROUP_GAP
        y_esc   = y_enter + ROW_GAP

        screen.blit(textSurface_score_bg, ((screen_width - textSurface_score_bg.get_width())//2, y_score+1))
        screen.blit(textSurface_score,    ((screen_width - textSurface_score.get_width())//2,    y_score))
        screen.blit(textSurface_enter_bg, ((screen_width - textSurface_enter_bg.get_width())//2, y_enter+1))
        screen.blit(textSurface_enter,    ((screen_width - textSurface_enter.get_width())//2,    y_enter))
        screen.blit(textSurface_esc_bg,   ((screen_width - textSurface_esc_bg.get_width())//2,   y_esc+1))
        screen.blit(textSurface_esc,      ((screen_width - textSurface_esc.get_width())//2,      y_esc))

        if not _not_practice:
            note_font_size = max(1, round(screen_height * Footer.REF_FONT_SIZE / Footer.REF_HEIGHT))
            note_font = io.get_font(note_font_size)
            note_surf = note_font.render(io.t("eM", "practice_note"), True, (140, 140, 140))
            note_y    = screen_height - Footer.BOTTOM_SPACE - note_font.get_linesize()
            screen.blit(note_surf, ((screen_width - note_surf.get_width())//2, note_y))

        screen.blit(imageEnd, ((screen_width - imageE_width)//2, screen_height//5))
        pg.display.flip()
    
    return current_state, score


