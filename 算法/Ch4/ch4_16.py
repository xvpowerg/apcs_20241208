def sqr_binary(x,min,max,pre=2):
    if max-min < 10**(-pre):
        return (min+max)/2
    mid = (min + max) /2
    if mid * mid < x:
       return  sqr_binary(x,mid,max,pre)
    else:
       return sqr_binary(x,min,mid,pre)
num = int(input("輸入整數"))
print(f"{num}的平方根{sqr_binary(num,0,num,3):.3f}")
