import pygame

class DynamicDisplay:
    def __init__(self, screen, x, y, title, size_x, size_y, *args):
    #def __init__(self, screen, x, y, title, size_x, size_y, num_contents, content_str, content_str2 = "default"):
        print("len args", len(args))
        print("args", args) #tuple
        print("*args", *args)
        print("args[x]", args[0]) #tuple
        #print("args[x]", args[1]) #tuple
        #*args fängt alle Positionsparameter ein, die nach den definierten Parametern in der Funktion übergeben werden.
        """
        Initialisiert eine dynamische Anzeige.

        Args:
            screen: Das Pygame-Display, auf dem die Anzeige gezeichnet wird.
            x: Die x-Koordinate der oberen linken Ecke der Anzeige.
            y: Die y-Koordinate der oberen linken Ecke der Anzeige.
            title: Der Titel der Anzeige.
            size_x: Die Breite der Anzeige in Pixeln.
            size_y: Die Höhe der Anzeige in Pixeln.
            num_contents: Die Anzahl der Inhaltstrings.
            content_str: Eine Liste von Strings, die den Inhalt der Anzeige darstellen.
        """

        self.screen = screen
        self.rect = pygame.Rect(x, y, size_x, size_y)
        self.title = title
        self.size_x = size_x
        self.size_y = size_y
        self.args = args
        #self.num_contents = num_contents
        #self.content_str = content_str
        #self.content_str2 = content_str2
        window_size = (0,1)
        window_size = pygame.display.get_window_size()
        font_size = window_size[0]//60
        print(font_size)
        gap_size = window_size[0]//60
        self.gap_size = gap_size
        print(gap_size)

        # Font initialisieren (passende Schriftart und Größe auswählen)
        fontPrototype = "graphics\\Prototype.ttf"
        self.font = pygame.font.Font(fontPrototype, font_size)
        yFactor = len(args)
        
        self.yFactor = yFactor # notwendig damit var als self.var in draw() (und der gesammten Klasse) aufrufbar ist
    def draw_one_info(self, args, length, gap_size):
        #length ist nur Platzhalter car für in dem Fall yFactor -> wird beim AUFRUFEN verwendet !!!
        for int in range (length):
        # content zeichnen
            #print("args[int]", args[int]) #tuple
            inColor = (55, 55, 55)
            title_surface = self.font.render(args[int], True, inColor)
            title_rect = title_surface.get_rect()
            #title_rect.topleft = self.rect.topleft
            title_rect.x = self.rect.x + gap_size 
            title_rect.y = self.rect.y + gap_size * (int+1) #height 
            self.screen.blit(title_surface, title_rect)
            


    def draw(self):
        #Zeichnet die Anzeige auf dem Bildschirm.
                # Hintergrund zeichnen
        #                                                       ,widht,boder_radius                    
        #pygame.draw.rect(self.screen, (255, 255, 255), self.rect,5,4)
         
        self.draw_one_info(self.args, self.yFactor, self.gap_size)
        #self.drawone(self.content_str,2)
        #self.drawone(self.content_str2,3)


        # Inhalt zeichnen - waagerechter string => senkrechte Einzelbuchstaben
"""         y_offset = title_rect.bottom + 10
        for content in self.content_strings:
            content_surface = self.font.render(content, True, (155, 155, 155))
            content_rect = content_surface.get_rect()
            content_rect.x = self.rect.x + 10
            content_rect.y = y_offset
            self.screen.blit(content_surface, content_rect)
            y_offset += content_rect.height + 5 """





