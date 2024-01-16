from typing import List

# # this solution lead me to runtime problems modifying the list while iterating.
# def remove_duplicates(nums: List[int]) -> int:
#     current_num = None
#
#     for i in range(len(nums)):
#         if current_num == nums[i]:
#             nums[i] = None
#         elif current_num != nums[i]:
#             current_num = nums[i]
#     return len([num for num in nums if num is not None])

def remove_duplicates(nums: List[int]) -> int:
    current_num = None
    non_duplicates = []

    for num in nums:
        if current_num != num:
            current_num = num
            non_duplicates.append(num)

    nums[:] = non_duplicates
    return len(non_duplicates)


if __name__ == '__main__':
    print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(remove_duplicates([1, 1, 2]))