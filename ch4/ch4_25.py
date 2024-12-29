def func1(x):
    return x*2
def func2(x):
    return x + 5
funcList = [func1,func2]
x = 9
tmp = x
for func in funcList:
    tmp = func(tmp)
    print(tmp)
