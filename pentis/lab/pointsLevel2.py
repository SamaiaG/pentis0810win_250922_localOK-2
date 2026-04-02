score = 0
level = 1
nxtLevel = 1
levelUp = 150
""" score += 3*level
#score += fullLines()         #rnd.randrange(11)
if score % 15 == 0:
        level += 1
score2 = 36 // 15 """
while score <=2000:
    score += 3*level

    if score >= level*150:
        #level += 1
        nxtLevel = score // (level*levelUp)
    
    if nxtLevel > 1:
        level = nxtLevel
        print(score, nxtLevel, level)
