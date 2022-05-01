# My turn
def solution(n):
    cnt, start, index, sum = 0,1,1,0 # 총 count 갯수, 셈을 시작할 숫자, 1씩 더해나가는 index, 총 합

    while start < n//2 + 1: # 절반 이상 넘어갈 필요가 없음(그 이상 연속 수의 합은 이미 n이 넘기에)
        sum += index # sum에 index를 누적
        if sum >= n: # 그 합이 n을 넘겼을 때
            if sum == n: # 합이 n과 같다면
                cnt += 1 # count를 1 증가
            start += 1 # start 숫자를 1 증가한다
            sum,index = 0,start # sum, index를 각각 0, start로 초기화
        else: # n을 넘기지 않았다면
            index += 1 # 인덱스 증가

    return cnt + 1 # 자기 자신을 더하는 것도 포함하여 count 반환

print(solution(15))

# Good Explanation
# https://gkalstn000.github.io/2021/01/21/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84/
def expressions(num):
    # n이하의 숫자 a 부터 k개의 숫자의 합이 n이라고 가정
    # a= n/k + (1−k)/2
    # a가 자연수가 되기위해선 k에 값만 조건을 달아준다
    # 1. n/k가 자연수가 되기위한 조건: k는n의약수
    # 2. (1−k)/2가 정수가 되기위해선 짝수가 되야하므로 k는 홀수
    # 3. k<n
    # (k == 홀수 여야 하지만, k = 2의 경우 특수하게 분모가 통일이 되기에 홀수 일때 2의 값도 추가 해야한다)

    return len([i  for i in range(1,num+1,2) if num % i is 0])