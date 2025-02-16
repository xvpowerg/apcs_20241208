poly1 = [1,-3,2]
x = 2
fx = 0
for i in range(len(poly1)):
    fx += poly1[i]*x**i
print(f"fx:{fx}")    
