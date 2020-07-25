import sys
from character_freqs import ChaFreqs


def main(filename):
    cf = ChaFreqs()
    try:
        f = open(filename)
    except FileNotFoundError:
        print("Can't find", filename)
        return

    for line in f:
        cf.count_line(line)

    print("\nCharacter counts dictionar:")
    print(cf.char_counts)  #attrubute

    print("\nAnd as a sorted list:")
    print(cf.sorted_counts) # @property 当做属性


main(sys.argv[1])
