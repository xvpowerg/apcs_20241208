test =  10
for i in range(5):
    if i == test:
        print("有break")
        break
    print(i,end=" ")
else:
    print("沒break") #會執行就else:是沒跑break

