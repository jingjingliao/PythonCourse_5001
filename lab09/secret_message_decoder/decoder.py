from string_processor import StringProcessor


def main():
    sp = StringProcessor()
    line = input("Input a line:\n")
    print(sp.process_string(line))


main()
