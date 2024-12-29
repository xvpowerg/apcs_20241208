def weight_sum(c,e=80,m=60):
    return c + e*2 + m*3
x = weight_sum(100)
print(x)
y = weight_sum(e=50,c=10)#只要一開使用了具名參數後面的參數必須使用
print(y)
z = weight_sum(20,m=10)
print(z)
