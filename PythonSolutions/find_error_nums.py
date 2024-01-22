from typing import List


def find_error_nums(nums: List[int]) -> List[int]:
    length_of_nums = len(nums)
    expected_sum = length_of_nums * (length_of_nums + 1) // 2
    actual_sum = sum(nums)
    diff = expected_sum - actual_sum
    seen = set()
    duplicate = 0
    for num in nums:
        if num in seen:
            duplicate = num
        else:
            seen.add(num)

    missing = duplicate + diff
    return [duplicate, missing]


if __name__ == '__main__':
    assert find_error_nums([1, 2, 2, 4]) == [2, 3]
    assert find_error_nums([1, 1]) == [1, 2]
