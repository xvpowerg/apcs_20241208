import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
data.sort()
showData(data)

def bin_search_rec(data,val,low,high):
    mid = (low + high) // 2
    if val == data[mid]:
        return mid
    if low > high:
        return -1
    elif val < data[mid]:
        high = mid - 1
    else:
        low = mid + 1
    return bin_search_rec(data,val,low,high)     
while True:
    val = int(input("請輸入搜尋1~100 輸入-1結束"))
    if val == -1:
        break
    pos = bin_search_rec(data,val,0,len(data) - 1)
    if pos == -1:
        print("找不到")
    else:       
        print(f"找到了第{pos+1}筆:{data[pos]}")

