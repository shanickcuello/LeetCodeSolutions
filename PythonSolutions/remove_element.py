from typing import List


def remove_element(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == '__main__':
    assert remove_element([3, 2, 2, 3], 3) == 2
    assert remove_element([0,1,2,2,3,0,4,2], 2) == 5
