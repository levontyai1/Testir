def reverse(s):
    if type(s) != str:
        raise TypeError(f"Ожидали тип str, получили {type(s)}")
    return s[::-1]


def test_reverse():
    assert reverse('abcd') == 'dcba'


def test_emty():
    assert reverse('') == ''


def test_one_sumbly():
    assert reverse("a") == "a"


def test_polyndrom():
    assert reverse('aba') == 'aba'
