#import time
import pygame as pg
pg.init()
import inoutput as io
from utils import screen, ost01, imageEnd
from utils import GAME, USERNAME, SCOREBOARD, OPTIONS, START_MENU, END_SCREEN
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
            if score > 0 and io.dataJS["14"] == 1:  # 14: practOn (1 = practice off = save scores)
                dataName = io.dataJS["10"]  # username
                dataMode = io.dataJS["11"]  # Mode: 11=std, 12=adv, 13=pro
                addHighscoresJS(dataMode, dataName, score)
            elif score > 0:
                print("Practice mode: Score not saved - Please try again in Standard/Advanced/Pro mode!")

        elif current_state == END_SCREEN:
            current_state, score = endLoop(current_state, True, score, imageEnd)
            if current_state == END_SCREEN:
                break  # Exit main loop

        else:
            # Unknown state - return to start menu
            current_state = START_MENU

    return current_state


main()