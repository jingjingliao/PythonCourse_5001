# Ask for an account number and determines whether or not the number is
# valid using Luhn’s algorithm


# get the user's input, check whether it is invalid
def get_input():
    account_num = input("Please enter your account number: ")
    while account_num.isdigit() is not True:
        print("Please enter numbers only")
        account_num = input("Please enter your account number: ")

    return account_num


# Beginning with the second to right-most digit. Modify every other digit
# moving from right to left
def num_list(account_num):
    DOUBLE_FACTOR = 2
    BIGGEST_SINGLE_DIGIT = 9
    FACTOR = 10

    num_list = [int(num) for num in account_num]
    for num in range(len(num_list)-2, -1, -2):
        num_list[num] *= DOUBLE_FACTOR   # double the digit's value

    # If the resulting number is a two digit number,
    # add the first digit of that value to the second digit,
    # yielding a single digit number.
    BIGGEST_SINGLE_DIGIT = 9
    FACTOR = 10
    for i in range(len(num_list)):
        if num_list[i] > BIGGEST_SINGLE_DIGIT:
            num_list[i] = num_list[i] // FACTOR + num_list[i] % FACTOR
        else:
            num_list[i] = num_list[i]

    total = sum(num_list)

    # If the resulting sum is evenly divisible by 10,
    # the sequence is valid. If the resulting sum is not divisible by 10,
    # the sequence is not valued.
    if total % FACTOR == 0:
        return "The account number {} is valid".format(account_num)
    else:
        return "The account number {} is invalid".format(account_num)


def main():
    account_num = get_input()
    result = num_list(account_num)

    print(result)


main()
