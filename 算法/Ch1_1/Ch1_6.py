a1 = int(input("首項"))
r = int(input("公比"))
n = int(input("項數"))
print("Loop")
for i in range(n):
    print(a1*r**i,end=" ")
print()    
def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) * r
print("遞迴")
for i in range(1,n+1):
    print(getAn(i),end=" ")
print()    
