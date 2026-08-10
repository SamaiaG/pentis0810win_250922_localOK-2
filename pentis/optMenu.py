import pygame as pg
import sys

import inoutput as io
from inoutput import imageSnoozed
import colors as clr
from utils import START_MENU
from utils import monitor_size90, screen, screen_width, screen_height, font, clock #toggleMusic            # pygame pg auch in die utils
from footer import Footer



pg.init()

#ost01 = 'sound\schwesternliebe1.mp3'

screen = pg.display.set_mode((screen_width, screen_height))
# Define menu options

global numPentos    #11=std  12=L  13=u
numPentos = 13

option_spacing = io.MENU_ITEM_GAP
competOn = 1
goonStart, goon, goonEnd = True, True, False

footer = Footer(screen, screen_width, screen_height)

#***************************************goonStart************************************************

def _build_opts():
    oM = io.iText[io.current_lang]
    options     = [oM["oM"][str(i)] for i in range(1, 9)]
    modeStr     = oM["game"]["mode"]        + " " + oM["Mode"][str(io.dataJS[io.KEY_MODE])]
    diffStr     = oM["game"]["pentominoes"] + " " + oM["Pentos"][str(io.dataJS[io.KEY_NUM_PENTOS])]
    usernameStr = oM["game"]["username"]    + " " + io.dataJS[io.KEY_USERNAME]
    return options, modeStr, diffStr, usernameStr

def optMenuLoop(current_state, bool1, screen):
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
                if event.key == pg.K_h:
                    io.helpScreen(screen)

                if event.key == pg.K_RETURN:
                    if selected_option == 0:        # username
                        original_username = io.dataJS[io.KEY_USERNAME]
                        io.promptUsername(screen, original_username)
                        options, modeStr, diffStr, usernameStr = _build_opts()

                    elif selected_option == 1:      # mode
                        numPentos = io.dataJS[io.KEY_NUM_PENTOS]
                        numPentos, competOn = io.modeOpts(screen, imageSnoozed)
                        io.dataJS[io.KEY_NUM_PENTOS] = numPentos
                        io.dataJS[io.KEY_MODE] = competOn
                        io.fileWriteData(io.dataJS)

                    elif selected_option == 2:      # pentominoes
                        numPentos = io.dataJS[io.KEY_NUM_PENTOS]
                        numPentos, competOn = io.pentosOpts(screen, imageSnoozed)
                        io.dataJS[io.KEY_NUM_PENTOS] = numPentos
                        io.dataJS[io.KEY_MODE] = competOn
                        io.fileWriteData(io.dataJS)

                    elif selected_option == 3:      # DAS
                        io.DASBox(screen, imageSnoozed)

                    elif selected_option == 4:      # sounds
                        io.soundsBox(screen, imageSnoozed)

                    elif selected_option == 5:      # controls
                        io.game_keys = io.controlsBox(screen, imageSnoozed)
                        selected_option = 0

                    elif selected_option == 6:      # language
                        io.langSelector(screen)
                        options, modeStr, diffStr, usernameStr = _build_opts()

                    elif selected_option == 7:      # about
                        io.aboutScreen(screen, imageSnoozed)

        screen.fill((0,0,0))        # füllen mit Schwarz
        screen.blit(imageSnoozed, (0, 0))
        
        # Footer is fixed/independent of layout — menu items center on the full screen
        container_height = screen_height
        block_height      = (len(options) - 1) * option_spacing
        first_item_y       = (container_height - block_height) / 2

        # Display menu options
        for i in range(len(options)):
            if i == selected_option:
                # Highlight selected option
                text = io.get_font(io.FONT_MENU_ITEM).render(options[i], True, clr.wht)
            else:
                text = io.get_font(io.FONT_MENU_ITEM).render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, first_item_y + i * option_spacing)
            if i == selected_option:
                pg.draw.rect(screen, clr.purple, text_rect.inflate(24, 12))
            screen.blit(text, text_rect)

        _u            = io.dataJS[io.KEY_USERNAME]
        _u_set        = bool(_u and _u != io.DEFAULT_USERNAME)
        _not_practice = io.dataJS[io.KEY_MODE] != 0
        username_line = usernameStr if (_u_set and _not_practice) else None
        warn_line     = io.t("sM", "username_warn") if (not _u_set and _not_practice) else None

        footer.draw(modeStr, diffStr, username=username_line, warn_str=warn_line,
                    help_str=io.t("game", "help"), back_str=io.t("game", "back"))
        pg.display.flip()
    return current_state

