## 英文字母接龍
str_result = input("請輸入字串")
nList = [str_result]
eCount = 0
while eCount < 5:
    print(f"目前字串:{str_result}")
    str_in = input(f"請輸入{str_result[-1]}開始的字串")
    if str_in[0] == str_result[-1]:
        nList.append(str_in)
        str_result ="-".join(nList)
    else:
        eCount += 1
        print(f"輸入錯{eCount}次")
print("超過5次結束")        
