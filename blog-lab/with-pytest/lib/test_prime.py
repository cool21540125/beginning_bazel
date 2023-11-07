# lib/test_prime.py

from lib.prime import is_prime


def test_primes():
    primes = [3, 5, 17, 31, 43]
    for p in primes:
        assert is_prime(p) == True


def test_non_primes():
    non_primes = [4, 10, 56, 48]
    for p in non_primes:
        assert is_prime(p) == False


def test_failing():
    assert is_prime(57) == False


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__]))
