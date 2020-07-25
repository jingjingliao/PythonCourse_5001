class NgramFrequencies:
    def __init__(self):
        self.ncount = 0
        self.ngram = {}

    def add_item(self, char):
        """Calculate the total count and the frequency of corresponding word"""
        self.ncount += 1
        if char in self.ngram:
            self.ngram[char] += 1
        else:
            self.ngram[char] = 1

    def top_n_counts(self):
        """returns a list of items sorted on the count, with the most
        frequent first"""
        return sorted(
                        self.ngram.items(),
                        key=lambda x: x[1],
                        reverse=True)

    def top_n_freqs(self):
        """returns a similar list as above, but with frequencies instead
        of counts."""
        DECIMAL_POINT = 3
        counts = self.top_n_counts()
        return [(k, round(v/self.ncount, DECIMAL_POINT)) for k, v in counts]

    def frequency(self, n):
        """takes an item and returns its frequency"""
        return self.top_n_freqs()[:n]
