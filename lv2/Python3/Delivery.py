import heapq
def solution(N, road, K):
    INF = int(1e9) # 초반 무한대 길이(도달할 수 없다고 가정하고 시작)
    distance = [INF] * (N + 1) # 1-index 형식을 위해 +1
    graph = [[] for _ in range(N+1)] # 1-index 형식을 위해 +1
    
    for r in road: 
        graph[r[0]].append((r[1],r[2])) # 해당 좌표에서 타 좌표까지 거리를 그래프 인덱스의 append
        graph[r[1]].append((r[0],r[2])) # 양방향
    
    def dijkstra(start): # 다익스트라 알고리즘
        q = [] # 우선순위 큐
        heapq.heappush(q, (0,start)) # 거리, 현재 좌표 (거리순으로 우선순위 정렬->pop할때)
        distance[start] = 0 # 현재 좌표에서 현재 좌표까지 거리는 당연히 0

        while q: # q가 차있을 동안
            cur_dist, cur_now = heapq.heappop(q) # 큐에서, 현재까지 거리, 현재의 좌표 뽑아옴

            if distance[cur_now] < cur_dist: # 큐에서 뽑은 현재 좌표의 현재까지 거리가 현재 좌표의 최단경로보다 길면 
                continue # 이미 방문한 것으로 처리

            for now, dist in graph[cur_now]: # 현재 좌표에서 갈 수 있는 다음 좌표, 그 좌표까지 거리 추출
                cost = cur_dist + dist # 해당 좌표까지의 거리는 지금 좌표의 현재까지 거리 + 다음 좌표까지의 거리

                if cost < distance[now]: # 계산된 비용이 다음 좌표까지 최단경로보다 작으면
                    distance[now] = cost # 갱신
                    heapq.heappush(q, (cost,now)) # 해당 좌표와 해당 좌표까지 최단경로를 q에 추가(다음 경로 탐색을 위해)
    dijkstra(1) # 출발지 1부터 시작
    return len([dis for dis in distance if dis <= K]) # K보다 작은 경로들이 몇개 있는지

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)