import pygame as pg
#import firebaseRW as fiba
import os, sys
from pathlib import Path

import json

import colors as clr
import cls_pentos as clsp
from storage import highscores, readHighscoresJS


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


imageStart = pg.transform.scale(imageStart, monitor_size90)


iText = {
  "en": {
    "sM": {
      "01": "Start",
      "02": "Username",
      "03": "Scoreboard", #TNM Plan
      "04": "Options",
      "05": "Quit"
    },
    "oM": {
      "1": "Mode",
      "2": "Pentominoes",
      "3": "DAS",
      "4": "Controls",
      "5": "Main Menu"
    },
    "Mode": {
      "0": "Practice'",
      "1": "Competitive'",
      "2": "Increment",
      "3": "Combat",
    }, 
    "Mode_subinfo": {
      "0": "speedup and scoreboard-save OFF",
      "1": "speedup and scoreboard-save ON",
      "2": "not in this release",
      "3": "not in this release",
    },    
    "Pentos": {       # Pentominoes
      "9": "Novice",
      "10": "lab 10",  
      "11": "Standard",
      "12": "Advanced - L",
      "13": "Pro - Lu",
      "14": "Hard",

    }, 
    "DAS": {
      "1": "Initial Delay",
      "2": "Repeat Rate"

    },    
    "Controls": {
      "0": "Left",
      "1": "Right",
      "2": "Down",
      "3": "Rotate CCW",
      "4": "Rotate CW",
      "5": "Rotate 180°",
      "6": "Smash"
      
    },
    "lbl": {        # label
      "1": "Lab 1",
      "2": "Lab 2",
      "3": "Lab 3",
      "4": "Lab 4",
      "5": "lab 5",
      "9": "Novicecomp",
      "10": "lab 10 comp",  
      "11": "Standardcomp",
      "12": "Advanced - Lcomp",
      "13": "Pro - Lucomp",
      "14": "Hardcomp",        
    },

    "Pause": {
      "1": "Pause",
      "2": "Enter to resume",
      "3": "ESC to quit"
    },    

    "eM": {
      "01": "Game started"
    },    
          
    "Game": {
      "01": "Game started"
    }
  },        # english end
}           # iText end



#infoL = DynamicDisplay(screen, screen_width*0.01, screen_height*0.8, 100, 150) #  modeStr, diffStr, usernameStr

# dict-json-sys: 1.dict->json(os-path) 2. start: load json 3. game: save->json
# diese beiden dict sind NUR für den ersten Start - danach vollk. sinnlos (oder wenn username.txt gelöscht wurde !)
                                    # da sie Z 108 dataJS = fileReadData() geladen werden
