# My turn
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q= deque() # 큐

    for city in cities: # 도시
        upper_city = city.upper() # 도시명을 대문자로 통일화
        if upper_city not in q: # 해당 도시가 큐에 없다면
            answer += 5 # cache miss
        else: # 큐에 해당 시가 있다면
            q.remove(upper_city) # 해당 도시를 제거
            answer += 1 # cache hit
        q.append(upper_city) # 큐에 삽입
        if len(q) > cacheSize: # q 길이가 cacheSize를 초과했다면
            q.popleft() # LRU(가장 오래된 것 빼내기)

    return answer

solution(3, ["A","B","A"])
#solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
#solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])

# Good Explanation
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize) # maxlen으로 큐(캐쉬) 크기 정함
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time