import time

import pygame as pg

import inoutput as  io
from utils import goon, monitor_size, monitor_size90, monitor_size30, screen, font, clock, ost01 #toggleMusic username, 
from utils import GAME, USERNAME, SCOREBOARD, OPTIONS, START_MENU, END_SCREEN
#import inoutput as  io
#from startMenu1 import start_Menu
from startMenu import startMenuLoop
from optMenu import optMenuLoop
from game import gameLoop
import firebaseRW as fiba
from endMenu import endLoop

#print("BoF - pentis")

# 5 - real pentis funtions username scoreboard options
# 6 - ""
# 6 - startmenuloop => startMenu.py
# 7 - main, stateMachine alles in startMenu.py
# 8 - 

#current_state = START_MENU 
#bool1 = True
#boolmain = True

def main():
    #global bool1
    current_state = START_MENU      # für Spiel Tests ==> GAME
    bool1 = True
    boolmain = True
    score = 0
    pg.mixer.music.load(ost01)

    #pg.mixer.music.play(-1,0.0,0)

    while (boolmain == True):      #diese while wird nur einmal nach dem input durch laufen
                            # weil in jeder input Möglichkeit wird bool1 -> false 
                            # wenn bool1 false - springt raus 
                            # und ist ABER IMMER NOCH IN DER HAUPT WHILE !!!!
        
        if current_state == START_MENU:
            #pg.mixer.music.load(ost01)
            #musicBusy = pg.mixer.music.get_busy()
            #if musicBusy == False:
            #    print("main-stratmenu-if musicplay False", musicBusy)
            #    pg.mixer.music.play(-1,0.0,0)
            #    musicBusy = pg.mixer.music.get_busy()
            #    print("main-stratmenu-if musicplay False - 2", musicBusy)
            #else:
            #    print("main-stratmenu-if musicplay True", musicBusy)
                #pass
            current_state = startMenuLoop(current_state, bool1, screen, io.username)
            #print("main 1", current_state)
        elif current_state == USERNAME:
            current_state = USERNAME
            bool1 = False
        elif current_state == SCOREBOARD:
            current_state = SCOREBOARD
            bool1 = False
        elif current_state == OPTIONS:
            current_state = optMenuLoop(current_state, bool1, screen, io.username)
            #print("main 4", current_state)
            
        elif current_state == GAME:
            #print("main 5", current_state)
            #gameLoop(goon, figur, figurnext, randlist, screen, username)
            current_state, score = gameLoop(current_state, bool1, screen, io.username, score)
            if score > 0:
                #print("io.dataJS[14]", io.dataJS["14"])
                if io.dataJS["14"] == 0:        #practOn 1/0
                    #if score > hscore10th[-1]["score"]:
                    dataName = io.dataJS["10"]
                    dataMode = io.dataJS["11"] #Mode 11std 12adv 13pro 
                    
                    fiba.addHighscore(dataMode, dataName, score)
                    gotHS = fiba.getHighscores(dataMode)
                    print(gotHS)
                else:
                    print("You are in Practive Mode - Your score will not be saved to the Scoreboard !)")           
            else:
                print("You didn't reach a highscore - Please try again !)")           
            #boolmain = False   
        elif current_state == END_SCREEN:
            #print("main 6", current_state)
            current_state, score =  endLoop(current_state, bool1, score)         
            if (current_state == END_SCREEN):
                boolmain = False     

        #elif time.time() - startTime >= 5.0:
        #    current_state = GAME
        

    return current_state
    

    optMenuLoop(current_state, bool1, screen, username)
    #print("2", current_state)
    

main()
#print("EoF - pentis")