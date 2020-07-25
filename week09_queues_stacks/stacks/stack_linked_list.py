from node import Node


class Stack:
    """A stack class implemented with linked list structure"""
    def __init__(self):
        self.top = None

    def __str__(self):
        return self.top.__str__()

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        val = self.top.value
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.value

    def is_empty(self):
        if self.top:
            return False
        else:
            return True
