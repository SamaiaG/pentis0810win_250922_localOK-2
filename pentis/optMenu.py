import pygame as pg
import sys

import inoutput as io
from inoutput import imageStart, toggleMusic
import colors as clr
from utils import START_MENU
from utils import monitor_size90, screen, screen_width, screen_height, font, clock #toggleMusic            # pygame pg auch in die utils
from DynamicDisplay import DynamicDisplay



pg.init()

#ost01 = 'sound\schwesternliebe1.mp3'

screen = pg.display.set_mode((screen_width, screen_height))
# Define menu options

global numPentos    #11=std  12=L  13=u
numPentos = 13

option_spacing = 36
competOn = 1
goonStart, goon, goonEnd = True, True, False

infoL = DynamicDisplay(screen, screen_width*0.01, screen_height*0.8, 100, 150) #  modeStr, diffStr, usernameStr
infoR = DynamicDisplay(screen, screen_width*0.8, screen_height*0.8, 100, 150) #  "p - pause", "m - music on/off", "space - smash"

#***************************************goonStart************************************************

def _build_opts():
    oM = io.iText[io.current_lang]
    options     = [oM["oM"][str(i)] for i in range(1, 7)]
    modeStr     = oM["game"]["mode"]        + " " + oM["Mode"][str(io.dataJS[io.KEY_MODE])]
    diffStr     = oM["game"]["pentominoes"] + " " + oM["Pentos"][str(io.dataJS[io.KEY_NUM_PENTOS])]
    usernameStr = oM["game"]["username"]    + " " + io.dataJS[io.KEY_USERNAME]
    return options, modeStr, diffStr, usernameStr

def optMenuLoop(current_state, bool1, screen, username):
    options, modeStr, diffStr, usernameStr = _build_opts()
    selected_option = 0
    

    while (bool1):               #bool1 == True
        clock.tick(80)      
        
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
                
            
            elif event.type == pg.KEYDOWN:        # 
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                    #selected_option = (selected_option - 1) % len(options)
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == pg.K_ESCAPE:
                    current_state = START_MENU
                    bool1 = False
 
                                                        
                if event.key == pg.K_RETURN:
                    if selected_option == 0:        # mode
                        numPentos = io.dataJS[io.KEY_NUM_PENTOS]
                        numPentos, competOn = io.modeOpts(screen, imageStart, infoL)
                        io.dataJS[io.KEY_NUM_PENTOS] = numPentos
                        io.dataJS[io.KEY_MODE] = competOn
                        io.fileWriteData(io.dataJS)
                        
                        

                    elif selected_option == 1:        # pentominoes - "definded by the Number (and diversity of pentominoes )"
                        numPentos = io.dataJS[io.KEY_NUM_PENTOS]
                        numPentos, competOn = io.pentosOpts(screen, imageStart, infoL)
                        io.dataJS[io.KEY_NUM_PENTOS] = numPentos
                        io.dataJS[io.KEY_MODE] = competOn
                        io.fileWriteData(io.dataJS)
                        


                    elif selected_option == 2: # DAS
                        io.DASBox(screen, imageStart)

                    elif selected_option == 3: # controls
                        #game_keys = {}
                        io.game_keys = io.controlsBox(screen, imageStart)
                        selected_option = 0                        
                    elif selected_option == 4:
                        io.langSelector(screen)
                        options, modeStr, diffStr, usernameStr = _build_opts()

                    elif selected_option == 5:
                        current_state = START_MENU
                        bool1 = False
                        
                if event.key == pg.K_m:
                    toggleMusic()  

        screen.fill((0,0,0))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        
        # Display menu options
        for i in range(len(options)):
            if i == selected_option:
                # Highlight selected option
                text = io.get_font(26).render(options[i], True, clr.wht, clr.purple)
            else:
                text = io.get_font(26).render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)      #  - textSurface_score.get_width()
            screen.blit(text, text_rect) 

        info_font = io.get_font(screen_width // 60)
        infoL.draw_info(modeStr, diffStr, usernameStr, font=info_font)
        infoR.draw_info(io.t("game", "help"), font=info_font)
        
        
        if not io.dataJS[io.KEY_USERNAME] or io.dataJS[io.KEY_USERNAME] == "Norbert Noname":
            gap_size     = screen_width // 60
            info_x       = int(screen_width * 0.01) + gap_size
            info_y       = int(screen_height * 0.8) + gap_size * 3
            warn_font    = pg.font.Font(io.fontRoboto, gap_size)
            username_w   = warn_font.render(io.t("game", "username") + " " + io.dataJS[io.KEY_USERNAME], True, (0,0,0)).get_width()
            warn_surf    = warn_font.render(io.t("sM", "username_warn"), True, clr.red3)
            screen.blit(warn_surf, (info_x + username_w + 6, info_y))
        pg.display.flip()
    return current_state

