def longest_common_prefix(list_of_words):
    if not list_of_words:
        return ""

    list_of_words.sort()

    first_str = list_of_words[0]
    last_str = list_of_words[-1]

    for i in range(len(first_str)):
        if i >= len(last_str) or first_str[i] != last_str[i]:
            return first_str[:i]

    return first_str


if __name__ == '__main__':
    list_of_words = ["flower", "flow", "flight"]
    print(longest_common_prefix(list_of_words))
    list_of_words2 = ["dog", "racecar", "car"]
    print(longest_common_prefix(list_of_words2))
    list_of_words3 = ["11123", "112345", "111111"]
    print(longest_common_prefix(list_of_words3))
    list_of_words4 = ["aar", "aa", "aaafaa", "aaff"]
    print(longest_common_prefix(list_of_words4))
