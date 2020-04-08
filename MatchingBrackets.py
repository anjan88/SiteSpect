
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

# creating a new file and writing into a file
file_name='sitespect.txt'                     # you can add your file here to check the code.
brackets=['[{}]()','()','[[]{}()]','[','][']
with open(file_name,'a')as f:
     for bracket in brackets:
         f.write(bracket)
         f.write('\n')

# reading from the txt file
with open(file_name,'r') as f:
     lines = f.readlines()
     for line in lines:
         line=line.strip()
         print(line,bracket_matching(line))



