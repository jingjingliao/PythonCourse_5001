from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    decode = StringProcessor()
    assert decode.process_string("ab") == ""
    decode.output = ""

    assert decode.process_string("ab*") == "b"
    decode.output = ""

    assert decode.process_string("ab^") == "ba"
    decode.output = ""

    assert decode.process_string("^") == ""
