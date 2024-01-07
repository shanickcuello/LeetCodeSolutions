def convertToTitle(columnNumber: int) -> str:
    result = ''
    abcd = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
           13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
           25: 'Z'}

    while columnNumber >= 1:
        columnNumber -= 1
        module = columnNumber % 26
        result += abcd[int(module)]
        columnNumber /= 26
    return result[::-1]



if __name__ == '__main__':
    print(convertToTitle(2002))
    print(convertToTitle(27))
