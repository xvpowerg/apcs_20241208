def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    num1,num2 = 0,1
    nextNum = num1 + num2
    for i in range(2,n):
        num1 = num2
        num2 = nextNum
        nextNum = num1 + num2
    return nextNum
def fib2(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib2(n-1) +  fib2(n-2)

def fib3(n,dataList):
    if dataList[n] != -1:
        return dataList[n]    
    ans = fib3(n-1,dataList) +  fib3(n-2,dataList)
    dataList[n] = ans 
    return ans

print(fib1(10))
print(fib1(100))
print(fib2(10))
#print(fib2(100))
n = 100
dataList = [-1 for i in range(n+1)]
dataList[0] = 0
dataList[1] = 1
dataList[2] = 1
print("ans:",fib3(n,dataList))

