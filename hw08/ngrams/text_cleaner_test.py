from text_cleaner import TextCleaner


def test_constructor():
    """Test the constructor"""
    text = TextCleaner()
    assert text.new_line is None
    assert text.text == []


def test_clean_file():
    """test the clean file method"""
    text = TextCleaner()
    f = open("test_file.txt")
    text.clean_file(f)
    assert (text.text) == [['a', 'bunch', 'of', 'cute', 'and', 'spooky',
                           'animals', 'are', 'dropping', 'by.'],
                           ['pick', 'trick', 'or', 'treat.'],
                           ['trick', 'COMMA', '', 'treat.'],
                           ['by', 'mr', 'zeng', 'COMMA', 'mrs', 'liao',
                           'and', 'dr', 'zhang']]
