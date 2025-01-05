class Employee:#建立一組建構式
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary

emp1 = Employee("Ken",50000)
print(emp1.name)
print(emp1.salary)
emp2 = Employee("Iris")
print(emp2.name)
print(emp2.salary)


