import pygame as pg
#import firebaseRW as fiba
import os, sys
from pathlib import Path

import json

import colors as clr
import cls_pentos as clsp
from storage import readHighscoresJS


#import utils


#from utils import GAME, USERNAME, SCOREBOARD, OPTIONS, START_MENU, END_SCREEN
#from utils import imageStart #monitor_size90
os.chdir(Path(__file__).parent)
#print("BoF - inoutput")

pg.init()

monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
monitor_size90 = [monitor_size[0]*0.8, monitor_size[1]*0.8]

screen = pg.display.set_mode(monitor_size90)
screen_width, screen_height = screen.get_size()

if os.name == 'nt':  # Windows
    #image_path = "graphics\\title3.png"


    imageStart = pg.image.load("graphics\\title3.png")
    imageStartAlpha = pg.image.load("graphics\\title3.png").convert_alpha()

    #print("in io.py - NO import: monitor_size90, screen, screen_width, screen_height, imageStart:",  monitor_size90, screen, screen_width, screen_height, imageStart)

    font3 = pg.font.Font("graphics\\OCRAEXT.TTF")
    fontStrOCR = "graphics\\OCRAEXT.TTF"

    # Info fonts scoreboard, username, ggf Infotext
    fontRoboto = "graphics\\Roboto-Medium.ttf"
    fontRusso = "graphics\\Prototype.ttf"

else:  # Linux oder andere
    #image_path = "graphics/title3.png"
    imageStart = pg.image.load("graphics/title3.png")
    imageStartAlpha = pg.image.load("graphics/title3.png").convert_alpha()

    #print("in io.py - NO import: monitor_size90, screen, screen_width, screen_height, imageStart:",  monitor_size90, screen, screen_width, screen_height, imageStart)

    font3 = pg.font.Font("graphics/OCRAEXT.TTF")
    fontStrOCR = "graphics/OCRAEXT.TTF"

    # Info fonts scoreboard, username, ggf Infotext
    fontRoboto = "graphics/Roboto-Medium.ttf"
    fontRusso = "graphics/Prototype.ttf"

LANG_FONTS = {
    "en": fontRusso,
    "de": fontRusso,
    "ro": fontRoboto,
}


imageStart = pg.transform.scale(imageStart, monitor_size90)


