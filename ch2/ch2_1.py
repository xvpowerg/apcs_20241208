height = int(input("請輸入身高單位公分"))
weight = float(input("請輸入體重單位公斤"))

bmi = weight / ((height / 100) ** 2)
bmi = round(bmi,3)#取到小數點第3位
print("bmi:",bmi)
