# My turn
def lcm(a,b): # 최소 공배수 구하는 함수
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i * (a//i) * (b//i)

def solution(arr):
    arr.sort() # 정렬(이전값이 항상 더 크다고 가정하려고)
    for i in range(len(arr)-1):
        arr[i+1] = lcm(arr[i], arr[i+1]) # 각각의 최소공배수를 구해주고
    return arr[-1] # 마지막 값 리턴
print(solution([2,6,8,14]))
print(solution([2,4,6,8]))
print(solution([1,2,3]))
print(solution([1,3,5,7]))
print(solution([3,6,9,12]))

# Good Explanation
from math import gcd # 코테에서 import 안될 수도 있음

def nlcm(num):      
    answer = num[0] # 첫번째 수를 answer에
    for n in num: # 수를 순회
        answer = n * answer // gcd(n, answer) # 각각의 최소공배수를 누적 시켜줌

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));