game_keys = {
    0: "Left", 10: pg.K_LEFT,
    1: "Right", 11: pg.K_RIGHT,
    2: "Down", 12: pg.K_DOWN,
    3: "Rotate CCW", 13: pg.K_y,
    4: "Rotate CW", 14: pg.K_x,
    5: "Rotate 180°", 15: pg.K_a,
    6: "Smash", 16: pg.K_SPACE,
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
    with open(file_path_keys, "r") as datei:
        game_keys = json.load(datei)    
    return game_keys

def fileRead(file_path_keys):
    with open(file_path_keys, "r") as datei:
        dictionary = json.load(datei)    
    return dictionary
#def fileWrite(game_scores): #
#    # Data in eine JSON-Datei schreiben
#    with open(file_path_data, "w") as datei:
#        json.dump(game_scores, datei)



#game_configs
dataJS = fileReadData()     # bei jeden Start werden die Dateien in ~/Pentis eingelesen 
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

    strOut = "Please type your own username  (->Enter):"
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
                running = False
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
                running = False
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
    
def highscoreBox(screen, imageStart):

    # Set up the screen - screen ist der Anzeigebereich dieser Funktion !!
    screen_width = monitor_size[0] * 0.5
    screen_height = monitor_size[1] * 0.45

    lastScoreboard2509_nov = [{'score': 28418, 'name': 'adalaine'}, {'score': 5461, 'name': 'Beatrice Default'}, {'score': 5333, 'name': 'Norbert Noname'}, {'score': 2123, 'name': 'lnx02'}, {'score': 1117, 'name': 'will'}, {'score': 1055, 'name': 'Timati'}, {'score': 124, 'name': 'mol'}, {'score': 90, 'name': 'Streamus'}, {'score': 33, 'name': ''}, {'score': 23, 'name': 'creatos240526'}]
    lastScoreboard2509_std = [{'score': 73171, 'name': 'Hepta'}, {'score': 68977, 'name': 'Mari'}, {'score': 64340, 'name': 'roncli'}, {'score': 59317, 'name': 'Aptiz712'}, {'score': 50099, 'name': 'acephoenix'}, {'score': 48617, 'name': 'Norbert Noname'}, {'score': 47253, 'name': 'hana'}, {'score': 42780, 'name': 'demfruit'}, {'score': 42205, 'name': 'cobra6731'}, {'score': 28923, 'name': 'perplexotic'}]
    lastScoreboard2509_adv = [{'score': 40239, 'name': 'Aptiz712'}, {'score': 26824, 'name': 'pete'}, {'score': 20367, 'name': 'demfruit'}, {'score': 14634, 'name': 'xylo'}, {'score': 9742, 'name': 'Norbert Noname'}, {'score': 7345, 'name': 'C_the_Can'}, {'score': 2843, 'name': 'will'}, {'score': 66, 'name': 'Monteith'}, {'score': 12, 'name': 'Willem Default'}]
    lastScoreboard2509_pro = [{'score': 28594, 'name': 'Aptiz712'}, {'score': 23735, 'name': 'demfruit'}, {'score': 11197, 'name': 'Norbert Noname'}, {'score': 9954, 'name': 'Tytris'}, {'score': 3329, 'name': 'Maestro Apfel'}, {'score': 1998, 'name': 'nji'}, {'score': 1285, 'name': 'Willem Default'}, {'score': 687, 'name': 'pete'}, {'score': 139, 'name': 'Darin'}, {'score': 84, 'name': 'will'}]
    #lastScoreboard2509_adv = 
    highscores = readHighscoresJS()
    #screen = pg.display.set_mode((screen_width, screen_height))
    #pg.display.set_caption("Pentis Scoreboard")
    dataMode = dataJS["11"] #Mode 9Nov 11std 12adv 13pro 
    modeDict = {9: "Novice", 11: "Standart", 12: "Advanced", 13: "Pro"} # 0722 weil die DB für 0722 erstellt wurden   
    scores = modeDict[dataMode]
    print("inner HSBox scores",scores)
    #scores = game_scores
    #scores = highscores["Novice"]
    scores = highscores
    print("inner highscoresBox:scores: ",scores)

    #scores = fiba.getHighscores(dataMode) # to show 1-10 switch line 304 height => 0.32 + datamode (std L Lu) argument
    #scores = fiba.getHighscores20(dataMode)

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(fontRusso, 36) #  "Name Score"
    font2 = pg.font.Font(fontRoboto, 30)
    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
                if event.key == pg.K_ESCAPE:
                    running = False                    
        
        # Draw the screen
        screen.fill((255, 255, 255))
        screen.blit(imageStart, (0, 0))
        
        #pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        
        sumH = 0.9# Summand (Hight nach unten) für scoreboard unter Pentis Title
        print_screen_w = (screen_width)//3
        lineSpace = 0.07
        nameTitle = "Name"
        text_surface = font.render(nameTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.2 + print_screen_w, screen_height * (0.05+sumH)))
        scoreTitle = "Score"
        text_surface = font.render(scoreTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.7 + print_screen_w, screen_height * (0.05+sumH)))
        
    #    for i in range(len(scores)):
    #        
    #        text_surface = font2.render(str(i+1), True, (0, 0, 0))
    #        screen.blit(text_surface, (screen_width * 0.05 + print_screen_w, screen_height * (0.15+sumH) + screen_height * lineSpace*i))
    #        
    #        strOut = scores[i]["name"]
    #        text_surface = font2.render(strOut, True, (0, 0, 0))
    #        screen.blit(text_surface, (screen_width * 0.2 + print_screen_w, screen_height * (0.15+sumH) + screen_height * lineSpace*i))#

    #        strOut2 = str(scores[i]["score"])
    #        text_surface = font2.render(strOut2, True, (0, 0, 0))
    #        screen.blit(text_surface, (screen_width * 0.7 + print_screen_w, screen_height * (0.15+sumH) + screen_height * lineSpace*i))    
        i = 1
        # Iterate through the "Novice" scores
        modeDict[dataMode]

        # Hole die Scores für den aktuellen Modus und sortiere sie nach Score
        
        #for player_name, score_data in scores["Novice"].items():
        
        #for player_name, score_data in scores[modeDict[dataMode]].items():
        sorted_scores = sorted(scores[modeDict[dataMode]].items(), key=lambda item: item[1]["score"], reverse=True)
        # Iteriere über die sortierten Scores
        for i, (name, score_data) in enumerate(sorted_scores):
            # Assign the player name
            strOut = name["name"]
            # Assign the score as a string
            strOut2 = str(score_data["score"])
    #        strOut = scores[i]["name"]
            text_surface = font2.render(strOut, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.2 + print_screen_w, screen_height * (0.15+sumH) + screen_height * lineSpace*i))#

    #        strOut2 = str(scores[i]["score"])
            text_surface = font2.render(strOut2, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.7 + print_screen_w, screen_height * (0.15+sumH) + screen_height * lineSpace*i))    
            i += 1

            
            # Print the results to check
            #print(f"Player: {strOut}, Score: {strOut2}")
        pg.display.update()
        
        # Limit the frame rate
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
                running = False  
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
                running = False  
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
    # Set up the screen
    
    #screen_width = monitor_size[0] #* 0.5
    #screen_height = monitor_size[1] #* 0.45
    #screen = pg.display.set_mode((screen_width, screen_height))
    #pg.display.set_caption("Set Controls")
    

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(fontRusso, 30)
        
    #options = ["Right", "Left", "Down", "Hard Drop", "Rotate"] 
    
    game_keys_len = 7

    selected_option = 0
    # Set up menu variables
    option_spacing = 40
    capturing = False  # A flag to indicate when we're capturing a new key
    running = True
    clock = pg.time.Clock()

    while running:               #bool1 == True
        clock.tick(80)      
        #print("while goonStart")
        
        for event in pg.event.get(): # momentane Events
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                #current_state = END_SCREEN
                running = False  
                
            
            elif event.type == pg.KEYDOWN:        # 

                if event.key == pg.K_ESCAPE:
                    #print("ESC - Highscore:", score)
                    running = False  
                                                        
                if event.key == pg.K_RETURN:
                    #print("Game started:", score)
                    running = False
                elif capturing and event.key != pg.K_RETURN:
                    # Update the selected game key with the new key
                    #game_keys[(selected_option, 0)] = game_keys[(selected_option, 1)]
                    
                    game_keys[str((selected_option+10))] = event.key   # pg.key.name(event.key)
                    #print(selected_option)
                    capturing = False  
                              



                if event.key == pg.K_m:
                    toggleMusic()  #-> ggf eine Ebene höher ins optMenu !?
           
                
        screen.fill((255,255,255))        # füllen mit Schwarz
        screen.blit(imageStart, (0, 0))
        # Display menu options
        #print("len dict:", len(game_keys.items))
        
        for i in range(game_keys_len):
            
            key = i
            action_key = i + 10
            #key_pair = game_keys[i], pg.key.name(game_keys[i+10])
            #key_pair = game_keys[(i, 0)], pg.key.name(int(game_keys[(i, 1)]))
            if i == selected_option:
                # Highlight selected option
                text = font.render(f"{game_keys[str(i)]}:{pg.key.name(game_keys[str(i+10)])}", True, clr.wht, clr.purple)
                #text = font.render(f"{key_pair[0]}: {key_pair[1]}", True, clr.wht, clr.purple)
            else:
                text = font.render(f"{game_keys[str(key)]}:{pg.key.name(game_keys[str(action_key)])}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = ((screen_width) //2, screen_height*0.55 + i * option_spacing)      #  - textSurface_score.get_width()
            screen.blit(text, text_rect) 
        
        textSurface = pg.font.SysFont('OCR A Extended', 23).render("m - music on/off", False, (50,50,50))
        screen.blit(textSurface,(screen_width*0.85, screen_height*0.9))

        
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()
    return game_keys

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
                #current_state = END_SCREEN
                running = False  
                
            
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
                running = False
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
                running = False
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
