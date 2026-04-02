import time

import pygame as pg
from utils import monitor_size, monitor_size90, monitor_size30, screen, font, imageStart, clock, username, toggleMusic
import firebaseRW as fiba
import inoutput as io
# 5 - real pentis funtions username scoreboard options

GAME = "Start Game"
USERNAME = "Username"
SCOREBOARD = "Scoreboard"
OPTIONS = "Options"
START_MENU = "start_menu"


END_SCREEN = "end_screen"


current_state = START_MENU 
bool1 = True


# Beispiel für einen Zustandsübergang vom Startmenü zum Spiel
if current_state == START_MENU: # and start_menu_done:
    current_state = START_MENU
    print("pre function if")

    # In start_menu.py

def start_menu_loop(current_state, bool1):

    #startTime = time.time()
    print("\n\nThats the start menu-Loop function")
    print("\nPress 1 for Start Game, \n2 for Username, \n3 for Scoreboard, \n4 for Options or \n5 to stay in START_MENU")
    user_input = input("\nEnter your choice: \n")    
    while (bool1 == True):      #diese while wird nur einmal nach dem input durch laufen
                                # weil in jeder input Möglichkeit wird bool1 -> false 
                                # wenn bool1 false - springt raus 
                                # und ist ABER IMMER NOCH IN DER HAUPT WHILE !!!!

        if user_input == "1":
            current_state = GAME
            bool1 = False
        elif user_input == "2":
            current_state = USERNAME
            bool1 = False
        elif user_input == "3":
            current_state = SCOREBOARD
            bool1 = False
        elif user_input == "4":
            current_state = OPTIONS
            bool1 = False
        elif user_input == "5":
            current_state = END_SCREEN
            bool1 = False            

        #elif time.time() - startTime >= 5.0:
        #    current_state = GAME

    return current_state





#*************************************************************************
#*****************************WHILE EVENT*********************************

while (True):  # Hauptschleife Ihrer Anwendung - läuft IMMER durch!!!

    if current_state == GAME:
        print("You choosed input 1 ==> GAME")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1) # in der function springt code in while(Tastaturauswahl)
                                                                # wenn bool1 true    
        # Zum Beispiel: start_menu_loop()
    elif current_state == USERNAME:
        print("\nYou choosed input 2 ==> Username")
        bool1 = True
        username = io.inputBox2()
        screen = pg.display.set_mode(monitor_size90)
        print("selectedOption:" + username)
        #break
        # Zum Beispiel: options_loop()
    elif current_state == SCOREBOARD:
        print("\nYou choosed input 3 ==> Scoreboard")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)
    elif current_state == OPTIONS:
        print("\nYou choosed input 4 ==> Options")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)                

        
        #break
    elif current_state == END_SCREEN:
        print("\nYou choosed input 5 ==> END")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)
        #break


    elif current_state == START_MENU:
        print("\nprint if user input 4 ==> START MENU")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)
        #current_state = OPTIONS
        #print("print 4")        

    # Weitere Logik für Zustandsübergänge hier




