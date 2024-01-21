from typing import List


def search_insert(nums: List[int], target: int) -> int:
    for i in range(0, len(nums)):
        if nums[i] == target:
            return nums.index(nums[i])
        if nums[i] > target:
            return nums.index(nums[i])

    return len(nums)

if __name__ == '__main__':
    assert search_insert([1,3,5,6], 5) == 2
    assert search_insert([1,3,5,6], 2) == 1
    assert search_insert([1,3,5,6], 7) == 4
