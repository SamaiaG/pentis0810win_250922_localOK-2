import random as rnd
i = 0
randlist = rnd.sample(range(0,11),11)
#print(randlist,len(randlist))
while (i <= 4):
    if (len(randlist) >= 1):

        print("in while",randlist)
        print("in while preview",randlist[1]) 
        
               
        randint = randlist.pop(0)
        print("in while",randint)
        

    if (len(randlist) <= 0):
        randlist = rnd.sample(range(0,11),11)  
        i = i + 1
      
