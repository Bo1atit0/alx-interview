#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): List of coin denominations.
        total (int): Target amount to achieve.

    Returns:
        int: Fewest number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)
    count = 0
    remaining = total

    for coin in coins:
        if remaining <= 0:
            break
        # Use as many of this coin as possible
        count += remaining // coin
        remaining %= coin

    # If there is still a remaining amount, it means it's not possible
    return count if remaining == 0 else -1
