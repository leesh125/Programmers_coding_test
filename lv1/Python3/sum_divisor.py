# My turn
def solution(n):
    answer = 0

    s = int(n ** 0.5)     # 약수는 제곱근까지만 해도 그 이후는 어차피 반복 곱임
    for i in range(1, s+1):   
        if n % i == 0 and i != (n/i):   # 약수이면서 제곱근이 아닐경우
            answer += i + (n/i)
        elif n % i == 0:            # 제곱근일경우
            answer += i 
    
        
    return answer

# Good explanation
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    # 약수는 약수/2를 넘길 수 없음 
    # 따라서 그 전까지만 해주면 됨
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])