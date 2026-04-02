

def inputBox():
    # Set up the screen
    screen_width = monitor_size[0] * 0.3            # 320
    screen_height = monitor_size[1] * 0.1          # 240

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Input Username")

    strOut = "Please type your username  (->Enter):"
    # Set up the font
    font = pg.font.Font(None, 32)

    # Set up the text input box
    input_box = pg.Rect(screen_width * 0.1, screen_height * 0.4, 200, 32)
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
                    
                    username = input_text
                    username_path = os.path.join(base_path, "username.txt")
                    fileWrite2(username_path)
                    input_text = ''
                    
                    print("Username changed: " + username)
                    print("Userpath changed: " + username_path)
                    running = False
                elif event.key == pg.K_BACKSPACE:
                    # Remove the last character when the user presses backspace
                    input_text = input_text[:-1]
                else:
                    # Add the character to the input text
                    input_text += event.unicode
        
        # Draw the screen
        screen.fill((255, 255, 255))
        text_surface = font.render(strOut, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.1, screen_height * 0.1))
        pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)
    return username


    
def highscoreBox():
    # Set up the screen
    
    screen_width = monitor_size[0] * 0.5
    screen_height = monitor_size[1] * 0.45
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Show Highscores")
    scores = fiba.getHighscores()

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(None, 45)
    font2 = pg.font.Font(None, 32)
    
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
        #scores = fiba.getHighscores()
        nameTitle = "Name"
        text_surface = font.render(nameTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.2, screen_height * 0.05))
        scoreTitle = "Score"
        text_surface = font.render(scoreTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.7, screen_height * 0.05))
        
        for i in range(len(scores)):
            
            text_surface = font2.render(str(i+1), True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.05, screen_height * 0.15 + screen_height * 0.08*i))
            
            strOut = scores[i]["name"]
            text_surface = font2.render(strOut, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.2, screen_height * 0.15 + screen_height * 0.08*i))

            strOut2 = str(scores[i]["score"])
            text_surface = font2.render(strOut2, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.7, screen_height * 0.15 + screen_height * 0.08*i))    
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)
