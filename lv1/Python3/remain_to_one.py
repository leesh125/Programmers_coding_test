# My turn
def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 1:
            answer = i
            break
    return answer

# Good explanation
def solution(n):
    answer = 0

    for divisior in range(2, (n-1//2)) : #2부터~반값까지 
        if (n-1) % divisior == 0: #약수가 있다면
            answer = divisior 
            break #탈출
    if answer == 0:
        answer = n-1
    return answer
