import pygame as pg
import os, sys
from pathlib import Path

import json

import colors as clr
import cls_pentos as clsp
from storage import readHighscoresJS




os.chdir(Path(__file__).parent)

pg.init()

monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
monitor_size90 = [monitor_size[0]*0.8, monitor_size[1]*0.8]

screen = pg.display.set_mode(monitor_size90)
screen_width, screen_height = screen.get_size()

if os.name == 'nt':  # Windows
    #image_path = "graphics\\title3.png"


    imageStart = pg.image.load("graphics\\title3.png")
    imageStartAlpha = pg.image.load("graphics\\title3.png").convert_alpha()


    font3 = pg.font.Font("graphics\\OCRAEXT.TTF")
    fontStrOCR = "graphics\\OCRAEXT.TTF"

    # Info fonts scoreboard, username, ggf Infotext
    fontRoboto = "graphics\\Roboto-Medium.ttf"
    fontRusso = "graphics\\Prototype.ttf"

else:  # Linux oder andere
    #image_path = "graphics/title3.png"
    imageStart = pg.image.load("graphics/title3.png")
    imageStartAlpha = pg.image.load("graphics/title3.png").convert_alpha()


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
      "02": "SCOREBOARD",
      "03": "OPTIONS",
      "04": "QUIT",
      "username_warn":  "Please set your own username!",
      "input_username": "Please set your own username  (-> Enter):",
      "username_empty": "Username cannot be empty.",
    },
    "oM": {
      "1": "Username",
      "2": "Mode",
      "3": "Difficulty",
      "4": "DAS",
      "5": "Sounds",
      "6": "Controls",
      "7": "Language",
      "8": "Back",
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
      "12": "Advanced",
      "13": "Pro",
      "14": "Hard",
    },
    "DAS": {
      "1": "Initial Delay",
      "2": "Repeat Rate",
      "input": "New DAS value (11-99)  (-> Enter):",
    },
    "Sounds": {
      "music": "Music",
      "sfx":   "Sound Effects",
      "on":    "ON",
      "off":   "OFF",
      "hint":  "UP/DOWN select    SPACE toggle    ESC save & exit",
    },
    "Controls": {
      "0": "Left",
      "1": "Right",
      "2": "Down",
      "3": "Rotate CCW",
      "4": "Rotate CW",
      "5": "Rotate 180",
      "6": "Smash",
      "press_key":    "press a key...",
      "already_used": "already used by",
      "reset_done":   "Keys reset to defaults!",
      "reset_btn":    "RESET KEYS",
      "hint":         "up/down navigate    SPACE assign/reset    ESC/ENTER save & exit",
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
      "pentominoes":   "Difficulty:",
      "mode":          "Mode:",
      "initial_delay": "Initial Delay:",
      "repeat_rate":   "Repeat Rate:",
      "help":          "H - Help",
      "music_toggle":  "M - Music",
    },
    "eM": {
      "highscore": "Highscore",
      "enter":     "Press Enter to go to main menu",
      "esc":       "Press ESC to close",
    },
    "modeSelect": {
      "title": "PLAYING MODE",
    },
    "username_conflict": {
      "line1": "\"{name}\" is already taken.",
      "line2": "Do you want to use it anyway?",
      "yes":   "YES",
      "no":    "NO",
    },
    "help": {
      "title":      "HELP",
      "close":      "ESC / ENTER  to close",
      "controls":   "CONTROLS",
      "pause_key":  "P / ESC   Pause",
      "music_key":  "M   Music",
      "help_key":   "H   Help",
      "objective":  "OBJECTIVE",
      "obj1":       "Fill complete rows of blocks to clear them.",
      "obj2":       "Pentominoes are 5-block shapes.",
      "modes":      "MODES",
      "modes_prac": "Practice: no speedup, scores not saved.",
      "modes_comp": "Competitive: speeds up, scores saved.",
      "difficulty": "DIFFICULTY",
      "scoring":    "SCORING",
      "score1":     "Points for each piece placed.",
      "score2":     "More lines at once = bigger bonus.",
    },
    "scoreboard": {
      "title":     "SCOREBOARD",
      "rank":      "Rank",
      "player":    "Player",
      "score":     "Score",
      "no_scores": "No scores available yet.",
      "back":      "Back: ESC",
    },
  },        # english end

  "de": {
    "sM": {
      "01": "SPIEL STARTEN",
      "02": "BESTENLISTE",
      "03": "OPTIONEN",
      "04": "BEENDEN",
      "username_warn":  "Bitte eigenen Benutzernamen setzen!",
      "input_username": "Bitte Benutzernamen eingeben  (-> Enter):",
      "username_empty": "Benutzername darf nicht leer sein.",
    },
    "oM": {
      "1": "Benutzername",
      "2": "Modus",
      "3": "Schwierigkeit",
      "4": "DAS",
      "5": "Klänge",
      "6": "Steuerung",
      "7": "Sprache",
      "8": "Zurück",
    },
    "Mode": {
      "0": "Übung",
      "1": "Wettbewerb",
      "2": "Ansteigend",
      "3": "Kampf",
    },
    "Mode_subinfo": {
      "0": "Beschleunigung und Highscore speichern - AUS",
      "1": "Beschleunigung und Highscore Speichern - AN",
      "2": "nicht in dieser Version",
      "3": "nicht in dieser Version",
    },
    "Pentos": {
      "9":  "Anfänger",
      "10": "lab 10",
      "11": "Standard",
      "12": "Fortgeschritten",
      "13": "Pro",
      "14": "Schwer",
    },
    "DAS": {
      "1": "Anfangsverz.",
      "2": "Wiederholrate",
      "input": "Neuen DAS-Wert eingeben (11-99)  (-> Enter):",
    },
    "Sounds": {
      "music": "Musik",
      "sfx":   "Soundeffekte",
      "on":    "AN",
      "off":   "AUS",
      "hint":  "HOCH/RUNTER wählen    LEERTASTE umschalten    ESC speichern",
    },
    "Controls": {
      "0": "Links",
      "1": "Rechts",
      "2": "Runter",
      "3": "Drehen (links)",
      "4": "Drehen (rechts)",
      "5": "Drehen 180",
      "6": "Smash",
      "press_key":    "Taste drücken...",
      "already_used": "bereits belegt von",
      "reset_done":   "Tasten zurückgesetzt!",
      "reset_btn":    "ZURÜCKSETZEN",
      "hint":         "HOCH/RUNTER navigieren    LEERTASTE zuweisen/zurücksetzen    ESC/ENTER speichern",
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
      "pentominoes":   "Schwierigkeit:",
      "mode":          "Modus:",
      "initial_delay": "Anfangsverz.:",
      "repeat_rate":   "Wiederholrate:",
      "help":          "H - Hilfe",
      "music_toggle":  "M - Musik",
    },
    "eM": {
      "highscore": "Bestpunktzahl",
      "enter":     "Enter drücken für Hauptmenü",
      "esc":       "ESC drücken zum Schliessen",
    },
    "modeSelect": {
      "title": "SPIELMODUS",
    },
    "username_conflict": {
      "line1": "\"{name}\" ist bereits vergeben.",
      "line2": "Möchtest du diesen Namen verwenden?",
      "yes":   "JA",
      "no":    "NEIN",
    },
    "help": {
      "title":      "HILFE",
      "close":      "ESC / ENTER  zum Schliessen",
      "controls":   "STEUERUNG",
      "pause_key":  "P / ESC   Pause",
      "music_key":  "M   Musik",
      "help_key":   "H   Hilfe",
      "objective":  "ZIEL",
      "obj1":       "Fülle Reihen komplett, um sie zu löschen.",
      "obj2":       "Pentominoes sind Formen aus 5 Blöcken.",
      "modes":      "MODI",
      "modes_prac": "Übung: kein Beschleunigen, kein Speichern.",
      "modes_comp": "Wettbewerb: Beschleunigung, Score gespeichert.",
      "difficulty": "SCHWIERIGKEIT",
      "scoring":    "PUNKTE",
      "score1":     "Punkte für jeden platzierten Stein.",
      "score2":     "Mehr Reihen auf einmal = grösserer Bonus.",
    },
    "scoreboard": {
      "title":     "BESTENLISTE",
      "rank":      "Rang",
      "player":    "Spieler",
      "score":     "Punkte",
      "no_scores": "Noch keine Einträge.",
      "back":      "Zurück: ESC",
    },
  },        # german end

  "ro": {
    "sM": {
      "01": "START JOC",
      "02": "CLASAMENT",
      "03": "OPŢIUNI",
      "04": "IEŞIRE",
      "username_warn":  "Setează propriul nume de utilizator!",
      "input_username": "Introdu propriul nume  (-> Enter):",
      "username_empty": "Numele nu poate fi gol.",
    },
    "oM": {
      "1": "Jucător",
      "2": "Mod",
      "3": "Dificultate",
      "4": "DAS",
      "5": "Sunete",
      "6": "Controale",
      "7": "Limbă",
      "8": "Înapoi",
    },
    "Mode": {
      "0": "Practică",
      "1": "Competitiv",
      "2": "Incrementat",
      "3": "Combat",
    },
    "Mode_subinfo": {
      "0": "accelerare şi salvare scor - DEZACTIVAT",
      "1": "accelerare şi salvare scor - ACTIVAT",
      "2": "nu în această versiune",
      "3": "nu în această versiune",
    },
    "Pentos": {
      "9":  "Începător",
      "10": "lab 10",
      "11": "Standard",
      "12": "Avansat",
      "13": "Pro",
      "14": "Dificil",
    },
    "DAS": {
      "1": "Întârziere iniţială",
      "2": "Rata de repetare",
      "input": "Valoare DAS nouă (11-99)  (-> Enter):",
    },
    "Sounds": {
      "music": "Muzică",
      "sfx":   "Efecte sonore",
      "on":    "PORNIT",
      "off":   "OPRIT",
      "hint":  "SUS/JOS selectare    SPAŢIU comutare    ESC salvare",
    },
    "Controls": {
      "0": "Stânga",
      "1": "Dreapta",
      "2": "Jos",
      "3": "Rotire (stânga)",
      "4": "Rotire (dreapta)",
      "5": "Rotire 180",
      "6": "Smash",
      "press_key":    "apasă o tastă...",
      "already_used": "deja folosit de",
      "reset_done":   "Taste resetate!",
      "reset_btn":    "RESETARE TASTE",
      "hint":         "SUS/JOS navigare    SPAŢIU atribuire/resetare    ESC/ENTER salvare",
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
      "end_game": "SFÂRŞIT JOC",
      "new_game": "JOC NOU",
    },
    "confirm": {
      "line1":    "Eşti sigur că vrei să",
      "quit_q":   "ieşi din joc?",
      "end_q":    "termini jocul curent?",
      "new_q":    "începi un joc nou?",
      "quit":     "IEŞIRE",
      "resume":   "CONTINUĂ",
      "end_game": "SFÂRŞIT JOC",
      "new_game": "JOC NOU",
    },
    "game": {
      "level":         "Nivel:",
      "username":      "Jucător:",
      "pentominoes":   "Dificultate:",
      "mode":          "Mod:",
      "initial_delay": "Întârziere iniţială:",
      "repeat_rate":   "Rata de repetare:",
      "help":          "H - Ajutor",
      "music_toggle":  "M - Muzică",
    },
    "eM": {
      "highscore": "Scor maxim",
      "enter":     "Apasă Enter pentru meniu principal",
      "esc":       "Apasă ESC pentru a închide",
    },
    "modeSelect": {
      "title": "MOD DE JOC",
    },
    "username_conflict": {
      "line1": "\"{name}\" este deja folosit.",
      "line2": "Vrei să folosesti oricum acest nume?",
      "yes":   "DA",
      "no":    "NU",
    },
    "help": {
      "title":      "AJUTOR",
      "close":      "ESC / ENTER  pentru a închide",
      "controls":   "CONTROALE",
      "pause_key":  "P / ESC   Pauză",
      "music_key":  "M   Muzică",
      "help_key":   "H   Ajutor",
      "objective":  "OBIECTIV",
      "obj1":       "Umple rânduri complete pentru a le şterge.",
      "obj2":       "Pentominouri au câte 5 blocuri.",
      "modes":      "MODURI",
      "modes_prac": "Practică: fără accelerare, scor nesalvat.",
      "modes_comp": "Competitiv: accelerare, scor salvat.",
      "difficulty": "DIFICULTATE",
      "scoring":    "PUNCTAJ",
      "score1":     "Puncte pentru fiecare piesă plasată.",
      "score2":     "Mai multe rânduri deodată = bonus mai mare.",
    },
    "scoreboard": {
      "title":     "CLASAMENT",
      "rank":      "Loc",
      "player":    "Jucător",
      "score":     "Punctaj",
      "no_scores": "Nu există scoruri încă.",
      "back":      "Înapoi: ESC",
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

    lang_keys      = list(LANGUAGES.keys())
    selected       = lang_keys.index(current_lang)
    n              = len(lang_keys)
    option_spacing = 50
    sw, sh         = screen.get_size()
    lang_clock     = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_UP, pg.K_LEFT):
                    selected = (selected - 1) % n
                elif event.key in (pg.K_DOWN, pg.K_RIGHT):
                    selected = (selected + 1) % n
                elif event.key == pg.K_RETURN:
                    current_lang = lang_keys[selected]
                    dataJS[KEY_LANG] = current_lang
                    fileWriteData(dataJS)
                    return
                elif event.key == pg.K_ESCAPE:
                    return

        screen.blit(imageStart, (0, 0))

        for i, key in enumerate(lang_keys):
            label     = LANGUAGES[key]
            lang_font = pg.font.Font(LANG_FONTS.get(key, fontRusso), 41)
            if i == selected:
                btn = lang_font.render(label, True, clr.wht, clr.purple)
            else:
                btn = lang_font.render(label, True, (0, 0, 0))
            btn_rect        = btn.get_rect()
            btn_rect.center = (sw // 2, sh * 0.6 + i * option_spacing)
            screen.blit(btn, btn_rect)

        sub_font = pg.font.Font(LANG_FONTS.get(current_lang, fontRusso), 20)
        sub = sub_font.render(LANGUAGES[current_lang], False, (50, 50, 50))
        screen.blit(sub, sub.get_rect(center=(sw // 2, int(sh * 0.9))))

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


# dataJS key constants — use these instead of bare string literals
KEY_USERNAME   = "10"
KEY_NUM_PENTOS = "11"
KEY_DAS_DELAY  = "12"
KEY_DAS_RATE   = "13"
KEY_MODE       = "14"
KEY_LANG       = "lang"
KEY_MUSIC      = "music"
KEY_SFX        = "sfx"

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
#    with open(file_path_data, "w") as datei:
#        json.dump(game_scores, datei)



#game_configs
dataJS = fileReadData()     # bei jeden Start werden die Dateien in ~/Pentis eingelesen
dataJS.setdefault(KEY_MUSIC, False)
dataJS.setdefault(KEY_SFX,   True)
current_lang = dataJS.get(KEY_LANG, "en")
game_keys = fileReadKeys()
game_scores = fileRead(file_path_scores)
#C:\Users\dem\AppData\Local\Pentis
#        $User
#fileWriteData(dataJS)
#fileWriteKeys(game_keys) # nur bei Testzwecken !!!

def toggleMusic():
    if pg.mixer.music.get_busy():
        pg.mixer.music.stop()
        dataJS[KEY_MUSIC] = False
    else:
        pg.mixer.music.play(-1)
        dataJS[KEY_MUSIC] = True
    fileWriteData(dataJS)

def restartMusic():
    if pg.mixer.music.get_busy():
        pg.mixer.music.rewind()
    else:
        pass

def displayInfo():
    pass


def sInfoBox(dict):
    textSurface = pg.font.SysFont('OCR A Extended', 23).render(dict[j], False, (50,50,50))
    # ==> screen + s_w h in io global definieren



def inputBox2(screen, imageStart):
    sw = monitor_size[0] * 0.8
    sh = monitor_size[1] * 0.8

    strOut    = t("sM", "input_username")
    font      = get_font(32)
    font_err  = get_font(20)
    input_box = pg.Rect(sw * 0.4, sh * 0.65, 200, 32)
    input_text = ''
    error_msg  = ''
    username   = None
    running    = True
    clock      = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if input_text.strip():
                        username = input_text.strip()
                        dataJS[KEY_USERNAME] = username
                        fileWriteData(dataJS)
                        running = False
                    else:
                        error_msg = t("sM", "username_empty")
                elif event.key == pg.K_ESCAPE:
                    running = False
                elif event.key == pg.K_BACKSPACE:
                    input_text = input_text[:-1]
                    error_msg  = ''
                else:
                    input_text += event.unicode
                    error_msg  = ''

        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))
        text_surface = font.render(strOut, True, (0, 0, 0))
        screen.blit(text_surface, (sw * 0.4, sh * 0.6))
        pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (sw * 0.4, sh * 0.65))
        if error_msg:
            err_surf = font_err.render(error_msg, True, clr.red3)
            screen.blit(err_surf, (sw * 0.4, sh * 0.71))
        pg.display.update()
        clock.tick(30)

    return username

def inputBoxDAS(selected_option, imageStart):
    # Set up the screen
    #screen_width = monitor_size[0] * 0.8            # 320
    #screen_height = monitor_size[1] * 0.8          # 240

    screen = pg.display.set_mode((screen_width, screen_height))
    #pg.display.set_caption("Input DAS")

    strOut = t("DAS", "input")
    font = get_font(28)

    # Set up the text input box
    input_box = pg.Rect((screen_width) //2, screen_height * 0.63, 46, 35)

    #box_rect = input_box.get_rect() 
    #box_rect.center = ((screen_width) //2, screen_height*0.6)

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
                        fileWriteData(dataJS)                    
                        input_text = ''
                        running = False
                    else:
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
                        
                    itl = len(input_text)
                    if itl >= 3: # und digit und Zahlenbereich !!!
                        
                        input_text = input_text[:-1]
                    #if input_text.isdigit() and len(input_text) <= 2:

        
        # Draw the screen
        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))


        text_surface = font.render(strOut, True, (0, 0, 0))
        text_rect = text_surface.get_rect() 
        text_rect.center = ((screen_width) //2, screen_height*0.6)
        screen.blit(text_surface, text_rect)

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
    
def modeSelectScreen(screen):
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])

    mode_keys      = [0, 1]   # Practice, Competitive
    prev           = dataJS.get(KEY_MODE, 1)
    selected       = mode_keys.index(prev) if prev in mode_keys else 1
    option_spacing = 52
    clock          = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_UP, pg.K_LEFT):
                    selected = (selected - 1) % len(mode_keys)
                elif event.key in (pg.K_DOWN, pg.K_RIGHT):
                    selected = (selected + 1) % len(mode_keys)
                elif event.key == pg.K_RETURN:
                    chosen = mode_keys[selected]
                    dataJS[KEY_MODE] = chosen
                    fileWriteData(dataJS)
                    return chosen
                elif event.key == pg.K_ESCAPE:
                    return None

        sw, sh = screen.get_size()
        screen.blit(imageStart, (0, 0))

        title = get_font(34).render(t("modeSelect", "title"), True, clr.purple)
        screen.blit(title, title.get_rect(center=(sw // 2, int(sh * 0.52))))

        for i, mode_idx in enumerate(mode_keys):
            label = t("Mode", str(mode_idx))
            if i == selected:
                surf = get_font(41).render(label, True, clr.wht, clr.purple)
            else:
                surf = get_font(41).render(label, True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(sw // 2, int(sh * 0.62) + i * option_spacing)))

        subinfo = get_font(20).render(t("Mode_subinfo", str(mode_keys[selected])), True, (50, 50, 50))
        screen.blit(subinfo, subinfo.get_rect(center=(sw // 2, int(sh * 0.88))))

        pg.display.flip()
        clock.tick(60)


def usernameConflictBox(screen, username):
    """Returns True (YES — use anyway) or False (NO — try a different name)."""
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])
    selected  = 1   # default highlight NO (safer choice)
    font_body = get_font(24)
    font_btn  = get_font(32)
    clock     = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_LEFT, pg.K_UP):
                    selected = 0
                elif event.key in (pg.K_RIGHT, pg.K_DOWN):
                    selected = 1
                elif event.key == pg.K_RETURN:
                    return selected == 0
                elif event.key == pg.K_ESCAPE:
                    return False

        sw, sh = screen.get_size()
        screen.blit(imageStart, (0, 0))

        line1 = font_body.render(t("username_conflict", "line1").format(name=username), True, clr.blk)
        line2 = font_body.render(t("username_conflict", "line2"), True, clr.blk)
        screen.blit(line1, line1.get_rect(center=(sw // 2, int(sh * 0.57))))
        screen.blit(line2, line2.get_rect(center=(sw // 2, int(sh * 0.63))))

        yes_surf = font_btn.render(t("username_conflict", "yes"), True,
                                   clr.wht if selected == 0 else clr.blk,
                                   clr.purple if selected == 0 else None)
        no_surf  = font_btn.render(t("username_conflict", "no"),  True,
                                   clr.wht if selected == 1 else clr.blk,
                                   clr.purple if selected == 1 else None)
        screen.blit(yes_surf, yes_surf.get_rect(center=(int(sw * 0.38), int(sh * 0.73))))
        screen.blit(no_surf,  no_surf.get_rect(center=(int(sw * 0.62), int(sh * 0.73))))

        pg.display.flip()
        clock.tick(60)


def ensureCompetitiveUsername(screen):
    """
    If username is already set, returns True immediately.
    Otherwise loops: prompt username → check conflict → confirm or retry.
    Returns True when ready to start, False if the player cancelled (ESC).
    """
    _u = dataJS[KEY_USERNAME]
    if _u and _u != "Norbert Noname":
        return True

    original_username = _u

    while True:
        new_u = inputBox2(screen, imageStart)
        if new_u is None:                       # player pressed ESC
            dataJS[KEY_USERNAME] = original_username
            fileWriteData(dataJS)
            return False

        saved = readHighscoresJS()
        taken = {name for scores in saved.values() for name in scores}

        if new_u in taken:
            if usernameConflictBox(screen, new_u):
                return True                     # YES — use the taken name
            # NO — revert and loop back to input
            dataJS[KEY_USERNAME] = original_username
            fileWriteData(dataJS)
        else:
            return True                         # fresh name, proceed


def helpScreen(screen):
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])
    help_clock = pg.time.Clock()

    font_title  = get_font(26)
    font_head   = get_font(19)
    font_body   = get_font(16)
    font_footer = get_font(15)

    H_HEAD = 27   # spacing after a section header
    H_BODY = 23   # spacing between body lines
    H_GAP  = 8    # extra gap between sections

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

        col_l = int(sw * 0.26)
        col_r = int(sw * 0.72)
        y0    = int(sh * 0.535)

        # Title
        title_surf = font_title.render(t("help", "title"), True, clr.purple)
        screen.blit(title_surf, title_surf.get_rect(center=(sw // 2, int(sh * 0.495))))

        # Vertical column divider
        pg.draw.line(screen, clr.gry1, (sw // 2, y0 - 8), (sw // 2, int(sh * 0.93)), 1)

        # ---- LEFT COLUMN: Controls ----
        y = y0
        surf = font_head.render(t("help", "controls"), True, clr.purple)
        screen.blit(surf, surf.get_rect(center=(col_l, y)))
        y += H_HEAD

        for i in range(7):
            action = t("Controls", str(i))
            key    = pg.key.name(game_keys[str(i + 10)])
            surf   = font_body.render(f"{action}:  {key}", True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(col_l, y)))
            y += H_BODY

        pg.draw.line(screen, clr.gry1, (int(sw * 0.05), y + 3), (int(sw * 0.47), y + 3), 1)
        y += 11

        for key_str in ("pause_key", "music_key", "help_key"):
            surf = font_body.render(t("help", key_str), True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(col_l, y)))
            y += H_BODY

        # ---- RIGHT COLUMN: Game info ----
        y = y0

        surf = font_head.render(t("help", "objective"), True, clr.purple)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        for key_str in ("obj1", "obj2"):
            surf = font_body.render(t("help", key_str), True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY
        y += H_GAP

        surf = font_head.render(t("help", "modes"), True, clr.purple)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        for key_str in ("modes_prac", "modes_comp"):
            surf = font_body.render(t("help", key_str), True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY
        y += H_GAP

        surf = font_head.render(t("help", "difficulty"), True, clr.purple)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        diff1 = f"{t('Pentos','9')}: 9     {t('Pentos','11')}: 11"
        diff2 = f"{t('Pentos','12')}: 12   {t('Pentos','13')}: 13"
        for diff_line in (diff1, diff2):
            surf = font_body.render(diff_line, True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY
        y += H_GAP

        surf = font_head.render(t("help", "scoring"), True, clr.purple)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        for key_str in ("score1", "score2"):
            surf = font_body.render(t("help", key_str), True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY

        footer = font_footer.render(t("help", "close"), True, (80, 80, 80))
        screen.blit(footer, footer.get_rect(center=(sw // 2, int(sh * 0.965))))

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
    dataMode = int(dataJS[KEY_NUM_PENTOS])
    modeDict = {9: 0, 11: 1, 12: 2, 13: 3}
    current_index = modeDict.get(dataMode, 0)

    font_title  = get_font(34)
    font_header = get_font(28)
    font_body   = pg.font.Font(fontRoboto, 24)
    font_footer = get_font(20)

    mode_labels = {
        "Novice":   t("Pentos", "9"),
        "Standard": t("Pentos", "11"),
        "Advanced": t("Pentos", "12"),
        "Pro":      t("Pentos", "13"),
    }

    def ordinal_rank(rank):
        if current_lang == "en":
            if rank == 1: return "1st"
            if rank == 2: return "2nd"
            if rank == 3: return "3rd"
            return f"{rank}th"
        return f"{rank}."

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
            t("scoreboard", "title") + " - " + mode_labels[current_mode].upper(),
            True, (20, 20, 20)
        )
        screen.blit(title, title.get_rect(center=(center_x, block_top - 60)))

        col_spacing = 220
        rank_x  = center_x - col_spacing
        name_x  = center_x
        score_x = center_x + col_spacing
        header_y = block_top

        screen.blit(font_header.render(t("scoreboard", "rank"),   True, (20, 20, 20)),
                    (rank_x - 40, header_y - 15))
        screen.blit(font_header.render(t("scoreboard", "player"), True, (20, 20, 20)),
                    (name_x - 60, header_y - 15))
        screen.blit(font_header.render(t("scoreboard", "score"),  True, (20, 20, 20)),
                    (score_x - 40, header_y - 15))

        row_start_y = header_y + 50
        row_height = 40
        max_visible = int((screen_height - row_start_y - 100) // row_height)
        max_scroll = max(0, len(sorted_scores) - max_visible)
        scroll_offset = max(0, min(scroll_offset, max_scroll))
        visible = sorted_scores[scroll_offset:scroll_offset + max_visible]

        if not visible:
            txt = font_body.render(t("scoreboard", "no_scores"), True, (120, 120, 120))
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
                text = t("scoreboard", "back")
                color = (120, 120, 120)
            else:
                is_active = (i == current_index)
                label = mode_labels[item]
                text = f"[{label}]" if is_active else label
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

    options = [t("Mode", "0"), t("Mode", "1"), t("Mode", "2"), t("Mode", "3")]
    
    #selected_option = dataJS[KEY_NUM_PENTOS]
    numPents = dataJS[KEY_NUM_PENTOS] 
    competOn = dataJS[KEY_MODE]
    
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
                text = get_font(41).render(options[i], True, clr.wht, clr.purple)
                text2 = get_font(20).render(t("Mode_subinfo", str(i)), False, (50,50,50))
            else:
                text = get_font(41).render(options[i], True, (0, 0, 0))
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

        # LEFT bottom info
        modeStr   = t("game", "mode")        + " " + t("Mode",  str(competOn))
        diffStr   = t("game", "pentominoes") + " " + t("Pentos", str(dataJS[KEY_NUM_PENTOS]))
        info_font = get_font(screen_width // 60)
        _u     = dataJS[KEY_USERNAME]
        _u_set = bool(_u and _u != "Norbert Noname")
        if _u_set and competOn != 0:
            infoL.draw_info(modeStr, diffStr, t("game", "username") + " " + _u, font=info_font)
        else:
            infoL.draw_info(modeStr, diffStr, font=info_font)

        pg.display.flip()
    return numPents, competOn

def pentosOpts(screen, imageStart, infoL):      #Pentominoes Options

    options = [t("Pentos", "9"), t("Pentos", "11"), t("Pentos", "12"), t("Pentos", "13")]
    
    #selected_option = dataJS[KEY_NUM_PENTOS]
    numPents = dataJS[KEY_NUM_PENTOS] 
    competOn = dataJS[KEY_MODE]
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
                        
                if event.key == pg.K_m:
                    toggleMusic()  

        
        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        
        # (ONLY Display !!)  menu options
        for i in range(len(options)):
            if i == selected_option:
                text = get_font(41).render(options[i], True, clr.wht, clr.purple)
            else:
                text = get_font(41).render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)
            screen.blit(text, text_rect)

        if j <= 8:
            j = 11

        # SUBMIDDLE INFO (height 0.9)
        text = get_font(20).render(t("Mode", str(competOn)) + " - " + t("Pentos", str(j)), False, (50,50,50))
        text_rect = text.get_rect()
        text_rect.center = ((screen_width) //2, screen_height*0.9)
        screen.blit(text, text_rect)

        modeStr   = t("game", "mode")        + " " + t("Mode",  str(competOn))
        diffStr   = t("game", "pentominoes") + " " + t("Pentos", str(numPents))
        info_font = get_font(screen_width // 60)
        _u     = dataJS[KEY_USERNAME]
        _u_set = bool(_u and _u != "Norbert Noname")
        if _u_set and competOn != 0:
            infoL.draw_info(modeStr, diffStr, t("game", "username") + " " + _u, font=info_font)
        else:
            infoL.draw_info(modeStr, diffStr, font=info_font)
        
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    return numPents, competOn

def controlsBox(screen, imageStart):
    font       = get_font(30)
    font_hint  = get_font(20)

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
                        conflict_idx = next(
                            (j for j in range(NUM_ACTIONS)
                             if j != selected_option and game_keys[str(j + 10)] == event.key),
                            None
                        )
                        if conflict_idx is not None:
                            conflict_msg = f"'{pg.key.name(event.key)}' {t('Controls', 'already_used')} {t('Controls', str(conflict_idx))}!"
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
                            conflict_msg = t("Controls", "reset_done")
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
            action_name = t("Controls", str(i))
            key_name    = pg.key.name(game_keys[str(i + 10)])
            label       = f"{action_name}:  {key_name}"

            col_x = col1_x if i < 4 else col2_x
            row   = i if i < 4 else i - 4
            y     = start_y + row * row_gap

            if i == selected_option:
                if capturing:
                    label = f"{action_name}:  [ {t('Controls', 'press_key')} ]"
                    text = font.render(label, True, clr.wht, clr.red1)
                else:
                    text = font.render(label, True, clr.wht, clr.purple)
            else:
                text = font.render(label, True, clr.blk)

            screen.blit(text, text.get_rect(center=(col_x, y)))

        # Reset Keys — bottom of right column
        reset_y    = start_y + 3 * row_gap
        reset_text = font.render(t("Controls", "reset_btn"), True,
                                 clr.wht if selected_option == RESET_OPTION else clr.blk,
                                 clr.purple if selected_option == RESET_OPTION else None)
        screen.blit(reset_text, reset_text.get_rect(center=(col2_x, reset_y)))

        if conflict_msg:
            warn_surf = font_hint.render(conflict_msg, True, clr.red2)
            screen.blit(warn_surf, warn_surf.get_rect(center=(screen_width // 2, int(screen_height * 0.92))))

        hint_surf = font_hint.render(t("Controls", "hint"), True, clr.gry1)
        screen.blit(hint_surf, hint_surf.get_rect(center=(screen_width // 2, int(screen_height * 0.88))))

        pg.display.flip()

def soundsBox(screen, imageStart):
    selected = 0
    clock = pg.time.Clock()
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_UP, pg.K_DOWN):
                    selected = 1 - selected
                elif event.key in (pg.K_RETURN, pg.K_SPACE):
                    if selected == 0:
                        dataJS[KEY_MUSIC] = not dataJS[KEY_MUSIC]
                    else:
                        dataJS[KEY_SFX] = not dataJS[KEY_SFX]
                    fileWriteData(dataJS)
                elif event.key == pg.K_ESCAPE:
                    return

        sw, sh = screen.get_size()
        screen.blit(imageStart, (0, 0))

        font      = get_font(36)
        font_hint = get_font(18)

        items = [
            (t("Sounds", "music"), dataJS[KEY_MUSIC]),
            (t("Sounds", "sfx"),   dataJS[KEY_SFX]),
        ]

        for i, (label, state) in enumerate(items):
            status = t("Sounds", "on") if state else t("Sounds", "off")
            line = f"{label}:  {status}"
            if i == selected:
                surf = font.render(line, True, clr.wht, clr.purple)
            else:
                surf = font.render(line, True, clr.blk)
            screen.blit(surf, surf.get_rect(center=(sw // 2, int(sh * 0.6) + i * 60)))

        hint = font_hint.render(t("Sounds", "hint"), True, (80, 80, 80))
        screen.blit(hint, hint.get_rect(center=(sw // 2, int(sh * 0.9))))

        pg.display.flip()
        clock.tick(60)


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
    font = get_font(36)

    DASval = [t("DAS", "1"), t("DAS", "2")]
    dataDAS_len = [2,3]

    # Set up menu variables
    selected_option = 0 # 0 und 1
    option_spacing = 50
    capturing = False  # A flag to indicate when we're capturing a new key
    running = True
    clock = pg.time.Clock()

    while running:               #bool1 == True
        clock.tick(80)      
        
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
                
            
            elif event.type == pg.KEYDOWN:        # 
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(DASval)
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(DASval)
                if event.key == pg.K_ESCAPE:
                    running = False  
                                                        
                if event.key == pg.K_RETURN:
                    capturing = True
                    newValue = inputBoxDAS(selected_option, imageStart)
                elif capturing and event.key != pg.K_RETURN:
                    # Update the selected game key with the new key
                    # Speichern in dict
                    #dataJS[12] = newValue
                    #fileWriteData(dataJS)
                    capturing = False  
                              



                if event.key == pg.K_m:
                    toggleMusic()  

            
                
        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        # Display menu options
        for i in range(len(DASval)):            #for num in -  for i in dataDAS_len:

            key = i
            action_key = i + 10
            #key_pair = dasval[(i, 0)], dasval[(i, 1)]
            label = DASval[i]
            value = dataJS[str(i + 12)]
            if i == selected_option:
                text = font.render(f"{label}: {value}", True, clr.wht, clr.purple)
            else:
                text = font.render(f"{label}: {value}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.6 + i * option_spacing)      #  - textSurface_score.get_width()
            screen.blit(text, text_rect) 
        

        
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

pg.quit()

#displayInit = pg.display.get_init

#displaySurface = pg.display.get_surface
