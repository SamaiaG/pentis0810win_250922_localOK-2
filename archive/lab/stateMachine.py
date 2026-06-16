import time

START_MENU = "start_menu"
OPTIONS = "options"
GAME = "game"
END_SCREEN = "end_screen"


current_state = START_MENU 
curNum = int(input("choose 1-4"))


# Beispiel für einen Zustandsübergang vom Startmenü zum Spiel
if current_state == START_MENU: # and start_menu_done:
    current_state = START_MENU
    print("print 1")

    # In start_menu.py

def start_menu_loop(current_state):
    while current_state == START_MENU:
        print("print 2")

        # Startmenü-Logik hier
        if (curNum == 1):#start_menu_condition:
            current_state = OPTIONS  # Beispiel für Zustandsübergang
            print("print 3")

    return current_state


#*************************************************************************
#*****************************WHILE EVENT*********************************

while (current_state == START_MENU):  # Hauptschleife Ihrer Anwendung
    
    
    
    if current_state == START_MENU:
        start_menu_loop(current_state)
        #current_state = OPTIONS
        #print("print 4")

        # Zum Beispiel: start_menu_loop()
    elif current_state == OPTIONS:
        print("print 5")
        current_state = start_menu_loop(current_state)
        
        # Zum Beispiel: options_loop()
    elif current_state == GAME:
        current_state = start_menu_loop(current_state)
        # Zum Beispiel: game_loop()
    elif current_state == END_SCREEN:
        current_state = start_menu_loop(current_state)
        # Zum Beispiel: end_screen_loop()

    # Weitere Logik für Zustandsübergänge hier




