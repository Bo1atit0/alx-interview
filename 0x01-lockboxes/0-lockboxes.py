#!/usr/bin/python3
"""
Module to determine if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists where each sublist represents
                                     the keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    opened = set()  # Set to keep track of opened boxes
    keys = [0]      # Start with the first box unlocked

    while keys:
        current = keys.pop()  # Get the next box to open
        if current not in opened:
            opened.add(current)
            # Add all keys in this box, but only if the keys are valid
            keys.extend(k for k in boxes[current] if k not in opened and k < n)

    # Check if all boxes have been opened
    return len(opened) == n
