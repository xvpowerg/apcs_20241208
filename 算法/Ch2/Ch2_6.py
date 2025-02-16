myList1 = []
#myList1內容是1~100
#希望用迴圈
for i in range(1,101):
    myList1.append(i)
print(myList1)
myList2 = [i for i in range(1,101)]
print(myList2)
myList3 =[]
for i in range(1,11):
    if i % 2 == 0:
        myList3.append(i)
print(myList3)
myList4 = [i for i in range(1,11) if i % 2 == 0]
print(myList4)
myList5 = [i *2 for i in range(1,11)]
print(myList5)
values = [0,10,20,30,40,50,60]
myList6 = [9/5*x+32 for x in values]
print(myList6)


