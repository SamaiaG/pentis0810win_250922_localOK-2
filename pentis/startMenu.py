import pygame as pg
import sys
import inoutput as io
from inoutput import imageStart
import colors as clr
from utils import GAME, OPTIONS, START_MENU
from utils import monitor_size90, screen, screen_width, screen_height, font, clock, ost01 # toggleMusic            # pygame pg auch in die utils
from DynamicDisplay import DynamicDisplay
# nur 20 Bilder/sec - nicht 200std
pg.init()
screen = pg.display.set_mode(monitor_size90)


# Define menu options
option_spacing = 50

infoL = DynamicDisplay(screen, screen_width*0.01, screen_height*0.8, 100, 150) #  modeStr, diffStr, usernameStr
infoR = DynamicDisplay(screen, screen_width*0.8, screen_height*0.8, 100, 150) #  "p - pause", "m - music on/off", "space - smash"


#***************************************startMenuLoop************************************************

def startMenuLoop(current_state, username):
    sM = io.iText[io.current_lang]["sM"]
    options = [sM["01"], sM["02"], sM["03"], sM["04"]]
    selected_option = 0
    bool1 = True
    while (bool1):               
        clock.tick(80)      
        
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
                
            
            elif event.type == pg.KEYDOWN:        # 
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit(0)
                if event.key == pg.K_h:
                    io.helpScreen(screen)
# menu engine                                                        
                if event.key == pg.K_RETURN:
                    if selected_option == 0:  # Start game — pick mode first
                        chosen_mode = io.modeSelectScreen(screen)
                        if chosen_mode == 1:        # Competitive: ensure username set
                            if io.ensureCompetitiveUsername(screen):
                                current_state = GAME
                                bool1 = False
                        elif chosen_mode == 0:      # Practice: go straight to game
                            current_state = GAME
                            bool1 = False

                    elif selected_option == 1:  # Highscores
                        io.highscoreBox(screen, imageStart)

                    elif selected_option == 2:  # Options
                        current_state = OPTIONS
                        bool1 = False

                    elif selected_option == 3:  # Quit
                        pg.quit()
                        sys.exit(0)

        #screen.fill((0,0,0))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        
        # Display menu options
        for i in range(len(options)):
            if i == selected_option:
                # Highlight selected option
                text = io.get_font(36).render(options[i], True, clr.wht, clr.purple)
            else:
                text = io.get_font(36).render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)      #  - textSurface_score.get_width()
            screen.blit(text, text_rect)
            
        gap_size  = screen_width // 60
        info_x    = int(screen_width * 0.01) + gap_size
        info_y    = int(screen_height * 0.8) + gap_size * 3
        info_font = io.get_font(gap_size)

        modeStr = io.t("game", "mode") + " " + io.t("Mode", str(io.dataJS[io.KEY_MODE]))
        diffStr = io.t("game", "pentominoes") + " " + io.t("Pentos", str(io.dataJS[io.KEY_NUM_PENTOS]))
        infoL.draw_info(modeStr, diffStr, font=info_font)
        infoR.draw_info(io.t("game", "help"), io.t("game", "music_toggle"), font=info_font)

        _u = io.dataJS[io.KEY_USERNAME]
        _u_set = bool(_u and _u != "Norbert Noname")
        _not_practice = io.dataJS[io.KEY_MODE] != 0
        if _u_set and _not_practice:
            username_surf = info_font.render(io.t("game", "username") + " " + _u, True, (55, 55, 55))
            screen.blit(username_surf, (info_x, info_y))
        elif not _u_set and _not_practice:
            warn_font = pg.font.Font(io.fontRoboto, gap_size)
            warn_surf = warn_font.render(io.t("sM", "username_warn"), True, clr.red3)
            screen.blit(warn_surf, (info_x, info_y))
        pg.display.flip()
    return current_state
