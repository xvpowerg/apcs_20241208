#列出輸入整數的所有質因數
num = int(input("輸入整數"))
for i in range(1,num + 1):
    if num % i != 0:
        continue
    print(i,end=" ")
