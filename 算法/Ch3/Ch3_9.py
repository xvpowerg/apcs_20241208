class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list():
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def add(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newNode
    def getNode(self,index):
            ptr = self.head
            for i in range(index):
                ptr = ptr.next
                if ptr == None:
                    break
            return ptr
    def insert(self,index,item):
            newNode = Node(item)
            if index == 0:
                newNode.next = self.head
                self.head = newNode
            else:
               preNode = self.getNode(index - 1)
               newNode.next = preNode.next
               preNode.next = newNode
link = Linked_list()
link.add(15)
link.add(25)
link.add(30)
link.print_list()
print("="*20)
link.insert(1,200)
link.print_list()

               
