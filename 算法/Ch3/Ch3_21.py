def square_rootl(x):
    i = 1
    while i * i  < x:
        i += 1
        if i * i == x:
            return i
    return i - 1
def square_root2(x,pre=2):
    step = 1
    r = step 
    while step >= 10**-pre:
        while r * r < x:
            r += step
            if r * r == x:
                return r
        r -= step
        step/=10
    return r    
    
num = int(input("輸入整數"))
print(f"{num}的平方根:{square_rootl(num)}")
print(f"{num}的平方根:{square_root2(num):.2f}")

