# My turn
def solution(arr, divisor):
    answer = []
    
    arr.sort() # 배열 먼저 정렬

    for i in arr:
        if i % divisor == 0:  # divisor와 나누어 떨어지는 수
            answer.append(i)  # answer 리스트에 추가

    if len(answer) == 0:      # return 된게 없으면
        answer.append(-1)     # -1 리스트에 추가
    return answer

# Good explanation
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
# return a or b 
# -> a의 값이 참이면 a, 거짓이면 b 리턴
