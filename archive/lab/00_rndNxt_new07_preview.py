import random as rnd
i = 0
randlist = rnd.sample(range(0,11),11)
#print(randlist,len(randlist))
while (i <= 4):
    if (len(randlist) >= 2):

        print("in while",randlist)
        randintNxt= randlist[1] # use this instead of the the first num of the next randlist
        print("in while preview",randintNxt) 
        
        if (len(randlist) < 2):
            randlist = rnd.sample(range(0,11),11)  
            i = i + 1               
        randint = randlist.pop(0)
        print("in while",randint)

        if (len(randlist) < 2):
            print("in while list < 2",randint)
        
        
        


      
