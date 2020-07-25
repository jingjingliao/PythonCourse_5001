# prompts the user for two integers of any length and adds them together.
# In addition to adding them, it also counts the number of times the "carry"
# operation needs to be carried out.


def main():
    num1, num2 = get_input()
    count, total_sum = count_carries(num1, num2)

    print("{} + {} = {}".format(num1, num2, total_sum))
    print("Number of carries: {}".format(count))


# get user's input, if it is invalid, prompt user to enter again
def get_input():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    while not num1.isdigit() or int(num1) < 0:
        num1 = input("Your input is not a number or not a positive number."
                     " Enter the first number: ")

    while not num2.isdigit() or int(num2) < 0:
        num2 = input("Your input is not a number or not a positive number."
                     " Enter the second number: ")

    return num1, num2


# convert string num1, num2 into a list with integer numbers
def convert_to_list(num1, num2):
    num1_list = list(num1)
    num1_integer = [int(num) for num in num1_list]
    num2_list = list(num2)
    num2_integer = [int(num) for num in num2_list]

    return num1_integer, num2_integer


# get the sum of two integer list
def sum_integers(num1, num2):
    num1_integer, num2_integer = convert_to_list(num1, num2)

    length_difference = abs(len(num1_integer) - len(num2_integer))
    zero_list = [0] * length_difference

    if len(num1_integer) < len(num2_integer):
        num1_integer = zero_list + (num1_integer)

    else:
        num2_integer = zero_list + (num2_integer)

    integer_list = [(num1_integer[i] + num2_integer[i])
                    for i in range(len(num1_integer))]

    return integer_list


# count carries
# if there is one number in the list, if the number is larger than 9, then
# count plus one and convert the list into an integer
# if there is more than one number in the list, check each number one by
# one from the end index of the list. If the integer is larger than 9, then
# count plus one and the previous number should plus one as well
# when finishing the for loop, if the last integer is larger than 9, then
# it should minus one, because in the for loop, it has added one when index
# is equal to 0
# at last, convert the integer in the list into integer
def count_carries(num1, num2):
    integer_list = sum_integers(num1, num2)
    count = 0

    if len(integer_list) == 1:
        if integer_list[0] > 9:
            count += 1
        total_sum = int("".join(str(j) for j in integer_list))
        return count, total_sum

    else:
        for j in range(len(integer_list) - 1, -1, -1):
            if integer_list[j] > 9:
                count += 1
                integer_list[j-1] += 1
        if integer_list[0] > 9:
            integer_list[-1] -= 1

        new_list = [integer_list[0]]

        for i in range(1, len(integer_list)):
            if integer_list[i] > 9:
                new_list.append(integer_list[i] % 10)
            else:
                new_list.append(integer_list[i])

        total_sum = int("".join([str(j) for j in new_list]))

        return count, total_sum


main()