iText = {
  "en": {
    "sM": {
      "01": "START GAME",
      "02": "USERNAME",
      "03": "SCOREBOARD",
      "04": "OPTIONS",
      "05": "QUIT",
      "username_warn": "-> Please set your own username !!",
    },
    "oM": {
      "1": "Mode",
      "2": "Pentominoes",
      "3": "DAS",
      "4": "Controls",
      "5": "Language",
      "6": "Back",
    },
    "Mode": {
      "0": "Practice",
      "1": "Competitive",
      "2": "Increment",
      "3": "Combat",
    },
    "Mode_subinfo": {
      "0": "speedup and scoreboard save - OFF",
      "1": "speedup and scoreboard save - ON",
      "2": "not in this release",
      "3": "not in this release",
    },
    "Pentos": {
      "9":  "Novice",
      "10": "lab 10",
      "11": "Standard",
      "12": "Advanced - L",
      "13": "Pro - Lu",
      "14": "Hard",
    },
    "DAS": {
      "1": "Initial Delay",
      "2": "Repeat Rate",
    },
    "Controls": {
      "0": "Left",
      "1": "Right",
      "2": "Down",
      "3": "Rotate CCW",
      "4": "Rotate CW",
      "5": "Rotate 180",
      "6": "Smash",
    },
    "lbl": {
      "1":  "Lab 1",
      "2":  "Lab 2",
      "3":  "Lab 3",
      "4":  "Lab 4",
      "5":  "lab 5",
      "9":  "Novicecomp",
      "10": "lab 10 comp",
      "11": "Standardcomp",
      "12": "Advanced - Lcomp",
      "13": "Pro - Lucomp",
      "14": "Hardcomp",
    },
    "Pause": {
      "title":    "PAUSED",
      "resume":   "RESUME",
      "end_game": "END GAME",
      "new_game": "NEW GAME",
    },
    "confirm": {
      "line1":    "Are you sure you want to",
      "quit_q":   "quit and exit the game?",
      "end_q":    "end the current game?",
      "new_q":    "start a new game?",
      "quit":     "QUIT",
      "resume":   "RESUME",
      "end_game": "END GAME",
      "new_game": "NEW GAME",
    },
    "game": {
      "level":         "Level:",
      "username":      "Username:",
      "pentominoes":   "Pentominoes:",
      "mode":          "Mode:",
      "initial_delay": "Initial Delay:",
      "repeat_rate":   "Repeat Rate:",
      "help":          "H - Help",
    },
    "eM": {
      "highscore": "Highscore",
      "enter":     "Press Enter to go to main menu",
      "esc":       "Press ESC to close",
    },
    "help": {
      "title": "HELP",
      "close": "ESC / ENTER  to close",
    },
  },        # english end

  "de": {
    "sM": {
      "01": "SPIEL STARTEN",
      "02": "BENUTZERNAME",
      "03": "BESTENLISTE",
      "04": "OPTIONEN",
      "05": "BEENDEN",
      "username_warn": "-> Bitte eigenen Benutzernamen setzen !!",
    },
    "oM": {
      "1": "Modus",
      "2": "Pentominoes",
      "3": "DAS",
      "4": "Steuerung",
      "5": "Sprache",
      "6": "Zurück",
    },
    "Mode": {
      "0": "Übung",
      "1": "Wettbewerb",
      "2": "Ansteigend",
      "3": "Kampf",
    },
    "Mode_subinfo": {
      "0": "Beschleunigung und Speichern - AUS",
      "1": "Beschleunigung und Speichern - AN",
      "2": "nicht in dieser Version",
      "3": "nicht in dieser Version",
    },
    "Pentos": {
      "9":  "Anfänger",
      "10": "lab 10",
      "11": "Standard",
      "12": "Fortgeschritten - L",
      "13": "Profi - Lu",
      "14": "Schwer",
    },
    "DAS": {
      "1": "Anfangsverz.",
      "2": "Wiederholrate",
    },
    "Controls": {
      "0": "Links",
      "1": "Rechts",
      "2": "Runter",
      "3": "Drehen (links)",
      "4": "Drehen (rechts)",
      "5": "Drehen 180",
      "6": "Smash",
    },
    "lbl": {
      "1":  "Lab 1",
      "2":  "Lab 2",
      "3":  "Lab 3",
      "4":  "Lab 4",
      "5":  "lab 5",
      "9":  "Novicecomp",
      "10": "lab 10 comp",
      "11": "Standardcomp",
      "12": "Advanced - Lcomp",
      "13": "Pro - Lucomp",
      "14": "Hardcomp",
    },
    "Pause": {
      "title":    "PAUSE",
      "resume":   "WEITER",
      "end_game": "SPIEL BEENDEN",
      "new_game": "NEUES SPIEL",
    },
    "confirm": {
      "line1":    "Bist du sicher, dass du",
      "quit_q":   "das Spiel beenden möchtest?",
      "end_q":    "die Partie beenden möchtest?",
      "new_q":    "ein neues Spiel starten möchtest?",
      "quit":     "BEENDEN",
      "resume":   "WEITER",
      "end_game": "SPIEL BEENDEN",
      "new_game": "NEUES SPIEL",
    },
    "game": {
      "level":         "Level:",
      "username":      "Benutzer:",
      "pentominoes":   "Pentominoes:",
      "mode":          "Modus:",
      "initial_delay": "Anfangsverz.:",
      "repeat_rate":   "Wiederholrate:",
      "help":          "H - Hilfe",
    },
    "eM": {
      "highscore": "Bestpunktzahl",
      "enter":     "Enter drücken für Hauptmenü",
      "esc":       "ESC drücken zum Schliessen",
    },
    "help": {
      "title": "HILFE",
      "close": "ESC / ENTER  zum Schliessen",
    },
  },        # german end

  "ro": {
    "sM": {
      "01": "ÎNCEPE JOCUL",
      "02": "UTILIZATOR",
      "03": "CLASAMENT",
      "04": "OPȚIUNI",
      "05": "IEȘIRE",
      "username_warn": "-> Vă rugăm să setați propriul nume de utilizator !!",
    },
    "oM": {
      "1": "Mod",
      "2": "Pentominouri",
      "3": "DAS",
      "4": "Controale",
      "5": "Limba",
      "6": "Înapoi",
    },
    "Mode": {
      "0": "Practică",
      "1": "Competitiv",
      "2": "Incrementat",
      "3": "Combat",
    },
    "Mode_subinfo": {
      "0": "accelerare și salvare - DEZACTIVARE",
      "1": "accelerare și salvare - ACTIVARE",
      "2": "nu în această versiune",
      "3": "nu în această versiune",
    },
    "Pentos": {
      "9":  "Începător",
      "10": "lab 10",
      "11": "Standard",
      "12": "Avansat - L",
      "13": "Pro - Lu",
      "14": "Dificil",
    },
    "DAS": {
      "1": "Întârziere inițială",
      "2": "Rata de repetare",
    },
    "Controls": {
      "0": "Stânga",
      "1": "Dreapta",
      "2": "Jos",
      "3": "Rotire (stânga)",
      "4": "Rotire (dreapta)",
      "5": "Rotire 180",
      "6": "Smash",
    },
    "lbl": {
      "1":  "Lab 1",
      "2":  "Lab 2",
      "3":  "Lab 3",
      "4":  "Lab 4",
      "5":  "lab 5",
      "9":  "Novicecomp",
      "10": "lab 10 comp",
      "11": "Standardcomp",
      "12": "Avansat - Lcomp",
      "13": "Pro - Lucomp",
      "14": "Dificilcomp",
    },
    "Pause": {
      "title":    "PAUZĂ",
      "resume":   "CONTINUĂ",
      "end_game": "SFÂRȘIT JOC",
      "new_game": "JOC NOU",
    },
    "confirm": {
      "line1":    "Ești sigur că vrei să",
      "quit_q":   "ieși din joc?",
      "end_q":    "termini jocul curent?",
      "new_q":    "începi un joc nou?",
      "quit":     "IEȘIRE",
      "resume":   "CONTINUĂ",
      "end_game": "SFÂRȘIT JOC",
      "new_game": "JOC NOU",
    },
    "game": {
      "level":         "Nivel:",
      "username":      "Utilizator:",
      "pentominoes":   "Pentominouri:",
      "mode":          "Mod:",
      "initial_delay": "Întârziere inițială:",
      "repeat_rate":   "Rata de repetare:",
      "help":          "H - Ajutor",
    },
    "eM": {
      "highscore": "Scor maxim",
      "enter":     "Apasă Enter pentru meniu principal",
      "esc":       "Apasă ESC pentru a închide",
    },
    "help": {
      "title": "AJUTOR",
      "close": "ESC / ENTER  pentru a închide",
    },
  },        # romanian end

}           # iText end

current_lang = "en"

def t(section, key):
    return iText[current_lang][section][key]

def get_font(size):
    return pg.font.Font(LANG_FONTS.get(current_lang, fontRusso), size)

LANGUAGES = {"en": "English", "de": "Deutsch", "ro": "Română"}

