from text_cleaner import TextCleaner
from ngrams import NgramFrequencies
import sys


def main():
    clean_text = TextCleaner()

    try:
        f = open(sys.argv[1])
        clean_text.clean_file(f)
    except FileNotFoundError:
        print("Can't find", sys.argv[1])
        return

    text = clean_text.text

    # Report top ten unigrams by frequency
    unigram = NgramFrequencies()
    print("Top 10 unigram:")
    for line in text:
        for char in line:
            unigram.add_item(char)
    print_output(unigram.frequency(10))

    # Report top ten bigrams by frequency
    # if word end with ".", then it cannot connect with the next word
    bigram = NgramFrequencies()
    print("Top 10 bigram:")
    for line in text:
        for i in range(len(line) - 1):
            if "." in line[i]:
                continue
            else:
                bi_pattern = line[i] + "_" + line[i + 1]
                bigram.add_item(bi_pattern)
    print_output(bigram.frequency(10))

    # Report top ten trigrams by frequency
    # if word itself and the next word end with "."
    # then they cannot form trigram
    trigram = NgramFrequencies()
    print("Top 10 trigram:")
    for line in text:
        for j in range(len(line) - 2):
            if "." in line[j] or "." in line[j+1]:
                continue
            else:
                tri_pattern = line[j] + "_" + line[j + 1] + "_" + line[j + 2]
                trigram.add_item(tri_pattern)
    print_output(trigram.frequency(10))


def print_output(collection):
    for item in collection:
        print("   ", item)


main()
