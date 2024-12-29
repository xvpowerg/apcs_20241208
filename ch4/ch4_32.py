list1 = [1,2,3,5,8,13,21,34,55,89]
#產生一個List2只包含list1內偶數的數值
list2 = []
for i in list1:
    if i % 2 == 0:
       list2.append(i)
print(list2)       
