import pygame as pg
import sys

import inoutput as io
from inoutput import imageStart, toggleMusic, fontRusso
import colors as clr
from utils import GAME, USERNAME, SCOREBOARD, OPTIONS, START_MENU, END_SCREEN
from utils import monitor_size90, screen, screen_width, screen_height, font, clock #toggleMusic            # pygame pg auch in die utils
#import firebaseRW as fiba
from DynamicDisplay import DynamicDisplay


#print("BoF - optMenu")
# nur 20 Bilder/sec - nicht 200std
#imageStart = pg.image.load("graphics\\title3.png")

#screen = pg.display.set_mode(monitor_size90)
#screen_width, screen_height = screen.get_size()

#imageStart = pg.transform.scale(imageStart, (monitor_size90))

pg.init()

#ost01 = 'sound\schwesternliebe1.mp3'
#pg.mixer.music.load(ost01)
#pg.mixer.music.play(-1,0.0,0)

screen = pg.display.set_mode((screen_width, screen_height))
# Define menu options

global numPentos    #11=std  12=L  13=u
numPentos = 13

options = ["Mode", "Pentominoes", "DAS", "Controls", "Back"]        # "Options"

option_spacing = 50
competOn = 1
goonStart, goon, goonEnd = True, True, False

modeStr = "Mode: " + io.iText["en"]["Mode"][str(io.dataJS["14"])]
diffStr = "Pentominoes: " + io.iText["en"]["Pentos"][str((io.dataJS["11"]))]
usernameStr = "Username: " + io.dataJS["10"]

infoL = DynamicDisplay(screen, screen_width*0.01, screen_height*0.8, 100, 150) #  modeStr, diffStr, usernameStr
infoR = DynamicDisplay(screen, screen_width*0.8, screen_height*0.8, 100, 150) #  "p - pause", "m - music on/off", "space - smash"

#***************************************goonStart************************************************

def optMenuLoop(current_state, bool1, screen, username):

    # Set up menu variables
    selected_option = 0
    

    while (bool1):               #bool1 == True
        clock.tick(80)      
        #print("while goonStart")
        
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
                    #print("ESC - Highscore:", score)
                    current_state = START_MENU
                    bool1 = False
 
                                                        
                if event.key == pg.K_RETURN:
                    #print("Game started:", score)
                    if selected_option == 0:        # mode
                        #print("io.dataJS - 1: ",io.dataJS)
                        #print(io.dataJS[str(11)])
                        numPentos = io.dataJS[str(11)]
                        numPentos, competOn = io.modeOpts(screen, imageStart, infoL)
                        #print("numPentos in optMenu after io.modeOpts:", numPentos)
                        io.dataJS[str(11)] = numPentos
                        io.dataJS[str(14)] = competOn
                        io.fileWriteData(io.dataJS)
                        
                        #print("io.dataJS - 2: ",io.dataJS)
                        

                    elif selected_option == 1:        # pentominoes - "definded by the Number (and diversity of pentominoes )"
                        #print("io.dataJS - 1: ",io.dataJS)
                        #print(io.dataJS[str(11)])
                        numPentos = io.dataJS[str(11)]
                        numPentos, competOn = io.pentosOpts(screen, imageStart, infoL)
                        #print("numPentos in optMenu after io.pentosOpts:", numPentos)
                        io.dataJS[str(11)] = numPentos
                        io.dataJS[str(14)] = competOn
                        io.fileWriteData(io.dataJS)
                        
                        #print("io.dataJS - 2: ",io.dataJS)


                    elif selected_option == 2: # DAS
                        io.DASBox(screen, imageStart)

                    elif selected_option == 3: # controls
                        #game_keys = {}
                        #print("The controls setup is not available yet")
                        game_keys = io.controlsBox(screen, imageStart)
                        #print(game_keys[str(10)])
                        #io.fileWriteKeys(game_keys)
                        #print("selectedOption:" + username)
                        selected_option = 0                        
                    elif selected_option == 4: 
                        #print("selected_option optMenu == 4: # back")
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
                text = font.render(options[i], True, clr.wht, clr.purple)
            else:
                text = font.render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)      #  - textSurface_score.get_width()
            screen.blit(text, text_rect) 

        modeStr = "Mode: " + io.iText["en"]["Mode"][str(io.dataJS["14"])]
        diffStr = "Pentominoes: " + io.iText["en"]["Pentos"][str((io.dataJS["11"]))]
        usernameStr = "Username: " + io.dataJS["10"]        
        infoL.draw_info(modeStr, diffStr, usernameStr)
        infoR.draw_info("p - pause", "m - music on/off", "space - smash")     
        
        
        if io.dataJS["10"] == "Norbert Noname":
            textSurface = pg.font.SysFont('OCR A Extended', 26).render("-> Please set your own username !!", False, clr.red3)
            screen.blit(textSurface,(screen_width*0.01, screen_height*0.93)) 
        
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    return current_state

#print("EoF - optMenu")
