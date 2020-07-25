from prime_generator import PrimeGenerator


def main():
    """contain a main function that call a method defined in that
    module that returns the list of primes, and finally it should print
    them out."""
    user_input = int(input("Enter an integer which is greater than 1, we will"
                     + " print out all of prime numbers: "))

    while user_input <= 1:
        print("Invalid input, please enter again: ")
        user_input = int(input(""))
    else:
        prime_num = PrimeGenerator()
        prime_list = prime_num.primes_to_max(user_input)

        print(prime_list)


main()
