# 1  1   2     3   5   8
# n1 n2 n1+n2    
#    n1  n2   n1+n2
#        n1   n2  n1+n2
max = int(input("費式係數範圍"))
num1,num2 = 1,1
print(num1,num2,sep=", ",end="")
next = num1 + num2
while next < max:
    print(f", {next}",end="")
    num1 = num2
    num2 = next
    next = num1 + num2
