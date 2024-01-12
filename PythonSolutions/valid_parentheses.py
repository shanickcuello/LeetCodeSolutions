def is_valid(s: str) -> bool:
    stack = []
    open_brackets = "({["
    for char in s:
        if char in open_brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            top_element = stack.pop()
            if (char == ')' and top_element != '(') or \
                    (char == '}' and top_element != '{') or \
                    (char == ']' and top_element != '['):
                return False
    return not stack

if __name__ == '__main__':
    is_valid("(")
    is_valid("()")
    is_valid("()[]")
    is_valid("()[{}]")