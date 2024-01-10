
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    number_as_string = str(x)
    number_as_list_of_chars = [char for char in number_as_string]

    while len(number_as_list_of_chars) > 0:
        if len(number_as_list_of_chars) == 1:
            return True
        elif number_as_list_of_chars[-1] == number_as_list_of_chars[0]:
            del number_as_list_of_chars[0]
            del number_as_list_of_chars[-1]
            if len(number_as_list_of_chars) == 0:
                return True
        else:
            return False


if __name__ == '__main__':
    is_palindrome(11)
    is_palindrome(122)
    is_palindrome(2222)
    is_palindrome(12)
    is_palindrome(-1)
    is_palindrome(1)
    is_palindrome(0)
