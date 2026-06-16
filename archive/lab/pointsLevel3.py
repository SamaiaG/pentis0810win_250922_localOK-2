score = 0
level = 1
nxtLevel = 1
levelUp = 300
while score < 1000:
    score += 3*level
    #score += fullLines()         #rnd.randrange(11)
    if score % 15 == 0:
            level += 1
    print(score, level)

