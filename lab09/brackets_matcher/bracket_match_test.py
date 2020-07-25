from bracket_match import BracketMatch


def test_brackets_match():
    """Test brackets_match method"""
    bracket = BracketMatch()
    assert bracket.brackets_match("()") is True
    assert bracket.brackets_match("a(a[a])a({a})") is True
    assert bracket.brackets_match("(") is False
    assert bracket.brackets_match("(}") is False
    assert bracket.brackets_match("a(a(a)a(a)") is False
    assert bracket.brackets_match("aa(a))a(a)") is False
