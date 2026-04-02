

if event.key == pg.K_RETURN:
    # Store the user's input when they press enter
    
    username = input_text
    fileWrite(username)
    input_text = ''
    
    print("Username changed: " + username)
    running = False
elif event.key == pg.K_BACKSPACE:
    # Remove the last character when the user presses backspace
    input_text = input_text[:-1]
else:
    # Add the character to the input text
    input_text += event.unicode


# Annahme: input_text ist eine leere Zeichenkette zu Beginn
input_text = ""

# Hier wird überprüft, ob event.unicode eine Ziffer ist
if event.unicode.isdigit():
    # Wenn es eine Ziffer ist, füge sie zum input_text hinzu
    input_text += event.unicode

# Hier kannst du input_text ausgeben, um die aktualisierte Zeichenkette zu überprüfen
print(input_text)


# Annahme: input_text ist eine leere Zeichenkette zu Beginn
input_text = ""

# Hier wird überprüft, ob alle Zeichen in input_text Ziffern sind
if all(char.isdigit() for char in input_text):
    # Hier kannst du mehr Zeichen zu input_text hinzufügen
    input_text += event.unicode
else:
    # Hier könntest du eine Benachrichtigung ausgeben oder etwas anderes tun,
    # wenn ein nicht numerisches Zeichen hinzugefügt wird
    pass

# Hier kannst du input_text ausgeben, um die aktualisierte Zeichenkette zu überprüfen
print(input_text)
