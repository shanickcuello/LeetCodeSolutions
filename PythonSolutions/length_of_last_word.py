def length_of_last_word(s: str) -> int:
    counter = 0
    previous = 0
    for i in s:
        if i == " ":
            if counter != 0:
                previous = counter
            counter = 0
        else:
            counter += 1
    return counter if counter != 0 else previous


if __name__ == '__main__':
    assert length_of_last_word("a") == 1
    assert length_of_last_word("a ") == 1
    assert length_of_last_word(" a") == 1
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon") == 4
    assert length_of_last_word("luffy is still joyboy") == 6
