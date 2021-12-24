# My turn
def solution(n):
    answer = []
    stn = str(n) # 숫자를 문자로

    for i in reversed(range(len(stn))): # 반복문 거꾸로
        answer.append(int(stn[i]))    # 다시 문자를 정수로
    return answer

print(solution(12345))

# Good explanation
def digit_reverse(n):
    # n을 문자열로 변환후 거꾸로 int형 으로 반환 후 이들을 list로
    return list(map(int, reversed(str(n))))