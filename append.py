from baseLL import Node 
class LinkedList:
     def __init__(self,value):
          self.head = Node(value)
          self.tail = self.head
          self.size =1
     def print_linkedlist(self):
           temp = self.head
           while self.size is not None:
                 print(temp.data)
                 temp = temp.next


     def append(self,value):
                node = Node(value)
                if self.head is None:
                    self.head = node
                    self.tail = node
                    self.size = 1
                else:
                    self.tail.next = node
                    self.tail = node
                    self.size += 1

my_list = LinkedList(5)
print(my_list.head.data) # 5
my_list.append(10)
print(my_list.tail.data) # 10
print(my_list.size) # 2 
my_list.print_linkedlist() # 5 10