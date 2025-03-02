class Stack():
    def __init__(self):
        self.my_stack = []
    def my_push(self,data):
        self.my_stack.append(data)
    def my_pop(self):
        return self.my_stack.pop()
    def size(self):
        return len(self.my_stack)
    def isEmpty(self):
        return self.size() == 0
stack = Stack()
fruits = ["Apple","Banana","Cherry","Mango"]
for fruit in fruits:
    stack.my_push(fruit)

print(stack.size())
while not stack.isEmpty():
    print(stack.my_pop())
