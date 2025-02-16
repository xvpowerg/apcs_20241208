x = [5,15,25,35,45]
for data in x:
    print(data,end = " ")
print("\n")
for i in range(len(x)):
    print(x[i],end = " ")
print("\n")
print("\n插入元素")
x.insert(2,100)
print(x)
x.insert(-3,999)
print(x)
print("\n附加")
x.append(250)
x.append(150)
print(x)
print("\n修改")
x[2] = 25
for i in range(1,3):
    x[i] = 580
print(x)
x[3],x[4] = x[4],x[3]
print(x)
print("\n刪除")
x.remove(25)
print(x)
#x.remove(580)
#print(x)
target = 580
while target in x:
    x.remove(target)
print(x)
n = x.pop()
print(n)
print(x)
n = x.pop(2)
print(n)
print(x)
#所有內容由頭依序彈出
try:
    while True:
        print(x.pop(0),end = " ") 
except:
    pass


'''
while len(x) > 0:
    print(x.pop(0),end=" ")
print(x)
'''











