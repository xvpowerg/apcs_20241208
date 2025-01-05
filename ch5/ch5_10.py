class Employee:
    company = "GJ"#Employee 這個類別共用
    phone="(02)2311-4537"
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
    def printInfo(self):
        print(self.name,self.salary,Employee.company,Employee.phone)

emp1 = Employee("Ken",50000)
emp2 = Employee("Iris")
Employee.company = "GJ2"
emp1.salary = 80000
emp1.printInfo()
emp2.printInfo()
