#!/usr/bin/python3
"""
Determine the winner of the prime game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list of int): Array where each value represents the range [1, n].

    Returns:
        str: Name of the winner ("Maria" or "Ben") or None if tied.
    """
    if not nums or x < 1:
        return None

    # Get the maximum number in nums
    max_n = max(nums)

    # Sieve of Eratosthenes to precompute primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    # Precompute the number of primes up to each number
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Simulate the game for each n in nums
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the primes in the range [1, n]
        prime_count = prime_counts[n]

        # Maria wins if the prime count is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
