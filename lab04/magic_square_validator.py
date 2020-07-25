# A 3x3 magic square is a 3 by 3 square arrangement of digits between 1 and 9
# (without duplicates) such that the sum of any 3 digits horizontally,
# vertically, or diagonally equals 15


MAGICAL_NUM = 15


def main():
    # ask user to put three digits between 1 and 9 for three times
    magic_num1 = input("Enter three digits between 1 and 9" +
                       " (without duplicates) for three times: \n")
    magic_num2 = input("")
    magic_num3 = input("")

    # convert every digits in string into integer and store them into a list,
    # calculate the sum of each list horizontally and diagonally
    list_num1 = [int(num1) for num1 in magic_num1]
    list_num2 = [int(num2) for num2 in magic_num2]
    list_num3 = [int(num3) for num3 in magic_num3]

    horizontal_sum1 = sum(list_num1)
    horizontal_sum2 = sum(list_num2)
    horizontal_sum3 = sum(list_num3)

    diagonal_list1 = [list_num1[0], list_num2[1], list_num3[2]]
    diagonal_list2 = [list_num1[2], list_num2[1], list_num3[0]]
    diagonal_sum1 = sum(diagonal_list1)
    diagonal_sum2 = sum(diagonal_list2)

    vertical_num = list(zip(list_num1, list_num2, list_num3))
    vertical_sum1 = sum(vertical_num[0])
    vertical_sum2 = sum(vertical_num[1])
    vertical_sum3 = sum(vertical_num[2])

    # determine whether their sum are all 15 horizontally
    if horizontal_sum1 == MAGICAL_NUM and horizontal_sum2 == MAGICAL_NUM and\
            horizontal_sum3 == MAGICAL_NUM:
        horizontal_check = True
    else:
        horizontal_check = False

    # determine whether their sum are all 15 diagonally
    if diagonal_sum1 == MAGICAL_NUM and diagonal_sum2 == MAGICAL_NUM:
        diagonal_check = True
    else:
        diagonal_check = False

    # determine whether their sum are all 15 vertically
    if vertical_sum1 == MAGICAL_NUM and vertical_sum2 == MAGICAL_NUM and\
            vertical_sum3 == MAGICAL_NUM:
        vertical_check = True
    else:
        vertical_check = False

    # determine whether their sum are all 15 horizontally, vertically and
    # vertically
    if horizontal_check and diagonal_check and vertical_check:
        print("This is a magic square!")
    else:
        print("Not a magic square!")


main()
