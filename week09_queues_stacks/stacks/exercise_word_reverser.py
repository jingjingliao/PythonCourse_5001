from stack_linked_list import Stack


def main():
    stack = Stack()
    reverse_string = ""

    in_string = input("Input a word:\n")
    for letter in in_string:
        stack.push(letter)

    for _ in range(len(in_string)):
        reverse_string += (stack.pop())

    print(reverse_string)

    # TODO:
    # use the stack to reverse the word. Push each
    # letter onto the stack, then create a new
    # string and build it up by popping characters
    # back out of the stack. Print out the reversed
    # string.


main()
