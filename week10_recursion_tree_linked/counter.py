def main(number):
    counter(1, 10)


def counter(value, number):
    if value <= number:
        print(value)
        counter(value+1, number)


main(10)
