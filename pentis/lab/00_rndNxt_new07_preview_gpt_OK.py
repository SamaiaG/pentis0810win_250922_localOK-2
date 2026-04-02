import random as rnd

i = 0
randlist = rnd.sample(range(0, 11), 11)
print(randlist, len(randlist))

while i <= 4:
    if len(randlist) >= 1:
        print("in while", randlist, len(randlist))
        randint = randlist.pop(0)
        print("in while", randint)

        if len(randlist) >= 1:
            preview = randlist[0]
            print("Preview:", preview)

    if len(randlist) <= 0:
        randlist = rnd.sample(range(0, 11), 11)
        i += 1

    if len(randlist) == 1 and i < 4: # wenn nur noch 1 Element in randlist
        print("randlist == 1 alt list. ", randlist, len(randlist))
        newrandlist = rnd.sample(range(0, 11), 11)
        print("randlist == 1 neu list: ", newrandlist, len(newrandlist))
        randint = randlist.pop(0)
        print("in while", randint)
        preview = newrandlist[0] # erst nach der neuen randlist !!
        print("Preview (next list):", preview)
        randlist = newrandlist
        i += 1
