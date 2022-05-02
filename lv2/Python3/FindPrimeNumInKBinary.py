def is_prime(n): # 소수 인지 판정하는 것
    if n == 1:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k): 
    answer = 0
    num = '' # k진수로 변환한 문자열을 나타낼 변수

    while n > 0: # k진수로 변환
        n, mod = divmod(n,k) # 몫, 나머지 이용
        num += str(mod) # 나머지를 계속 추가
    num = num[::-1] # 거꾸로
    num_set = num.split('0') # '0'을 기점으로 분리하면 조건에 충족됨
    
    for num in num_set: # 0을 기점으로 분리된 수
        if num != '' and is_prime(int(num)): # 빈 문자가 아니고 소수이면
            answer += 1 # 답 += 1
    
    return answer
#solution(437674,3)
solution(110011,10)