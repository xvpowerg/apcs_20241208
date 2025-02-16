myList2x3 = [["A","B","C"],
             [100,98,73]]
print(myList2x3[1][2])
print(myList2x3[0][1])

for i in range(len(myList2x3)):
    inLen  = len(myList2x3[i])
    for x in range(inLen):
        print(myList2x3[i][x],end = " ")
    print()

print("===="*70)
for tmpList in myList2x3:
    for v in tmpList:
        print(v,end=" ")
    print()    
