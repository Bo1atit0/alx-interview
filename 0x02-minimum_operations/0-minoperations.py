#!/usr/bin/python3
"""
MOdule to  Calculates the minimum number
of operations to achieve n H characters.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to achieve n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations, or 0 if n is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
