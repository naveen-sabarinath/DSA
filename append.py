from baseLL import Node 
class LinkedList:
     def __init__(self,data):
          self.head = Node(data)
          self.tail = self.head
          self.size =1
     def print_linkedlist(self):
           temp = self.head
           while self.size !=0:
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
     def pop(self):
           if self.size ==0:
                 return None
           if self.size ==1:
                 temp = self.head
                 self.head =None
                 self.tail = None
                 self.size =0
                 return temp
           else:
                 temp = self.tail
                 current = self.head
                 while current.next != temp:
                    current = current.next
                    self.tail = current
                    self.tail.next = None
                    self.size -= 1

                 

my_list = LinkedList(5)
print(my_list.head.data) # 5
my_list.append(10)
my_list.pop()