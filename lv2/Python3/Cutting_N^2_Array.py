def solution(n, left, right):
    answer = []

    for i in range(left,right+1): # 결과 배열 인덱스는 right-left 임
        if i // n < i % n: # 인덱스를 n으로 나눴을 때 나머지가 더 크면
            answer.append(i%n+1) # 그 값에 +1을 추가
        else: # 인덱스를 n으로 나눴을 때 몫이 더 크면
            answer.append(i//n+1) # 그 값에 +1을 추가

    return answer

solution(3,2,5)
solution(4,7,14)