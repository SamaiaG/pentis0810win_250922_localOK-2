import csv




pentoPoints = 3

score = 0
level = 1
speed = 1000
nxtLevel = 1
levelUp = 300

repeat_rate_rl = 100  # milliseconds 70
repeat_rate_hdown = 30

initial_delay = 20
dropstep = 0



lines = 5
lineScore = 2560
# 1 - 115 - 2 420 - 3 933 - 4 1650 - 5 2560

filename = "output2.csv"
# Spaltenüberschriften
fieldnames = ["ds", "s", "l", "sp", "rr", "id"]

# CSV-Datei öffnen und Spaltenüberschriften schreiben
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()


    while score < 40000:
        score += pentoPoints
        #lines, lineScore = fullLines()         #rnd.randrange(11)
        score += lineScore
        level = level + lines                    #+ lines
        #if score >= nxtLevel:
            
        if lines >= 1:
            print("lineScore:", lineScore)
            if speed <= 1000 and speed >= 600:

                speed = speed - (20 * lines)# 3 hoch lines 
                repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 35
                print("level > 5 <= 100",speed)

            elif speed < 600 and speed >= 400:

                speed = speed - (18 * lines)# 3 hoch lines 
                repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 30
                print("level > 5 <= 100",speed)

            elif speed < 400 and speed >= 250:

                speed = speed - (12 * lines)# 3 hoch lines 
                repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 20
                print("level > 5 <= 100",speed) 

            elif speed < 250 and speed >= 50:

                speed = speed - (6 * lines)# 3 hoch lines 
                if speed < 50:
                    speed = 50
                repeat_rate_rl = repeat_rate_rl - (1*lines)
                if repeat_rate_rl < 10:
                    repeat_rate_rl = 10                
                initial_delay = 50      # muss auf 57 hoch
                print("level > 5 <= 100",speed)                           
            
            else: 
                
                repeat_rate_rl = repeat_rate_rl - (1*lines)
                initial_delay = 15
                
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
