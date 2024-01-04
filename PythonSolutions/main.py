from collections import Counter
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

result = min_operations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12])

if __name__ == '__main__':
    print(result)

