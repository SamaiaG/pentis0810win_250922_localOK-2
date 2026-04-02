import os 
from pathlib import Path
import inoutput as io
import json
import os
from cryptography.fernet import Fernet 
os.chdir(Path(__file__).parent)


file_path_iText = os.path.join(os.path.expanduser('~'), 'Pentis', 'iText.json')
# Create a file path to the highscores.json file
file_path = os.path.join(os.path.expanduser('~'), 'Pentis', 'highscores.json')

def writeJS(dict): #ex fileWriteJS()
    # Data in eine JSON-Datei schreiben
    with open(file_path_iText, "w") as datei:
        #json.dump(dict, datei)
        json.dump(dict, datei, indent=2, ensure_ascii=False, separators=(',', ': ')) #, newline='\n'

#writeJS(iText)

def readJS(filePath):
    with open(filePath, "r") as datei:        # Vorsicht file_path = path UND die (json)-Datei
    #with open(filePath, "r", encoding="utf-8") as datei:        # Vorsicht file_path = path UND die (json)-Datei
        dataJS = json.load(datei)    
    return dataJS




# Generate a key for encryption (do this once and save the key securely)
# key = Fernet.generate_key()
# print(key.decode())  # Save this key securely
# Generate a key
ENCRYPTION_KEY = Fernet.generate_key()
#ENCRYPTION_KEY = b'your-encryption-key'  # Replace with your actual encryption key
cipher = Fernet(ENCRYPTION_KEY)

def encrypt(data):
    
    return cipher.encrypt(data.encode()).decode()

modeDict = 12
def writeHighscores(game_scores, data_mode):
    file_path_scores = os.path.join(os.path.expanduser('~'), 'Pentis', 'highscores.json')
    # Validate data_mode to ensure it's one of the predefined modes
    #if data_mode not in modeDict:
    #    raise ValueError("Invalid mode; must be one of 9, 11, 12, or 13.")

    # Assign the current scoreboard based on mode
    mode_scores = modeDict[data_mode]

    # Update the scoreboard with new game scores
    mode_scores.update(game_scores)

    # Write the updated scores to the JSON file
    with open(file_path_scores, "w") as file:
        json.dump(mode_scores, file, indent=4)

def readHighscoresJS():
    # Read existing highscores
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                highscores = json.loads(data)
    return highscores

highscores = readHighscoresJS()
def addHighscoresJS(dataMode, name, score):
    modeDict = {
        9: "Novice",
        11: "Standart",
        12: "Advanced",
        13: "Pro"
    }
    

    # Initialize the highscores structure
    #highscores = {}
    
    # Read existing highscores
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                highscores = json.loads(data)

    # Create a mode-specific entry if it doesn't exist
    if modeDict[dataMode] not in highscores:
        highscores[modeDict[dataMode]] = {}

    # Check if the player already exists
    existing_entry = highscores[modeDict[dataMode]].get(name, None)
    print("existing_entry", existing_entry)
    if existing_entry:
        if existing_entry['score'] >= score:
            print(f"{name} is already in the collection with a higher score.")
            return
        else:
            existing_entry['score'] = score  # Update score
            print(f"{name} has been updated with the new score.")
    else:
        # Add new entry
        highscores[modeDict[dataMode]]['name': name] = {'score': score}
        print(f"{name} has been added to the collection.")

    # Encrypt and save the updated highscores
    # Uncomment the following line if you want to encrypt the data before saving:
    # encrypted_data = encrypt(json.dumps(highscores))  # Make sure to implement the encrypt function
    with open(file_path, "w") as datei:
        json.dump(highscores, datei, indent=4)


def addHighscoresJS_2(dataMode, name, score):
    modeDict = {
        9: "pentis0800_novice",
        11: "pentis0722_std",
        12: "pentis0722_L",
        13: "pentis0722_Lu"
    }
    
    file_path = f"{modeDict[dataMode]}_highscores.js"  # Create a file path based on the mode
    file_path = os.path.join(os.path.expanduser('~'), 'Pentis', f"{modeDict[dataMode]}_highscores.json")

    new_entry = {"name": name, "score": score}

    # Read existing highscores
    highscores = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                highscores = json.loads(data)

    # Check if the player already exists
    existing_entry = next((entry for entry in highscores if entry['name'] == name), None)
    if existing_entry:
        if existing_entry['score'] >= score:
            print(f"{name} is already in the collection with a higher score.")
            return
        else:
            existing_entry['score'] = score  # Update score
            print(f"{name} has been updated with the new score.")
    else:
        highscores.append(new_entry)  # Add new entry
        print(f"{name} has been added to the collection.")




    # Encrypt and save the updated highscores
    encrypted_data = encrypt(json.dumps(highscores))
    encrypted_data = highscores

    #with open(file_path, 'w') as file:
        #file.write(encrypted_data)
    with open(file_path, "w") as datei:
        json.dump(encrypted_data, datei)
# Example usage
#addHighscoresJS(11, 'Player1', 1500)