score = 27
level = 1
pentoPoints = 3
nxtLevel = 200
levelUp = 200
speed = 900
""" score += 3*level
#score += fullLines()         #rnd.randrange(11)
if score % 15 == 0:
        level += 1
score2 = 36 // 15 """
while score <=10000:
    score += pentoPoints

    if score >= nxtLevel:
        print("************next Level*******************")
        level = level + 1
        speed = speed + 20
        nxtLevel = level*levelUp
        
        #levelUp = nxtLevel
        #nxtLevel = score // level
    #if nxtLevel > 0:
    #    level = nxtLevel
    print(pentoPoints, score, level, nxtLevel, speed)



#nxtLevel = score // (level*2*levelUp)