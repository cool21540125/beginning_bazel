# test_main.py

from main import get_all_primes


def test_main():
    expected_primes = [
        1,
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    actual_primes = get_all_primes()
    assert expected_primes == actual_primes
