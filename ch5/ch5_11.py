class Item:
    count = 0
    def __init__(self,name):
        self.name = name
        Item.count += 1
    def __del__(self):
        print(self.name,"刪除")
        Item.count -= 1
        
    def printInfo(self):
        print(self.name)
    def printCount():
        print(f"我有{Item.count}筆")
i1 = Item("I1")
i2 = Item("I2")
i3 = Item("I3")
i1.printInfo()
i2.printInfo()
i3.printInfo()
del i1
Item.printCount()
