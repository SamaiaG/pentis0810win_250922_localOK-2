import random as rnd


randlist = rnd.sample(range(0,11),11)
    #print(randlist)
i = 0
#def randNext(randlist):
while i<=31:
    if len(randlist) > 1:
        print("randlist", randlist, len(randlist))
        randint = randlist.pop(0)
        print("Pento", randint)
        i = i+1
        if len(randlist) > 1:
            preview = randlist[0]
            print("Preview:", preview)

    #if len(randlist) <= 0:
    #    randlist = rnd.sample(range(0, 10), 10)
    if len(randlist) == 1: # wenn nur noch 1 Element in randlist
        
        print("randlist == 1 alt list. ", randlist, len(randlist))
        newrandlist = rnd.sample(range(0, 11), 11)
        print("randlist == 1 neu list: ", newrandlist, len(newrandlist))
        randint = randlist.pop(0)
        print("==1 Pento last", randint)
        preview = newrandlist[0] # erst nach der neuen randlist !!
        print("==1 Preview (next list):", preview)
        randlist = newrandlist

    #print("randint in func randNext:",randint)
    #return randint, randlist, preview #, randintnext, randlistnext


    #randint, randlist, preview = randNext()