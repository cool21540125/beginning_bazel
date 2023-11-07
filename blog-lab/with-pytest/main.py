# main.py

from lib.prime import is_prime


def get_all_primes():
    primes = []
    for i in range(1, 100):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == "__main__":
    primes = get_all_primes()
    for prime in primes:
        print(prime)
