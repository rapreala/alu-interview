#!/usr/bin/python3

"""
rain module calculates the total amount of water retained between walls.
"""


def rain(walls):
    """
    Calculate the total amount of water retained between walls.

    Args:
        walls (List[int]): A list of non-negative integers
          representing the heights of walls.

    Returns:
        int: Total amount of rainwater retained.

    Raises:
        None.

    """
    if not walls:
        return 0

    total_water = 0
    left_max = right_max = 0
    left = 0
    right = len(walls) - 1

    while left < right:
        if walls[left] <= walls[right]:
            left_max = max(left_max, walls[left])
            water_level = left_max - walls[left]
            if water_level > 0:
                total_water += water_level
            left += 1
        else:
            right_max = max(right_max, walls[right])
            water_level = right_max - walls[right]
            if water_level > 0:
                total_water += water_level
            right -= 1

    return total_water
