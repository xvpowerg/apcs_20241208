cars=["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]
print(cars)
n = len(cars)
for i in range(1,n):
    for j in range(n-i):
        if cars[j] > cars[j+1]:
           cars[j],cars[j + 1] = cars[j + 1],cars[j]
    print(f"第{i}次的結果是:{cars}")
print("排序後:",cars)    
