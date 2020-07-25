from a_class import AClass


def test_constructor():
    """Test the constructor"""
    ac = AClass("test attribute")
    assert ac.an_attribute == "test attribute"


def test_return_a_value():
    """Test the return_a_value method"""
    ac = AClass("teat attribute")
    assert ac.return_a_value(1, 2, 3) == 6
    assert ac.return_a_value(-1, 0, 0) == -1
