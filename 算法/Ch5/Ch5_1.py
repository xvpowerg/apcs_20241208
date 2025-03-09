def showdata(data_list):
    for i in range(len(data_list)):
        print(f"({i}:{data_list[i]})",end=" ")
    print("\n===================")
data=[16,25,39,63,27,12,8,45]   
showdata(data)

n = len(data)
for i in range(1,n):
    for j in range(n-i):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
    print(f"第{i}次排序後的結果",end="")
    showdata(data)
print("最後排序的結果:")
showdata(data)
