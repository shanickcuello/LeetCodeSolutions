#https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty
from typing import List

def min_operations(nums: List[int]) -> int:
    ans = {}
    for val in nums:
        ans[val] = ans.get(val, 0) + 1
    count = 0
    for i in ans.keys():
        k = ans[i]
        if k < 2:
            return -1
        elif k % 3 == 0:
            count += k // 3
        elif k % 3 == 1 or k % 3 == 2:
            count += k // 3 + 1
    return count
