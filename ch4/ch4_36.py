str1 = "This is his dogs"
search1 = "is"
index =  str1.find(search1)#找不道回傳-1
print(index)
index =  str1.find(search1,index+1)
print(index)
