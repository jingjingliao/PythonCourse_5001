def capitalized_vowels():
    string = input("Please input a string: ")
    update_string = ""
    for letter in string:
        if letter.upper() in "AEIOU":
            update_string += letter.upper()
        else:
            update_string += letter.lower()
    print(update_string)


capitalized_vowels()
