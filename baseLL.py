class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,value):
        self.head =Node(value)
        self.tail = self.head
        self.size = 1
    def append(self,value):
        node = Node(value)
        if self.head in None:
            self.head = node
            self.tail = node
            self.size = 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1
