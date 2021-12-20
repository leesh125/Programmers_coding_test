# My turn
def solution(arr, divisor):
    answer = []
    
    arr.sort()

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)
    return answer

# Good explanation
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
