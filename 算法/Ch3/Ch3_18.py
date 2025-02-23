import math
def is_prime(number):
    for i in range(2,int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True
def pListFunc(number):
    pList = []
    for n in range(2,number+1):
        if is_prime(n):
            pList.append(n)
    return pList            
n = int(input("輸入一個正整數"))
pList = pListFunc(n)
print(pList)
