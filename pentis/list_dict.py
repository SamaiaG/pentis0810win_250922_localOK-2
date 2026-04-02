
import pygame as pg
import json
import os
from pathlib import Path
os.chdir(Path(__file__).parent)


# Pfad mit os.chdir(Path(__file__).parent)

# Pad ohne os.chdir(Path(__file__).parent)
# in der 

dataJS = {
    0: "Username", 10: 10, # erstmal einf nicht verwenden - am Ende switchen
    1: "Mode", 11: 11,
    2: "Initial Delay[ms]", 12: 30,
    3: "Repeat Rate[ms]", 13: 55,
}
dataJS[11] = 43
print(dataJS[11]) #44

loaded_dict = {"0": "Lef", "10": 1073741904, "1": "Right", "11": 1073741903}

for i in range(7):
    key1 = str(i) #!!!!!! in string umwandeln
    key2 = str(i + 10)
    
    value1 = loaded_dict.get(key1, "N/A")
    value2 = loaded_dict.get(key2, "N/A")
    
    print(f"{value1}\t {value2}")
    #print(f"Group {i}: {value1}, {value2}")


# Ein Dictionary mit numerischem Schlüssel
my_dict = {0: "Lef", 10: 1073741904, 1: "Right", 11: 1073741903}

# In eine JSON-Datei schreiben
with open("example.json", "w") as file:
    json.dump(my_dict, file)

# Aus der JSON-Datei lesen
with open("example.json", "r") as file:
    loaded_dict = json.load(file)

for key, value in loaded_dict.items():
    int_key = int(key) #!!!!!!
    # Hier kannst du int_key und value verwenden
    print(f"Key: {int_key}, Value: {value}")


# Der geladene Dictionary hat wieder einen numerischen Schlüssel

game_keys = {
    0: "Lef", 10: pg.K_LEFT,
    1: "Right", 11: pg.K_RIGHT,
}



#print(game_keys[10]) 
def fileWriteJS(game_keys):
    # Data in eine JSON-Datei schreiben
    with open("data_withOSP.json", "w") as datei:
        json.dump(game_keys, datei)


def fileReadJS():
    with open("data_withOSP.json", "r") as datei:
        game_keys = json.load(datei)    
    return game_keys


def jsonRange(game_keys2):
    game_keys_len = 7
    for i in range(game_keys_len):
        print(game_keys2[int(i)])
        key_pair = game_keys2[int(i)], pg.key.name(game_keys2[int(i)+10])
        print(key_pair)


#fileWriteJS(game_keys)
#print(game_keys)
game_keys2 = fileReadJS()
#print(game_keys2)    
jsonRange(game_keys2)




