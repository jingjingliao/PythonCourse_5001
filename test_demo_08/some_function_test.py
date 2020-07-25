import some_functions as sf


def test_multiply_numbers():
    """Test the multiply numbers function"""
    assert sf.multiply_numbers(5, 10) == 50
    assert sf.multiply_numbers(5, -10) == -50


def test_flatten_list_of_strings():
    s1 = "hello "
    s2 = "world."
    s3 = "12345"
    list_argument = [s1, s2, s3]
    conc = "hello world.12345"
    assert sf.flatten_list_of_strings(list_argument) == conc
