from dataclasses import dataclass


breite, spalten, zeilen = 448, 16, 30
#Blockbreite = Blockhoehe = abstand
abstand = breite // spalten             # // Ganzzahldivision keine floats - Blöcke nebeneinander
#26.6
hoehe = abstand * zeilen


@dataclass          #decorator      # self Platzhalter für späteren individuellen Objektnamen
class Tetromino():
    #Eigenschaften - Position Eintritt - Zeile Spalte
    tet     : list          # ein Tetromino  - übergeben 5x5 Werte in diese Liste
                            # für self Wert müssenals erstes kommen - danach default werte - z und s
    zeile   : int = 0       # oberste zeile
    spalte  : int = 5       # 4. Spalte

    def valid(self, z, s): # z s - nicht aktuelle sondern (zu prüfende) zukünftige Position
            for n, farbe in enumerate(self.tet): # alle elemente der tetromino liste durchgehen
                if farbe > 0: # (0=sw -> >0 - eine Farbe also tetromino)
                    z1 = z + n // 5 # z1 s1 dürfen nicht über den Rand hinausragen
                    s1 = s + n % 5 # wie sieht wert, der einzelnen Spalten/Zeilen aus, der nicht null ist - diese werte dürfen nciht über scrrenrand rausragen
                    #    >= 20(unten screenout)   li screen   re screen        collision detect -> block - in grid schon eine farbe vorhanden
                    if z1 >= zeilen         or s1 < 0       or s1 >= spalten or grid[z1 * spalten + s1] > 0:        #  - wär ausserhalb screen
                                                                            #grid ist 1D - Stelle inn der Grid an der ein Tetr existiert- z1,s1 geht nicht - 
                        #print("sth alreary there - future Zeile/Spalte:",z, z1,s,s1)
                        
                    
                        if self.zeile <= 0 and s1 >= 0  and s1 < spalten:               # MUSS nciht geknüpft an Tastendruck !?
                            print("self.zeile <= 0: ")
                            global goon
                            goon = False
                            return goon #score
                        
                        return False #kann nicht zeichnen weil es schon was gibt oder screen out

                                                
                        

            return True # nichts da - kann reinzeichnen
        

grid = [0] * spalten * zeilen
print(grid)
grid = [1] * spalten * zeilen
print(type(grid))
print(grid)
Tetromino.valid(1,0)
