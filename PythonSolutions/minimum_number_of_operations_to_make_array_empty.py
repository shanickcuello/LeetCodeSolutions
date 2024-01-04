from typing import List
from collections import Counter


def min_operations(nums: List[int]) -> int:
    counter = Counter(nums)
    operations = 0
    for key in counter:
        if counter[key] % 3 == 0 or counter[key] % 2 == 0:
            operations += 1
        else:
            return -1
    return operations
