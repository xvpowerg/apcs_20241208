list1 = [1,2,3,5,8,13,21,34,55,89]
list2 = filter(lambda x: x % 2 == 0,list1)
print(list(list2))
