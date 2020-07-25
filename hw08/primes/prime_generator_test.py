from prime_generator import PrimeGenerator


def test_constructor():
    """Test the constructor"""
    prime_g = PrimeGenerator()
    assert prime_g.composed_set == set()
    assert prime_g.prime_list == []


def test_primes_to_max():
    """Test primes_to_max method"""
    prime_g = PrimeGenerator()
    assert prime_g.primes_to_max(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                          31, 37, 41, 43, 47, 53, 59, 61, 67,
                                          71, 73, 79, 83, 89, 97]

    prime_g = PrimeGenerator()
    assert prime_g.primes_to_max(2) == [2]
