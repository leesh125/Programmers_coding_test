# My turn
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0 # 걸리는 시간
    truck_q = deque(truck_weights) # 트럭의 큐
    bridge_q = deque() # 다리의 큐
    weight_on_bridge = 0 # 현재 다리위에 있는 트럭의 무게
    
    while truck_q: # 트럭 큐가 빌 때 까지(마지막 트럭이 다리에 올라서는 순간 끝남)
        now_truck = truck_q.popleft() # 트럭에 가장 왼쪽부터 출발
        if not bridge_q: # 다리에 아무 트럭이 없다면
            bridge_q.append(now_truck) # 다리에 현재 트럭 추가
            weight_on_bridge += now_truck # 다리위에 있는 트럭의 무게 += 현재 트럭의 무게
            answer += 1 # 걸리는 시간 += 1
        else: # 트럭이 다리위에 있을 때
            if len(bridge_q) == bridge_length: # 다리가 트럭으로 꽉 찼을 경우
                weight_on_bridge -= bridge_q.popleft() # 선두 트럭을 빼준다(그에 따른 다리위에 트럭 무게도 빼줌)
            if weight_on_bridge + now_truck > weight: # 만약 다리위에 있는 트럭 무게와 현재 출발하려는 트럭의 무게가 하중되는 무게보다 크면
                while True: # 순환(선두 트럭을 뺏을때도 다리 하중이 버티지 못하면 루프)
                    if len(bridge_q) != bridge_length: # 다리 길이가 꽉차지 않으면
                        bridge_q.append(0) # 의미없는 (0) 무게 추가
                        answer += 1 # 다리 위 트럭 한 칸씩 앞으로
                    else: # 다리 길이가 꽉찼을 때
                        weight_on_bridge -= bridge_q.popleft() # 선두 트럭을 빼준다(그에 따른 다리위에 트럭 무게도 빼줌)
                        if weight_on_bridge + now_truck <= weight: # 만약 선두 트럭을 뺏을 때 하중이 버틸 수 있는 정도라면
                            bridge_q.append(now_truck) # 현재 트럭을 다리에 추가
                            answer += 1 # 한칸씩 이동(1초+1)
                            weight_on_bridge += now_truck # 현재 트럭무게 만큼 하중 추가
                            break # 순환 빠져나오기
            else: # 만약 다리위에 있는 트럭 무게와 현재 출발하려는 트럭의 무게가 하중되는 무게보다 작으면
                weight_on_bridge += now_truck # 현재 트럭의 무게를 다리 위에 있는 트럭의 무게에 누적시킴
                bridge_q.append(now_truck) # 현재 트럭을 다리에 추가
                answer += 1 # 한칸씩 이동
    
    return answer + bridge_length # 마지막 트럭이 이제 막 들어왔음. 즉, 이 트럭이 빠져나가려면 다리 길이만큼 시간을 추가해줘야힘

solution(5,5,[2,2,2,2,1,1,1,1,1])
solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])


# Good Explanation 1
import collections

DUMMY_TRUCK = 0

# 다리 클래스를 만듦
class Bridge(object):

    def __init__(self, length, weight): # 초기값 초기화
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck): # 트럭을 다리에 추가시키는 함수
        next_weight = self._current_weight + truck # 현재 다리의 하중과 출발하는 트럭에 무게를 합친 변수
        # 위 변수가 다리의 하중보다 작고 다리에 현태 트럭이 올라갈 자리가 있으면
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck) # 트럭을 다리에 추가
            self._current_weight = next_weight # 무게도 갱신
            return True
        else: # 위 변수가 다리의 하중보다 크거나 현재 트럭이 올라갈 자리가 없으면
            return False # false 리턴

    def pop(self): # 선두 트럭을 빼내는 함수
        item = self._queue.popleft()
        self._current_weight -= item # 무게도 빼준만큼 갱신해준다
        return item # 뺀 트럭의 무게 리턴

    def __len__(self): # 현재 다리의 길이
        return len(self._queue)

    def __repr__(self): # 객체를 표현
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight) # 다리 객체의 초기값 설정
    trucks = collections.deque(w for w in truck_weights) # 트럭들의 무게를 큐로

    for _ in range(bridge_length): # 다리 길이만큼
        bridge.push(DUMMY_TRUCK) # 모든 다리 구간 0으로 초기화

    count = 0
    while trucks: # 트럭큐에 트럭이 있을동안
        bridge.pop() # 다리 마지막을 뺴줌(초기 0을 뺌)

        if bridge.push(trucks[0]): # 트럭 큐에 첫번째 트럭을 출발(해당 함수의 조건을 충족하면)
            trucks.popleft() 
        else: # 정의한 push 함수의 조건을 충족 하지 못하면
            bridge.push(DUMMY_TRUCK) # 0을 추가함

        count += 1 # +1

    while bridge: # 다리에 트럭이 있을때(마지막 트럭을 골인시키기 위해서 해주는 것)
        bridge.pop() # 하나씩 빼줌
        count += 1 # +1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()


# Good Explanation 2
def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length # 다리 길이만큼 리스트
    sec=0 # 걸리는 시간
    while q: # 다리가 비면 빠져나옴
        sec+=1 # 시간 + 1(이동)
        q.pop(0) # 첫번째 다리 구간 빼기
        if truck_weights: # 출발하지 못한 트럭이 있으면
            if sum(q)+truck_weights[0]<=weight: # 다리 위에 있는 트럭의 합 + 출발하고자 하는 트럭이 하중보다 작으면
                q.append(truck_weights.pop(0)) # 트럭을 다리위로
            else: # 다리 위에 있는 트럭의 합 + 출발하고자 하는 트럭이 하중보다 크면
                q.append(0) # 의미없는 0추가
    return sec