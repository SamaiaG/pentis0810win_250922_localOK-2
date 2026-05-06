import pygame as pg
import os
import sys
from dataclasses import dataclass
import random as rnd
import colors as clr
import inoutput as io
from inoutput import toggleMusic, restartMusic

#import firebaseRW as fiba

from utils import START_MENU, END_SCREEN
from utils import abstand, monitor_size, monitor_size90, monitor_size30, screen, screen_width, screen_height, bilder, bilder2, font, clock, ost02 
#from cls_pentos import Pentominoes, num_pentominoes
import optMenu as oM

#print("BoF - game")

#   UserEvent #   speedup

speedup = pg.USEREVENT+2
ue1 = pg.time.set_timer(speedup, 20000) # alle 30 sec(30000) geht speed up

pause = pg.USEREVENT+3
#pg.time.set_timer(pause,)
#print("game-Z27: abstand//monitor_size90[1]", abstand, monitor_size90, screen)

def gameLoop(current_state, bool1, screen, username, score):
    
    speed = 1000     # default 1000
    level = 1
    pentoPoints = 3
    
    #print("game-gameLoop-Z35: abstand//monitor_size90[1]", abstand, monitor_size90, screen)
    #************************EVENTS*******************************************

    #   UserEvent tetrominodown(usereventID)
    tetrominodown = pg.USEREVENT+1      # 1. step
    pg.time.set_timer(tetrominodown, speed) # läuft stoppuhr - alle 500 ms schiesst so ein eveent los -> pen fällt 1 runter


    #grid[333] = 4
    tetrominoes = [
                [0,0,0,0,0,
                1,1,1,1,1,      #1      green l
                0,0,0,0,0,
                0,0,0,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #2    yellow y
                0,2,0,0,0,
                0,2,2,0,0,
                0,0,2,0,0,
                0,0,2,0,0],
                [0,0,0,0,0,     # 3     orange T
                0,3,3,3,0,
                0,0,3,0,0,
                0,0,3,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #4    blue light - stairs
                0,0,0,4,0,
                0,0,4,4,0,
                0,4,4,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,         #5 dark red   L 
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,5,0],
                [0,0,0,0,0,       #6   pink y 2
                0,0,0,6,0,
                0,0,6,6,0,
                0,0,6,0,0,
                0,0,6,0,0],
                [0,0,0,0,0,       #7   #dark blue  p
                0,0,7,7,0,
                0,0,7,7,0,
                0,0,7,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #8  purple L 2
                0,0,8,0,0,         
                0,0,8,0,0,
                0,0,8,0,0,
                0,8,8,0,0],
                [0,0,0,0,0,         #9 blue q
                0,9,9,0,0,
                0,9,9,0,0,
                0,0,9,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #10  red   t
                0,0,0,10,0,
                0,0,10,10,0,
                0,0,0,10,0,
                0,0,0,10,0],
                [0,0,0,0,0,       #11 brown rev t
                0,0,11,0,0,
                0,0,11,11,0,
                0,0,11,0,0,
                0,0,11,0,0],
                [0,0,0,0,0,       #12  big L
                0,12,12,12,0,
                0,12,0,0,0,
                0,12,0,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #13  dark purple u
                0,13,0,13,0,
                0,13,13,13,0,
                0,0,0,0,0,
                0,0,0,0,0]]

    nextPentos = [
                [0,0,0,0,0,
                1,1,1,1,1,      #1      green l
                0,0,0,0,0,
                0,0,0,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #2    yellow y
                0,2,0,0,0,
                0,2,2,0,0,
                0,0,2,0,0,
                0,0,2,0,0],
                [0,0,0,0,0,     # 3     orange T
                0,3,3,3,0,
                0,0,3,0,0,
                0,0,3,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #4    blue light - stairs
                0,0,0,4,0,
                0,0,4,4,0,
                0,4,4,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,         #5 dark red   L 
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,5,0],
                [0,0,0,0,0,       #6   pink y 2
                0,0,0,6,0,
                0,0,6,6,0,
                0,0,6,0,0,
                0,0,6,0,0],
                [0,0,0,0,0,       #7   #dark blue  p
                0,0,7,7,0,
                0,0,7,7,0,
                0,0,7,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #8  purple L 2
                0,0,8,0,0,         
                0,0,8,0,0,
                0,0,8,0,0,
                0,8,8,0,0],
                [0,0,0,0,0,         #9 blue q
                0,9,9,0,0,
                0,9,9,0,0,
                0,0,9,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #10  red   t
                0,0,0,10,0,
                0,0,10,10,0,
                0,0,0,10,0,
                0,0,0,10,0],
                [0,0,0,0,0,       #11 brown rev t
                0,0,11,0,0,
                0,0,11,11,0,
                0,0,11,0,0,
                0,0,11,0,0],
                [0,0,0,0,0,       #12  big L
                0,12,12,12,0,
                0,12,0,0,0,
                0,12,0,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #13  dark purple u
                0,13,0,13,0,
                0,13,13,13,0,
                0,0,0,0,0,
                0,0,0,0,0]]


    @dataclass          #decorator
    class NextTet():
        #Eigenschaften - Position Eintritt - Zeile Spalte
        netet     : list          # ein Tetromino  - übergeben 5x5 Werte in diese Liste
                                # für self Wert müssenals erstes kommen - danach default werte - z und s
        zeile   : int = 1       # oberste zeile
        spalte  : int = 16       # 11 => 4. Spalte
        #bool2lab: bool = True
            
        def show(self):
            #alle Zellen durchgehen bis 199 - Positionsfindung
            #print(self.netet)
            for n, farbe in enumerate(self.netet):
                if farbe > 0:           # nur was zeichnen wenn ein anderer Wert als 0 vorkommt
                    y = (self.zeile  + n // 5) * abstand    # n in Wert umwandeln - und eine zeile/Spalte herausfinden - nicht Spalte weil nur 4x4
                    x = (self.spalte + n % 5) * abstand    # in pixel koord -> mit abstand also quadratblock arbeiten
                    
                    screen.blit(bilder2[farbe], (x,y))      # bilder = blocks 

    @dataclass          #decorator      # self Platzhalter für späteren individuellen Objektnamen
    class Tetromino():
        #Eigenschaften - Position Eintritt - Zeile Spalte
        tet     : list          # ein Tetromino  - übergeben 5x5 Werte in diese Liste
                                # für self Wert müssenals erstes kommen - danach default werte - z und s
        zeile   : int = 0       # oberste zeile
        spalte  : int = 5        # 4. Spalte
        bool2lab: bool = True
        
        
        def show(self):
            #alle Zellen durchgehen bis 199 - Positionsfindung
            
            for n, farbe in enumerate(self.tet):
                if farbe > 0:           # nur was zeichnen wenn ein anderer Wert als 0 vorkommt
                    y = (self.zeile + n // 5) * abstand    # n in Wert umwandeln - und eine zeile/Spalte herausfinden - nicht Spalte weil nur 4x4
                    x = (self.spalte + n % 5) * abstand    # in pixel koord -> mit abstand also quadratblock arbeiten
                    
                    screen.blit(bilder[farbe], (x,y)) # aus liste der Bilder ein Bild herausnehmen
                    
                    #screen.blit(bilder[farbe],(x+150,y))
            # greift nat wieder auf obj variablen zu - > desw self
        
        #zeilen spalten = gesamte Anzahl Zeilen Spalten

        

        def valid(self, z, s): # z s - nicht aktuelle sondern (zu prüfende) zukünftige Position
            i = 0
            if (i < 1):
                current_state = START_MENU      # für Spiel Tests ==> GAME
                #bool1 = True
                i = i + 1
            for n, farbe in enumerate(self.tet): # alle elemente der tetromino liste durchgehen
                if farbe > 0: # (0=sw -> >0 - eine Farbe also tetromino)
                    z1 = z + n // 5 # z1 s1 dürfen nicht über den Rand hinausragen
                    s1 = s + n % 5 # wie sieht wert, der einzelnen Spalten/Zeilen aus, der nicht null ist - diese werte dürfen nciht über scrrenrand rausragen
                    #    >= 20(unten screenout)   li screen   re screen        collision detect -> block - in grid schon eine farbe vorhanden
                    if z1 >= zeilen         or s1 < 0       or s1 >= spalten or grid[z1 * spalten + s1] > 0:        #  - wär ausserhalb screen
                                                                            #grid ist 1D - Stelle inn der Grid an der ein Tetr existiert- z1,s1 geht nicht - 
                        #print("sth alreary there - future Zeile/Spalte:",z, z1,s,s1)
                        
                    
                        if self.zeile <= 0 and s1 >= 0  and s1 < spalten:               # MUSS nciht geknüpft an Tastendruck !?
                            global bool1
                            self.bool2lab = False
                            bool1 = False
                            current_state = END_SCREEN
                            #print("**********self.zeile <= 0:************* ",score)

                            #print("valid 0", self.bool2lab, current_state, bool1, score)               
                            return bool1, score #, current_state


                        
                        return False #, bool1, score, current_state #kann nicht zeichnen weil es schon was gibt oder screen out

            #print("inner valid(): valid 2", self, current_state, bool1, score )
            return True # nichts da - kann reinzeichnen
        #print("after valid() self.bool2labTet", bool2lab)
        def valid2(self, z, s): # z s - nicht aktuelle sondern (zu prüfende) zukünftige Position
            for n, farbe in enumerate(self.tet): # alle elemente der tetromino liste durchgehen
                if farbe > 0: # (0=sw -> >0 - eine Farbe also tetromino)
                    z1 = z + n // 5 # z1 s1 dürfen nicht über den Rand hinausragen
                    s1 = s + n % 5 # wie sieht wert, der einzelnen Spalten/Zeilen aus, der nicht null ist - diese werte dürfen nciht über scrrenrand rausragen
                    #    >= 20(unten screenout)   li screen   re screen        collision detect -> block - in grid schon eine farbe vorhanden
                    if z1 >= zeilen         or s1 < 0       or s1 >= spalten or grid[z1 * spalten + s1] > 0:        #  - wär ausserhalb screen
                                                                            #grid ist 1D - Stelle inn der Grid an der ein Tetr existiert- z1,s1 geht nicht - 
                        #print("sth alreary there - future Zeile/Spalte:",z, z1,s,s1)
                        
                        return False #kann nicht zeichnen weil es schon was gibt oder screen out
                

            return True # nichts da - kann reinzeichnen



        def drop(self, z, s):
            lines_down = 0

            while self.valid2(z + lines_down + 1, s):  # Check if the next position is valid
                lines_down += 1

            return lines_down # auch bool


        def update(self, zoff, soff):      #Zeilen off set (versetzt) - spalten off set - Veränderungspositin(Z/S) - um welchen Wert ändert sich in Zeile /Spalte


            if self.valid(self.zeile + zoff, self.spalte + soff): #   valid check nach dem rotate ->
                self.zeile += zoff
                self.spalte += soff
                #print("inner update()self.spalte:", self.zeile)
                return True # tet konnte bewegt werden
            
            return False # ist unten angekommen - später mit ! update ausgelöst
        
        
    
        def updateFast(self, zoff, soff):
            if self.valid(self.zeile + zoff, self.spalte + soff):
                self.zeile += zoff
                self.spalte += soff
                return True  # tet konnte bewegt werden
            #else:
                #self.zeile = self.valid(self.zeile + zoff, self.spalte + soff)  # Setze die Zeile auf den unteren Rand
            return False  # ist unten angekommen

        
        def rotate(self):   # jede Zelle des tet (Zeilenweise und Spaltenweise) durchgehen - Position verändern
            saveTet = self.tet.copy()   # sichern der bisherigen Position existiert später noch als unverändrt. Ursprungszustand
                                        # ohne Kopie wärs nur eine Referenz/Pointer
            for n, farbe in enumerate(saveTet): #n 0-24
                z = n //5
                s = n % 5
                #new = (4-s)*5+z
                self.tet[(4-s)*5+z] = farbe # verändern an best Pos den Wert
                #print(n, new, farbe)
            if not self.valid(self.zeile, self.spalte):
                self.tet = saveTet.copy() # Ursprungszustand gesichert - wenn nciht valid - quasi kein rotate

        def rotateCW(self):
            saveTet = self.tet.copy()
            for n, farbe in enumerate(saveTet):
                z = n // 5
                s = n % 5
                new = s * 5 + (4 - z)
                self.tet[new] = farbe
                #print(n, new, farbe)
            if not self.valid(self.zeile, self.spalte):
                self.tet = saveTet.copy() # Ursprungszustand gesichert - wenn nciht valid - quasi kein rotate
                #print("self.tet: ", self.tet)  

        def rotate180(self):
            saveTet = self.tet.copy()
            for n, farbe in enumerate(saveTet):
                z = n // 5
                s = n % 5
                new = ((4 - z) * 5) + (4 - s)
                self.tet[new] = farbe
            if not self.valid(self.zeile, self.spalte):
                self.tet = saveTet.copy()




    def objToGrid():
        #print("inner objectToGrid(): ",current_state, bool1, screen, username, score)
        for n, farbe in enumerate(figur.tet): # nicht merh self , weil es ist ja schon die Instanz
            if farbe > 0:
                z = figur.zeile + n // 5    # ZeilenPos der Figur
                s = figur.spalte + n % 5
                grid[z*spalten+s] = farbe # grid bekommt an der jeweiligen Position den Wert der Farbe des Tetrominos



                            
    def fullLines():
        lines = 0
        newLines = 0.0
        for zeile in range(zeilen):
            for spalte in range(spalten):       #wenn eine dieser Spalten eine 0 - kann Zeile nicht voll sein
                if grid[zeile*spalten+spalte] == 0:
                    break
            else:                           # wenn aber alle spalten ok - muss jede spalte einen Wert 0                           
                del grid[zeile*spalten:zeile*spalten+spalten]      #von         bis
                                                                # 1.zeile - 1x10 = index 10 : 1x10+20 = 20
                grid[0:0] = [0]*spalten 
                lines += 1
                if lines == 1:
                    sfxLines01.play()
                elif lines == 2:
                    sfxLines01.play()
                elif lines == 3:
                    sfxLines01.play()
                elif lines == 4:
                    sfxLines01.play()
                elif lines == 5:
                    sfxLines02.play()
        #newLines = lines + 1.3 
           
        return lines, lines**2*100


    def gamePause(current_state):
        loop = 1
        goon = True
        #screen_width, screen_height = screen.get_size()
        pg.draw.rect(screen, clr.blk, (0, 0, screen_width, screen_height))                
        textpause = pg.font.SysFont(io.fontRusso, gamefont).render("Pause", False, (255,255,255), (80,80,80))
        textp_rect = textpause.get_rect()
        textp_rect.center = ((screen_width) //2, screen_height*0.4)
        screen.blit(textpause, textp_rect)
        textpause = pg.font.SysFont(io.fontRusso, gamefont).render("Enter to resume", False, (255,255,255), (0,0,0))
        textp_rect = textpause.get_rect()
        textp_rect.center = ((screen_width) //2, screen_height*0.5)
        screen.blit(textpause, textp_rect)
        textpause = pg.font.SysFont(io.fontRusso, gamefont).render("ESC to quit", False, (255,255,255), (0,0,0))
        textp_rect = textpause.get_rect()
        textp_rect.center = ((screen_width) //2, screen_height*0.6)
        screen.blit(textpause, textp_rect)
        #text_surface = font.render(strOut, True, (0, 0, 0))
        #text_rect = text_surface.get_rect() 
        #text_rect.center = ((screen_width) //2, screen_height*0.6)
        #screen.blit(text_surface, text_rect)        
        

        while loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit(0)
                    if event.key == pg.K_RETURN:
                        loop = 0
                        
                        #print ("gamePause - return - goons 1-3:",goonStart, goon, goonEnd)
                    if event.key == pg.K_p:
                        loop = 0
                        
                        #print ("gamePause - p - goons 1-3:",goonStart, goon, goonEnd)
            pg.display.update()
            clock.tick(60)
        return goon, current_state



#**************************************************************************************************
#********************************************************************************************************
#***********************************************************goon************************************************
#def gameLoop(goon, figur, figurnext, randlist, screen, username):
    #numPentosLab = 7
    #print("Please enter the number of pentominoes you want to play with (only 2-13 possible !)")
    #numPentosLab = int(numPentosLab)  # String in Ganzzahl (Integer) umwandeln
    #print("You set the number of pentominoes to:", numPentosLab)
    #io.dataJS[str(11)] = numPentosLab


    randlist = rnd.sample(range(0,io.dataJS[str(11)]),io.dataJS[str(11)]) # 10 soll = oM.numPentos
    #print("oM.numPentos - start game 433:", io.dataJS[str(11)])

    def randNext(randlist):
        if len(randlist) >= 1: #ggf >=1 !!
            #print("randlist", randlist, len(randlist))
            randint = randlist.pop(0)   #!!!!! und geh dann AUCH in die ==1 Schleife !!!
            #print("Pento", randint)

            if len(randlist) > 1:   # ggf >=1
                preview = randlist[0]
                #print("Preview:", preview)

        if len(randlist) == 1: # wenn nur noch 1 Element in randlist
            preview = randlist[0] # das preview muss irgendwie next randint werden
            #print("preview len2--> len1", preview)
            
        if len(randlist) == 0:
            #randint = preview
            newrandlist = rnd.sample(range(0, io.dataJS[str(11)]), io.dataJS[str(11)]) # soll = cls_pentos num_pentominoes

            #print("randlist == 1 neu list: ", newrandlist, len(newrandlist))  
            preview = newrandlist[0] 
            #print("Preview newradnlist:", preview)         
            randlist = newrandlist
            #print("Preview len 0:")

        return randint, randlist, preview #, randintnext, randlistnext
        
    # (erste) Spielfigur rnd.randrange(11)
    #tetRandom = rnd.randrange(10)

            #class      list
    #print("pre figur 0 and 2:")
    #print("first randlist:", randlist)
    randint = randlist.pop(0)
    #print("first randint:", randint, randlist)

    #global figur, figurnext
    
    figur = Tetromino(tetrominoes[randint]) # obj angelegt mit namen figur - 1. Pentomino
    randint = randlist[0]
    #print("first preview randint:", randint, randlist)
    figurnext = NextTet(nextPentos[randint])        # dreht sich auch wenn figur = fihurenext
    #figurDisplay = NextTet(tetrominoes[2]) 

    
    #global speed
    #current_state = GAME
    #bool1 = True
    score = 0
    level = 1
    pentoPoints = 3

    #abstand = 30        # 1 Block zum Quadrat - Blockbreite = Blockhoehe = abstand
    #abstand = monitor_size[0] // 64
    spalten = 16
    zeilen = 32
    border = 0

    breite = border + abstand * spalten
    hoehe = abstand * zeilen
    grid = [0] * spalten * zeilen

    gamefont = int(abstand * 1.2)
    infoW01 = 0.43
    #infoW02 = 0.63
    infoH01 = 0.6
    infoH02 = 0.66
    infoH03 = 0.7
    infoH04 = 0.74
    infoH05 = 0.78



    #ost02 = 'sound\medinet3.mp3'


#***************************************goon************************************************
    #screen = pg.display.set_mode([breite, hoehe])           # sollte wohl zweiter Screen AUF dem anderen Screen sein
    screen = pg.display.set_mode(monitor_size90)
    #pg.display.set_caption(goonTitle)
    pg.mixer.music.load(ost02)
    #if pg.mixer.music.get_busy():
    #    pg.mixer.music.play(-1,0.0,0)
    #    pg.mixer.music.play()
    toggleMusic()

    if os.name == 'nt':  # Windows

        #sfx01 = pg.mixer.Sound("sound\\blockHit.wav")
        #sfxRot01 = pg.mixer.Sound("sound\\rotate01.mp3")
        #sfxRot02 = pg.mixer.Sound("sound\\rotate02.mp3")
        #sfxRot180 = pg.mixer.Sound("sound\\rotate180.mp3")
        #sfxDown01 = pg.mixer.Sound("sound\\down02.mp3")
        sfxLines01 = pg.mixer.Sound("sound\\lines01.mp3")
        sfxLines02 = pg.mixer.Sound("sound\\lines02.mp3")
        #sfxLines03 = pg.mixer.Sound("sound\\lines03.mp3")
        #sfxLines04 = pg.mixer.Sound("sound\\lines04.mp3")
        #sfxLines05 = pg.mixer.Sound("sound\\lines05.mp3")
        sfxMenu01 = pg.mixer.Sound("sound\\menu01.mp3")
    else:
        #sfx01 = pg.mixer.Sound("sound/blockHit.wav")
        #sfxRot01 = pg.mixer.Sound("sound/rotate01.mp3")
        #sfxRot02 = pg.mixer.Sound("sound/rotate02.mp3")
        #sfxRot180 = pg.mixer.Sound("sound/rotate180.mp3")
        #sfxDown01 = pg.mixer.Sound("sound/down02.mp3")
        sfxLines01 = pg.mixer.Sound("sound/lines01.mp3")
        sfxLines02 = pg.mixer.Sound("sound/lines02.mp3")
        #sfxLines03 = pg.mixer.Sound("sound/lines03.mp3")
        #sfxLines04 = pg.mixer.Sound("sound/lines04.mp3")
        #sfxLines05 = pg.mixer.Sound("sound/lines05.mp3")
        sfxMenu01 = pg.mixer.Sound("sound/menu01.mp3")

    pg.event.wait()
    #repDelay = 120
    #repIntervall = 50

    #print("repeatKey pre GOON: delay, intervall",repDelay,repIntervall)

    pg.key.set_repeat()

    # Set the repeat rates for each key DAS !!!
    #repeat_rate_rl = 90  # milliseconds 70 - smaller->faster
    #initial_delay = 20
    initial_delay = int(io.dataJS[str(12)])
    repeat_rate_rl = int(io.dataJS[str(13)])  # milliseconds 70
    speedOn = io.dataJS[str(14)]    # competon = 1 –> speedOn = 1 -
    #if speedOff == 1:
    #    speedOff = 0
    #else:
    #    speedOff = 1

    #**************************
    repeat_rate_down = 33  # milliseconds - smaller->faster
        
    dropstep = 0

    # Initialize the key states
    key_state_1 = False
    key_state_2 = False
    key_state_3 = False
    key_time_1 = 0
    key_time_2 = 0
    key_time_3 = 0

    
    bool2labTet = figur.bool2lab
    #print("pre while(bool1) in gameloop()", bool2labTet, figur.bool2lab)


    while bool1:
        bool2labTet = figur.bool2lab        # figur instanced at 378
        #print("start in while(bool1) in gameloop()", bool2labTet, figur.bool2lab) # !!Dauerfeuer printed!!
        #print("start while bool1") => wird unendlich ausgegeben -> wenn x quit: geht in main 5 Start Game
        clock.tick(80)      # variable clock soll nur dann die Schleife durchlaufen, wenn best Zeit vergangen ist -> ergibt 20 Bilder/sec
                            # wegen set_timer 500ms ist die framerate 80 egal
        lineScore = 0
        lines = 0

        keys = pg.key.get_pressed()
        #print("keys:",keys)

        # Handle key RIGHT
        if keys[pg.K_RIGHT]:
            # Check if the key is being held down
            if key_state_1: # => WÄRE dann wohl key_repeat_settings[key] !!!!
                # Check if enough time has passed to repeat the action
                # nachdem erste mal SPACE gedrückt -> time1 gespeicherte Startzeit - get-ticks aber schon weiter
                # repRate1 100: geht NUR hier rein wenn laufende UHR(getTicks) - startZeit(Taste gehalten-Zeit) KLEINER als 100 ms 
                # ERGO: gibt alle 100ms ein Key1 repeated aus
                if pg.time.get_ticks() - key_time_1 > repeat_rate_rl:
                    # Repeat the action
                    figur.update(0,1)
                    #print("Key 1 repeated", key_time_1, repeat_rate_rl)
                    key_time_1 = pg.time.get_ticks()
            else: # 1st Step
                # Start the key press - geht erstmal hier rein wenn SPACE pressed - >state1 = True UND time1 = Startzeit wann SPACE gedrückt wurde
                #print("Key 1 pressed", key_time_1, repeat_rate_rl)
                key_state_1 = True
                key_time_1 = pg.time.get_ticks() + initial_delay # Add initial delay

        else:
            # End the key press
            if key_state_1:
                #print("Key 1 released", key_time_1, repeat_rate_rl)
                key_state_1 = False

        # Handle key 2
        if keys[pg.K_LEFT]:
            # Check if the key is being held down
            if key_state_2:
                # Check if enough time has passed to repeat the action
                if pg.time.get_ticks() - key_time_2 > repeat_rate_rl:
                    # Repeat the action
                    figur.update(0,-1)
                    #print("Key 2 repeated", key_time_2, repeat_rate_rl)
                    key_time_2 = pg.time.get_ticks()
            else:
                # Start the key press
                #print("Key 2 pressed", key_time_2, repeat_rate_rl)
                key_state_2 = True
                key_time_2 = pg.time.get_ticks() + initial_delay # Add initial delay

        else:
            # End the key press
            if key_state_2:
                #print("Key 2 released", key_time_2, repeat_rate_rl)
                key_state_2 = False               

        if keys[pg.K_DOWN]:
            # Check if the key is being held down
            if key_state_3:
                # Check if enough time has passed to repeat the action
                if pg.time.get_ticks() - key_time_3 > repeat_rate_down:
                    # Repeat the action
                    figur.update(1,0)
                    #print("Key 2 repeated", key_time_3, repeat_rate_down)
                    key_time_3 = pg.time.get_ticks()
            else:
                # Start the key press
                #print("Key 2 pressed", key_time_3, repeat_rate_down)
                key_state_3 = True
                key_time_3 = pg.time.get_ticks()

        else:
            # End the key press
            if key_state_3:
                #print("Key 2 released", key_time_3, repeat_rate_down)
                key_state_3 = False  

        # EVENT GET
        for event in pg.event.get(): # welche Events liegen momentan an
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                pg.quit()
                sys.exit(0)
               
            if event.type == tetrominodown:     # = USEREVENT1
                if not figur.update(1,0):       # 1 runter // + man kann func auch einf als if-Bedingung verwenden !!!
                                                              # die func WIRD ausgeführt UND dient dann 
                    objToGrid()
                    if bool2labTet == False:
                        bool1 = False
                        current_state = END_SCREEN
                    #print("not figur.update:", bool2labTet, bool1, current_state)
                    #if figur.valid

                    #objToGrid() ursprüngl standart Position !!!!
                    dropstep = dropstep + 1 # Count pentominoes
                    #oneScore = pentoPoints - figur.spalte
                    score += pentoPoints # - figur.spalte
                    lines, lineScore = fullLines()         #rnd.randrange(11)
                    #print("lines number:", lines)
                    score += lineScore
                    level = level + lines                    #+ lines
                        
                    if lines >= 1:
                        print("lineScore:", lineScore)
                        if level >= 1 and level <= 21:
                            speed = speed - (speedOn * 15 * lines)# 3 hoch lines 
                            #print("Level 1-21",speed)
                        elif level >= 22 and level <= 31:
                            speed = speed - (speedOn * 12 * lines)# 3 hoch lines 
                            #print("Level 22-31",speed)
                        elif level >= 32 and level <= 51:
                            speed = speed - (speedOn * 8 * lines)# 3 hoch lines * pracON
                            if speed <=69:
                                speed = 69                
                            #print("Level 32-51",speed) 
                        elif level >= 52 and level <= 71:
                            speed = speed - (speedOn * 6 * lines)# 3 hoch lines ? 
                            if speed <=69:
                                speed = 69
                            #print("Level 52-71",speed)   
                        elif level >= 72 and level <= 101:
                            speed = speed - (speedOn * 5 * lines)# 3 hoch lines ? 
                            if speed <=69:
                                speed = 69
                            print("Level 72-101",speed) 
                        elif level >= 102 and level <= 131:
                            speed = speed - (speedOn * 4 * lines)# 3 hoch lines ? 
                            if speed <=69:
                                speed = 69
                            print("Level 102-131",speed) 
                        elif level >= 132 and level <= 161:
                            speed = speed - (speedOn * 3 * lines)# 3 hoch lines ? 
                            if speed <=69:
                                speed = 69
                            print("Level 132-161",speed)                             
                        else: 
                            speed = speed - (speedOn * 2 * lines)
                            if speed <=69:
                                speed = 69                
                            
                            print("else",speed)

                        pg.time.set_timer(tetrominodown, speed)
                        
                        #print("ds", dropstep, "s:",score, "l:", level, "sp:", speed,"rr:", repeat_rate_rl, "id:",initial_delay)
                    
                    
                    #print("pre randNext:",randint, randlist)
                    #figur = figurnext
                    randint, randlist, randintnext  = randNext(randlist) # , randintnext, randlistnext
                    #print("after randNext:", randlist, "next: ", randint, "next: ",randintnext)
                    #objToGrid() - gab extreme CleanLines- teilweise kommen Lines dazu oder passiert nichts
                    figur = Tetromino(tetrominoes[randint])
                    tetrominoes = nextPentos
                    figurnext = NextTet(nextPentos[randintnext])
                    #print("Tetro: ", Tetromino(tetrominoes[randint]))
                    #print("nextPento: ", NextTet(nextPentos[randintnext]))
                    
            
            if event.type == speedup:           # # = USEREVENT2
                pass
                #speed = int(speed * 1)
                #pg.time.set_timer(tetrominodown, speed)
                #level += 1                                  # zu schnell



            if event.type == pg.KEYDOWN:

                    
                if event.key == io.game_keys[str((10))]:    #left
                    figur.update(0,-1)
                if event.key == io.game_keys[str((11))]:    #right
                    figur.update(0,1)
                if event.key == io.game_keys[str((12))]:    #down
                    if event.type != tetrominodown:         # elif ??!
                        figur.update(1,0)
                if event.key == io.game_keys[str((16))]:    #smash space
                    if event.type != tetrominodown:
                        linesDown = figur.drop(figur.zeile, figur.spalte)
                        figur.update(linesDown, 0)
                        objToGrid()
                        #sfxDown01.play()
                        
               
                                                                      
                #if event.key == pg.K_RIGHT and pg.K_DOWN:

                if event.key == io.game_keys[str((13))] or event.key == pg.K_z or event.key == pg.K_s:
                    figur.rotate() 
                    #sfxRot01.play() 
                if event.key == io.game_keys[str((14))] or event.key == pg.K_d or event.key == pg.K_UP:
                    figur.rotateCW()
                    #sfxRot02.play() 
                if event.key == io.game_keys[str((15))]:
                    figur.rotate180()
                    #sfxRot180.play()   
                #if event.key == pg.K_u:
                #    #speed = speed - 100 
                #    repeat_rate_rl = repeat_rate_rl - 10
                #    print("speed key, repeat_rate_rl up",speed, repeat_rate_rl)                                              
                #if event.key == pg.K_j:
                #    #speed = speed + 100  
                #    repeat_rate_rl = repeat_rate_rl + 10        
                #    print("speed key, repeat_rate_rl down",speed, repeat_rate_rl)                                              
                
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit(0)
                if event.key == pg.K_p:
                    sfxMenu01.play()
                    bool1, current_state = gamePause(current_state)
                    #print ("after game pause - p - goons 1-3:", bool1, current_state)
                if event.key == pg.K_m:
                    toggleMusic()
                    
                #if event.key == pg.K_f:
                #    pg.display.toggle_fullscreen()



        
            
                
        screen.fill((0,0,0))        # Schwarz
        
        figur.show()                # Obj Figur inkl Eigenschaften meths der Klasse
        
        figurnext.show()            #Preview pentominoe
        #schaune nach ob es irgendwas in der grid gibt was = 0 ist
        # n ist Zähler - farbe enthält den Inhalt an der entspr Stelle - brauch dann Position 0-199 - desw enumerate
        for n, farbe in enumerate(grid):
            if farbe > 0:
                # aus lauenden Zahl Zeilen udn Spalten herauszufinden
                x = n % spalten * abstand # nimmt 15 / 10 = 1 rst5 - also 6.Spalte - weil jede Spalte mit einer 0 anfängt - aber brauchen Pixelwerte
                                    # deswegen mit abstand (Block) multipliieren
                y = n // spalten * abstand
                # jew bild wird als Zahl in Farbe auf den screen - wo zeichen ? - x,y

                screen.blit(bilder[farbe],(x,y))
        
        pg.draw.rect(screen, clr.gry0, (breite, 0, hoehe*2, breite ),2)
        pg.draw.rect(screen, clr.gry0, (breite, breite, hoehe*2, breite ),2)
        #textSurface = pg.font.SysFont(io.fontRusso, 20).render(f'{io.dataJS["10"]:}', False, (150,150,150))
        #screen.blit(textSurface,(breite * 0.33, 5)) 
        #print(textSurface.get_width())      automatic font sizes 


        
        textSurface = pg.font.SysFont(io.fontRusso, gamefont).render(f'{score:,}', False, (255,255,255))
        screen.blit(textSurface,(screen_width*infoW01, screen_height*0.32))
        #screen.blit(textSurface,(breite //8 - textSurface.get_width() // 2, 30))
        textSurface = pg.font.SysFont(io.fontRusso, gamefont).render(f'Level: {level:}', False, (150,150,150))
        screen.blit(textSurface,(screen_width*infoW01, screen_height*0.42))
        #*******
        textSurface = pg.font.SysFont(io.fontRusso, 36).render("Username: " + io.dataJS["10"], False, (150,150,150)) 
        screen.blit(textSurface,(screen_width*infoW01, screen_height*infoH01))  
        textSurface = pg.font.SysFont(io.fontRusso, gamefont).render("Pentominoes: " + io.iText["en"]["Pentos"][str((io.dataJS["11"]))], False, (150,150,150))
        screen.blit(textSurface,(screen_width*infoW01, screen_height*infoH02))               
        textSurface = pg.font.SysFont(io.fontRusso, gamefont).render("Mode: " + io.iText["en"]["Mode"][str(io.dataJS["14"])], False, (150,150,150))
        screen.blit(textSurface,(screen_width*infoW01, screen_height*infoH03))           
            

        textSurface = pg.font.SysFont(io.fontRusso, gamefont).render("Initial Delay: " + str(io.dataJS["12"]), False, (150,150,150))
        screen.blit(textSurface,(screen_width*infoW01, screen_height*infoH04))    
        textSurface = pg.font.SysFont(io.fontRusso, gamefont).render("Repeat Rate: " + str(io.dataJS["13"]), False, (150,150,150))
        screen.blit(textSurface,(screen_width*infoW01, screen_height*infoH05)) 

        #print("game-Z811: abstand//monitor_size90[1]", abstand, monitor_size90, screen, screen_width, screen_height )           

        #def show():
            #alle Zellen durchgehen bis 199 - Positionsfindung
            
        #for n, farbe in enumerate(nextPentos[7]):
        #    if farbe >= 0:           # nur was zeichnen wenn ein anderer Wert als 0 vorkommt
        #        #print("n, Farbe", n, farbe)
        #        y = ((screen_height) //2 + n // 5) * 20    # n in Wert umwandeln - und eine zeile/Spalte herausfinden - nicht Spalte weil nur 4x4
        #        x = ((screen_width) //2 + n % 5) * 20    # in pixel koord -> mit abstand also quadratblock arbeiten
        #        
        #        screen.blit(bilder[farbe], ((screen_width) //2, (screen_height) //2)) # aus liste der Bilder ein Bild herausnehmen
        #show()
        #screen.blit(bilder[nextPentos[6]], ((screen_width) //2, (screen_height) //2)) - bilder next pentos vorher auf surface bekommen
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()       # 100/200 mal pro sekunde wird bildschirm durchlaufen - +1 - in 1 Sec 200 Zeilen runter
    io.dataJS[str(13)] = str(repeat_rate_rl)
    #print(io.dataJS)
    io.fileWriteData(io.dataJS)
    
    #print ("last - after game while", current_state, bool1)
    return current_state, score

#print("EoF - game")
