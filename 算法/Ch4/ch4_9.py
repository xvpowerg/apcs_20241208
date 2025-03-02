def f1(n):
    reuslt = 1
    for i in range(n,0,-1):
        reuslt *= i
    return reuslt
def f2(n):
    if n == 1:
        return 1
    else:
        return n * f2(n-1)
print(f1(5))
print(f2(5))
