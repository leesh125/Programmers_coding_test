def solution(s):
    if s[0] == ')' or s[-1] == '(': return False
    stack = [s[0]]

    for i in range(1, len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                return False
    if len(stack) == 0: return True
    else: return False