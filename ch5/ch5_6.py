search = 5
try:
    for i in range(1,10):
        print("i:",i)
        for k in range(1,10):
            print("k===============:",k)
            for y in range(1,10):
                print("y:",y)
                if k == search:
                    raise Exception()
except:
    pass