def langSelector(screen):
    global current_lang
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])

    lang_keys = list(LANGUAGES.keys())
    selected  = lang_keys.index(current_lang)

    font_title = get_font(30)

    sw, sh     = screen.get_size()
    n          = len(lang_keys)
    item_gap   = 44
    box_w      = int(sw * 0.4)
    box_h      = 80 + n * item_gap
    box_x      = (sw - box_w) // 2
    box_y      = (sh - box_h) // 2

    lang_clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_LEFT, pg.K_UP):
                    selected = (selected - 1) % n
                elif event.key in (pg.K_RIGHT, pg.K_DOWN):
                    selected = (selected + 1) % n
                elif event.key == pg.K_RETURN:
                    current_lang = lang_keys[selected]
                    dataJS["lang"] = current_lang
                    fileWriteData(dataJS)
                    return
                elif event.key == pg.K_ESCAPE:
                    return

        screen.blit(imageStart, (0, 0))
        pg.draw.rect(screen, (20, 20, 20), (box_x, box_y, box_w, box_h))
        pg.draw.rect(screen, clr.gry3,     (box_x, box_y, box_w, box_h), 2)

        title_surf = font_title.render(t("oM", "5"), True, clr.purple)
        screen.blit(title_surf, title_surf.get_rect(center=(sw // 2, box_y + 28)))

        items_top = box_y + 60
        for i, key in enumerate(lang_keys):
            label = LANGUAGES[key]
            lang_font = pg.font.Font(LANG_FONTS.get(key, fontRusso), 24)
            if i == selected:
                btn = lang_font.render(label, True, clr.wht, clr.purple)
            else:
                btn = lang_font.render(label, True, clr.gry2)
            btn_x = (sw - btn.get_width()) // 2
            btn_y = items_top + i * item_gap
            screen.blit(btn, (btn_x, btn_y))

        pg.display.flip()
        lang_clock.tick(60)


#infoL = DynamicDisplay(screen, screen_width*0.01, screen_height*0.8, 100, 150) #  modeStr, diffStr, usernameStr

# dict-json-sys: 1.dict->json(os-path) 2. start: load json 3. game: save->json
# diese beiden dict sind NUR für den ersten Start - danach vollk. sinnlos (oder wenn username.txt gelöscht wurde !)
                                    # da sie Z 108 dataJS = fileReadData() geladen werden
game_keys = {
    0: "Left",             10: pg.K_LEFT,
    1: "Right",            11: pg.K_RIGHT,
    2: "Down",             12: pg.K_DOWN,
    3: "R Counter-Clock",  13: pg.K_z,
    4: "R Clockwise",      14: pg.K_x,
    5: "R 180",            15: pg.K_c,
    6: "Smash",            16: pg.K_SPACE,
}

# Snapshot of defaults — used by Reset Keys; kept as strings to match JSON structure
DEFAULT_KEYS = {
    "0": "Left",            "10": pg.K_LEFT,
    "1": "Right",           "11": pg.K_RIGHT,
    "2": "Down",            "12": pg.K_DOWN,
    "3": "R Counter-Clock", "13": pg.K_z,
    "4": "R Clockwise",     "14": pg.K_x,
    "5": "R 180",           "15": pg.K_c,
    "6": "Smash",           "16": pg.K_SPACE,
}

dataJS = {
    0: "Username", 10: 'Norbert Noname', # erstmal einf nicht verwenden - am Ende switchen
    1: "Mode", 11: 9,
    2: "Initial Delay[ms]", 12: 33,
    3: "Repeat Rate[ms]", 13: 43,
    4: "competOn", 14: 1,
}

# set the path for the text file to be saved
file_path_data = os.path.join(os.path.expanduser('~'), 'Pentis', 'data.json')
file_path_keys = os.path.join(os.path.expanduser('~'), 'Pentis', 'keys.json')
file_path_scores = os.path.join(os.path.expanduser('~'), 'Pentis', 'pentis0722_L_highscores.json')
# check if the file exists, if not create it
if not os.path.exists(file_path_data):
    os.makedirs(os.path.dirname(file_path_data), exist_ok=True)
    #print(file_path_data)

    with open(file_path_data, "w") as datei:            #Zeile legt json Datei an, auch wenn next line falsch ist
        json.dump(dataJS, datei)   
    with open(file_path_keys, "w") as datei:            
        json.dump(game_keys, datei) 


if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")


username = dataJS[10]

def fileWriteData(dataJS): # fileWrite* werden nur verwendet wenn Spieler Optionen ändert: Save dict --> save dict in json
    # Data in eine JSON-Datei schreiben
    #with open("data.json", "w") as datei:
    with open(file_path_data, "w") as datei:
        json.dump(dataJS, datei)

def fileWriteKeys(game_keys): #ex fileWriteJS()
    # Data in eine JSON-Datei schreiben
    with open(file_path_keys, "w") as datei:
        json.dump(game_keys, datei)
        #json.dump(info_dict, json_file, indent=2, ensure_ascii=False, separators=(',', ': '), newline='\n')

def fileReadData():
    with open(file_path_data, "r") as datei:        # Vorsicht file_path = path UND die (json)-Datei
        dataJS = json.load(datei)    
    return dataJS
def fileReadKeys():
    if not os.path.exists(file_path_keys):
        fileWriteKeys(game_keys)
    with open(file_path_keys, "r") as datei:
        return json.load(datei)

def fileRead(file_path_keys):
    if not os.path.exists(file_path_keys):
        os.makedirs(os.path.dirname(file_path_keys), exist_ok=True)
        with open(file_path_keys, "w") as datei:
            json.dump({}, datei)
        return {}
    try:
        with open(file_path_keys, "r") as datei:
            dictionary = json.load(datei)    
        return dictionary
    except json.JSONDecodeError:
        with open(file_path_keys, "w") as datei:
            json.dump({}, datei)
        return {}
#def fileWrite(game_scores): #
#    # Data in eine JSON-Datei schreiben
#    with open(file_path_data, "w") as datei:
#        json.dump(game_scores, datei)



#game_configs
dataJS = fileReadData()     # bei jeden Start werden die Dateien in ~/Pentis eingelesen
current_lang = dataJS.get("lang", "en")
game_keys = fileReadKeys()
game_scores = fileRead(file_path_scores) 
print("loaded game_scores in io",game_scores)
#C:\Users\dem\AppData\Local\Pentis
#        $User
#fileWriteData(dataJS)
#fileWriteKeys(game_keys) # nur bei Testzwecken !!!

def toggleMusic():
    if pg.mixer.music.get_busy():
        pg.mixer.music.stop()
    else:
        pg.mixer.music.play()

def restartMusic():
    if pg.mixer.music.get_busy():
        pg.mixer.music.rewind()
    else:
        pass

def displayInfo():
    pass


def sInfoBox(dict):
    textSurface = pg.font.SysFont('OCR A Extended', 23).render(dict[j], False, (50,50,50))
    #screen.blit(textSurface,((screen_width) //2.5, screen_height*0.7))    
    # ==> screen + s_w h in io global definieren



def inputBox2(screen, imageStart): # for username
    #print("io:inputBox2")
    # Set up the screen
    screen_width = monitor_size[0] * 0.8            # 320
    screen_height = monitor_size[1] * 0.8          # 240

    #screen = pg.display.set_mode((screen_width, screen_height))
    #pg.display.set_caption("Input Username")

    strOut = "Please type your own username  (-> Enter):"
    # Set up the font
    font = pg.font.Font(fontRusso, 32)

    # Set up the text input box
    input_box = pg.Rect(screen_width * 0.4, screen_height * 0.65, 200, 32)
    input_text = ''

    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Store the user's input when press enter
                    username = input_text
                    dataJS[str(10)] = username
                    #print(dataJS)
                    fileWriteData(dataJS) 
                    input_text = ''
                    running = False
                    
                elif event.key == pg.K_BACKSPACE:
                    # Remove the last character when the user presses backspace
                    input_text = input_text[:-1]
                else:
                    # Add the character to the input text
                    input_text += event.unicode
        
        # Draw the screen
        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))
        
        text_surface = font.render(strOut, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.4, screen_height * 0.6))
        pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(input_text, True, (0, 0, 0))
        #screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        screen.blit(text_surface, (screen_width * 0.4, screen_height * 0.65))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)
    return username

