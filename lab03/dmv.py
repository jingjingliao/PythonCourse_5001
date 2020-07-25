import random as rnd

# A random driver’s license number consists of 7 random digits
# The function is to get the 7 random digits


def random_num():
    seven_random_digits = []
    for _ in range(7):
        seven_random_digits.append(str(rnd.randint(0, 9)))
    random_num = "".join(seven_random_digits)
    return random_num

# The function is to get the driver's license information, based on
# the driver's name and date of birth


def get_license():
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    fullname = input("Please enter your first, middle, and last name: \n")
    date_of_birth = input("Enter date of birth (MM/DD/YY): \n")
    print("--------------------------------")

    name_break = fullname.rfind(" ")
    family_name = fullname[name_break+1:]
    first_and_middle_name = fullname[:name_break]
    birthdate_break = date_of_birth.rfind("/")
    birthdate_year = date_of_birth[birthdate_break+1:]

    print("Washington Driver License")
    print("DL", " ", random_num())
    print("LN", " ", family_name.title())
    print("FN", " ", first_and_middle_name.title())
    print("DOB", " ", date_of_birth)
    print("EXP", " ", date_of_birth.replace(birthdate_year, str(21)))
    print("--------------------------------")


get_license()
