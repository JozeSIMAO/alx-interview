#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """

    if n <= 1:
        return 0

    # Initialize an array to store the minimum
    # number of operations for each number of characters
    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = float('inf')  # Initialize to infinity
        for j in range(1, i // 2 + 1):
            # Check if dividing i by j results in an integer
            # quotient and if min_ops[j] is not infinity
            if i % j == 0 and min_ops[j] != float('inf'):
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    return min_ops[n]
