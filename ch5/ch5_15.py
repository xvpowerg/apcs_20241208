#Student 屬性 name 與 score
# 希望可用score排序
# 並顯示(name,score)
class Student:
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
    def __str__(self):
        return f"({self.name},{self.score})"
    def __lt__(self,other):
        return self.score < other.score 
st1 = Student("Ken",80)
st2 = Student("Vivin",25)
st3 = Student("Lucy",75)
print(st1,st2,st3)
stList = [st1,st2,st3]
stList.sort()
for s in stList:
    print(s)
