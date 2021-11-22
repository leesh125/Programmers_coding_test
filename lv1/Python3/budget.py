# My turn
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget < i:
            break
        budget -= i
        answer += 1
    return answer

# Good explanation
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)