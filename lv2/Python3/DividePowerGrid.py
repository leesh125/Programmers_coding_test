# My turn
from collections import deque
def solution(n, wires):
    answer = int(1e9) # 최솟값 비교를 위한 임시 무한대 수
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)] # 무방향 그래프
    for wire in wires: # 양방향 그래프 연결
        graph[wire[0]][wire[1]] = 1
        graph[wire[1]][wire[0]] = 1


    def bfs(start): # bfs
        q = deque([start]) # 매개변수 좌표를 삽입
        visited = [False for _ in range(n+1)] # 각 노드마다 방문표시
        visited[start] = True # 매개변수 좌표를 방문처리
        cnt = 1 # 인접한 노드들의 누적개수를 담을 cnt 변수
        while q: # q에 값이 있으면
            now = q.popleft() # 현재 노드 빼기
            
            for i in range(1,n+1): # 1~마지막 노드까지
                if not visited[i] and graph[now][i] == 1: # 방문하지 않았고 인접했다면
                    q.append(i) # q에 인접한 노드 추가
                    cnt += 1 # 누적갯수 + 1
                    visited[i] = True # 해당 노드 방문 처리
            
        return cnt # 인접한 갯수 반환
    
    for start, end in wires: # 시작노드, 끝녿,
        graph[start][end] = 0 # 끊기
        graph[end][start] = 0 # 끊기
        answer = min(answer, abs(bfs(start)-bfs(end))) # 인접한 노드의 차이 최솟값 찾기(두개를 끊었으면 두 점을 기점으로 인접한 노드를 찾으면 됨)
        graph[start][end] = 1 # 복구
        graph[end][start] = 1 # 복구
    
    return answer

solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])

# Good Explanation
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))): # 현재 wire를 제외한 나머지 wire들
        s = set(sub[0]) # 첫번째 wire
        # 하나를 짜른 wire묶음에서 선택한 wire 중 하나의 숫자라도 겹치는게 있으면(& 연산) 중복 제거해서 set에 담기
        [s.update(v) for _ in sub for v in sub if set(v) & s] 
        ans = min(ans, abs(2 * len(s) - n)) # 인접한 점들 * 2 - n 을 해주면 나머지 집합과의 차이를 알 수 있음
    return ans

#solution(4,[[1,2],[2,3],[3,4]])
solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])