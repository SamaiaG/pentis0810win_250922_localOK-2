import csv


# Name der CSV-Datei
filename = "output.csv"


pentoPoints = 3
lineScore = 100
lines = 3

score = 0
level = 1
speed = 1000
nxtLevel = 1
levelUp = 300

repeat_rate_rl = 70  # milliseconds 70
repeat_rate_hdown = 30

initial_delay = 20
dropstep = 0






filename = "output.csv"
# Spaltenüberschriften
fieldnames = ["ds", "s", "l", "sp", "rr", "id"]

# CSV-Datei öffnen und Spaltenüberschriften schreiben
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()


    while score < 33000:
        score += pentoPoints
        #lines, lineScore = fullLines()         #rnd.randrange(11)
        score += lineScore
        level = level + lines                    #+ lines
        #if score >= nxtLevel:
            
        if lines >= 1:
            print("lineScore:", lineScore)
            if level > 5 and level <= 20:
                speed = speed - (15 * lines)
                repeat_rate_rl = 60
                print("level > 5 <= 20",speed)
            elif level > 20 and level <= 30:
                speed = speed - (15 * lines)
                repeat_rate_rl = 50
                print("level kleiner = 30",speed) # speed ca 700 - 400 -> -10?
            elif level > 30 and level <= 40:
                speed = speed - (15 * lines)
                if (repeat_rate_rl > 35):
                    repeat_rate_rl = repeat_rate_rl - 1
                if (initial_delay < 40):
                    initial_delay = initial_delay + 1                            
                print("level kleiner = 40",speed)
            elif level > 40 and level <= 50:
                if (speed > 5):     # speed grenze höher setzen !!
                    speed = speed - (10 * lines)
                if (repeat_rate_rl > 20):
                    repeat_rate_rl = repeat_rate_rl - 1
                if (initial_delay < 57):
                    initial_delay = initial_delay + 1                            
                print("level kleiner = 45",speed)
            elif level > 50:
                if (speed > 4):
                    speed = speed - (5 * lines)
                if (repeat_rate_rl > 11):
                    repeat_rate_rl = repeat_rate_rl - 1
                    
                print("level groesser 50",speed)
            else: 
                speed = speed - 2
                
                print("else",speed, repeat_rate_rl)
            #pg.time.set_timer(tetrominodown, speed)
            nxtLevel = level*levelUp
            #print("ds", dropstep, "s:",score, "l:", level, "sp:", speed,"rr:", repeat_rate_rl, "id:",initial_delay)
            # Daten zum Schreiben in die CSV-Datei
            # Daten zum Schreiben in die CSV-Datei
            data = {
                "ds": dropstep,
                "s": score,
                "l": level,
                "sp": speed,
                "rr": repeat_rate_rl,
                "id": initial_delay
            }

            # Schreibe eine neue Zeile in die CSV-Datei
            writer.writerow(data)



# CSV-Datei öffnen und Daten schreiben


print("Die Daten wurden erfolgreich in die CSV-Datei geschrieben.")
