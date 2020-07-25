# prompts the user for a file name, then prints out counts of words,
# non-whitespace characters (including punctuation), and
# alphanumeric characters (letters and numbers, excluding punctuation)

import re


# prompt the user to input a file name, if it is valid, open the file and
# execute the functions below it. If it is not valid, give the user a message
# that he cannot open it
def main():
    file_name = input("Enter the file name: ")
    try:
        file = open(file_name, "r")

        count(file)
        file.close()

    except:
        print("Can't open {}".format(file_name))
        return


# use split build in function to put all the word in list and
# count the word using for loop
# count non-whitespace characters (including punctuation), and
# alphanumeric characters (letters and numbers, excluding punctuation)
# using regular expression
# "\S" matches any non-whitespace character
# "\w" matches any alphanumeric character
def count(file):
    word_count = 0
    character_count = 0
    letter_num = 0

    for line in file.readlines():
        for word in line.strip().split(" "):
            if word == "":
                continue
            word_count += 1

        for char in line.strip():
            if re.findall("\\S", char):
                character_count += 1
            if re.findall("\\w", char):
                letter_num += 1

    print("Words:", word_count)
    print("Characters:", character_count)
    print("Letters & numbers:", letter_num)


main()
