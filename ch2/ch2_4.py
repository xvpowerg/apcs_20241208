name = "小民"
age = 12
height = 178.123456
print(name,"今年",age,"歲",sep="")
msg = name+"今年"+str(age)+"歲"
print(msg)
#小民今年12歲
# %s 表示要填入字串 %d 表示要填入整數 %f表示要填入浮點數
msg2 = "%s今年%d歲"%(name,age)
print(msg2)
msg3 = f"{name}今年{age}歲"#{name} 表示name變數
print(msg3)
msg4 = "%s今年%d歲身%.2f"%(name,age,height)
print(msg4)
msg5 = f"{name}今年{age}歲身高{height:.2f}"#{name} 表示name變數
print(msg5)
