GAME = "start_game"
USERNAME = "Username"
SCOREBOARD = "Scoreboard"
OPTIONS = "Options"
START_MENU = "start_menu"
END_SCREEN = "end_screen"


def valid(self, z, s): # z s - nicht aktuelle sondern (zu prüfende) zukünftige Position
            global bool1, current_state
            i = 0
            farbe = 0
            if (i < 1):
                current_state = START_MENU      # für Spiel Tests ==> GAME
                bool1 = True
                i = i + 1
            for n, farbe in enumerate(self.tet): # alle elemente der tetromino liste durchgehen
                if farbe > 0: # (0=sw -> >0 - eine Farbe also tetromino)
                    z1 = z + n // 5 # z1 s1 dürfen nicht über den Rand hinausragen
                    s1 = s + n % 5 # wie sieht wert, der einzelnen Spalten/Zeilen aus, der nicht null ist - diese werte dürfen nciht über scrrenrand rausragen
                    #    >= 20(unten screenout)   li screen   re screen        collision detect -> block - in grid schon eine farbe vorhanden
                    if z1 >= 3         or s1 < 0:
                                                                            #grid ist 1D - Stelle inn der Grid an der ein Tetr existiert- z1,s1 geht nicht - 
                        #print("sth alreary there - future Zeile/Spalte:",z, z1,s,s1)
                        
                    
                        if self.zeile <= 0 and s1 >= 0  and s1 < 3:               # MUSS nciht geknüpft an Tastendruck !?
                            bool1 = False
                            current_state = END_SCREEN
                            print("**********self.zeile <= 0:************* ",score)

                            print("valid 0", self, current_state, bool1, score)               
                            return bool1, score, current_state

                        
                        #bool1 = False
                        #current_state = END_SCREEN
                        print("inner valid(): valid 1", self, current_state, bool1, score )
                        
                        return False#, bool1, score, current_state #kann nicht zeichnen weil es schon was gibt oder screen out

            print("inner valid(): valid 2", self, current_state, bool1, score )
            return True # nichts da - kann reinzeichnen
