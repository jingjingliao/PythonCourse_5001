from word_ladder import WordLadder
import stack


def test_make_ladder():
    wordlist = set()
    with open('words_alpha.txt') as word_file:
        for line in word_file:
            word = line.strip().split()
            wordlist.add(word[0])

    ladder = WordLadder("cat", "hat", wordlist)
    assert repr(ladder.make_ladder()) == "cat\that\t"

    ladder = WordLadder("love", "hate", wordlist)
    assert repr(ladder.make_ladder()) == "love\thove\thave\thate\t"
