# My turn
def solution(left, right):
    sum = 0
    cnt = 0

    for i in range(left,right+1):
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            sum += i
            cnt = 0
        else:
            sum -= i
            cnt = 0
    return sum

print(solution(13,17))

# Good explanation
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer