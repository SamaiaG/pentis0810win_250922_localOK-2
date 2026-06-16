import csv




pentoPoints = 3

score = 0
level = 1
speed = 1000
nxtLevel = 1
levelUp = 300

repeat_rate_rl = 70  # milliseconds 70
repeat_rate_hdown = 30

initial_delay = 20
dropstep = 0



lines = 3
lineScore = 933
# 1 - 115 - 2 420 - 3 933 - 4 1650 - 5 2560

filename = "output2.csv"
# Spaltenüberschriften
fieldnames = ["ds", "s", "l", "sp", "rr", "id"]

# CSV-Datei öffnen und Spaltenüberschriften schreiben
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()


    while score < 60000:
        score += pentoPoints
        #lines, lineScore = fullLines()         #rnd.randrange(11)
        score += lineScore
        level = level + lines                    #+ lines
        #if score >= nxtLevel:
            
        if lines >= 1:
            print("lineScore:", lineScore)
            if level >= 1 and level <= 21:

                speed = speed - (15 * lines)# 3 hoch lines 
                repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 50
                print("speed 1000-600",speed)

            elif level >= 22 and level <= 31:

                speed = speed - (12 * lines)# 3 hoch lines 
                repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 40
                print("speed > 5 <= 100",speed)

            elif level >= 32 and level <= 51:
                speed = speed - (8 * lines)# 3 hoch lines 
                if speed <=11:
                    speed = 11                
                if repeat_rate_rl >=6:
                    repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 25
                print("level 31-50",speed) 

            elif level >= 52 and level <= 71:
                speed = speed - (6 * lines)# 3 hoch lines ? 
                if speed <=11:
                    speed = 11
                if repeat_rate_rl >=6:
                    repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 40
                print("speed > 5 <= 100",speed)                           
            
            else: 
                
                speed = speed - (5 * lines)
                if speed <=11:
                    speed = 11                
                if repeat_rate_rl >=6:
                    repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 55
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
