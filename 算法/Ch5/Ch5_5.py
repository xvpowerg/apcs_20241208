def showdata(data_list):
    for i in range(len(data_list)):
        print(f"({i}:{data_list[i]})",end=" ")
    print("\n===================")
data=[16,25,39,63,27,12,8,45]
showdata(data)
n = len(data)
for i in range(1,n):
    tmp = data[i]
    for j in range(i):
        if data[j] > tmp:
            data.insert(j,tmp)
            del data[i+1]
            break
    print(f"第{i}次的結果是:")
    showdata(data)
print("排好的結果")    
showdata(data)        
