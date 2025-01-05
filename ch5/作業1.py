def calcBMI(h,w):
    return w/((h/100)**2)

def diagnose(bmi):
    result = '數值錯誤'
    if(bmi>30):
        result = '肥胖'
    elif(bmi>25):
        result = '過重'
    elif(bmi>18.5):
        result = '正常'
    elif(bmi>0):
        result = '過輕'
    return result

height = float(input('請輸入身高，單位為公分: '))
weight = int(input('請輸入體重，單位為公斤: '))
bmi = calcBMI(height, weight)
print("bmi: %.2f, 判定結果: %s" %(bmi, diagnose(bmi)))
