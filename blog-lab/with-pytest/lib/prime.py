# lib/prime.py

from math import sqrt


def is_prime(n):
    flag = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag
