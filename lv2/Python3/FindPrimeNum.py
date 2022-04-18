from itertools import permutations

# My turn
def isPrime(num): # 소수 판별 함수
    if num == 1: return False # 1은 소수 아님
    i = 2
    while i*i <= num: # 해당 수의 제곱수가 숫자보다 작을동안(제곱수까지만 비교해도 됨)
        if num % i == 0: # 0으로 나눠 떨어지는게 있다면 
            return False # 소수 아님
        else:
            i += 1 # i += 1
    return True # 0으로 나눠 떨어지는게 없으면 True

def solution(numbers):
    answer = []
    res = [] # 주어진 수로 만들 수 있는 짝들을 담은 list
    cnt = 0 # 소수의 갯수를 셀 cnt 변수
    
    for i in range(1,len(numbers)+1): # 1 ~ 현재 숫자의 길이만큼 표현할 수 있는 짝들을 list로
        answer.append(list(map(list,permutations(numbers,i))))
    
    for i in range(len(answer)): # 1 ~ 현재 숫자의 길이만큼 표현된 수의 리스트 수
        for j in range(len(answer[i])): # 현재 길이 만큼 표현된 수의 리스트 수
            if answer[i][j][0] != '0': # 앞자리가 '0'이면 안 담음
                res.append(''.join(answer[i][j])) # 하나의 이어진 숫자형태로 담음

    for r in set(res): # 담겨진 수에서
        if isPrime(int(r)): cnt += 1 # 소수이면 cnt +=1

    return cnt


# Good Explanation
def solution(n):
    a = set()
    for i in range(len(n)): # 주어진 숫자의 길이만큼
        # 중복을 제거하면서, a에 누적시키면서 담기
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2)) # 0,1 을 뺴주기(비교할 필요 X)
    # 에라토스테네스의 체
    for i in range(2, int(max(a) ** 0.5) + 1): # 구해진 수 중에서 가장 큰 수를 기점으로 제곰근까지
        # 가능한 조합 a에서 자기 자신(i)를 제외한 소수들을 제거해나가기
        a -= set(range(i * 2, max(a) + 1, i))
        

    return len(a)

solution("17")
solution("011")