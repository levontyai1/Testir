def reverse(s):
    if type(s) != str:
        raise TypeError(f"Ожидали тип str, получили {type(s)}")
    return s[::-1]
