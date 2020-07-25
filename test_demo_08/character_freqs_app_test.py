from character_freqs import ChaFreqs


def test_constructor():
    char_freqs = ChaFreqs()
    assert char_freqs.total_count == 0
    assert char_freqs.char_counts == {}