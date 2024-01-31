import math


def getPermutation(n: int, k: int) -> str:
    nums = [str(i) for i in range(1, n + 1)]
    result = []

    k -= 1
    for i in range(n, 0, -1):
        index, k = divmod(k, math.factorial(i - 1))
        result.append(nums.pop(index))

    return ''.join(result)

if __name__ == '__main__':
    assert getPermutation(3, 3) == "213"
    assert getPermutation(4, 9) == "2314"
    assert getPermutation(3, 1) == "123"
    assert getPermutation(2, 2) == "21"