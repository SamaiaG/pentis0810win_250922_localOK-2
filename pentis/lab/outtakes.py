""" if len(randlistnext) < 1:
            print("if", len(randlistnext))
            randlist = rnd.sample(range(0,11),11)
            randlistnext = randlist.copy()
else:
    print("else", len(randlistnext))
    randint = randlist.pop(0) """
            #print("*********************a:",a)

#print("1 if",len(randlist))
            #print("1 else",len(randlist))
            #print("2 if.1",len(randlistnext))
            #print("2 if.2",randlistnext,len(randlistnext))
            #print("2 else",len(randlistnext))
        #print("***********\n NEW   randlist", randlist, len(randlist))
        #print("randint",randint, "\n\n")
        #print("randlistnext",randlistnext)
        #print("randintnext",randintnext)


randlist = []    
    #randlist = rnd.sample(range(0,11),11)
    def randNext(randlist):
        a, randint, randintnext = 0, 0, 0
        
        
        if not randlist:
            print("1 if",len(randlist))
            randlist = rnd.sample(range(0,11),11)
            randlistnext = randlist.copy()
            randint = randlist.pop(0)
            randintnext = randlistnext.pop(1)
        else: 
            print("1 else",len(randlist))
            randint = randlist.pop(0)

        if len(randlistnext) <= 1:
            print("2 if",len(randlistnext))
            randlistnext.insert(0,0)
            #randintnext = randlistnext.pop(1)
        else:
            print("2 else",len(randlistnext))
            randintnext = randlistnext.pop(1)

            print("***********\n NEW   randlist", randlist)
        print("randint",randint)
        print("randlistnext",randlistnext)
        print("randintnext",randintnext)



*******************************

randlist = rnd.sample(range(0,11),11)
    def randNext(randlist):
        a, randint, randintnext = 0, 0, 0
        randlistnext = randlist.copy()
        
        #randintnext = randlistnext.pop(1)
        if len(randlistnext) < 1:
            print("if", len(randlistnext))
            randlist = rnd.sample(range(0,11),11)
            randlistnext = randlist.copy()
            randint = randlist.pop(0)
            randintnext = randlistnext.pop(1)
                        
        else:
            print("else", len(randlistnext))
            randint = randlist.pop(0)
            if len(randlistnext) < 1:
                randintnext = randlistnext.insert(0,0)
                randintnext = randlistnext.pop(1)
            else:
                randintnext = randlistnext.pop(1)
            

        print(randlist)
        print(randint)
        print(randlistnext)
        print(randintnext)

        #if len(randlist) < 1:
        #    randlist = rnd.sample(range(0,11),10)
        a += 1 
        return randint, randintnext