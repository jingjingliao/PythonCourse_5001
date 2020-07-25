from ngrams import NgramFrequencies


def test_constructor():
    """Test the constructor"""
    ng = NgramFrequencies()
    assert ng.ncount == 0
    assert ng.ngram == {}


def test_add_item():
    """Test the add item method"""
    ng = NgramFrequencies()
    ng.add_item("aa")
    ng.add_item("aa")
    ng.add_item("bc")
    ng.add_item("de")
    ng.add_item("abc")
    ng.add_item("aa")
    ng.add_item("abc")
    assert ng.ncount == 7
    assert ng.ngram == {'aa': 3, 'bc': 1, 'de': 1, 'abc': 2}


def test_top_n_counts():
    """Test top n counts"""
    ng = NgramFrequencies()
    ng.add_item("aa")
    ng.add_item("aa")
    ng.add_item("aa")
    ng.add_item("aa")
    ng.add_item("aa")
    ng.add_item("bc")
    ng.add_item("bc")
    ng.add_item("abc")
    ng.add_item("abc")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    assert ng.top_n_counts() == [('a', 7), ('aa', 5), ('bc', 2), ('abc', 2)]


def test_top_n_freqs():
    ng = NgramFrequencies()
    ng.add_item("ab")
    ng.add_item("bc")
    ng.add_item("bc")
    ng.add_item("abc")
    ng.add_item("abc")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    count = ng.top_n_counts()
    assert ng.top_n_freqs() == [('a', 0.444), ('bc', 0.222),
                                ('abc', 0.222), ('ab', 0.111)]


def test_frequency():
    ng = NgramFrequencies()
    ng.add_item("ab")
    ng.add_item("bc")
    ng.add_item("bc")
    ng.add_item("abc")
    ng.add_item("abc")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    ng.add_item("a")
    count = ng.top_n_counts()
    assert ng.frequency(3) == [('a', 0.444), ('bc', 0.222), ('abc', 0.222)]
