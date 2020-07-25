# prints out the list of triangular number
def main():
    triangular_list = user_input()
    print(triangular_list)


# The user_input function is to repeatedly prompts the user for numbers
# (until the user inputs done) and also check whether the input is invalid
# then, call triangular number function, adds the corresponding triangular
# number to a list. When the input is done, return the list
def user_input():
    num = input("Enter a number, or enter 'done': ")
    triangular_list = []

    while num != "done":
        triangular_num = triangular_number(num)
        triangular_list.append(triangular_num)
        print("The triangular number for", num, "is", triangular_num)
        num = input("Enter a number, or enter 'done': ")
    else:
        return (triangular_list)


# triangular_number function is to generate a triangular number based on
# customer's input in main function
def triangular_number(num):
    ADD_NUM = 1
    DIVIDE_FACTOR = 2
    triangular_num = int((int(num) * (int(num) + ADD_NUM)) / DIVIDE_FACTOR)

    return triangular_num


main()
