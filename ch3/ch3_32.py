## list 可修改
## tuple 不可修改
myList = [99,"A",True]
print(myList[0])
print(myList[1])
print(myList[2])
myTuple = (10,"ken",False)
for v in myTuple:
    print(v,end=" ")
    
print()
myList[0] = 88
print(myList[0])
#myTuple[0] = 77
