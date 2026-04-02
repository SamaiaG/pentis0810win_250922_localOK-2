import time

import pygame as pg
from utils import username, goon, monitor_size, monitor_size90, monitor_size30, screen, font, imageStart, clock, toggleMusic
from utils import GAME, USERNAME, SCOREBOARD, OPTIONS, START_MENU, END_SCREEN
#from startMenu1 import start_Menu
from startMenu import startMenuLoop
from optMenu import optMenuLoop
from game import gameLoop
from endMenu import endLoop
#import firebaseRW as fiba
import inoutput as  io




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
    score = 23

    while (boolmain == True):      #diese while wird nur einmal nach dem input durch laufen
                            # weil in jeder input Möglichkeit wird bool1 -> false 
                            # wenn bool1 false - springt raus 
                            # und ist ABER IMMER NOCH IN DER HAUPT WHILE !!!!
        
        if current_state == START_MENU:
            current_state = startMenuLoop(current_state, bool1, screen, username)
            print("main 1", current_state)
        elif current_state == USERNAME:
            current_state = USERNAME
            bool1 = False
        elif current_state == SCOREBOARD:
            current_state = SCOREBOARD
            bool1 = False
        elif current_state == OPTIONS:
            current_state = optMenuLoop(current_state, bool1, screen, username)
            print("main 4", current_state)
            
        elif current_state == GAME:
            print("main 5", current_state)
            #gameLoop(goon, figur, figurnext, randlist, screen, username)
            current_state, score = gameLoop(current_state, bool1, screen, username, score)
            #boolmain = False   
        elif current_state == END_SCREEN:
            print("main 6", current_state)
            current_state, score =  endLoop(current_state, bool1, score)         
            if (current_state == END_SCREEN):
                boolmain = False     

        #elif time.time() - startTime >= 5.0:
        #    current_state = GAME
        

    return current_state
    

    optMenuLoop(current_state, bool1, screen, username)
    print("2", current_state)
    

main()