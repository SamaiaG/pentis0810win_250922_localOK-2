import pygame as pg
import os, sys
import webbrowser
from pathlib import Path

import json

import colors as clr
import cls_pentos as clsp
from storage import readHighscoresJS
from footer import Footer




os.chdir(Path(__file__).parent)

pg.init()

monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
monitor_size90 = [monitor_size[0]*0.8, monitor_size[1]*0.8]

screen = pg.display.set_mode(monitor_size90)
screen_width, screen_height = screen.get_size()

DEFAULT_USERNAME = "Norbert Noname"

_BASE   = screen_height / 24.0
FONT_XL = int(_BASE * 1.16)   # start menu items — biggest in game
FONT_LG = int(_BASE)           # sub-menu items, page titles
FONT_MD = int(_BASE * 0.8)    # options menu, dialog body, prompts
FONT_SM = int(_BASE * 0.6)   # hints, secondary labels
FONT_XS = int(_BASE * 0.5)    # footer info bar — smallest

# Reusable sizing for stacked vertical menu lists (Options and future menu screens)
FONT_MENU_ITEM = int(_BASE * 0.95)
MENU_ITEM_GAP  = int(_BASE * 1.8)

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

# Snoozed (faded) background — used on every screen except the splash and the main menu
imageSnoozed = imageStart.copy()
_snooze_overlay = pg.Surface(imageSnoozed.get_size())
_snooze_overlay.fill((255, 255, 255))
_snooze_overlay.set_alpha(210)
imageSnoozed.blit(_snooze_overlay, (0, 0))


