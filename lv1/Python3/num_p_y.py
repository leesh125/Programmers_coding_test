# My turn
def solution(s):
    p = 0
    y = 0
    for i in s:
        if i == 'p' or i == 'P':    # p, P 이면 p ++
            p += 1
        elif i == 'y' or i == 'Y':  # y, Y 이면 y ++
            y += 1

    return (p == y)   # p == y 의 bool 연산

# Good explanation
def numPY(s):
    # count 집계함수 사용
    return s.lower().count('p') == s.lower().count('y') 