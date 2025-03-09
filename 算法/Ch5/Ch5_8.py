cars = ["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]

print(cars)

car = input("請輸入車廠牌:")

for i in range(len(cars)):
    if car ==  cars[i]:
        print(f"找到位置是:{i}")
        break
else:
    print("不存在")
