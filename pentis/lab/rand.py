import random as rnd


list2 = []



a = 0
randlist = rnd.sample(range(0,11),10)
while(a <= 9):
    
    print(randlist)
    
    randint = randlist.pop(0)
    print(randint)
    #print(rnd.sample(range(0,10),10))
    a += 1


""" for count in range(22):
    tetRandom = rnd.randrange(11)
    list2.append(tetRandom)
    print(list2[count]) """