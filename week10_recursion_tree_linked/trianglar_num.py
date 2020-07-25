# def main(number):
#     (add_up(number))


# def add_up(number):
#     if number == 0:
#         return 0
#     else:
#         n = number + add_up(number - 1)
#         print(n)
#         return n


# main(5)

def main(number):
    print(add_up(number, 0, 0))


def add_up(number, counter, total):
    if counter == number:
        return total
    else:
        count += 1
        total += counter
        print(total)
        return add_up(number, counter, total)
