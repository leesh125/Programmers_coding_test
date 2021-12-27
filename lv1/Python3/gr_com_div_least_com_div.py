# My turn
def solution(n, m):
    answer = [1,1]
    if n > m:      # 쉽게 계산히기 위해 작은수를 앞으로
        n,m = m,n

    for i in range(n, 1, -1):   # 작은수 기준으로 역순 for문
        if n % i == 0 and m % i == 0:   # 나눠 떨어지면
            answer[0] = i  # 최대공약수 선정
            break
    answer[1] = answer[0] * m/answer[0] * n/answer[0] #최소공배수 구하기

    return answer

# Good explanation
def gcdlcm(a, b):  # 유클리드 호제법
    c, d = max(a, b), min(a, b)  # 큰 값을 앞으로 작은 값을 뒤로
    t = 1
    while t > 0:  # 큰 수 / 작은수(계속 바뀜)이 0이면 반복문 탈출
        t = c % d  # 큰 수 / 작은수 != 0 이면
        c, d = d, t # 작은 수 / 나머지를 반복
    answer = [c, int(a*b/c)] # 최대공약수 = (수1 * 수2) / 최대공약수

    return answer