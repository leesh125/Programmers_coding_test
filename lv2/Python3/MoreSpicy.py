import heapq

def solution(scoville, K):
    cnt = 0
    scoville.sort() # 가장 작은 값이 맨 앞에 오도록

    while scoville[0] < K: # 가장 작은 값이 해당 스코빌 지수보다 낮을 동안
        
        if len(scoville) <= 1: # 하나밖에 없다면
            return -1 # 불가능
        else:
            n1 = heapq.heappop(scoville) # 가장 작은 수
            n2 = heapq.heappop(scoville) * 2 # 두번쨰로 작은 수 * 2
            heapq.heappush(scoville,(n1+n2)) # 그 값을 heapq에 추가
            cnt += 1 # 섞은 횟수 증가
    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))

# Good Explanation
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville) # pq로 만들기
    answer = 0
    while True:
        first = hq.heappop(scoville) # 가장 작은 값 빼기
        if first >= K: # 그 값이 스코빌 지수보다 크면
            break # 빠져나오기
        if len(scoville) == 0: # 못만들면
            return -1 # 불가능
        second = hq.heappop(scoville) # 두번째로 작은 값
        hq.heappush(scoville, first + second*2) # 연산한 값 힙큐에 추가
        answer += 1  # 섞은 횟수 1 증가

    return answer