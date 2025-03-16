arr=[[0]*6 for row in range(6)]                 #宣告矩陣arr
    
data=[[1,2],[2,1],[2,3],[2,4],[4,3],[4,1]]      #圖形各邊的起點值及終點值
for i in range(6):                              #讀取圖形資料
    tmpi=data[i][0]                             #tmpi為起始頂點
    tmpj=data[i][1]                             #tmpj為終止頂點
    arr[tmpi][tmpj]=1                           #有邊的點填入1

print('有向圖形矩陣：')
for i in range(1,6):
    for j in range(1,6):
        print('[%d] ' %arr[i][j],end='')        #列印矩陣內容
    print()
