def bracket_matching(s):
    d = {']': '[', ')': '(', '}': '{'}
    stack = []
    while (s):
        c = s[0]
        if (c in d and len(stack) == 0) or (c in d and stack[-1] != d[c]):
            return False
        if c in d and stack[-1] == d[c]:
            stack.pop()
        elif c not in d:
            stack.append(c)
        s = s[1:]
    if stack:
        return False
    return True


print(bracket_matching('[{}]()'))
print(bracket_matching('()'))
print(bracket_matching('[[]{}()]'))
print(bracket_matching('['))
print(bracket_matching(']['))
