from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        self.output = ""

    def process_string(self, line):
        stack = Stack()
        POP_TWICE = 2
        for char in line:
            if char not in "*^":
                stack.push(char)
            elif char == "*":
                if stack.peek() is None:
                    return self.output
                else:
                    self.output += stack.pop()
            elif char == "^":
                for _ in range(POP_TWICE):
                    if stack.peek() is None:
                        return self.output
                    else:
                        self.output += stack.pop()
        return self.output
