import re


class ChaFreqs:
    def __init__(self):
        self.char_counts = {}
        self.total_count = 0

    def count_line(self, line):
        """process a line of characters"""
        chars = re.findall(r"\w", line.lower())
        for c in chars:
            self.add_char(c)

    def add_char(self, char):
        """Add a character to the counts"""
        self.total_count += 1
        if char in self.char_counts:
            self.char_counts[char] += 1
        else:
            self.char_counts[char] = 1

    @property
    def sorted_counts(self):
        return sorted(
            self.char_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

    @property
    def char_freqs(self):
        return {key: round(self.char_counts[key]/self.total_count, 2)
                for key in self.char_counts.keys()}  # dict comprehension

    
    
