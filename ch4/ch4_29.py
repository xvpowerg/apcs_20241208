def func1(x):
    return x + 2
list1 = [1,2,3,4,5]
list2 = map(func1,list1)
print(list(list2))
