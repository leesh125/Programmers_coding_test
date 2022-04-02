import heapq

INF = int(1e9)  # 무한대
def solution(n, edges, k, a, b):
    count = 0
    graph = [[] for _ in range(n + 1)]
    for e in edges:
        graph[e[0]].append((e[1],1))

    for i in range(n):
        if i != a:
            if dijkstra(n,a,graph)[i] + dijkstra(n,i,graph)[b] <= k:
                count += 1
    return count

def dijkstra(n,start,graph):
    q = []  # 우선순위 큐
    heapq.heappush(q, (0, start))  # 우선순위 큐 삽입(거리오름차순 으로)
    distance = [INF] * (n + 1)
    distance[start] = 0  # 시작점의 최소비용은 0

    while q:
        dist, now = heapq.heappop(q)  # 우선순위 큐에서 pop(현재 노드의 최단비용,현재 노드)

        if distance[now] < dist:  # 현재 노드에 최단 거리가 큐에 있는 현재 노드 최단거리 작으면
            continue  # 갱신 안함(이미 방문한 노드임)

        for g in graph[now]:  # 현재 노드와 이어진 노드, 그 비용
            cost = dist + g[1]  # 현재 노드 최단거리 + 이어진 다른 노드까지의 거리

            if cost < distance[g[0]]:  # 그 비용이 현재 노드에 최단 거리보다 작으면
                distance[g[0]] = cost  # 갱신
                heapq.heappush(q, (cost, g[0]))  # 큐에 삽입
    return distance

