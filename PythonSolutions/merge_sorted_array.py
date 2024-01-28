from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

if __name__ == '__main__':
    nums1_case1 = [1, 2, 3, 0, 0, 0]
    m_case1 = 3
    nums2_case1 = [2, 5, 6]
    n_case1 = 3
    merge(nums1_case1, m_case1, nums2_case1, n_case1)
    assert nums1_case1 == [1, 2, 2, 3, 5, 6]

    nums1_case2 = [1]
    m_case2 = 1
    nums2_case2 = []
    n_case2 = 0
    merge(nums1_case2, m_case2, nums2_case2, n_case2)
    assert nums1_case2 == [1]

    nums1_case3 = [0]
    m_case3 = 0
    nums2_case3 = [1]
    n_case3 = 1
    merge(nums1_case3, m_case3, nums2_case3, n_case3)
    assert nums1_case3 == [1]