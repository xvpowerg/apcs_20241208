list1 = ["a","b","c"]
print("len:",len(list1))
list1.append(50)
list1.append(75)
print("len:",len(list1))
print(list1)

##list2 = ["def","ghjk"]
##list1.append(list2)
##print(list1)

list2 = ["def","ghjk"]
list1.extend(list2)
print(list1)



