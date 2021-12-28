# My turn
def solution(x, n):
    answer = []

    for i in range(n):
        answer.append((i+1)*x) # 입력된 x 만큼 곱해주기

    return answer

# Good explanation
def number_generator(x, n):
    
    return [i * x + x for i in range(n)]