def test_func1(a,b,c=1):
    return a * b * c

a1 = test_func1(2,5)

a2 = test_func1(6,2,3)

print("a1:",a1)
print("a2:",a2)
