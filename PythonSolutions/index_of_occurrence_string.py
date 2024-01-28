def string_occurrence(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

if __name__ == '__main__':
    haystack1, needle1 = "sadbutsad", "sad"
    assert string_occurrence(haystack1, needle1) == 0

    haystack2, needle2 = "leetcode", "leeto"
    assert string_occurrence(haystack2, needle2) == -1

    assert string_occurrence("abcdefg", "def") == 3
    assert string_occurrence("abcabc", "abc") == 0
    assert string_occurrence("mississippi", "issi") == 1