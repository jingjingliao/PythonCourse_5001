import random as rnd


# RANGE presents the differences between user's input and random number


RANGE_1 = 1
RANGE_2 = 2
RANGE_3 = 3
RANGE_4 = 5
RANGE_5 = 8
RANGE_6 = 13
RANGE_7 = 20


def guess_game():
    print("Welcome to the Guessing Game!")
    guess_question = "I picked a number between 1 and 50. Try and guess!\n"
    input_num = int(input(guess_question))
    random_num = rnd.randint(1, 50)
    time = 1
    print("You guessed {}".format(input_num))
    while input_num != random_num:
        difference = abs(input_num - random_num)
        if difference <= RANGE_1:
            print("Your guess is scalding hot")
        elif difference <= RANGE_2:
            print("Your guess is extremely warm")
        elif difference <= RANGE_3:
            print("Your guess is very warm")
        elif difference <= RANGE_4:
            print("Your guess is warm")
        elif difference <= RANGE_5:
            print("Your guess is cold")
        elif difference <= RANGE_6:
            print("Your guess is very cold")
        elif difference <= RANGE_7:
            print("Your guess is extremely cold")
        else:
            print("Your guess is icy freezing miserably cold")
        input_num = int(input(""))
        time += 1

    else:
        print("Congratulations. You figured it out in {} tries.".format(time))


guess_game()
