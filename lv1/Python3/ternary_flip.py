# My turn
def solution(n):
    answer = 0
    i = 0
    ternary = []

    while n != 0:
        ternary.append(n% 3)
        n //= 3
    
    for t in reversed(ternary):
        answer += (3 ** i) * t
        i += 1

    return answer



# Good explanation
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3
        
    answer = int(tmp, 3)
    return answer

print(solution(45))