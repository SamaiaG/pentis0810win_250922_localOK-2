import pygame as pg
import os
from pathlib import Path 
from dataclasses import dataclass
import random as rnd


os.chdir(Path(__file__).parent)


#global vars
#       Anzahl    Anzahl
breite, spalten, zeilen = 448, 16, 30
#Blockbreite = Blockhoehe = abstand
abstand = breite // spalten             # // Ganzzahldivision keine floats - Blöcke nebeneinander
#26.6
hoehe = abstand * zeilen
grid = [0] * spalten * zeilen




def game():
    speed = 500
    score = 0
    scorebool = True
    level = 0
    bilder = []
    title = "pentis Ver. 0.5"
    icon = pg.image.load('graphics\\block08.png')
    for n in range(12):
        bilder.append(pg.transform.scale(pg.image.load(f'graphics\\block0{n}.png'),(abstand,abstand)))
        
    pg.init()
    screen = pg.display.set_mode([breite, hoehe])
    pg.display.set_caption(title)
    pg.display.set_icon(icon)
    pg.key.set_repeat(200,150)

    #************************EVENTS*******************************************

    #   UserEvent tetrominodown(usereventID)
    tetrominodown = pg.USEREVENT+1      # 1. step
    pg.time.set_timer(tetrominodown, speed) # läuft stoppuhr - alle 500 ms schiesst so ein eveent los -> pen fällt 1 runter

    #   UserEvent #   speedup

    speedup = pg.USEREVENT+2
    ue1 = pg.time.set_timer(speedup, 20000) # alle 30 sec(30000) geht speed up

    pause = pg.USEREVENT+3
    #pg.time.set_timer(pause,)




    #grid[333] = 4
    tetrominoes = [
                [0,0,0,0,0,
                1,1,1,1,1,
                0,0,0,0,0,
                0,0,0,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #2
                0,2,0,0,0,
                0,2,2,0,0,
                0,0,2,0,0,
                0,0,2,0,0],
                [0,0,0,0,0,
                0,3,3,3,0,
                0,0,3,0,0,
                0,0,3,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #4
                0,0,0,4,0,
                0,0,4,4,0,
                0,4,4,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,5,0],
                [0,0,0,0,0,       #6
                0,0,0,6,0,
                0,0,6,6,0,
                0,0,6,0,0,
                0,0,6,0,0],
                [0,0,0,0,0,       
                0,7,0,0,0,
                0,7,7,0,0,
                0,0,7,7,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #8
                0,0,11,0,0,
                0,0,11,0,0,
                0,0,11,0,0,
                0,11,11,0,0],
                [0,0,0,0,0,
                0,9,9,0,0,
                0,9,9,0,0,
                0,0,9,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #10
                0,0,10,10,0,
                0,0,10,10,0,
                0,0,10,0,0,
                0,0,0,0,0],
                [0,0,0,0,0,       #(8)
                0,0,0,8,0,
                0,0,8,8,0,
                0,0,0,8,0,
                0,0,0,8,0]]

    @dataclass          #decorator
    class NextTet():
        #Eigenschaften - Position Eintritt - Zeile Spalte
        netet     : list          # ein Tetromino  - übergeben 5x5 Werte in diese Liste
                                # für self Wert müssenals erstes kommen - danach default werte - z und s
        zeile   : int = 1       # oberste zeile
        spalte  : int = 11       # 4. Spalte
            
        def show(self):
            #alle Zellen durchgehen bis 199 - Positionsfindung
            
            for n, farbe in enumerate(self.netet):
                if farbe > 0:           # nur was zeichnen wenn ein anderer Wert als 0 vorkommt
                    y = (self.zeile + n // 5) * abstand    # n in Wert umwandeln - und eine zeile/Spalte herausfinden - nicht Spalte weil nur 4x4
                    x = (self.spalte + n % 5) * abstand    # in pixel koord -> mit abstand also quadratblock arbeiten
                    
                    screen.blit(bilder[farbe], (x,y))

    @dataclass          #decorator      # self Platzhalter für späteren individuellen Objektnamen
    class Tetromino():
        #Eigenschaften - Position Eintritt - Zeile Spalte
        tet     : list          # ein Tetromino  - übergeben 5x5 Werte in diese Liste
                                # für self Wert müssenals erstes kommen - danach default werte - z und s
        zeile   : int = 0       # oberste zeile
        spalte  : int = 5       # 4. Spalte
        
        
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
            for n, farbe in enumerate(self.tet): # alle elemente der tetromino liste durchgehen
                if farbe > 0: # (0=sw -> >0 - eine Farbe also tetromino)
                    z1 = z + n // 5 # z1 s1 dürfen nicht über den Rand hinausragen
                    s1 = s + n % 5
                    #    >= 20(unten screenout)   li screen   re screen    kollision detect -> block - in grid schon eine farbe vorhanden
                    if z1 >= zeilen         or s1 < 0       or s1 >= spalten or grid[z1 * spalten + s1] > 0:        #  - wär ausserhalb screen
                                                                            #grid ist 1D - Stelle inn der Grid an der ein Tetr existiert- z1,s1 geht nicht - 
                        #print("sth alreary there - future Zeile/Spalte:",z, z1,s,s1)
                        
                    
                        if self.zeile <= 0:               # MUSS nciht geknüpft an Tastendruck !?
                            print("gameover - self.zeile",self.zeile, "///  z (now pos)", z , "///  z1(next pos)", z1 )
                            global goon
                            goon = False
                            return goon
                        
                        return False #kann nicht zeichnen weil es schon was gibt oder screen out

                                                
                        

            return True # nichts da - kann reinzeichnen
        
        def update(self, zoff, soff):      #Zeilen off set (versetzt) - spalten off set - Veränderungspositin(Z/S) - um welchen Wert ändert sich in Zeile /Spalte
            if self.valid(self.zeile + zoff, self.spalte + soff): #   valid check nach dem rotate ->
                self.zeile += zoff
                self.spalte += soff
                return True # tet konnte bewegt werden
            return False # ist unten angekommen
        
        def rotate(self):   # jede Zelle des tet (Zeilenweise und Spaltenweise) durchgehen - Position verändern
            saveTet = self.tet.copy()   # sichern der bisherigen Position existiert später noch als unverändrt. Ursprungszustand
                                        # ohne Kopie wärs nur eine Referenz/Pointer
            for n, farbe in enumerate(saveTet): #n 0-24
                z = n //5
                s = n % 5
                new = (4-s)*5+z
                self.tet[(4-s)*5+z] = farbe # verändern an best Pos den Wert
                #print(n, new, farbe)
            if not self.valid(self.zeile, self.spalte):
                self.tet = saveTet.copy() # Ursprungszustand gesichert

    def objToGrid():
        
        for n, farbe in enumerate(figur.tet): # nicht merh self , weil es ist ja schon die Instanz
            if farbe > 0:
                z = figur.zeile + n // 5    # ZeilenPos der Figur
                s = figur.spalte + n % 5
                grid[z*spalten+s] = farbe # grid bekommt an der jeweiligen Position den Wert der Farbe des Tetrominos
                            
    def fullLines():
        allLines = 0
        for zeile in range(zeilen):
            for spalte in range(spalten):       #wenn eine dieser Spalten eine 0 - kann Zeile nicht voll sein
                if grid[zeile*spalten+spalte] == 0:
                    break
            else:                           # wenn aber alle spalten ok - muss jede spalte einen Wert 0                           
                del grid[zeile*spalten:zeile*spalten+spalten]      #von         bis
                                                                # 1.zeile - 1x10 = index 10 : 1x10+20 = 20
                grid[0:0] = [0]*spalten 
                allLines += 1
        return allLines**2*100



    randlist = rnd.sample(range(0,11),11)

    def randNext(randlist):

        randint, randintnext = 0, 0
        randlistnext = randlist.copy()              #1
        
        if not randlist:
            randlist = rnd.sample(range(0,11),11)
            randlistnext = randlist.copy()
        else: 
            pass

        randint = randlist.pop(0)                   #2

        if len(randlistnext) <= 1:
            randlist = rnd.sample(range(0,11),11)
            randlistnext.insert(0,randlist.pop(0))                                #3
            print("2 if.1",randlistnext,len(randlistnext))
            randintnext = randlistnext.pop(1)                       #4
            
            print("2 if.2",randlistnext,len(randlistnext))
        else:
            randintnext = randlistnext.pop(1)         #3
            print("2 else",len(randlistnext))        


        return randint, randlist, randintnext, randlistnext
        

    # (erste) Spielfigur rnd.randrange(11)
    tetRandom = rnd.randrange(11)
    
            #class      list
    print("pre figur 0 and 2:")
    figur = Tetromino(tetrominoes[0]) # obj angelegt mit namen figur - 1. Pentomino
    figurnext = NextTet(tetrominoes[2])        # dreht sich auch wenn figur1 die 5 ist
    print("after figur 0 and 2:",figur)
    global goon
    goon = True
    # nur 20 Bilder/sec - nicht 200std
    clock = pg.time.Clock()     #clock von pygame
    while goon:
        clock.tick(80)      # variable clock soll nur dann die Schleife durchlaufen, wenn best Zeit vergangen ist -> ergibt 20 Bilder/sec
                            # wegen set_timer 500ms ist die framerate 80 egal
        for event in pg.event.get(): # welche Events liegen momentan an
            if event.type == pg.QUIT:       # X - event vom Typ pg quit
                print("quit -> goon = false")
                goon = False
                
            if event.type == tetrominodown:     # = USEREVENT1
                if not figur.update(1,0):       # 1 runter 
                    objToGrid()
                    score += 3
                    score += fullLines()         #rnd.randrange(11)
                    if score % 15 == 0:
                            level += 1
                    #print("pre randNext:",randint, randlist, randintnext, randlistnext)
                    randint, randlist, randintnext, randlistnext = randNext(randlist)
                    print("after randNext:", randlist, "next: ", randlistnext, randint, "next: ",randintnext)
                    
                    figur = Tetromino(tetrominoes[randint])
                    figurnext = NextTet(tetrominoes[randintnext])

            
            if event.type == speedup:           # # = USEREVENT2
                speed = int(speed * 0.99)
                #pg.time.set_timer(tetrominodown, speed)
                #level += 1                                  # zu schnell
                
            if event.type == pg.KEYDOWN:        #    
                if event.key == pg.K_LEFT:
                    figur.update(0,-1)
                if event.key == pg.K_RIGHT:
                    figur.update(0,1)
                if event.key == pg.K_DOWN:
                    if event.type != tetrominodown:
                        figur.update(1,0)
                #if event.key == pg.K_RIGHT and pg.K_DOWN:
                    
                if event.key == pg.K_UP:
                    figur.rotate()
                if event.key == pg.K_LCTRL:
                    figur.rotate()
            
        
            
                
        screen.fill((0,0,0))        # füllen mit Schwarz
        figur.show()                # nach dem Schwarzen Hintergrund - Obj Figur mit allen Eogenschaften und meths der Klasse
        
        figurnext.show()            #zeigt nur das erste einmal und verschwindet dann
        #schaune nach ob es irgendwas in der grid gibt was = 0 ist
        # n ist Zähler - farbe enthält den Inhalt an der entspr Stelle - brauch dann Position 0-199 - desw enumerate
        for n, farbe in enumerate(grid):
            if farbe > 0:
                # aus lauenden Zahl Zeilen udn Spalten herauszufinden
                x = n % spalten * abstand # nimmt 15 / 10 = 1 rst5 - also 6.Spalte - weil jede Spalte mit einer 0 anfängt - aber brauchen Pixel werte
                                    # deswegen mit abstand (Block) multipliieren
                y = n // spalten * abstand
                # jew bild wird als Zahl in Farbe auf den screen - wo zeichen ? - x,y
                screen.blit(bilder[farbe],(x,y))
                
        
        textSurface = pg.font.SysFont('OCR A Extended', 23).render(f'{score:,}', False, (255,255,255))
        screen.blit(textSurface,(breite //10 - textSurface.get_width() // 2, 5))
        textSurface = pg.font.SysFont('OCR A Extended', 23).render(f'Level: {level:}', False, (150,150,150))
        screen.blit(textSurface,(breite - textSurface.get_width() -10, 5))
            # pygame malt erst unsichbar im HG - erst nach Vorne (gleichzeitig ein neuer HB screeen) -flip - kein flackern
        pg.display.flip()       # 100/200 mal pro sekunde wird bildschirm durchlaufen - +1 - in 1 Sec 200 Zeilen runter
    pg.quit() # <-> pg.init


def main():
    global goon # wenn nicht global -> programm startet nach abbrechen immer wieder
    goon = True
    while(goon):
        game()    


main()

