'''
十分逼近法練習：log
'''
def myLog(a,b,pre=6):
    step = 1
    ans = step
    while step >= 10**-pre:
        while b ** ans < a:
            ans += step
            if b ** ans == a:
                return ans
        ans -= step
        step /= 10
    return ans


a = int(input("輸入數值"))
b = int(input("輸入基數"))
print(f"{a}以{b}為底的對數是:{myLog(a,b):.6f}")





