# 攝氏溫度轉換華氏溫度程式
#請使用函數完成
#c是攝氏溫
# 9/5*c+32
def c2f(c):
    f = 9 / 5 * c + 32    
    return f

#輸入攝氏溫度 如果輸入了q才離開結束輸入
while True:
    inStr = input("輸入攝氏溫度(輸入q離開)")
    if inStr == "q":
        break
    tc = float(inStr)
    fc = c2f(tc)
    print(f"攝氏溫度{fc:.2f}")
    
