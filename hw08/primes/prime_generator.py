class PrimeGenerator:
    def __init__(self):
        self.composed_set = set()
        self.prime_list = []

    def primes_to_max(self, number):
        MIN_PRIME = 2
        """takes an integer argument and returns a list of all primes
        from 2 to the argument value"""
        for i in range(MIN_PRIME, number + 1):
            if i in self.composed_set:
                continue
            else:
                self.prime_list.append(i)
            for j in range(MIN_PRIME * i, (number + 1), i):
                self.composed_set.add(j)
                continue

        return self.prime_list
