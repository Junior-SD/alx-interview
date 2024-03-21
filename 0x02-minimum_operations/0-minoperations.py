#!/usr/bin/python3
"""Solution to alx interview question
"""


def minOperations(n):
    """Minimum Operations
    @param (n): <int>

    Return: <int> fewest number of operation need to result in exactly n of H
    """
    if n <= 1:
        return 0

    count = 0
    for i in range(2, n + 1):
        while n % i == 0:
            count += i
            n //= i
    return count
