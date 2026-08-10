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
from splashScreen import splashScreen


def main():
    """Main game loop with proper state machine transitions"""
    current_state = START_MENU
    score = 0
    is_new_highscore = False
    pg.mixer.music.load(ost01)

    splashScreen(screen)

    while True:
        if current_state == START_MENU:
            current_state = startMenuLoop(current_state)

        elif current_state == OPTIONS:
            current_state = optMenuLoop(current_state, True, screen)

        elif current_state == GAME:
            if io.dataJS.get(io.KEY_SHOW_INTRO, True):
                io.introTipsModal(screen)
                io.dataJS[io.KEY_SHOW_INTRO] = False
                io.fileWriteData(io.dataJS)

            current_state, score = gameLoop(current_state, True, screen, score)

            # Save highscores if not in practice mode and score > 0
            is_new_highscore = False
            if score > 0 and io.dataJS[io.KEY_MODE] == 1:
                dataName = io.dataJS[io.KEY_USERNAME]
                dataMode = io.dataJS[io.KEY_NUM_PENTOS]
                is_new_highscore = addHighscoresJS(dataMode, dataName, score)

        elif current_state == END_SCREEN:
            current_state, score = endLoop(current_state, True, score, imageEnd, is_new_highscore)
            if current_state == END_SCREEN:
                break  # Exit main loop

        else:
            # Unknown state - return to start menu
            current_state = START_MENU

    return current_state


main()