def inputBoxDAS(selected_option, imageStart):
    #print("io:inputBoxDAS")
    # Set up the screen
    #screen_width = monitor_size[0] * 0.8            # 320
    #screen_height = monitor_size[1] * 0.8          # 240

    screen = pg.display.set_mode((screen_width, screen_height))
    #pg.display.set_caption("Input DAS")

    strOut = "Please type your new DAS value (11-99) (->Enter):"
    # Set up the font
    font = pg.font.Font(fontRusso, 28)

    # Set up the text input box
    input_box = pg.Rect((screen_width) //2, screen_height * 0.63, 46, 35)

    #box_rect = input_box.get_rect() 
    #box_rect.center = ((screen_width) //2, screen_height*0.6)
    #screen.blit(text_surface, box_rect)

    input_text = ''
    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Store the user's input when they press enter
                    if int(input_text) >=11 and int(input_text) <= 99:
                        newValue = input_text
                        dataJS[str(selected_option + 12)] = newValue
                        #print(dataJS)
                        fileWriteData(dataJS)                    
                        input_text = ''
                        #print("dataJS[12] = newValue changed: " + newValue)
                        running = False
                    else:
                        #print("Your new DAS value is NOT between 11 and 99")
                        input_text = ''


                elif event.key == pg.K_BACKSPACE:
                    # Remove the last character when the user presses backspace
                    input_text = input_text[:-1]
                elif event.key == pg.K_ESCAPE:
                    # Remove the last character when the user presses backspace
                    newValue = dataJS[str(selected_option + 12)]
                    running = False                
                else:
                    # Add the character to the input text
                    input_text += event.unicode
                    itd = input_text.isdigit()
                    if itd == False:
                        input_text = input_text[:-1]
                        #print(len(input_text))    
                        
                    itl = len(input_text)
                    if itl >= 3: # und digit und Zahlenbereich !!!
                        
                        input_text = input_text[:-1]
                        #print(len(input_text))
                    #if input_text.isdigit() and len(input_text) <= 2:

        
        # Draw the screen
        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))


        text_surface = font.render(strOut, True, (0, 0, 0))
        text_rect = text_surface.get_rect() 
        text_rect.center = ((screen_width) //2, screen_height*0.6)
        screen.blit(text_surface, text_rect)
        #screen.blit(text_surface, ((screen_width) //2, screen_height * 0.5))

        pg.draw.rect(screen, (0, 0, 0), input_box, 2) #==> 269
        #pg.draw.rect(screen, (0, 0, 0), box_rect, 2) #==> 269
        
        text_surface = font.render(input_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect() 
        text_rect.center = ((screen_width) //2, screen_height*0.75)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)
    return newValue
    
def helpScreen(screen):
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])

    font_title  = pg.font.Font(fontRusso, 34)
    font_footer = pg.font.Font(fontRusso, 18)

    help_clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                    return

        sw, sh = screen.get_size()
        screen.blit(imageStart, (0, 0))

        title_surf = font_title.render(t("help", "title"), True, clr.purple)
        screen.blit(title_surf, title_surf.get_rect(center=(sw * 0.5, sh * 0.55)))

        footer = font_footer.render(t("help", "close"), True, (80, 80, 80))
        screen.blit(footer, footer.get_rect(center=(sw * 0.5, sh * 0.96)))

        pg.display.flip()
        help_clock.tick(60)


def highscoreBox(screen, imageStart):

    highscores = readHighscoresJS()

    # Hardcoded baseline scores (always present)
    hardcoded = {
        "Novice": [
            {'score': 28418, 'name': 'adalaine'}, {'score': 5461, 'name': 'Beatrice Default'},
            {'score': 5333, 'name': 'Norbert Noname'}, {'score': 2123, 'name': 'lnx02'},
            {'score': 1117, 'name': 'will'}, {'score': 1055, 'name': 'Timati'},
            {'score': 124, 'name': 'mol'}, {'score': 90, 'name': 'Streamus'},
            {'score': 33, 'name': ''}, {'score': 23, 'name': 'creatos240526'}
        ],
        "Standard": [
            {'score': 73171, 'name': 'Hepta'}, {'score': 68977, 'name': 'Mari'},
            {'score': 64340, 'name': 'roncli'}, {'score': 59317, 'name': 'Aptiz712'},
            {'score': 50099, 'name': 'acephoenix'}, {'score': 48617, 'name': 'Norbert Noname'},
            {'score': 47253, 'name': 'hana'}, {'score': 42780, 'name': 'demfruit'},
            {'score': 42205, 'name': 'cobra6731'}, {'score': 28923, 'name': 'perplexotic'}
        ],
        "Advanced": [
            {'score': 40239, 'name': 'Aptiz712'}, {'score': 26824, 'name': 'pete'},
            {'score': 20367, 'name': 'demfruit'}, {'score': 14634, 'name': 'xylo'},
            {'score': 9742, 'name': 'Norbert Noname'}, {'score': 7345, 'name': 'C_the_Can'},
            {'score': 2843, 'name': 'will'}, {'score': 66, 'name': 'Monteith'},
            {'score': 12, 'name': 'Willem Default'}
        ],
        "Pro": [
            {'score': 28594, 'name': 'Aptiz712'}, {'score': 23735, 'name': 'demfruit'},
            {'score': 11197, 'name': 'Norbert Noname'}, {'score': 9954, 'name': 'Tytris'},
            {'score': 3329, 'name': 'Maestro Apfel'}, {'score': 1998, 'name': 'nji'},
            {'score': 1285, 'name': 'Willem Default'}, {'score': 687, 'name': 'pete'},
            {'score': 139, 'name': 'Darin'}, {'score': 84, 'name': 'will'}
        ],
    }

    modes = ["Novice", "Standard", "Advanced", "Pro"]

    # map saved mode → index
    dataMode = int(dataJS["11"])
    modeDict = {9: 0, 11: 1, 12: 2, 13: 3}
    current_index = modeDict.get(dataMode, 0)

    font_title = pg.font.Font(fontRusso, 34)
    font_header = pg.font.Font(fontRusso, 28)
    font_body = pg.font.Font(fontRoboto, 24)
    font_footer = pg.font.Font(fontRoboto, 20)

    def ordinal_rank(rank):
        if rank == 1: return "1st"
        if rank == 2: return "2nd"
        if rank == 3: return "3rd"
        return f"{rank}th"

    clock = pg.time.Clock()
    scroll_offset = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_RETURN, pg.K_ESCAPE):
                    return
                elif event.key == pg.K_RIGHT:
                    current_index = (current_index + 1) % len(modes)
                    scroll_offset = 0
                elif event.key == pg.K_LEFT:
                    current_index = (current_index - 1) % len(modes)
                    scroll_offset = 0
                elif event.key == pg.K_DOWN:
                    scroll_offset += 1
                elif event.key == pg.K_UP:
                    scroll_offset -= 1

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_offset -= 1
                elif event.button == 5:
                    scroll_offset += 1

        # ================= data =================
        current_mode = modes[current_index]

        # Merge: start with hardcoded entries as {name: {score}} dict
        merged = {}
        for entry in hardcoded.get(current_mode, []):
            name = entry['name']
            # Use name as key; if duplicate names exist keep the higher score
            if name not in merged or entry['score'] > merged[name]['score']:
                merged[name] = {'score': entry['score']}

        # Overlay with saved scores (saved score wins if higher)
        mode_scores = highscores.get(current_mode, {})
        for name, data in mode_scores.items():
            if name not in merged or data['score'] > merged[name]['score']:
                merged[name] = {'score': data['score']}

        sorted_scores = sorted(
            merged.items(),
            key=lambda item: item[1]['score'],
            reverse=True
        )

        screen_width, screen_height = screen.get_size()

        # ================= draw =================
        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))

        center_x = screen_width * 0.5
        block_top = screen_height * 0.6

        title = font_title.render(
            f"SCOREBOARD - {current_mode.upper()}",
            True, (20, 20, 20)
        )
        screen.blit(title, title.get_rect(center=(center_x, block_top - 60)))

        col_spacing = 220
        rank_x  = center_x - col_spacing
        name_x  = center_x
        score_x = center_x + col_spacing
        header_y = block_top

        screen.blit(font_header.render("Rank", True, (20, 20, 20)),
                    (rank_x - 40, header_y - 15))
        screen.blit(font_header.render("Player", True, (20, 20, 20)),
                    (name_x - 60, header_y - 15))
        screen.blit(font_header.render("Score", True, (20, 20, 20)),
                    (score_x - 40, header_y - 15))

        row_start_y = header_y + 50
        row_height = 40
        max_visible = int((screen_height - row_start_y - 100) // row_height)
        max_scroll = max(0, len(sorted_scores) - max_visible)
        scroll_offset = max(0, min(scroll_offset, max_scroll))
        visible = sorted_scores[scroll_offset:scroll_offset + max_visible]

        if not visible:
            txt = font_body.render("No scores available yet.", True, (120, 120, 120))
            screen.blit(txt, txt.get_rect(center=(center_x, row_start_y)))
        else:
            for i, (name, data) in enumerate(visible, start=1):
                y = row_start_y + (i - 1) * row_height
                rank = i + scroll_offset
                score = data.get('score', 0)

                screen.blit(font_body.render(ordinal_rank(rank), True, (0, 0, 0)),
                            (rank_x - 20, y))
                screen.blit(font_body.render(name, True, (0, 0, 0)),
                            (name_x - 60, y))
                screen.blit(font_body.render(str(score), True, (0, 0, 0)),
                            (score_x - 20, y))

        footer_y = screen_height - 60
        items = modes + ["Exit"]
        total_items = len(items)
        spacing = 150
        start_x = center_x - ((total_items - 1) / 2) * spacing

        for i, item in enumerate(items):
            x = start_x + i * spacing
            if item == "Exit":
                text = "Back: ESC"
                color = (120, 120, 120)
            else:
                is_active = (i == current_index)
                text = f"[{item}]" if is_active else item
                color = (34, 197, 94) if is_active else (140, 140, 140)
            surf = font_footer.render(text, True, color)
            screen.blit(surf, surf.get_rect(center=(x, footer_y)))

        if max_scroll > 0:
            info = font_footer.render(
                f"{scroll_offset+1}-{scroll_offset+len(visible)} / {len(sorted_scores)}",
                True, (120, 120, 120)
            )
            screen.blit(info, info.get_rect(center=(center_x, footer_y - 30)))

        pg.display.update()
        clock.tick(30)
           
def modeOpts(screen, imageStart, infoL):            # Mode Options
    
    #print("inner modeBox dataJS",dataJS)

    #strOut = "Please type your online username for the highscore list"

    font = pg.font.Font(fontRusso, 41)
    options = ["Practice", "Competitive", "#Increment", "#Combat"] 
    
    #selected_option = dataJS[str(11)]
    numPents = dataJS[str(11)] 
    competOn = dataJS[str(14)]
    
    # Set up menu variables
    option_spacing = 50
    capturing = False  # A flag to indicate when we're capturing a new key
    running = True
    clock = pg.time.Clock()
    selected_option = 0
    k = numPents - 10

    while (running):               #bool1 == True
        clock.tick(80)      
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
            #MENU Options "KEY PRESSED ENGINE"
            elif event.type == pg.KEYDOWN:        # 
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % (len(options))
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % (len(options))
                if event.key == pg.K_ESCAPE:
                    running = False  
                                                        
                if event.key == pg.K_RETURN:
                    if selected_option == 0: # Practice
                        competOn = 0
                    elif selected_option == 1: # Competitive
                        competOn = 1
                    elif selected_option == 2: # Increment
                        print("not in this release")
                    elif selected_option == 3: # Combat
                        print("not in this release")

                if event.key == pg.K_m:
                    toggleMusic()  

        
        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        
        # (ONLY (uo-down) Display PURPLE MARKING !!)  menu options (height 0.6)
        for i in range(len(options)):
            if i == selected_option:
                # Highlight selected option
                text = font.render(options[i], True, clr.wht, clr.purple)
                text2 = pg.font.Font(fontRusso, 20).render(iText["en"]["Mode_subinfo"][str(i)], False, (50,50,50))
            else:
                text = font.render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing) #  - textSurface_score.get_width()
            screen.blit(text, text_rect) 
            
           # SUBMIDDLE INFO (height 0.9) 
            text_rect2 = text2.get_rect()
            text_rect2.center = ((screen_width) //2, screen_height*0.9)
            screen.blit(text2, text_rect2)
        


        
        if k <=10:
            k =11
        # Display info left
        #print("j=====>", j)

        # LEFT bottom info
        modeStr = "Mode: " + iText["en"]["Mode"][str(competOn)]
        diffStr = "Pentominoes: " + iText["en"]["Pentos"][str((dataJS["11"]))]
        usernameStr = "Username: " + dataJS["10"]        
        infoL.draw_info(modeStr, diffStr, usernameStr)
        
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    return numPents, competOn

def pentosOpts(screen, imageStart, infoL):      #Pentominoes Options
    #strOut = "Please type your online username for the highscore list"

    font = pg.font.Font(fontRusso, 41)

    options = ["Novice", "Standard", "Advanced", "Pro"] 
    
    #selected_option = dataJS[str(11)]
    numPents = dataJS[str(11)] 
    competOn = dataJS[str(14)]
    # Set up menu variables
    option_spacing = 50
    capturing = False  # A flag to indicate when we're capturing a new key
       
    running = True
    clock = pg.time.Clock()
    selected_option = 0
    # var j ???
    j = numPents
    

    while (running):               #bool1 == True
        clock.tick(80)      
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
            #MENU KEY PRESSED
            elif event.type == pg.KEYDOWN:        # 
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % (len(options))
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % (len(options))
                if event.key == pg.K_ESCAPE:
                    running = False  
                                                        
                if event.key == pg.K_RETURN:
                    if selected_option == 0: # Practice
                        numPents = 9
                        j = 9
                    elif selected_option == 1: # Std
                        numPents = 11
                        j = 11
                    elif selected_option == 2: # L Advanced
                        numPents = 12
                        j = 12
                    elif selected_option == 3: # Lu Pro
                        numPents = 13
                        j = 13
                        #print("numPents:", numPents, dataJS)
                        
                if event.key == pg.K_m:
                    toggleMusic()  

        
        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        
        # (ONLY Display !!)  menu options
        for i in range(len(options)):
            if i == selected_option:
                # Highlight selected option
                text = font.render(options[i], True, clr.wht, clr.purple)
            else:
                text = font.render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)      #  - textSurface_score.get_width()
            screen.blit(text, text_rect) 


        # Sicherheitsabfrage für Test-Zwecke mit # Pentos in game
        if j <=8:
            j =11

        
        # SUBMIDDLE INFO (height 0.9)
        text = pg.font.Font(fontRusso, 20).render(iText["en"]["Mode"][str(competOn)] + " - " +  iText["en"]["Pentos"][str(j)], False, (50,50,50))
        text_rect = text.get_rect()
        text_rect.center = ((screen_width) //2, screen_height*0.9)
        screen.blit(text, text_rect)
        
        #print("j=====>", j)
        
        modeStr = "Mode: " + iText["en"]["Mode"][str(competOn)]
        diffStr = "Pentominoes: " + iText["en"]["Pentos"][str(numPents)]     # [str((dataJS["11"]))]
        usernameStr = "Username: " + dataJS["10"]        
        infoL.draw_info(modeStr, diffStr, usernameStr)
        
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    return numPents, competOn

def controlsBox(screen, imageStart):
    font       = pg.font.Font(fontRusso, 30)
    font_hint  = pg.font.Font(fontRusso, 20)

    NUM_ACTIONS  = 7
    RESET_OPTION = 7
    num_rows        = 8
    selected_option = 0
    option_spacing  = 40
    capturing       = False
    clock = pg.time.Clock()

    conflict_msg   = ""
    conflict_timer = 0

    while True:
        clock.tick(80)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

            elif event.type == pg.KEYDOWN:
                if capturing:
                    if event.key == pg.K_ESCAPE:
                        capturing = False
                        conflict_msg = ""
                    else:
                        conflict = next(
                            (game_keys[str(j)] for j in range(NUM_ACTIONS)
                             if j != selected_option and game_keys[str(j + 10)] == event.key),
                            None
                        )
                        if conflict:
                            conflict_msg = f"\'{pg.key.name(event.key)}\' already used by {conflict}!"
                            conflict_timer = 180
                        else:
                            game_keys[str(selected_option + 10)] = event.key
                            conflict_msg = ""
                            capturing = False
                else:
                    if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                        fileWriteKeys(game_keys)
                        return game_keys
                    elif event.key == pg.K_UP:
                        selected_option = (selected_option - 1) % num_rows
                    elif event.key == pg.K_DOWN:
                        selected_option = (selected_option + 1) % num_rows
                    elif event.key == pg.K_SPACE:
                        if selected_option == RESET_OPTION:
                            game_keys.update(DEFAULT_KEYS)
                            fileWriteKeys(game_keys)
                            conflict_msg = "Keys reset to defaults!"
                            conflict_timer = 180
                        else:
                            capturing = True
                            conflict_msg = ""
                    elif event.key == pg.K_m:
                        toggleMusic()

        if conflict_timer > 0:
            conflict_timer -= 1
        else:
            conflict_msg = ""

        screen.blit(imageStart, (0, 0))

        # Layout: 2 columns, 4 rows each
        # Left col (0–3): Left, Right, Down, R Counter-Clock
        # Right col (4–6 + Reset): R Clockwise, R 180, Smash, Reset Keys
        col1_x    = int(screen_width * 0.28)
        col2_x    = int(screen_width * 0.72)
        start_y   = int(screen_height * 0.58)
        row_gap   = 50

        # Divider line between columns
        mid_x = screen_width // 2
        pg.draw.line(screen, clr.gry1, (mid_x, start_y - 45), (mid_x, start_y + 3 * row_gap + 20), 1)

        for i in range(NUM_ACTIONS):
            action_name = game_keys[str(i)]
            key_name    = pg.key.name(game_keys[str(i + 10)])
            label       = f"{action_name}:  {key_name}"

            col_x = col1_x if i < 4 else col2_x
            row   = i if i < 4 else i - 4
            y     = start_y + row * row_gap

            if i == selected_option:
                if capturing:
                    label = f"{action_name}:  [ press a key... ]"
                    text = font.render(label, True, clr.wht, clr.red1)
                else:
                    text = font.render(label, True, clr.wht, clr.purple)
            else:
                text = font.render(label, True, clr.blk)

            screen.blit(text, text.get_rect(center=(col_x, y)))

        # Reset Keys — bottom of right column
        reset_y    = start_y + 3 * row_gap
        reset_text = font.render("RESET KEYS", True,
                                 clr.wht if selected_option == RESET_OPTION else clr.blk,
                                 clr.purple if selected_option == RESET_OPTION else None)
        screen.blit(reset_text, reset_text.get_rect(center=(col2_x, reset_y)))

        if conflict_msg:
            warn_surf = font_hint.render(conflict_msg, True, clr.red2)
            screen.blit(warn_surf, warn_surf.get_rect(center=(screen_width // 2, int(screen_height * 0.92))))

        hint = "up/down navigate    SPACE assign/reset    ESC / ENTER save & exit"
        hint_surf = font_hint.render(hint, True, clr.gry1)
        screen.blit(hint_surf, hint_surf.get_rect(center=(screen_width // 2, int(screen_height * 0.88))))

        pg.display.flip()

def DASBox(screen, imageStart):
    # Set up the screen
    
    #screen_width = monitor_size90[0]# * 0.5
    #screen_height = monitor_size90[1]# * 0.45
    #screen = pg.display.set_mode((screen_width, screen_height))
    #screen = pg.display.set_mode(monitor_size90)

    #pg.display.set_caption("Set Delayed Auto Shift")
    

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(fontRusso, 36)
    
    
    DASval = [dataJS['2'], dataJS['3']] 
    dataDAS_len = [2,3]

    # Set up menu variables
    selected_option = 0 # 0 und 1
    option_spacing = 50
    capturing = False  # A flag to indicate when we're capturing a new key
    running = True
    clock = pg.time.Clock()

    while running:               #bool1 == True
        clock.tick(80)      
        #print("while goonStart")
        
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
                
            
            elif event.type == pg.KEYDOWN:        # 
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(DASval)
                    #print(selected_option, DASval)
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(DASval)
                    #print(selected_option, DASval)
                if event.key == pg.K_ESCAPE:
                    #print("ESC - Highscore:", score)
                    running = False  
                                                        
                if event.key == pg.K_RETURN:
                    #print("Game started:", score)
                    capturing = True
                    newValue = inputBoxDAS(selected_option, imageStart)
                elif capturing and event.key != pg.K_RETURN:
                    # Update the selected game key with the new key
                    # Speichern in dict
                    #dataJS[12] = newValue
                    #print("dataJS vor capturing false in DASBox ", dataJS)
                    #fileWriteData(dataJS)
                    capturing = False  
                              



                if event.key == pg.K_m:
                    toggleMusic()  

            
                
        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        # Display menu options
        #print("len dict:", len(game_keys.items))
        for i in range(len(DASval)):            #for num in -  for i in dataDAS_len:

            key = i
            action_key = i + 10
            #key_pair = dasval[(i, 0)], dasval[(i, 1)]
            if i == selected_option: #selected_option
                # Highlight selected option
                text = font.render(f"{dataJS[str(i+2)]}:{dataJS[str(i+2+10)]}", True, clr.wht, clr.purple)
            else:
                text = font.render(f"{dataJS[str(i+2)]}:{dataJS[str(i+2+10)]}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)      #  - textSurface_score.get_width()
            screen.blit(text, text_rect) 
        
        #textSurface = pg.font.SysFont('OCR A Extended', 23).render("m - music on/off", False, (50,50,50))
        #screen.blit(textSurface,(screen_width*0.85, screen_height*0.9))

        
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    #return current_state    

def infoBox(strOut):
    # Set up the screen

    screen_width = 800
    screen_height = 600
    screen = pg.display.set_mode((screen_width, screen_height))
    #pg.display.set_caption("Show Highscores")

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(None, 32)

    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
                if event.key == pg.K_ESCAPE:
                    running = False                    
        
        # Draw the screen
        screen.fill((255, 255, 255))
        #pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(strOut, True, (0, 0, 0))
        screen.blit(text_surface, (50, 50))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)  

def keyBox():           # pg.init !!!
    
    #pg.init()          # !!!!! beim pg.init clean rausgenommen !!

    # Set up the screen
    screen_width = monitor_size[0] * 0.5
    screen_height = monitor_size[1] * 0.45
    screen = pg.display.set_mode((screen_width, screen_height))
    #pg.display.set_caption("Info Box")

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)

    #font = pg.font.Font(None, 32)

    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
                if event.key == pg.K_ESCAPE:
                    running = False                    
        
        # Draw the screen
        screen.fill((255, 255, 255))
        #pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        
        textSurface_update = pg.font.SysFont('Consolas', 35).render(f'There has been a Pentis update', False, (clr.blk))
        textSurface_update_bg = pg.font.SysFont('Consolas', 35).render(f'There has been a Pentis update', False, (clr.gry1))        
        
        textSurface_score = pg.font.SysFont('Consolas', 35).render(f'Please download the new version of Pentis', False, (clr.blk))
        textSurface_score_bg = pg.font.SysFont('Consolas', 35).render(f'Please download the new version of Pentis', False, (clr.gry1))
        textSurface_url = pg.font.SysFont('Consolas', 33).render(f'https://grapefruit256.itch.io/pentis', False, (clr.blk))
        textSurface_url_bg = pg.font.SysFont('Consolas', 33).render(f'https://grapefruit256.itch.io/pentis', False, (clr.gry2))
        textSurface_enter = pg.font.SysFont('Consolas', 30).render(f'Press Enter to quit', False, (clr.blk))
        textSurface_enter_bg = pg.font.SysFont('Consolas', 30).render(f'Press Enter to quit', False, (clr.gry3))

        screen.blit(textSurface_update_bg,((screen_width - textSurface_update_bg.get_width())//2, screen_height//3+1))
        screen.blit(textSurface_update,((screen_width - textSurface_update.get_width()) //2, screen_height//3))

        screen.blit(textSurface_score_bg,((screen_width - textSurface_score_bg.get_width())//2, screen_height//3+51))
        screen.blit(textSurface_score,((screen_width - textSurface_score.get_width()) //2, screen_height//3 + 50))
        screen.blit(textSurface_url_bg,((screen_width - textSurface_url_bg.get_width()) //2, screen_height//3 +121))
        screen.blit(textSurface_url,((screen_width - textSurface_url.get_width()) //2, screen_height//3 +120))
        screen.blit(textSurface_enter_bg,((screen_width - textSurface_enter_bg.get_width()) //2, screen_height//3 +191))
        screen.blit(textSurface_enter,((screen_width - textSurface_enter.get_width()) //2, screen_height//3 +190))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)  

#highscoreBox()
#keyBox()
#displayInit = pg.display.get_init

#displaySurface = pg.display.get_surface
#print("io before pg.quit: displayInit, displaySurface ", displayInit, displaySurface )

pg.quit()

#displayInit = pg.display.get_init

#displaySurface = pg.display.get_surface
#print("io after pg.quit: displayInit, displaySurface ", displayInit, displaySurface )
#print("EoF - inoutput")
