#檢查是否為質數
num = int(input("輸入整數"))

isPrimeNum = True
for i in range(2,num):
    if num % i == 0:
        isPrimeNum = False
        break    
if isPrimeNum:
    print("是質數")
else:
    print("不是質數")
