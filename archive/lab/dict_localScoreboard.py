
import json
import os
file_path = os.path.join(os.path.expanduser('~'), 'Pentis', 'highscores_2.json')
file_path = os.path.join(os.path.expanduser('~'), 'Pentis', 'highscores_2.json')
#load dict from json

lastScoreboard2509_nov = [{'score': 28418, 'name': 'adalaine'}, {'score': 5461, 'name': 'Beatrice Default'}, {'score': 5333, 'name': 'Norbert Noname'}, {'score': 2123, 'name': 'lnx02'}, {'score': 1117, 'name': 'will'}, {'score': 1055, 'name': 'Timati'}, {'score': 124, 'name': 'mol'}, {'score': 90, 'name': 'Streamus'}, {'score': 33, 'name': ''}, {'score': 23, 'name': 'creatos240526'}]
lastScoreboard2509_std = [{'score': 73171, 'name': 'Hepta'}, {'score': 68977, 'name': 'Mari'}, {'score': 64340, 'name': 'roncli'}, {'score': 59317, 'name': 'Aptiz712'}, {'score': 50099, 'name': 'acephoenix'}, {'score': 48617, 'name': 'Norbert Noname'}, {'score': 47253, 'name': 'hana'}, {'score': 42780, 'name': 'demfruit'}, {'score': 42205, 'name': 'cobra6731'}, {'score': 28923, 'name': 'perplexotic'}]
lastScoreboard2509_adv = [{'score': 40239, 'name': 'Aptiz712'}, {'score': 26824, 'name': 'pete'}, {'score': 20367, 'name': 'demfruit'}, {'score': 14634, 'name': 'xylo'}, {'score': 9742, 'name': 'Norbert Noname'}, {'score': 7345, 'name': 'C_the_Can'}, {'score': 2843, 'name': 'will'}, {'score': 66, 'name': 'Monteith'}, {'score': 12, 'name': 'Willem Default'}]
lastScoreboard2509_pro = [{'score': 28594, 'name': 'Aptiz712'}, {'score': 23735, 'name': 'demfruit'}, {'score': 11197, 'name': 'Norbert Noname'}, {'score': 9954, 'name': 'Tytris'}, {'score': 3329, 'name': 'Maestro Apfel'}, {'score': 1998, 'name': 'nji'}, {'score': 1285, 'name': 'Willem Default'}, {'score': 687, 'name': 'pete'}, {'score': 139, 'name': 'Darin'}, {'score': 84, 'name': 'will'}]

def readHighscoresJS():
    # Read existing highscores
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                highscores = json.loads(data)
    return highscores
def writeHighscoresJS(score_list):
    with open(file_path, "w") as file:
        json.dump(score_list, file, indent=4)
#print loaded dict to check keys and values
loaded_HS = readHighscoresJS()
#print specific scoreboard
#print(loaded_HS['pentis0722_L'])

modeDict = {9: 'Novice', 11: 'lastScoreboard2509_std', 12: 'lastScoreboard2509_adv', 13: 'lastScoreboard2509_pro'} # 0722 weil die DB für 0722 erstellt wurden   

#print("loaded_HS[modeDict[9]]",loaded_HS[modeDict[9]])
scoreboard = loaded_HS[modeDict[9]]
# Sort by value
#sorted_scoreboard = dict(sorted(scoreboard.items(), key=lambda item: item[1]['score'], reverse=True))
#print("sorted_scoreboard", sorted_scoreboard)
#strOut = sorted_scoreboard['score']
#print("name", strOut)
scoreboard_keys = list(scoreboard.keys())
scoreboard_values = list(scoreboard.values())
print(scoreboard_keys)
print(scoreboard[scoreboard_keys[0]])
print(scoreboard_values)
print("*****************")
score_list = {
'bob': 56,
'Pat': 23,
'brenda': 43,
'moe': 78
}
#make the keys a list
score_list_keys = list(score_list.keys())
#print the list of the keys
print(score_list_keys)
#print certain key
print(score_list_keys[1])
#print certain key value
print(score_list[score_list_keys[1]])

#writeHighscoresJS(score_list)