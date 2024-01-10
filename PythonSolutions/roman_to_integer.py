def roman_to_int(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous_value = 0

    for char in s:
        current_value = roman_values[char]
        result += current_value

        if current_value > previous_value:
            result -= 2 * previous_value
        previous_value = current_value
    return result

if __name__ == '__main__':
    print(roman_to_int("III"))
