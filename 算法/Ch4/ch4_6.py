class Stack:
    def __init__(self,capacity):
        self.my_stakc = [None] * capacity
        self.top = -1
        self.capacity = capacity
    def push(self,data):
        if self.isFull():
            print("滿")
        else:
            self.top += 1
            self.my_stakc[self.top] = data           
    def pop(self):
        if self.isEmpty():
            print("空")
            return None
        else:
            data = self.my_stakc[self.top]
            self.my_stakc[self.top] = None
            self.top -= 1
            return data
       
    def size(self):
        return self.top + 1       
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        if self.top >= self.capacity -1:
            return True
        else:
            return False
stack = Stack(3)
stack.push("A")
stack.push("B")
stack.push("C")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())        
