from node import Node


class Queue:
    """a queue class using a linked
    list-style implementation"""
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        return self.first.__str__()

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = self.last.next

    def dequeue(self):
        val = self.first.value
        self.first = self.first.next
        return val

    def peek(self):
        return self.first.value

    def is_empty(self):
        if self.first:
            return False
        else:
            return True
