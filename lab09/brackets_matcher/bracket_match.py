from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    # TODO: Implement bracket matching functionality
    # as required by bracket_checker.py and by
    # bracket_match_test.py
    def __init__(self):
        self.bracket_dict = {")": "(", "]": "[", "}": "{"}

    def brackets_match(self, line):
        stack = Stack()
        for char in line:
            if char in self.bracket_dict.values():
                stack.push(char)
            elif char in self.bracket_dict.keys():
                if not stack.peek():
                    return False
                else:
                    if stack.peek() == self.bracket_dict[char]:
                        stack.pop()
        if stack.peek() is None:
            return True
        else:
            return False
