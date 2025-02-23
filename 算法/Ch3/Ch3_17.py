def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True     
n = int(input("輸入一個整數"))
if is_prime(n):
    print(f"{n}是質數")
else:
    print(f"{n}不是質數")

pList = []    
for j in range(2,n+1):
    if is_prime(j):
        pList.append(j)
print(pList)        
