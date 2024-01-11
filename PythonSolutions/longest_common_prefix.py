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
    strs1 = ["flower", "flow", "flight"]
    print(longest_common_prefix(strs1))
    strs2 = ["dog", "racecar", "car"]
    print(longest_common_prefix(strs2))