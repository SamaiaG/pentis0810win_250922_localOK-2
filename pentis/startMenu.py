import pygame as pg
import inoutput as io
from inoutput import imageStart, toggleMusic, fontRusso
import colors as clr
from utils import GAME, USERNAME, SCOREBOARD, OPTIONS, START_MENU, END_SCREEN
from utils import monitor_size90, screen, screen_width, screen_height, font, clock, ost01 # toggleMusic            # pygame pg auch in die utils
#import firebaseRW as fiba
from DynamicDisplay import DynamicDisplay
#print("in StartMenu.py - import io: imageStart", imageStart)
# nur 20 Bilder/sec - nicht 200std
#print("in StartMenu.py - import utils: 1 - monitor_size90, screen, screen_width, screen_height:",  monitor_size90, screen, screen_width, screen_height)
pg.init()
screen = pg.display.set_mode(monitor_size90)


#print("in StartMenu.py - import utils: 2 - monitor_size90, screen, screen_width, screen_height:",  monitor_size90, screen, screen_width, screen_height)
# Define menu options
options = ["START GAME", "USERNAME", "SCOREBOARD", "OPTIONS", "QUIT"]        # "Options"
option_spacing = 50

infoL = DynamicDisplay(screen, screen_width*0.01, screen_height*0.8, 100, 150) #  modeStr, diffStr, usernameStr
infoR = DynamicDisplay(screen, screen_width*0.8, screen_height*0.8, 100, 150) #  "p - pause", "m - music on/off", "space - smash"


#***************************************startMenuLoop************************************************

def startMenuLoop(current_state, username):
    # Set up menu variables
    selected_option = 0
    bool1 = True
    while (bool1):               
        clock.tick(80)      
        
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                current_state = END_SCREEN
                bool1 = False  
                
            
            elif event.type == pg.KEYDOWN:        # 
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == pg.K_ESCAPE:
                    current_state = END_SCREEN
                    bool1 = False 
# menu engine                                                        
                if event.key == pg.K_RETURN:
                    if selected_option == 0:  # Start game 
                        current_state = GAME
                        bool1 = False

                    elif selected_option == 1: # input username
                        username = io.inputBox2(screen, imageStart)
                        io.dataJS["10"] = username
                        #print("after inputBox2 - io.dataJS[10]:" + io.dataJS["10"])
                        selected_option = 0
                        # no bool1 = False ===> still in this
                         
                    elif selected_option == 2: # Highscores
                        io.highscoreBox(screen, imageStart)
                        
                        print("online highscores will be available asap")

 
                    elif selected_option == 3: # options
                        current_state = OPTIONS
                        bool1 = False
                        
                    elif selected_option == 4: # quit
                        #print("selected_option == 4: # quit")
                        current_state = END_SCREEN
                        bool1 = False 

                if event.key == pg.K_m:
                    toggleMusic()  

        #screen.fill((0,0,0))        # füllen mit Schwarz
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
            textSurface = pg.font.SysFont(fontRusso, 26).render("-> Please set your own username !!", False, clr.red3)
            screen.blit(textSurface,(screen_width*0.01, screen_height*0.93)) 
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    return current_state
