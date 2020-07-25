# name: Jingjing Liao
# produce a program that generates faux user names and suggested three
# passwords for users, based on the input information.

import random


# print the welcome message and ask for user's first name, last name and
# favorite word.
# then call the user_name, password1, password2, password3 function
def main():
    print("Welcome to the username and password generator!")

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    fav_word = input("Please enter your favorite word: ")

    user_name(first_name, last_name, fav_word)
    password1(first_name, last_name, fav_word)
    password2(first_name, last_name, fav_word)
    password3(first_name, last_name, fav_word)


# generate random number between 0 and 99, and convert it into string
def random_num():
    random_num = str(random.randint(0, 99))
    return random_num


# generate user's name. The first part is the first letter of user's
# first name. The second part is the first seven letter of user's last name.
# if the length of last name is less than seven, then add "*" until
# the number of whole second part reaches to seven letters.
# The third part is random number between 0 and 99, which has already wrapped
# it into a function. Each letter in the user_name should be in lower case
def user_name(first_name, last_name, fav_word):
    REQUIRED_LENGTH = 7
    first_letter = first_name[0]

    if len(last_name) < REQUIRED_LENGTH:
        first_seven_number = (last_name + "*" *
                              (REQUIRED_LENGTH - len(last_name)))
    else:
        first_seven_number = last_name[:REQUIRED_LENGTH]

    last_two_number = random_num()

    user_name = (first_letter + first_seven_number + last_two_number).lower()
    print("\nThanks {}, your user name is {}".format(first_name, user_name))
    print("\nHere are three suggested passwords for you to consider:")


# generate user's first password. It is the concatenation of the user's first
# and last names, in lower case, with a random integer in the range 0 – 99
# between them. If "a" or "o" or "l" or "s" in password, we need to replace
# them with "@","0","1","$"
def password1(first_name, last_name, fav_word):
    rand_num = random_num()
    password1 = (first_name + rand_num + last_name).lower()

    if "a" or "o" or "l" or "s" in password1:
        new_password = password1.replace("a", "@").replace("o", "0").\
         replace("l", "1").replace("s", "$")

    print("\nPassword 1: {}".format(new_password))


# generate user's second password. It consists of the first and last character
# from the user's first name, the first and last character of their last name,
# and the first and last letter of their favorite word.
# In each case, the first letter of the pair should be lower case and
# the second should be upper case.
def password2(first_name, last_name, fav_word):
    first_letter, second_letter = first_name[0].lower(), first_name[-1].upper()
    third_letter, fourth_letter = last_name[0].lower(), last_name[-1].upper()
    fifth_letter, six_letter = fav_word[0].lower(), fav_word[-1].upper()

    password2 = (first_letter + second_letter + third_letter + fourth_letter +
                 fifth_letter + six_letter)

    print("Password 2: {}".format(password2))


# generate user's third password
# generate all of the possible combination of the letters in the first name
# (last name, and favorite word) and put them into a list.
# each combination should start at the beginning of the that string.
# The least one is the first letter in that string,
# the largest one is the whole string.
def password3(first_name, last_name, fav_word):
    list_first_name = []

    for i in range(len(last_name)):
        list_first_name.append(first_name[:i+1])

    list_last_name = []
    for i in range(len(last_name)):
        list_last_name.append(last_name[:i+1])

    list_fav = []
    for i in range(len(fav_word)):
        list_fav.append(fav_word[:i+1])

    # at least one character from each part (first name, last name,
    # and favorite word) should appear in the password. So randomly select
    # one combination from first name list, last name list, and fav list
    random_first = random.choice(list_first_name)
    random_last = random.choice(list_last_name)
    random_fav = random.choice(list_fav)

    # put the selected three words together in the random_list, and shuffle
    # those words, putting them into an order randomly
    random_list = []
    random_list.append(random_first)
    random_list.append(random_last)
    random_list.append(random_fav)

    random.shuffle(random_list)

    # convert the lists with three words in a random order to string in the end
    password3 = ("".join(random_list))
    print("Password 3: {}".format(password3))


main()
