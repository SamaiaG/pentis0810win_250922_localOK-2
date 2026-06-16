def func1(a,b):
    a+b


def validLine0(self, z, s): # z s - nicht aktuelle sondern (zu prüfende) zukünftige Position
        for n, farbe in enumerate(self.tet): # alle elemente der tetromino liste durchgehen
            if farbe > 0: # (0=sw -> >0 - eine Farbe also tetromino)
                z1 = z + n // 5 # z1 s1 dürfen nicht über den Rand hinausragen
                s1 = s + n % 5
                #    >= 20(unten screenout)   li screen   re screen    kollision detect -> block - in grid schon eine farbe vorhanden
                
                if z <=1:
                    print("gameover")
                        
                    return False #kann nciht zeichnen weil es schon was gibt oder screen out

        return True # nichts da - kann reinzeichnen