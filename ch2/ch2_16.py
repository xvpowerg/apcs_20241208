#練習：字串練習
#檢查使用者輸入的字串是否為迴文
#是顯示True 不是顯示False
#ABA
inStr = input("輸入字串")
test = inStr == inStr[::-1]
print(test)
