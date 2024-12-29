def printUserInfo(name,age,**other):
    print("==info===")
    print("name:",name)
    print("age:",age)
    for key in other:
        print(key,":",other[key])
        
printUserInfo("Sean",40)       
printUserInfo("David",35,phone="098755123",company="GJ")      
