from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist
        self.unique_word = set()

    def make_ladder(self):
        ASCII_VALUE_A = 97
        ASCII_VALUE_Z = 122
        stack = Stack()
        queue = Queue()
        stack.push(self.w1)
        queue.enqueue(stack)
        self.unique_word.add(self.w1)

        while not queue.isEmpty():
            stack1 = queue.dequeue()
            word = stack1.peek()

            for i in range(len(word)):
                word_list = list(word)
                for letter in range(ASCII_VALUE_A, ASCII_VALUE_Z + 1):
                    word_list[i] = chr(letter)
                    new_word = "".join(word_list)
                    if (new_word in self.wordlist and
                       new_word not in self.unique_word):
                        self.unique_word.add(new_word)
                        new_stack = stack1.copy()
                        new_stack.push(new_word)
                        if new_word == self.w2:
                            return new_stack
                        else:
                            queue.enqueue(new_stack)
        else:
            return None
