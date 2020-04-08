while True:
 def bracket_matching(s):
    d = {']': '[', ')': '(', '}': '{'}
    stack = []
    while (s):
        c = s[0]
        if (c in d and len(stack) == 0) or (c in d and stack[-1] != d[c]):
            return ("pair not matching")
        if c in d and stack[-1] == d[c]:
            stack.pop()
        elif c not in d:
            stack.append(c)
        s = s[1:]
    if stack:
        return ("pair not matching")
    return ("matching pairs")
 print(bracket_matching(input("enter the brackets as many pairs as you want:")))
 opt= (input("enter 'N' to stop: "))
 if opt=="N":
  break



