def josphus(ls,skip):
    idx = skip -1
    while len(ls) > 1:
        print(ls,end="\t")
        print(ls.pop(idx))
        idx = (idx + skip - 1) % len(ls)
    print("Survivor:",ls[0])
n = int(input("輸入總人數:"))
m = int(input("淘汰間距:"))
list1 = list(range(1,n+1))
josphus(list1,m)
    
