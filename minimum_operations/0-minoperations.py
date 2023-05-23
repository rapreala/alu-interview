#!/usr/bin/python3
"""
Minimum Operations

This module contains a function that calculates the fewest
number of operations needed to result in exactly n H characters.

"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations.

    """
    if n <= 1:
        return 0
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return sum(factors)
