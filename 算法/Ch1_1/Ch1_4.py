def dec_to_bin(num):
    v = []
    while True:
        num,rem = divmod(num,2)
        v.append(str(rem))
        if num == 0:
            return "".join(v[::-1])
def dec_to_oct(num):
    v = []
    while True:
        num,rem = divmod(num,8)
        v.append(str(rem))
        if num == 0:
            return "".join(v[::-1])
def dec_to_hex(num):
    base=["0","1","2","3","4","5","6","7"
          ,"8","9","A","B","C","D","E","F"]
    v = []
    while True:
        num,rem = divmod(num,16)
        v.append(base[rem])
        if num == 0:
            return "".join(v[::-1])
        
testNume = int(input("輸入十進位整數:"))
print("二進位:",dec_to_bin(testNume))
print("8進位:",dec_to_oct(testNume))
print("16進位:",dec_to_hex(testNume))
