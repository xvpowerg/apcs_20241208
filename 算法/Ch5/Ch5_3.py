def showdata(data_list):
    for i in range(len(data_list)):
        print(f"({i}:{data_list[i]})",end=" ")
    print("\n===================")
data=[16,25,39,63,27,12,8,45]
showdata(data)
n = len(data)
for i in range(n - 1):
    minIdx = i
    for j in range(i+1,n):
        if data[j] <data[minIdx]:
            minIdx = j
    data[i],data[minIdx] = data[minIdx],data[i]
    print(f"第{i+1}的結果")
    showdata(data)
print("完成:")
showdata(data)
