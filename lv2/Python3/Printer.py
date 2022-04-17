# My turn
from collections import deque
def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i)) # 현재 숫자와 현재 인덱스가 담긴 queue
    sort_q = deque(sorted(priorities,reverse=True)) # 우선순위별로 정렬된 queue
    
    cnt = 0 # 해당 숫자와 인덱스가 몇번째로 출력되는지 나타낼 변수
    while q: # q가 차있을동안
        now_num, now_idx = q.popleft() # 현재 숫자와, 현재 인덱스 pop

        if now_num >= sort_q[0]: # 현재 뽑은게 가장 큰 우선순위거나 그거보다 높다면
            cnt += 1 # 해당 숫자의 출력 순서 +1
            sort_q.popleft() # 우선순위별 가장 큰 우선순위 제거
            if now_idx == location: # 현재 인덱스가 매개변수의 숫자 위치와 같다면
                return cnt # 그것을 답으로 반환
        else: # 현재 뽑은 숫자가 우선순위보다 낮다면
            q.append((now_num,now_idx)) # 뒤로 밀림



# Good Explanation
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)] # 현재 인덱스와 현재 숫자를 나타낸 리스트
    answer = 0
    
    while True:
        cur = queue.pop(0) # 가장 앞에 있는 숫자와 인덱스 뽑기
        if any(cur[1] < q[1] for q in queue): # queue에 있는 숫자중에서 현재 뽑은 숫자보다 큰게 하나라도 있으면
            queue.append(cur) # 뒤로 밀림
        else:
            answer += 1 # 해당 숫자와 인덱스가 몇번째로 출력되는지 나타낼 변수+1
            if cur[0] == location: # 만약 현재 인덱스가 매개변수 location과 같다면
                return answer # 그것을 답으로

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1]	,0))