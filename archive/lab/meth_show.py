
from dataclasses import dataclass


spalten = 16
zeilen = 32
abstand = 5
grid = [0] * spalten * zeilen
bilder = []
for n in range(12):
    #bilder.append(pg.transform.scale(pg.image.load(f'graphics\\block0{n}.png'),(abstand,abstand)))
    bilder.append("bild" + str(n))


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
            [0,0,0,0,0,       #10   #dark blue  p
            0,0,10,10,0,
            0,0,10,10,0,
            0,0,10,0,0,
            0,0,0,0,0],
            [0,0,0,0,0,       #11  red   t
            0,0,0,11,0,
            0,0,11,11,0,
            0,0,0,11,0,
            0,0,0,11,0]]


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
                
                print(bilder[farbe], (x,y)) # aus liste der Bilder ein Bild herausnehmen
                
                #screen.blit(bilder[farbe],(x+150,y))
        # greift nat wieder auf obj variablen zu - > desw self

    #zeilen spalten = gesamte Anzahl Zeilen Spalten
tetro01 = Tetromino(tetrominoes[3])
tetro01.show()

print(grid)
print(bilder)