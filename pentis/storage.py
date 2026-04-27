"""Highscores storage module - manages local JSON-based score persistence"""
import os
import json
from pathlib import Path

os.chdir(Path(__file__).parent)

# Create Pentis directory if it doesn't exist
pentis_dir = os.path.join(os.path.expanduser('~'), 'Pentis')
os.makedirs(pentis_dir, exist_ok=True)

file_path_iText = os.path.join(os.path.expanduser('~'), 'Pentis', 'iText.json')
# Create a file path to the highscores.json file
file_path = os.path.join(os.path.expanduser('~'), 'Pentis', 'highscores.json')


def writeJS(data):
    """Write JSON data to iText file"""
    with open(file_path_iText, "w") as datei:
        json.dump(data, datei, indent=2, ensure_ascii=False, separators=(',', ': '))


def readJS(filePath):
    """Read JSON data from file"""
    with open(filePath, "r", encoding="utf-8") as datei:
        return json.load(datei)

def readHighscoresJS():
    """Read all highscores from the local JSON file"""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
    except (json.JSONDecodeError, IOError):
        pass
    return {}


def addHighscoresJS(dataMode, name, score):
    """Add or update a highscore in the local JSON file"""
    # Mode mapping
    modeDict = {
        9: "Novice",
        11: "Standard",
        12: "Advanced",
        13: "Pro"
    }

    if dataMode not in modeDict:
        raise ValueError(f"Invalid mode: {dataMode}. Must be one of {list(modeDict.keys())}")

    mode_name = modeDict[dataMode]
    highscores = readHighscoresJS()

    # Create a mode-specific entry if it doesn't exist
    if mode_name not in highscores:
        highscores[mode_name] = {}

    # Check if the player already exists
    existing_entry = highscores[mode_name].get(name, None)

    if existing_entry:
        if existing_entry['score'] >= score:
            print(f"Score not saved: {name} already has a higher score ({existing_entry['score']})")
            return
        else:
            existing_entry['score'] = score
            print(f"Score updated: {name} = {score}")
    else:
        # Add new entry
        highscores[mode_name][name] = {'score': score}
        print(f"New highscore saved: {name} = {score}")

    # Save the updated highscores
    try:
        with open(file_path, "w") as file:
            json.dump(highscores, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving highscore: {e}")