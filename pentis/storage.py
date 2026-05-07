"""Highscores storage module - manages local JSON-based score persistence"""
import os
import json
import platform
from pathlib import Path
from cryptography.fernet import Fernet

os.chdir(Path(__file__).parent)

# Encryption key (Fernet-compatible base64-encoded 32-byte key)
ENCRYPTION_KEY = b'NdXFi88mM5JX3V-XTgnbnHpMY5PwiCBDEI5SpyrPvfA='
cipher = Fernet(ENCRYPTION_KEY)

def encrypt_data(data):
    """Encrypt JSON data"""
    json_str = json.dumps(data, indent=4, ensure_ascii=False)
    encrypted = cipher.encrypt(json_str.encode('utf-8'))
    return encrypted

def decrypt_data(encrypted_data):
    """Decrypt JSON data"""
    try:
        decrypted = cipher.decrypt(encrypted_data)
        return json.loads(decrypted.decode('utf-8'))
    except Exception as e:
        print(f"Error decrypting data: {e}")
        return {}

# Get platform-specific data directory
def get_app_data_dir():
    """Return platform-specific application data directory"""
    system = platform.system()
    
    if system == 'Windows':
        # Windows: C:\Users\<username>\AppData\Local\Pentis
        app_data = os.getenv('LOCALAPPDATA')
        if app_data:
            return os.path.join(app_data, 'Pentis')
        else:
            return os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Pentis')
    elif system == 'Darwin':
        # macOS: ~/Library/Application Support/Pentis
        return os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Pentis')
    else:
        # Linux and others: ~/.local/share/pentis
        return os.path.join(os.path.expanduser('~'), '.local', 'share', 'pentis')

# Create Pentis directory if it doesn't exist
pentis_dir = get_app_data_dir()
os.makedirs(pentis_dir, exist_ok=True)

file_path_iText = os.path.join(pentis_dir, 'iText.json')
# Create a file path to the highscores.json file
file_path = os.path.join(pentis_dir, 'highscores.json')


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
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
            if encrypted_data:
                return decrypt_data(encrypted_data)
    except Exception as e:
        print(f"Error reading highscores: {e}")
        return {}
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
        encrypted_data = encrypt_data(highscores)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
    except Exception as e:
        print(f"Error saving highscore: {e}")