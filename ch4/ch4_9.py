def fun1(a,b):
    return a * b
def fun1(a,b,c):#覆蓋了fun1(a,b)
    return a*b*c

print(fun1(5,2,3))
