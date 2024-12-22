test =  11
isBreak = False
for i in range(5):
    if i == test:
        isBreak = True
        break
    print(i,end=" ")
        

#有break
if isBreak:
    print("有break")
