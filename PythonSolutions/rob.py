from typing import List


def rob(nums: List[int]) -> int:
    previous_max = 0
    curr_max = 0
    for money in nums:
        new_max = max(curr_max, previous_max + money)
        previous_max = curr_max
        curr_max = new_max
    return max(previous_max, curr_max)

if __name__ == '__main__':
    assert rob([1,2,3,1]) == 4
    assert rob([2,7,9,3,1]) == 12