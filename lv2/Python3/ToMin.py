# My turn
def solution(A,B):
    answer = 0
    A.sort() # A와 B정렬
    B.sort()

    for i in range(len(A)): 
        answer += A[i] * B[-i-1] # a중에서 제일 작은거 b 중에서 제일 큰거 곱하기
    
    return answer

solution([1,4,2], [5,4,4])
solution([1,2], [3,4])

# Good Explanation
def getMinSum(A,B):
    # 람다 함수로 오름차순 A와 내림차순 B에 관련하여 map을 통해 원소마다 접근하여 합을 구함
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))
    
def getMinSum(A,B):
    # zip으로 오름차순 A와 내림차순 B 원소에 하나씩 접근
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))