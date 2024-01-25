from typing import List


def plus_one(digits: List[int]) -> List[int]:
    numbers_as_strings = ""
    new_digits = []
    for i in range(0, len(digits)):
        numbers_as_strings+=str(digits[i])

    numbers_as_int = int(numbers_as_strings) + 1

    for i in range(0, len(str(numbers_as_int))):
        char = str(numbers_as_int)[i]
        new_digits.append(int(char))

    return list(new_digits)

if __name__ == '__main__':
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([9]) == [1, 0]
    assert plus_one([9,9]) == [1,0,0]
