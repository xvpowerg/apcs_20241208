num1 = 18
num2 = 0
nums = [1,3,5,7,9]
print("Start")
try:
    print(nums[1])
    print(num1 / num2)
except ZeroDivisionError:    
    print("分母不可為0")
except IndexError:
    print("index錯誤")
    
print("End")
#IndexError
#ZeroDivisionError
