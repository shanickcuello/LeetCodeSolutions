from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

if __name__ == '__main__':
    shuffle([2,5,1,3,4,7], 3)
    shuffle([1,2,3,4,4,3,2,1], 4)
    shuffle([1,1,2,2], 2)

