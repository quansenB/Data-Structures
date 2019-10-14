import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        if self.first == None:
            self.first = QueueNode(value)
        else:
            self.first.add_at_end(QueueNode(value))
        self.size += 1

    def dequeue(self):       
        if self.first != None:
            temp = self.first
            self.first = self.first.next
            self.size -= 1
            return temp.value
        
        return None

    def len(self):
        return self.size

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_at_end(self, node):
        if self.next == None:
            self.next = node
        else: 
            self.next.add_at_end(node)
    