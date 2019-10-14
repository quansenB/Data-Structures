import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.top = StackNode(value, self.top)
        self.size += 1

    def pop(self):
        if self.top != None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        return None

    def len(self):
        return self.size

class StackNode:
    def __init__(self, value, nextNode):
        self.value = value
        self.next = nextNode

    