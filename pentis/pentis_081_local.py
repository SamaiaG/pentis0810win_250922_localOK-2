#import time
import pygame as pg
pg.init()
import inoutput as io
from utils import screen, ost01, imageEnd
from utils import GAME, OPTIONS, START_MENU, END_SCREEN
from storage import addHighscoresJS

from startMenu import startMenuLoop
from optMenu import optMenuLoop
from game import gameLoop
from endMenu import endLoop


def main():
    """Main game loop with proper state machine transitions"""
    current_state = START_MENU
    score = 0
    pg.mixer.music.load(ost01)

    while True:
        if current_state == START_MENU:
            current_state = startMenuLoop(current_state, io.username)

        elif current_state == OPTIONS:
            current_state = optMenuLoop(current_state, True, screen, io.username)

        elif current_state == GAME:
            current_state, score = gameLoop(current_state, True, screen, io.username, score)

            # Save highscores if not in practice mode and score > 0
            if score > 0 and io.dataJS[io.KEY_MODE] == 1:
                dataName = io.dataJS[io.KEY_USERNAME]
                dataMode = io.dataJS[io.KEY_NUM_PENTOS]
                addHighscoresJS(dataMode, dataName, score)

        elif current_state == END_SCREEN:
            current_state, score = endLoop(current_state, True, score, imageEnd)
            if current_state == END_SCREEN:
                break  # Exit main loop

        else:
            # Unknown state - return to start menu
            current_state = START_MENU

    return current_state


main()