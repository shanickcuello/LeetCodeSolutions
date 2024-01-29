def mySqrt(x: int) -> int:
    left = 1
    right = x
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

if __name__ == '__main__':
    assert mySqrt(8) == 2
    assert mySqrt(4) == 2