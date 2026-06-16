level = 1
speed = 1000
repIntervall = 120
while(level <= 100):
    level = level + 1
    if level <= 10:
        speed = speed - 25
        print("level kleiner = 10",level, speed, repIntervall)
    elif level <= 20:
        speed = speed - 20
        repIntervall = repIntervall - 1 
        print("level kleiner = 20",level, speed, repIntervall)
    elif level <= 30:
        speed = speed - 15
        repIntervall = repIntervall - 2
        print("level kleiner = 30",level, speed, repIntervall)
    elif level <= 40:
        speed = speed - 10
        repIntervall = repIntervall - 2
        print("level kleiner = 40",level, speed, repIntervall)
    elif level <= 45:
        speed = speed - 5
        repIntervall = repIntervall - 2
        print("level kleiner = 45",level, speed, repIntervall)        
    else: 
        speed = speed - 2
        repIntervall = repIntervall - 3
        print("level groesser 45",speed)        
        print("level groesser  40",level, speed, repIntervall)




#print(pentoPoints, score, level, nxtLevel, speed, repIntervall)