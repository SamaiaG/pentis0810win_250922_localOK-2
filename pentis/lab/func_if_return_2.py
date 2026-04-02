GAME = "start_game"
USERNAME = "Username"
SCOREBOARD = "Scoreboard"
OPTIONS = "Options"
START_MENU = "start_menu"
END_SCREEN = "end_screen"

def bool_Lab():
    global i, bool1, current_state
    i = 3
    farbe = 0
    if (i < 1):
        current_state = START_MENU      # für Spiel Tests ==> GAME
        bool1 = True
        i = i + 1
        print(i)
        return True

i = 2

while (i < 5):
    current_state = START_MENU      # für Spiel Tests ==> GAME
    bool1 = True
    i = i + 1
    print(i)

if bool_Lab():
    print ("bool_Lab is true")