iText = {
  "en": {
    "sM": {
      "01": "START GAME",
      "02": "SCOREBOARD",
      "03": "OPTIONS",
      "04": "QUIT",
      "username_warn":  "Please set your own username!",
      "input_username": "Please set your own username:",
      "username_empty": "Username cannot be empty.",
      "save_username":  "Save: ENTER",
    },
    "oM": {
      "1": "Username",
      "2": "Mode",
      "3": "Difficulty",
      "4": "DAS",
      "5": "Sounds",
      "6": "Controls",
      "7": "Language",
      "8": "About",
    },
    "Mode": {
      "0": "Practice",
      "1": "Competitive",
      "2": "Increment",
      "3": "Combat",
    },
    "Mode_subinfo": {
      "0": "Speed boost & save scores: OFF",
      "1": "Speed boost & save scores: ON",
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
      "input_delay": "Set a new initial delay value [11-99]:",
      "input_rate":  "Set a new repeat rate value [11-99]:",
    },
    "Sounds": {
      "music": "Music",
      "sfx":   "Sound Effects",
      "on":    "ON",
      "off":   "OFF",
      "hint":  "UP/DOWN select    SPACE toggle    ESC save & exit",
      "toggle": "Toggle: SPACE",
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
      "hint":         "UP/DOWN navigate    SPACE assign/reset    ESC/ENTER save & exit",
      "select_key_hint": "Select key: SPACE",
    },
    "Pause": {
      "title":    "PAUSED",
      "resume":   "RESUME",
      "end_game": "END GAME",
      "new_game": "NEW GAME",
    },
    "intro": {
      "title":         "Quick Tips",
      "controls_line": "Use {left}/{right}/{down} to move, {ccw}/{cw}/{r180} to rotate, {smash} to smash.",
      "close":         "CLOSE",
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
      "points":        "Points:",
      "level":         "Level:",
      "username":      "Username:",
      "pentominoes":   "Difficulty:",
      "mode":          "Mode:",
      "initial_delay": "Initial Delay:",
      "repeat_rate":   "Repeat Rate:",
      "help":          "Help - H",
      "back":          "Back - ESC",
      "music_toggle":  "M - Music",
      "current_language": "Current language:",
      "language_set":     "Language was set: {name}",
      "mode_set":         "Mode was set: {name}",
      "difficulty_set":   "Difficulty was set: {name}",
      "initial_delay_set": "Initial delay was set: {value}",
      "repeat_rate_set":   "Repeat rate was set: {value}",
    },
    "eM": {
      "highscore":      "Highscore",
      "new_highscore":  "New Highscore",
      "enter":          "Press ENTER to go to main menu",
      "esc":            "Press ESC to close",
      "practice_note":  "Practice mode — score not saved",
    },
    "modeSelect": {
      "title": "PLAYING MODE",
    },
    "username_conflict": {
      "line1": "\"{name}\" is already taken.",
      "line2": "Do you want to use it anyway?",
      "yes":   "YES",
      "no":    "NO",
      "set_confirm": "Username was set: {name}",
    },
    "play_as": {
      "question":    "Play as \"{name}\"?",
      "play":        "PLAY",
      "create_user": "CREATE USER",
    },
    "help": {
      "title":      "HELP",
      "close":      "ESC / ENTER  to close",
      "controls":   "CONTROLS",
      "pause_key":  "P / ESC   Pause",
      "music_key":  "M for Music",
      "help_key":   "H for Help",
      "das":        "DAS  (Delayed Auto Shift)",
      "das1":       "Hold a key: it waits, then repeats.",
      "das2":       "Adjust the delay in Options > DAS.",
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
    "splash": {
      "loading": "Loading...",
    },
    "about": {
      "title":        "ABOUT",
      "tagline":      "A pentomino puzzle game - built with Python & Pygame",
      "owner_label":  "Project Owner: Martin",
      "dev_label":    "Developer: Samy",
    },
  },        # english end

  "de": {
    "sM": {
      "01": "SPIEL STARTEN",
      "02": "BESTENLISTE",
      "03": "OPTIONEN",
      "04": "BEENDEN",
      "username_warn":  "Bitte eigenen Benutzernamen setzen!",
      "input_username": "Bitte eigenen Benutzernamen setzen:",
      "username_empty": "Benutzername darf nicht leer sein.",
      "save_username":  "Speichern: ENTER",
    },
    "oM": {
      "1": "Benutzername",
      "2": "Modus",
      "3": "Schwierigkeit",
      "4": "DAS",
      "5": "Klänge",
      "6": "Steuerung",
      "7": "Sprache",
      "8": "Über",
    },
    "Mode": {
      "0": "Übung",
      "1": "Wettbewerb",
      "2": "Ansteigend",
      "3": "Kampf",
    },
    "Mode_subinfo": {
      "0": "Geschwindigkeitsschub & Punkte speichern: AUS",
      "1": "Geschwindigkeitsschub & Punkte speichern: AN",
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
      "input_delay": "Neue Anfangsverzögerung festlegen [11-99]:",
      "input_rate":  "Neue Wiederholrate festlegen [11-99]:",
    },
    "Sounds": {
      "music": "Musik",
      "sfx":   "Soundeffekte",
      "on":    "AN",
      "off":   "AUS",
      "hint":  "HOCH/RUNTER wählen    LEERTASTE umschalten    ESC speichern",
      "toggle": "Umschalten: LEERTASTE",
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
      "select_key_hint": "Taste wählen: LEERTASTE",
    },
    "Pause": {
      "title":    "PAUSE",
      "resume":   "WEITER",
      "end_game": "SPIEL BEENDEN",
      "new_game": "NEUES SPIEL",
    },
    "intro": {
      "title":         "Kurztipps",
      "controls_line": "{left}/{right}/{down} zum Bewegen, {ccw}/{cw}/{r180} zum Drehen, {smash} zum Fallenlassen.",
      "close":         "SCHLIESSEN",
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
      "points":        "Punkte:",
      "level":         "Level:",
      "username":      "Benutzer:",
      "pentominoes":   "Schwierigkeit:",
      "mode":          "Modus:",
      "initial_delay": "Anfangsverz.:",
      "repeat_rate":   "Wiederholrate:",
      "help":          "Hilfe - H",
      "back":          "Zurück - ESC",
      "music_toggle":  "M - Musik",
      "current_language": "Aktuelle Sprache:",
      "language_set":     "Sprache wurde festgelegt: {name}",
      "mode_set":         "Modus wurde festgelegt: {name}",
      "difficulty_set":   "Schwierigkeit wurde festgelegt: {name}",
      "initial_delay_set": "Anfangsverzögerung wurde festgelegt: {value}",
      "repeat_rate_set":   "Wiederholrate wurde festgelegt: {value}",
    },
    "eM": {
      "highscore":      "Bestpunktzahl",
      "new_highscore":  "Neue Bestpunktzahl",
      "enter":          "ENTER drücken für Hauptmenü",
      "esc":            "ESC drücken zum Schliessen",
      "practice_note":  "Übungsmodus — Punkte nicht gespeichert",
    },
    "modeSelect": {
      "title": "SPIELMODUS",
    },
    "username_conflict": {
      "line1": "\"{name}\" ist bereits vergeben.",
      "line2": "Möchtest du diesen Namen verwenden?",
      "yes":   "JA",
      "no":    "NEIN",
      "set_confirm": "Benutzername wurde festgelegt: {name}",
    },
    "play_as": {
      "question":    "Als \"{name}\" spielen?",
      "play":        "SPIELEN",
      "create_user": "NEUEN SPIELER ERSTELLEN",
    },
    "help": {
      "title":      "HILFE",
      "close":      "ESC / ENTER  zum Schliessen",
      "controls":   "STEUERUNG",
      "pause_key":  "P / ESC   Pause",
      "music_key":  "M für Musik",
      "help_key":   "H für Hilfe",
      "das":        "DAS  (Verzögerter Auto-Shift)",
      "das1":       "Taste gehalten: kurze Pause, dann Wiederholung.",
      "das2":       "Einstellbar in Optionen > DAS.",
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
    "splash": {
      "loading": "Lädt...",
    },
    "about": {
      "title":        "ÜBER",
      "tagline":      "Ein Pentomino-Puzzlespiel - entwickelt mit Python & Pygame",
      "owner_label":  "Projektinhaber: Martin",
      "dev_label":    "Entwickler: Samy",
    },
  },        # german end

  "ro": {
    "sM": {
      "01": "START JOC",
      "02": "CLASAMENT",
      "03": "OPŢIUNI",
      "04": "IEŞIRE",
      "username_warn":  "Setează propriul nume de utilizator!",
      "input_username": "Setează propriul nume de utilizator:",
      "username_empty": "Numele nu poate fi gol.",
      "save_username":  "Salvează: ENTER",
    },
    "oM": {
      "1": "Jucător",
      "2": "Mod",
      "3": "Dificultate",
      "4": "DAS",
      "5": "Sunete",
      "6": "Controale",
      "7": "Limbă",
      "8": "Despre",
    },
    "Mode": {
      "0": "Practică",
      "1": "Competitiv",
      "2": "Incrementat",
      "3": "Combat",
    },
    "Mode_subinfo": {
      "0": "Impuls de viteză & salvare scoruri: DEZACTIVAT",
      "1": "Impuls de viteză & salvare scoruri: ACTIVAT",
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
      "input_delay": "Setează o nouă întârziere inițială [11-99]:",
      "input_rate":  "Setează o nouă rată de repetare [11-99]:",
    },
    "Sounds": {
      "music": "Muzică",
      "sfx":   "Efecte sonore",
      "on":    "PORNIT",
      "off":   "OPRIT",
      "hint":  "SUS/JOS selectare    SPAŢIU comutare    ESC salvare",
      "toggle": "Comutare: SPAŢIU",
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
      "select_key_hint": "Selectează tasta: SPAŢIU",
    },
    "Pause": {
      "title":    "PAUZĂ",
      "resume":   "CONTINUĂ",
      "end_game": "SFÂRŞIT JOC",
      "new_game": "JOC NOU",
    },
    "intro": {
      "title":         "Sfaturi rapide",
      "controls_line": "Foloseşte {left}/{right}/{down} pentru mişcare, {ccw}/{cw}/{r180} pentru rotire, {smash} pentru smash.",
      "close":         "ÎNCHIDE",
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
      "points":        "Puncte:",
      "level":         "Nivel:",
      "username":      "Jucător:",
      "pentominoes":   "Dificultate:",
      "mode":          "Mod:",
      "initial_delay": "Întârziere iniţială:",
      "repeat_rate":   "Rata de repetare:",
      "help":          "Ajutor - H",
      "back":          "Înapoi - ESC",
      "music_toggle":  "M - Muzică",
      "current_language": "Limba curentă:",
      "language_set":     "Limba a fost setată: {name}",
      "mode_set":         "Modul a fost setat: {name}",
      "difficulty_set":   "Dificultatea a fost setată: {name}",
      "initial_delay_set": "Întârzierea inițială a fost setată: {value}",
      "repeat_rate_set":   "Rata de repetare a fost setată: {value}",
    },
    "eM": {
      "highscore":      "Scor maxim",
      "new_highscore":  "Scor maxim nou",
      "enter":          "Apasă ENTER pentru meniu principal",
      "esc":            "Apasă ESC pentru a închide",
      "practice_note":  "Mod practică — scor nesalvat",
    },
    "modeSelect": {
      "title": "MOD DE JOC",
    },
    "username_conflict": {
      "line1": "\"{name}\" este deja folosit.",
      "line2": "Vrei să folosesti oricum acest nume?",
      "yes":   "DA",
      "no":    "NU",
      "set_confirm": "Numele de utilizator a fost setat: {name}",
    },
    "play_as": {
      "question":    "Joci ca \"{name}\"?",
      "play":        "JOACĂ",
      "create_user": "CREEAZĂ UTILIZATOR",
    },
    "help": {
      "title":      "AJUTOR",
      "close":      "ESC / ENTER  pentru a închide",
      "controls":   "CONTROALE",
      "pause_key":  "P / ESC   Pauză",
      "music_key":  "M pentru Muzică",
      "help_key":   "H pentru Ajutor",
      "das":        "DAS  (Auto-deplasare amânată)",
      "das1":       "Ţii apăsată tasta: pauză, apoi repetiţie.",
      "das2":       "Ajustabil în Opţiuni > DAS.",
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
    "splash": {
      "loading": "Se încarcă...",
    },
    "about": {
      "title":        "DESPRE",
      "tagline":      "Un joc puzzle cu pentomino - realizat cu Python & Pygame",
      "owner_label":  "Proprietar proiect: Martin",
      "dev_label":    "Dezvoltator: Samy",
    },
  },        # romanian end

}           # iText end

current_lang = "en"

def t(section, key):
    return iText[current_lang][section][key]

def get_font(size):
    return pg.font.Font(LANG_FONTS.get(current_lang, fontRusso), size)

def _set_cursor(cursor_id):
    """Best-effort cursor change — some platforms/drivers don't support custom cursors."""
    try:
        pg.mouse.set_cursor(cursor_id)
    except pg.error:
        pass

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
    footer         = Footer(screen, sw, sh)

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
                    _showConfirmToast(screen, t("game", "language_set").format(name=LANGUAGES[current_lang]))
                    return
                elif event.key == pg.K_ESCAPE:
                    return
                elif event.key == pg.K_h:
                    helpScreen(screen)

        screen.blit(imageSnoozed, (0, 0))

        container_height = sh
        block_height      = (n - 1) * option_spacing   # language buttons only
        first_y           = (container_height - block_height) / 2

        for i, key in enumerate(lang_keys):
            label     = LANGUAGES[key]
            lang_font = pg.font.Font(LANG_FONTS.get(key, fontRusso), FONT_LG)
            if i == selected:
                btn = lang_font.render(label, True, clr.wht)
            else:
                btn = lang_font.render(label, True, (0, 0, 0))
            btn_rect        = btn.get_rect()
            btn_rect.center = (sw // 2, first_y + i * option_spacing)
            if i == selected:
                pg.draw.rect(screen, clr.purple, btn_rect.inflate(24, 12))
            screen.blit(btn, btn_rect)

        modeStr = t("game", "mode")        + " " + t("Mode",  str(dataJS[KEY_MODE]))
        diffStr = t("game", "pentominoes") + " " + t("Pentos", str(dataJS[KEY_NUM_PENTOS]))
        _u      = dataJS[KEY_USERNAME]
        _u_set  = bool(_u and _u != DEFAULT_USERNAME)
        username_line   = (t("game", "username") + " " + _u) if (_u_set and dataJS[KEY_MODE] != 0) else None
        current_lang_str = t("game", "current_language") + " " + LANGUAGES[current_lang]
        footer.draw(modeStr, diffStr, username=username_line,
                    help_str=t("game", "help"), back_str=t("game", "back"), center_str=current_lang_str)

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
KEY_SHOW_INTRO = "show_intro"   # True = show the quick-tips modal before the next game starts

dataJS = {
    0: "Username", 10: DEFAULT_USERNAME,
    1: "Mode", 11: 9,
    2: "Initial Delay[ms]", 12: 33,
    3: "Repeat Rate[ms]", 13: 43,
    4: "competOn", 14: 1,
    "show_intro": True,
}

# set the path for the text file to be saved
file_path_data = os.path.join(os.path.expanduser('~'), 'Pentis', 'data.json')
file_path_keys = os.path.join(os.path.expanduser('~'), 'Pentis', 'keys.json')
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


def inputBox2(screen, imageStart):
    sw, sh = screen.get_size()

    strOut     = t("sM", "input_username")
    font       = get_font(FONT_MD)
    font_err   = get_font(FONT_SM)
    font_hint  = get_font(FONT_SM)
    input_text = ''
    error_msg  = ''
    username   = None
    running    = True
    clock      = pg.time.Clock()

    GAP      = 20
    HINT_GAP = 40

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

        prompt_surf = font.render(strOut, True, (0, 0, 0))
        box_width   = prompt_surf.get_width()
        box_height  = font.get_linesize() * 2 * 0.7

        save_surf = font_hint.render(t("sM", "save_username"), True, (0, 0, 0))
        back_surf = font_hint.render(t("scoreboard", "back"), True, (0, 0, 0))
        hint_row_w = save_surf.get_width() + HINT_GAP + back_surf.get_width()

        hint_h  = max(save_surf.get_height(), back_surf.get_height())
        err_h   = font_err.get_linesize()
        block_height = prompt_surf.get_height() + GAP + box_height + GAP + hint_h + GAP + err_h
        top_y = (sh - block_height) / 2

        prompt_rect = prompt_surf.get_rect(center=(sw // 2, top_y + prompt_surf.get_height() // 2))
        screen.blit(prompt_surf, prompt_rect)

        box_y     = prompt_rect.bottom + GAP
        input_box = pg.Rect(sw // 2 - box_width // 2, box_y, box_width, box_height)
        pg.draw.rect(screen, (255, 255, 255), input_box)
        pg.draw.rect(screen, (0, 0, 0), input_box, 2)

        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, text_surface.get_rect(center=input_box.center))

        hint_y = input_box.bottom + GAP
        hint_x = sw // 2 - hint_row_w // 2
        screen.blit(save_surf, (hint_x, hint_y))
        screen.blit(back_surf, (hint_x + save_surf.get_width() + HINT_GAP, hint_y))

        if error_msg:
            err_surf = font_err.render(error_msg, True, clr.red3)
            screen.blit(err_surf, err_surf.get_rect(center=(sw // 2, hint_y + hint_h + GAP // 2 + err_h // 2)))

        pg.display.update()
        clock.tick(30)

    return username

def inputBoxDAS(selected_option, imageStart):
    screen = pg.display.set_mode((screen_width, screen_height))
    sw, sh = screen_width, screen_height

    strOut    = t("DAS", "input_delay") if selected_option == 0 else t("DAS", "input_rate")
    font      = get_font(FONT_MD)
    font_hint = get_font(FONT_SM)

    GAP      = 20
    HINT_GAP = 40

    input_text = ''

    # Set up the loop variables
    running = True
    clock  = pg.time.Clock()
    footer = Footer(screen, sw, sh)

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Store the user's input when they press enter
                    if input_text.isdigit() and 11 <= int(input_text) <= 99:
                        newValue = input_text
                        dataJS[str(selected_option + 12)] = newValue
                        fileWriteData(dataJS)
                        toast_key = "initial_delay_set" if selected_option == 0 else "repeat_rate_set"
                        _showConfirmToast(screen, t("game", toast_key).format(value=newValue))
                        input_text = ''
                        running = False
                    else:
                        input_text = ''

                elif event.key == pg.K_BACKSPACE:
                    # Remove the last character when the user presses backspace
                    input_text = input_text[:-1]
                elif event.key == pg.K_ESCAPE:
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

        # Draw the screen
        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))

        prompt_surf = font.render(strOut, True, (0, 0, 0))
        box_width   = prompt_surf.get_width()
        box_height  = font.get_linesize() * 2 * 0.7

        save_surf = font_hint.render(t("sM", "save_username"), True, (0, 0, 0))
        back_surf = font_hint.render(t("scoreboard", "back"), True, (0, 0, 0))
        hint_row_w = save_surf.get_width() + HINT_GAP + back_surf.get_width()

        hint_h       = max(save_surf.get_height(), back_surf.get_height())
        block_height = prompt_surf.get_height() + GAP + box_height + GAP + hint_h
        top_y        = (sh - block_height) / 2

        prompt_rect = prompt_surf.get_rect(center=(sw // 2, top_y + prompt_surf.get_height() // 2))
        screen.blit(prompt_surf, prompt_rect)

        box_y     = prompt_rect.bottom + GAP
        input_box = pg.Rect(sw // 2 - box_width // 2, box_y, box_width, box_height)
        pg.draw.rect(screen, (255, 255, 255), input_box)
        pg.draw.rect(screen, (0, 0, 0), input_box, 2)

        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, text_surface.get_rect(center=input_box.center))

        hint_y = input_box.bottom + GAP
        hint_x = sw // 2 - hint_row_w // 2
        screen.blit(save_surf, (hint_x, hint_y))
        screen.blit(back_surf, (hint_x + save_surf.get_width() + HINT_GAP, hint_y))

        footer.draw(back_str=t("game", "back"))

        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)
    return newValue
    
def modeSelectScreen(screen):
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])

    mode_keys      = [0, 1]   # Practice, Competitive
    prev           = dataJS.get(KEY_MODE, 1)
    selected       = mode_keys.index(prev) if prev in mode_keys else 1
    option_spacing = 60
    clock          = pg.time.Clock()
    footer         = Footer(screen, *screen.get_size())

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
                elif event.key == pg.K_h:
                    helpScreen(screen)

        sw, sh = screen.get_size()
        screen.blit(imageSnoozed, (0, 0))

        container_height = sh
        first_y           = (container_height - 2 * option_spacing) / 2

        for i, mode_idx in enumerate(mode_keys):
            label = t("Mode", str(mode_idx))
            if i == selected:
                surf = get_font(FONT_LG).render(label, True, clr.wht)
            else:
                surf = get_font(FONT_LG).render(label, True, clr.blk)
            surf_rect = surf.get_rect(center=(sw // 2, first_y + i * option_spacing))
            if i == selected:
                pg.draw.rect(screen, clr.purple, surf_rect.inflate(24, 12))
            screen.blit(surf, surf_rect)

        subinfo = get_font(FONT_SM).render(t("Mode_subinfo", str(mode_keys[selected])), True, (50, 50, 50))
        screen.blit(subinfo, subinfo.get_rect(center=(sw // 2, first_y + 2 * option_spacing)))

        modeStr = t("game", "mode")        + " " + t("Mode",  str(dataJS[KEY_MODE]))
        diffStr = t("game", "pentominoes") + " " + t("Pentos", str(dataJS[KEY_NUM_PENTOS]))
        _u      = dataJS[KEY_USERNAME]
        _u_set  = bool(_u and _u != DEFAULT_USERNAME)
        username_line = (t("game", "username") + " " + _u) if (_u_set and dataJS[KEY_MODE] != 0) else None
        footer.draw(modeStr, diffStr, username=username_line,
                    help_str=t("game", "help"), back_str=t("game", "back"))

        pg.display.flip()
        clock.tick(60)


def usernameConflictBox(screen, username):
    """Returns True (YES — use anyway) or False (NO — try a different name)."""
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])
    selected = 1   # default highlight NO (safer choice)
    q_font   = get_font(FONT_MD)
    btn_font = get_font(FONT_LG)
    clock    = pg.time.Clock()

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
        screen.fill((0, 0, 0))

        question = q_font.render(
            t("username_conflict", "line1").format(name=username) + " " + t("username_conflict", "line2"),
            True, clr.wht
        )

        box_w = min(int(sw * 0.92), max(int(sw * 0.5), question.get_width() + 80))
        box_h = int(sh * 0.28)
        box_x = (sw - box_w) // 2
        box_y = (sh - box_h) // 2

        pg.draw.rect(screen, (20, 20, 20), (box_x, box_y, box_w, box_h))
        pg.draw.rect(screen, clr.gry3, (box_x, box_y, box_w, box_h), 2)

        screen.blit(question, ((sw - question.get_width()) // 2, box_y + int(box_h * 0.28)))

        for i, label in enumerate((t("username_conflict", "yes"), t("username_conflict", "no"))):
            surf = btn_font.render(label, True, clr.wht if i == selected else clr.gry2)
            btn_x = sw // 2 + (i * 2 - 1) * int(box_w * 0.22) - surf.get_width() // 2
            btn_y = box_y + int(box_h * 0.68)
            rect = surf.get_rect(topleft=(btn_x, btn_y))
            if i == selected:
                pg.draw.rect(screen, clr.purple, rect.inflate(24, 12))
            screen.blit(surf, rect)

        pg.display.flip()
        clock.tick(60)


def playAsExistingUserBox(screen, username):
    """Returns True (PLAY — keep the existing username) or False (CREATE USER)."""
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])
    selected = 0   # default highlight PLAY
    q_font   = get_font(FONT_MD)
    btn_font = get_font(FONT_LG)
    clock    = pg.time.Clock()

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
                    return True

        sw, sh = screen.get_size()
        screen.fill((0, 0, 0))

        question = q_font.render(t("play_as", "question").format(name=username), True, clr.wht)
        btn_labels = (t("play_as", "play"), t("play_as", "create_user"))
        btn_surfs  = [btn_font.render(label, True, clr.wht) for label in btn_labels]

        box_w = min(int(sw * 0.92), max(int(sw * 0.5), question.get_width() + 80,
                                         sum(s.get_width() for s in btn_surfs) + 160))
        box_h = int(sh * 0.28)
        box_x = (sw - box_w) // 2
        box_y = (sh - box_h) // 2

        pg.draw.rect(screen, (20, 20, 20), (box_x, box_y, box_w, box_h))
        pg.draw.rect(screen, clr.gry3, (box_x, box_y, box_w, box_h), 2)

        screen.blit(question, ((sw - question.get_width()) // 2, box_y + int(box_h * 0.28)))

        for i, surf in enumerate(btn_surfs):
            surf = btn_font.render(btn_labels[i], True, clr.wht if i == selected else clr.gry2)
            btn_x = sw // 2 + (i * 2 - 1) * int(box_w * 0.24) - surf.get_width() // 2
            btn_y = box_y + int(box_h * 0.68)
            rect = surf.get_rect(topleft=(btn_x, btn_y))
            if i == selected:
                pg.draw.rect(screen, clr.purple, rect.inflate(24, 12))
            screen.blit(surf, rect)

        pg.display.flip()
        clock.tick(60)


def introTipsModal(screen):
    """First-time / new-username welcome modal with a few quick play tips."""
    clock = pg.time.Clock()
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])

    font_title = get_font(FONT_LG)
    font_body  = get_font(FONT_MD)
    font_btn   = get_font(FONT_MD)

    # Reflects the player's actual (possibly remapped) key bindings, same as helpScreen.
    key_names = {
        "left":  pg.key.name(game_keys["10"]).upper(),
        "right": pg.key.name(game_keys["11"]).upper(),
        "down":  pg.key.name(game_keys["12"]).upper(),
        "ccw":   pg.key.name(game_keys["13"]).upper(),
        "cw":    pg.key.name(game_keys["14"]).upper(),
        "r180":  pg.key.name(game_keys["15"]).upper(),
        "smash": pg.key.name(game_keys["16"]).upper(),
    }

    body_lines = [
        t("intro", "controls_line").format(**key_names),
        t("help", "music_key") + ",   " + t("help", "help_key"),
    ]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_RETURN, pg.K_ESCAPE):
                    return

        sw, sh = screen.get_size()
        screen.fill((0, 0, 0))

        title_surf = font_title.render(t("intro", "title"), True, clr.purple)
        body_surfs = [font_body.render(line, True, clr.wht) for line in body_lines]
        btn_surf   = font_btn.render(t("intro", "close"), True, clr.wht)

        content_w = max([title_surf.get_width()] + [s.get_width() for s in body_surfs] + [btn_surf.get_width()])
        box_w = min(int(sw * 0.92), max(int(sw * 0.5), content_w + 80))

        row_gap    = 44
        top_pad    = 40
        btn_pad    = 72
        btn_h      = btn_surf.get_height() + 12
        box_h      = top_pad + row_gap * (len(body_surfs) + 1) + btn_pad + btn_h
        box_x = (sw - box_w) // 2
        box_y = (sh - box_h) // 2

        pg.draw.rect(screen, (20, 20, 20), (box_x, box_y, box_w, box_h))
        pg.draw.rect(screen, clr.gry3, (box_x, box_y, box_w, box_h), 2)

        y = box_y + top_pad
        screen.blit(title_surf, title_surf.get_rect(center=(sw // 2, y)))
        y += row_gap

        for surf in body_surfs:
            y += row_gap
            screen.blit(surf, surf.get_rect(center=(sw // 2, y)))

        y += btn_pad
        btn_rect = btn_surf.get_rect(center=(sw // 2, y))
        pg.draw.rect(screen, clr.purple, btn_rect.inflate(24, 12))
        screen.blit(btn_surf, btn_rect)

        pg.display.flip()
        clock.tick(60)


def _showConfirmToast(screen, message):
    """Brief purple toast confirming an action was applied — auto-closes after ~1.5s."""
    saved = screen.copy()
    clock = pg.time.Clock()

    font = get_font(FONT_MD)
    surf = font.render(message, True, clr.wht)

    sw, sh = screen.get_size()
    box_w  = min(int(sw * 0.92), max(int(sw * 0.4), surf.get_width() + 80))
    box_h  = int(sh * 0.14)
    box_rect = pg.Rect(0, 0, box_w, box_h)
    box_rect.center = (sw // 2, sh // 2)

    start = pg.time.get_ticks()
    while pg.time.get_ticks() - start < 1500:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

        screen.blit(saved, (0, 0))
        pg.draw.rect(screen, clr.purple, box_rect, border_radius=8)
        screen.blit(surf, surf.get_rect(center=box_rect.center))

        pg.display.flip()
        clock.tick(60)


def promptUsername(screen, original_username):
    """
    Prompts for a username, checking it against existing highscores.
    Loops: prompt username → check conflict → confirm or retry.
    Returns True when a username was accepted, False if the player cancelled (ESC),
    in which case dataJS[KEY_USERNAME] is reverted to original_username.
    """
    while True:
        new_u = inputBox2(screen, imageSnoozed)
        if new_u is None:                       # player pressed ESC
            dataJS[KEY_USERNAME] = original_username
            fileWriteData(dataJS)
            return False

        saved = readHighscoresJS()
        taken = {name for scores in saved.values() for name in scores}

        if new_u in taken:
            if usernameConflictBox(screen, new_u):
                dataJS[KEY_SHOW_INTRO] = True
                fileWriteData(dataJS)
                _showConfirmToast(screen, t("username_conflict", "set_confirm").format(name=new_u))
                return True                     # YES — use the taken name
            # NO — revert and loop back to input
            dataJS[KEY_USERNAME] = original_username
            fileWriteData(dataJS)
        else:
            dataJS[KEY_SHOW_INTRO] = True
            fileWriteData(dataJS)
            _showConfirmToast(screen, t("username_conflict", "set_confirm").format(name=new_u))
            return True                         # fresh name, proceed


def ensureCompetitiveUsername(screen):
    """
    If username is already set, asks whether to keep playing as that user or
    create a new one. Otherwise this is the player's first time setting one,
    so prompt with the same conflict check as Options > Username.
    Returns True when ready to start, False if the player cancelled (ESC).
    """
    _u = dataJS[KEY_USERNAME]
    if _u and _u != DEFAULT_USERNAME:
        if playAsExistingUserBox(screen, _u):
            return True                     # PLAY — keep the existing username
        return promptUsername(screen, _u)   # CREATE USER — set a new one

    return promptUsername(screen, _u)


_HELP_TITLE  = FONT_LG
_HELP_HEAD   = FONT_MD
_HELP_BODY   = FONT_SM
_HELP_SP_HEAD = int(FONT_MD * 1.3)
_HELP_SP_BODY = int(FONT_SM * 1.2)
_HELP_SP_GAP  = int(FONT_XS * 0.6)


def helpScreen(screen):
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])
    help_clock = pg.time.Clock()

    font_title  = get_font(_HELP_TITLE)
    font_head   = get_font(_HELP_HEAD)
    font_body   = get_font(_HELP_BODY)
    footer      = Footer(screen, *screen.get_size())

    # Spacing — more generous to fill full screen height
    H_HEAD = int(FONT_LG * 1.6)
    H_BODY = int(FONT_MD * 1.6)
    H_GAP  = int(FONT_LG * 0.9)

    CLR_HEAD = clr.purple
    CLR_BODY = clr.blk

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                    return

        sw, sh = screen.get_size()
        screen.fill((255, 255, 255))

        col_l = int(sw * 0.26)
        col_r = int(sw * 0.72)
        y0    = int(sh * 0.12)

        # Title
        title_surf = font_title.render(t("help", "title"), True, CLR_HEAD)
        screen.blit(title_surf, title_surf.get_rect(center=(sw // 2, int(sh * 0.06))))

        # ---- LEFT COLUMN: Controls ----
        y = y0
        surf = font_head.render(t("help", "controls"), True, CLR_HEAD)
        screen.blit(surf, surf.get_rect(center=(col_l, y)))
        y += H_HEAD

        for i in range(7):
            action = t("Controls", str(i))
            key    = pg.key.name(game_keys[str(i + 10)])
            surf   = font_body.render(f"{action}:  {key}", True, CLR_BODY)
            screen.blit(surf, surf.get_rect(center=(col_l, y)))
            y += H_BODY

        y += H_GAP

        for key_str in ("pause_key", "music_key", "help_key"):
            surf = font_body.render(t("help", key_str), True, CLR_BODY)
            screen.blit(surf, surf.get_rect(center=(col_l, y)))
            y += H_BODY

        y += H_GAP
        surf = font_head.render(t("help", "das"), True, CLR_HEAD)
        screen.blit(surf, surf.get_rect(center=(col_l, y)))
        y += H_HEAD
        for key_str in ("das1", "das2"):
            surf = font_body.render(t("help", key_str), True, CLR_BODY)
            screen.blit(surf, surf.get_rect(center=(col_l, y)))
            y += H_BODY

        # ---- RIGHT COLUMN: Game info ----
        y = y0

        surf = font_head.render(t("help", "objective"), True, CLR_HEAD)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        for key_str in ("obj1", "obj2"):
            surf = font_body.render(t("help", key_str), True, CLR_BODY)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY
        y += H_GAP

        surf = font_head.render(t("help", "modes"), True, CLR_HEAD)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        for key_str in ("modes_prac", "modes_comp"):
            surf = font_body.render(t("help", key_str), True, CLR_BODY)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY
        y += H_GAP

        surf = font_head.render(t("help", "difficulty"), True, CLR_HEAD)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        diff1 = f"{t('Pentos','9')}: 9     {t('Pentos','11')}: 11"
        diff2 = f"{t('Pentos','12')}: 12   {t('Pentos','13')}: 13"
        for diff_line in (diff1, diff2):
            surf = font_body.render(diff_line, True, CLR_BODY)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY
        y += H_GAP

        surf = font_head.render(t("help", "scoring"), True, CLR_HEAD)
        screen.blit(surf, surf.get_rect(center=(col_r, y)))
        y += H_HEAD
        for key_str in ("score1", "score2"):
            surf = font_body.render(t("help", key_str), True, CLR_BODY)
            screen.blit(surf, surf.get_rect(center=(col_r, y)))
            y += H_BODY

        footer.draw(center_str=t("game", "back"))

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

    def _scores_for_mode(mode_name):
        # Merge: start with hardcoded entries as {name: {score}} dict
        merged = {}
        for entry in hardcoded.get(mode_name, []):
            name = entry['name']
            # Use name as key; if duplicate names exist keep the higher score
            if name not in merged or entry['score'] > merged[name]['score']:
                merged[name] = {'score': entry['score']}

        # Overlay with saved scores (saved score wins if higher)
        mode_scores = highscores.get(mode_name, {})
        for name, data in mode_scores.items():
            if name not in merged or data['score'] > merged[name]['score']:
                merged[name] = {'score': data['score']}

        return sorted(merged.items(), key=lambda item: item[1]['score'], reverse=True)

    # map saved mode → index
    dataMode = int(dataJS[KEY_NUM_PENTOS])
    modeDict = {9: 0, 11: 1, 12: 2, 13: 3}
    current_index = modeDict.get(dataMode, 0)

    font_title  = get_font(FONT_LG)
    font_header = get_font(FONT_MD)
    font_body   = get_font(FONT_MD)
    font_footer = get_font(FONT_SM)

    mode_labels = {
        "Novice":   t("Pentos", "9"),
        "Standard": t("Pentos", "11"),
        "Advanced": t("Pentos", "12"),
        "Pro":      t("Pentos", "13"),
    }

    PAGE_SIZE  = 10
    ROW_GAP    = 28

    clock = pg.time.Clock()
    page  = 0
    focus = "mode"   # "mode" = difficulty tabs have the arrow keys, "page" = pagination does

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_RETURN, pg.K_ESCAPE):
                    return
                elif event.key == pg.K_RIGHT:
                    if focus == "page":
                        page += 1
                    else:
                        current_index = (current_index + 1) % len(modes)
                        page = 0
                elif event.key == pg.K_LEFT:
                    if focus == "page":
                        page -= 1
                    else:
                        current_index = (current_index - 1) % len(modes)
                        page = 0
                elif event.key == pg.K_UP:
                    if focus == "mode":
                        pages_here = max(1, -(-len(_scores_for_mode(modes[current_index])) // PAGE_SIZE))
                        if pages_here > 1:
                            focus = "page"
                elif event.key == pg.K_DOWN:
                    if focus == "page":
                        focus = "mode"

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    page -= 1
                elif event.button == 5:
                    page += 1

        # ================= data =================
        current_mode  = modes[current_index]
        sorted_scores = _scores_for_mode(current_mode)

        screen_width, screen_height = screen.get_size()

        total_pages = max(1, -(-len(sorted_scores) // PAGE_SIZE))  # ceil div
        page = max(0, min(page, total_pages - 1))
        visible = sorted_scores[page * PAGE_SIZE:(page + 1) * PAGE_SIZE]

        # ================= draw =================
        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))

        center_x = screen_width * 0.5
        title_y  = int(screen_height * 0.15)
        header_y = int(screen_height * 0.29)

        title = font_title.render(t("scoreboard", "title"), True, (20, 20, 20))
        screen.blit(title, title.get_rect(center=(center_x, title_y)))

        rank_x  = center_x - 220
        name_x  = center_x - 90
        score_x = center_x + 210

        screen.blit(font_header.render(t("scoreboard", "rank"),   True, (20, 20, 20)), (rank_x, header_y))
        screen.blit(font_header.render(t("scoreboard", "player"), True, (20, 20, 20)), (name_x, header_y))
        screen.blit(font_header.render(t("scoreboard", "score"),  True, (20, 20, 20)), (score_x, header_y))

        row_start_y = header_y + ROW_GAP + 9
        row_height  = ROW_GAP + 6

        if not visible:
            txt = font_body.render(t("scoreboard", "no_scores"), True, (120, 120, 120))
            screen.blit(txt, txt.get_rect(center=(center_x, row_start_y)))
        else:
            for i, (name, data) in enumerate(visible):
                y = row_start_y + i * row_height
                rank = page * PAGE_SIZE + i + 1
                score = data.get('score', 0)

                screen.blit(font_body.render(str(rank), True, (0, 0, 0)), (rank_x, y))
                screen.blit(font_body.render(name,       True, (0, 0, 0)), (name_x, y))
                screen.blit(font_body.render(f"{score:,}", True, (0, 0, 0)), (score_x, y))

        if total_pages > 1:
            pager_y   = row_start_y + PAGE_SIZE * row_height + 20
            pager_txt = f"<   {page + 1} / {total_pages}   >"
            if focus == "page":
                pager = font_footer.render(pager_txt, True, clr.wht)
            else:
                pager = font_footer.render(pager_txt, True, (120, 120, 120))
            pager_rect = pager.get_rect(center=(center_x, pager_y))
            if focus == "page":
                pg.draw.rect(screen, clr.purple, pager_rect.inflate(24, 12))
            screen.blit(pager, pager_rect)

        # Bottom bar: mode tabs + Back, evenly spaced and centered on the page
        bar_y   = screen_height - Footer.BOTTOM_SPACE - font_footer.get_linesize()
        bar_gap = 80

        bar_items = []
        for i, mode in enumerate(modes):
            is_active = (i == current_index)
            label = mode_labels[mode]
            text  = f"[{label}]" if is_active else label
            color = (34, 197, 94) if is_active else (80, 80, 80)
            bar_items.append((text, color))
        bar_items.append((t("scoreboard", "back"), (0, 0, 0)))

        bar_surfaces = [(font_footer.render(text, True, color)) for text, color in bar_items]
        total_width  = sum(surf.get_width() for surf in bar_surfaces) + bar_gap * (len(bar_surfaces) - 1)

        x = center_x - total_width / 2
        for surf in bar_surfaces:
            screen.blit(surf, (x, bar_y))
            x += surf.get_width() + bar_gap

        pg.display.update()
        clock.tick(30)
           
def modeOpts(screen, imageStart):            # Mode Options

    options = [t("Mode", "0"), t("Mode", "1")]      # only available modes; add "2","3" when Increment/Combat ship

    #selected_option = dataJS[KEY_NUM_PENTOS]
    numPents = dataJS[KEY_NUM_PENTOS]
    competOn = dataJS[KEY_MODE]

    # Set up menu variables
    option_spacing = 60
    capturing = False  # A flag to indicate when we're capturing a new key
    running = True
    clock = pg.time.Clock()
    footer = Footer(screen, screen_width, screen_height)
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
                    _showConfirmToast(screen, t("game", "mode_set").format(name=t("Mode", str(competOn))))

                if event.key == pg.K_m:
                    toggleMusic()
                if event.key == pg.K_h:
                    helpScreen(screen)


        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))

        container_height = screen_height
        first_y           = (container_height - 2 * option_spacing) / 2

        # (ONLY (uo-down) Display PURPLE MARKING !!)  menu options
        for i in range(len(options)):
            if i == selected_option:
                # Highlight selected option
                text = get_font(FONT_LG).render(options[i], True, clr.wht)
                text2 = get_font(FONT_SM).render(t("Mode_subinfo", str(i)), False, (50,50,50))
            else:
                text = get_font(FONT_LG).render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, first_y + i * option_spacing)
            if i == selected_option:
                pg.draw.rect(screen, clr.purple, text_rect.inflate(24, 12))
            screen.blit(text, text_rect)

           # SUBMIDDLE INFO
            text_rect2 = text2.get_rect()
            text_rect2.center = ((screen_width) //2, first_y + 2 * option_spacing)
            screen.blit(text2, text_rect2)




        if k <=10:
            k =11

        # Footer info
        modeStr = t("game", "mode")        + " " + t("Mode",  str(competOn))
        diffStr = t("game", "pentominoes") + " " + t("Pentos", str(dataJS[KEY_NUM_PENTOS]))
        _u      = dataJS[KEY_USERNAME]
        _u_set  = bool(_u and _u != DEFAULT_USERNAME)
        username_line = (t("game", "username") + " " + _u) if (_u_set and competOn != 0) else None
        footer.draw(modeStr, diffStr, username=username_line, help_str=t("game", "help"), back_str=t("game", "back"))

        pg.display.flip()
    return numPents, competOn

def _draw_pento_preview(screen, shapes, center_y):
    """Render miniature B&W pentomino shapes centred horizontally at center_y."""
    cell    = 9         # px per grid cell
    gap     = 8         # px gap between shapes
    shape_w = 5 * cell  # each shape occupies a 5×5 box
    sw      = screen.get_width()
    total_w = len(shapes) * shape_w + (len(shapes) - 1) * gap
    start_x = (sw - total_w) // 2

    for i, shape in enumerate(shapes):
        grid = shape[0]            # flat 25-element rotation-0 grid
        ox   = start_x + i * (shape_w + gap)
        oy   = int(center_y) - shape_w // 2
        for idx, val in enumerate(grid):
            if val != 0:
                r = idx // 5
                c = idx % 5
                pg.draw.rect(screen, (30, 30, 30),
                             (ox + c * cell, oy + r * cell, cell - 1, cell - 1))


def pentosOpts(screen, imageStart):      #Pentominoes Options

    options = [t("Pentos", "9"), t("Pentos", "11"), t("Pentos", "12"), t("Pentos", "13")]

    numPents = dataJS[KEY_NUM_PENTOS]
    competOn = dataJS[KEY_MODE]
    option_spacing = 60
    running = True
    clock = pg.time.Clock()
    footer = Footer(screen, screen_width, screen_height)
    selected_option = 0
    j = numPents

    diff_shapes = [
        clsp.Pentominoes(9).selected_pentominoes,   # Novice
        clsp.Pentominoes(11).selected_pentominoes,  # Standard
        clsp.Pentominoes(12).selected_pentominoes,  # Advanced
        clsp.Pentominoes(13).selected_pentominoes,  # Pro
    ]
    

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
                    _showConfirmToast(screen, t("game", "difficulty_set").format(name=t("Pentos", str(numPents))))

                if event.key == pg.K_m:
                    toggleMusic()
                if event.key == pg.K_h:
                    helpScreen(screen)


        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))

        container_height = screen_height
        first_y           = (container_height - 4 * option_spacing) / 2

        # (ONLY Display !!)  menu options
        for i in range(len(options)):
            if i == selected_option:
                text = get_font(FONT_LG).render(options[i], True, clr.wht)
            else:
                text = get_font(FONT_LG).render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, first_y + i * option_spacing)
            if i == selected_option:
                pg.draw.rect(screen, clr.purple, text_rect.inflate(24, 12))
            screen.blit(text, text_rect)

        if j <= 8:
            j = 11

        # SUBMIDDLE INFO — miniature shape preview for hovered difficulty
        _draw_pento_preview(screen, diff_shapes[selected_option], first_y + 4 * option_spacing)

        modeStr = t("game", "mode")        + " " + t("Mode",  str(competOn))
        diffStr = t("game", "pentominoes") + " " + t("Pentos", str(numPents))
        _u      = dataJS[KEY_USERNAME]
        _u_set  = bool(_u and _u != DEFAULT_USERNAME)
        username_line = (t("game", "username") + " " + _u) if (_u_set and competOn != 0) else None
        footer.draw(modeStr, diffStr, username=username_line, help_str=t("game", "help"), back_str=t("game", "back"))

            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    return numPents, competOn

def controlsBox(screen, imageStart):
    font       = get_font(FONT_MD)
    font_hint  = get_font(FONT_SM)

    NUM_ACTIONS  = 7
    RESET_OPTION = 7
    selected_option = 0
    option_spacing  = 40
    capturing       = False
    clock = pg.time.Clock()
    footer = Footer(screen, screen_width, screen_height)

    conflict_msg      = ""
    conflict_timer    = 0
    reset_modal_timer = 0

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
                    if event.key == pg.K_ESCAPE:
                        fileWriteKeys(game_keys)
                        return game_keys
                    elif event.key == pg.K_RETURN:
                        if selected_option == RESET_OPTION:
                            game_keys.update(DEFAULT_KEYS)
                            fileWriteKeys(game_keys)
                            reset_modal_timer = 180
                        else:
                            fileWriteKeys(game_keys)
                            return game_keys
                    elif event.key == pg.K_UP:
                        col, row = divmod(selected_option, 4)
                        selected_option = col * 4 + (row - 1) % 4
                    elif event.key == pg.K_DOWN:
                        col, row = divmod(selected_option, 4)
                        selected_option = col * 4 + (row + 1) % 4
                    elif event.key == pg.K_LEFT:
                        selected_option = selected_option % 4
                    elif event.key == pg.K_RIGHT:
                        selected_option = selected_option % 4 + 4
                    elif event.key == pg.K_SPACE:
                        if selected_option == RESET_OPTION:
                            game_keys.update(DEFAULT_KEYS)
                            fileWriteKeys(game_keys)
                            reset_modal_timer = 180
                        else:
                            capturing = True
                            conflict_msg = ""
                    elif event.key == pg.K_m:
                        toggleMusic()
                    elif event.key == pg.K_h:
                        helpScreen(screen)

        if conflict_timer > 0:
            conflict_timer -= 1
        else:
            conflict_msg = ""

        if reset_modal_timer > 0:
            reset_modal_timer -= 1

        screen.blit(imageStart, (0, 0))

        # Layout: 2 columns, 4 rows each
        # Left col (0–3): Left, Right, Down, R Counter-Clock
        # Right col (4–6 + Reset): R Clockwise, R 180, Smash, Reset Keys
        col1_x    = int(screen_width * 0.28)
        col2_x    = int(screen_width * 0.72)
        row_gap   = 50
        container_height = screen_height
        grid_span = 3 * row_gap
        start_y   = (container_height - grid_span) / 2

        for i in range(NUM_ACTIONS):
            action_name = t("Controls", str(i))
            key_name    = pg.key.name(game_keys[str(i + 10)]).upper()
            label       = f"{action_name}: {key_name}"

            col_x = col1_x if i < 4 else col2_x
            row   = i if i < 4 else i - 4
            y     = start_y + row * row_gap

            if i == selected_option:
                if capturing:
                    label = f"{action_name}: [ {t('Controls', 'press_key')} ]"
                    text = font.render(label, True, clr.wht)
                    highlight_color = clr.red1
                else:
                    text = font.render(label, True, clr.wht)
                    highlight_color = clr.purple
                text_rect = text.get_rect(center=(col_x, y))
                pg.draw.rect(screen, highlight_color, text_rect.inflate(24, 12))
                screen.blit(text, text_rect)
            else:
                text = font.render(label, True, clr.blk)
                screen.blit(text, text.get_rect(center=(col_x, y)))

        # Reset Keys — bottom of right column
        reset_y           = start_y + 3 * row_gap
        is_reset_selected  = (selected_option == RESET_OPTION)
        reset_text = font.render(t("Controls", "reset_btn"), True, clr.wht if is_reset_selected else clr.blk)
        reset_rect = reset_text.get_rect(center=(col2_x, reset_y))
        if is_reset_selected:
            pg.draw.rect(screen, clr.purple, reset_rect.inflate(24, 12))
        screen.blit(reset_text, reset_rect)

        if conflict_msg:
            warn_surf = font_hint.render(conflict_msg, True, clr.red2)
            screen.blit(warn_surf, warn_surf.get_rect(center=(screen_width // 2, start_y + grid_span + 40)))

        modeStr = t("game", "mode")        + " " + t("Mode",  str(dataJS[KEY_MODE]))
        diffStr = t("game", "pentominoes") + " " + t("Pentos", str(dataJS[KEY_NUM_PENTOS]))
        _u      = dataJS[KEY_USERNAME]
        _u_set  = bool(_u and _u != DEFAULT_USERNAME)
        username_line = (t("game", "username") + " " + _u) if (_u_set and dataJS[KEY_MODE] != 0) else None
        footer.draw(modeStr, diffStr, username=username_line,
                    help_str=t("game", "help"), back_str=t("game", "back"),
                    center_str=t("Controls", "select_key_hint"))

        if reset_modal_timer > 0:
            modal_surf = font.render(t("Controls", "reset_done"), True, clr.wht)
            modal_rect = modal_surf.get_rect(center=(screen_width // 2, screen_height // 2))
            pg.draw.rect(screen, clr.purple, modal_rect.inflate(48, 28), border_radius=8)
            screen.blit(modal_surf, modal_rect)

        pg.display.flip()

def soundsBox(screen, imageStart):
    selected = 0
    clock = pg.time.Clock()
    footer = Footer(screen, *screen.get_size())
    row_gap = 60
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
                elif event.key == pg.K_h:
                    helpScreen(screen)

        sw, sh = screen.get_size()
        screen.blit(imageStart, (0, 0))

        font = get_font(FONT_LG)

        container_height = sh
        first_y           = (container_height - row_gap) / 2

        items = [
            (t("Sounds", "music"), dataJS[KEY_MUSIC]),
            (t("Sounds", "sfx"),   dataJS[KEY_SFX]),
        ]

        for i, (label, state) in enumerate(items):
            status = t("Sounds", "on") if state else t("Sounds", "off")
            line = f"{label}:  {status}"
            if i == selected:
                surf = font.render(line, True, clr.wht)
            else:
                surf = font.render(line, True, clr.blk)
            surf_rect = surf.get_rect(center=(sw // 2, first_y + i * row_gap))
            if i == selected:
                pg.draw.rect(screen, clr.purple, surf_rect.inflate(24, 12))
            screen.blit(surf, surf_rect)

        modeStr = t("game", "mode")        + " " + t("Mode",  str(dataJS[KEY_MODE]))
        diffStr = t("game", "pentominoes") + " " + t("Pentos", str(dataJS[KEY_NUM_PENTOS]))
        _u      = dataJS[KEY_USERNAME]
        _u_set  = bool(_u and _u != DEFAULT_USERNAME)
        username_line = (t("game", "username") + " " + _u) if (_u_set and dataJS[KEY_MODE] != 0) else None
        footer.draw(modeStr, diffStr, username=username_line,
                    help_str=t("game", "help"), back_str=t("game", "back"), center_str=t("Sounds", "toggle"))

        pg.display.flip()
        clock.tick(60)


def aboutScreen(screen, imageStart):
    clock = pg.time.Clock()
    pg.event.clear([pg.KEYDOWN, pg.KEYUP])

    font_title   = get_font(FONT_LG)
    font_heading = get_font(FONT_MD)
    font_body    = get_font(FONT_SM)

    GRAY      = (100, 100, 100)
    GAP_SM    = 10
    GAP_LG    = 30
    GAP_TITLE = 70   # gap between the page title and the content below it
    LINK_TEXT = "grapefruit256.itch.io/pentis"
    LINK_URL  = "https://grapefruit256.itch.io/pentis"

    footer    = Footer(screen, *screen.get_size())
    link_rect = pg.Rect(0, 0, 0, 0)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                    _set_cursor(pg.SYSTEM_CURSOR_ARROW)
                    return
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1 and link_rect.collidepoint(event.pos):
                    webbrowser.open(LINK_URL)

        sw, sh = screen.get_size()
        screen.blit(imageStart, (0, 0))

        hovered = link_rect.collidepoint(pg.mouse.get_pos())
        _set_cursor(pg.SYSTEM_CURSOR_HAND if hovered else pg.SYSTEM_CURSOR_ARROW)

        lines = [
            (font_title,   t("about", "title"),      clr.purple, 0),
            (font_heading, "Pentis",                  clr.blk,    GAP_TITLE),
            (font_body,    "v0.9",                    GRAY,       GAP_SM),
            (font_body,    t("about", "tagline"),     GRAY,       GAP_SM),
            (font_heading, "grapefruit256",           clr.blk,    GAP_LG),
            (font_body,    t("about", "owner_label"), GRAY,       GAP_SM),
            (font_body,    t("about", "dev_label"),   GRAY,       GAP_SM),
        ]

        link_surf = font_body.render(LINK_TEXT, True, clr.blue2 if hovered else clr.purple)

        rendered = [(font.render(text, True, color), gap_before) for font, text, color, gap_before in lines]
        rendered.append((link_surf, GAP_LG))
        total_h  = sum(gap_before + surf.get_height() for surf, gap_before in rendered)

        y = (sh - total_h) / 2
        for surf, gap_before in rendered:
            y += gap_before
            rect = surf.get_rect(center=(sw // 2, y + surf.get_height() // 2))
            screen.blit(surf, rect)
            if surf is link_surf:
                link_rect = rect
                if hovered:
                    pg.draw.line(screen, clr.blue2, rect.bottomleft, rect.bottomright, 1)
            y += surf.get_height()

        footer.draw(center_str=t("game", "back"))

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
    font = get_font(FONT_LG)

    DASval = [t("DAS", "1"), t("DAS", "2")]
    dataDAS_len = [2,3]

    # Set up menu variables
    selected_option = 0 # 0 und 1
    option_spacing = 60
    capturing = False  # A flag to indicate when we're capturing a new key
    running = True
    clock = pg.time.Clock()
    footer = Footer(screen, screen_width, screen_height)

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

        container_height = screen_height
        first_y           = (container_height - option_spacing) / 2

        # Display menu options
        for i in range(len(DASval)):            #for num in -  for i in dataDAS_len:

            key = i
            action_key = i + 10
            #key_pair = dasval[(i, 0)], dasval[(i, 1)]
            label = DASval[i]
            value = dataJS[str(i + 12)]
            if i == selected_option:
                text = font.render(f"{label}: {value}", True, clr.wht)
            else:
                text = font.render(f"{label}: {value}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, first_y + i * option_spacing)
            if i == selected_option:
                pg.draw.rect(screen, clr.purple, text_rect.inflate(24, 12))
            screen.blit(text, text_rect)

        footer.draw(back_str=t("game", "back"))

            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    #return current_state


#displayInit = pg.display.get_init

#displaySurface = pg.display.get_surface

pg.quit()

#displayInit = pg.display.get_init

#displaySurface = pg.display.get_surface
