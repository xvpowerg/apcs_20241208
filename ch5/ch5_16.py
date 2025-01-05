import random
ans = random.randint(1,5)
guess = int(input("請輸入1~5之間的數"))
if guess == ans:
    print("恭喜猜對了")
else:
    print("猜錯了,答案是",ans)

