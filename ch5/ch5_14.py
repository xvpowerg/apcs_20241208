class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __len__(self):
        return self.x ** 2 + self.y ** 2
    def __lt__(self,other):
        self_len = len(self)
        other_len = len(other)
        return self_len < other_len
    def __eq__(self,other):
        return len(self) == len(other)
p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(0,1)
print(p1 > p2)
myList = [p1,p2,p3]
myList.sort(reverse=True)
for p in myList:
    print(p)

