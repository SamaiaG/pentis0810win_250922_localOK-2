
from dataclasses import dataclass
#import pygame as pg
import random as rnd
import os
from pathlib import Path 
import pentis as ps
os.chdir(Path(__file__).parent)


#global vars
#       Anzahl    Anzahl
breite, spalten, zeilen = 448, 16, 30
#Blockbreite = Blockhoehe = abstand
abstand = breite // spalten             # // Ganzzahldivision keine floats - Blöcke nebeneinander
#26.6
hoehe = abstand * zeilen
grid = [0] * spalten * zeilen
bilder = []

for n in range(12):
    bilder.append(ps.pg.transform.scale(ps.pg.image.load(f'graphics\\block0{n}.png'),(abstand,abstand)))

score = 0
scorebool = True
level = 0
title = "pentis Ver. 0.5"
icon = ps.pg.image.load('graphics\\block08.png')


    
ps.pg.init()
screen = ps.pg.display.set_mode([breite, hoehe])
ps.pg.display.set_caption(title)
ps.pg.display.set_icon(icon)
ps.pg.key.set_repeat(200,150)

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
                    print("sth alreary there - future Zeile/Spalte:",z, z1,s,s1)
                    
                
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
    
    for n, farbe in enumerate(ps.figur.tet): # nicht merh self , weil es ist ja schon die Instanz
        if farbe > 0:
            z = ps.figur.zeile + n // 5    # ZeilenPos der Figur
            s = ps.figur.spalte + n % 5
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

# (erste) Spielfigur rnd.randrange(11)
tetRandom = rnd.randrange(11)
tetRandom2 = tetRandom
