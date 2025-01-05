class Student:
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
    def printInfo(self):
        print(self.name,self.score)
    def test(self):
        if self.score >= 60:
            print(self.name+"及格")
        else:
            print(self.name+"不及格")
st1 = Student("Lucy",80)
st2 = Student("Iris",50)
st1.printInfo()
st1.test()#Lucy及格
st2.printInfo()
st2.test()#Iris不及格

