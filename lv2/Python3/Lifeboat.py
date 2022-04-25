# My turn
from collections import deque

def solution(people, limit):
    people_q = deque(sorted(people)) # 큐 형태로 정렬된 리스트 담기
    answer = 0

    while people_q: # 큐가 비지 않으면
        if len(people_q) == 1: # 짝이 없는 깍두기만 있을 때
            answer += 1 # 그 친구는 혼자서 나감
            break # 빠져나오기
        if people_q[0] + people_q[-1] <= limit: # 젤 마른사람과 젤 뚱뚱한 사람의 합이 제한무게보다 적다면
            people_q.pop() # 둘을 짝으로
            people_q.popleft() # 빼내기
        else: # 무게 초과라면
            people_q.pop() # 젤 뚱뚱한 애는 혼자 나감
        answer += 1 # 짝 + 1
    return answer 

#solution([30, 30, 40, 70,70,80,90],100)
#solution([30, 30, 40, 70,70,80,90],100)
solution([40, 50,150,160],200)
solution([100, 500,500,900,950],1000)
solution([40,40,40], 120)
print(solution([20,50,50,80], 100))

# Good Explanation
def solution(people, limit) :
    answer = 0
    people.sort() # 정렬하기

    a = 0 # 처음 인덱스 0
    b = len(people) - 1 # 제일 마지막 인덱스
    while a < b : # 짝을 모두 비교했다면 break
        if people[b] + people[a] <= limit : # 양 끝 무게의 합이 제한무게 이하라면
            a += 1 # 첫번째 친구는 짝 지어 나감
            answer += 1 # 짝 +1
        b -= 1 # 마지막 친구는 짝이 있든 없든 나가리
    return len(people) - answer # 전체 사람 수 - 짝 지어진 만큼하면 답
