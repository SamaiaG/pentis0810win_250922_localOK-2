import time

START_MENU = "start_menu"
OPTIONS = "options"
GAME = "game"
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
    print("Thats the start menu-Loop function")
    print("Press 1 for GAME, 2 for OPTIONS, 3 for END_SCREEN, or 4 to stay in START_MENU")
    user_input = input("Enter your choice: ")    
    while (bool1 == True):

        if user_input == "1":
            current_state = GAME
            bool1 = False
        elif user_input == "2":
            current_state = OPTIONS
            bool1 = False
        elif user_input == "3":
            current_state = END_SCREEN
            bool1 = False
        elif user_input == "4":
            current_state = START_MENU
            bool1 = False

        #elif time.time() - startTime >= 5.0:
        #    current_state = GAME

    return current_state


#*************************************************************************
#*****************************WHILE EVENT*********************************

while (True):  # Hauptschleife Ihrer Anwendung

    if current_state == GAME:
        print("print if user input 1 ==> GAME")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)        

        # Zum Beispiel: start_menu_loop()
    elif current_state == OPTIONS:
        print("print if user input 2 ==> OPTIONS")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)
        #break
        # Zum Beispiel: options_loop()

        
        #break
    elif current_state == END_SCREEN:
        print("print if user input 3 ==> END")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)
        #break


    elif current_state == START_MENU:
        print("print if user input 4 ==> START MENU")
        bool1 = True
        current_state = start_menu_loop(current_state, bool1)
        #current_state = OPTIONS
        #print("print 4")        

    # Weitere Logik für Zustandsübergänge hier




