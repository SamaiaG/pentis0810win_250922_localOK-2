
list1 = []
def listfunc(a,b):
    list1.append(a)
    list1.append(b)
    r1 = list1.pop(1)
    return r1

nmbr = listfunc(1,2)
if len(list1) <= 1:
    print(nmbr)

#list1.sort()
