import random as rnd
i = 0
randlist = [5,1]
randlist = rnd.sample(range(0,11),11)
while i<=33:
    if 'reserveList' not in locals():
        reserveList = []
        print("reservelist created 1", reserveList)
    reserveList.append(randlist[0])
    if 'reserveList' not in locals():
        reserveList = []
        print("reservelist created 2", reserveList)
    reserveList.append(randlist[0])    
    print(reserveList)

    if len(randlist) >= 1: #ggf >=1 !!
        print("randlist", randlist, len(randlist))
        randint = randlist.pop(0)   #!!!!! und geh dann AUCH in die ==1 Schleife !!!
        print("Pento", randint)

        if len(randlist) > 1:   # ggf >=1
            preview = randlist[0]
            print("Preview:", preview)

    #if len(randlist) <= 0:
    #    randlist = rnd.sample(range(0, 10), 10)
    if len(randlist) == 1: # wenn nur noch 1 Element in randlist
        
        preview = randlist[0] # das preview muss irgendwie next randint werden
        print("preview len2--> len1", preview)
        #print("randlist == 1 alt list. ", randlist, len(randlist))

        #preview = newrandlist[0]            
        #randint = randlist.pop(0)      # !!ausgeklammerte !!!11!!
        #print("==1 Pento last", randint)
        #preview = newrandlist[0] # erst nach der neuen randlist !!
        #print("==1 Preview (next list):", preview)
        
    if len(randlist) == 0:
        #randint = preview
        newrandlist = rnd.sample(range(0, 11), 11)
        print("randlist == 1 neu list: ", newrandlist, len(newrandlist))  
        preview = newrandlist[0] 
        print("Preview newradnlist:", preview)         
        randlist = newrandlist
        #print("Preview len 0:")