from collections import deque
def solution(maps):
    n,m = len(maps), len(maps[0]) # 행, 열의 길이

    def bfs(): # bfs 탐색
        dx = [-1,1,0,0] # x가 이동할 좌표
        dy = [0,0,-1,1] # y가 이동할 좌표
        visited = [[0] * m for _ in range(n)] # 방문했는지 안했는지 체크를 위한 리스트
        q = deque() # 큐 사용
        q.append((0,0)) # 시작점(0,0) 추가

        while q: # q가 비지 않을동안
            x,y = q.popleft() # q 가장 앞에거 꺼내오기

            for i in range(4): # x,y가 이동하는 거리 (상,하,좌,우)
                nx = x + dx[i] # 이동한 x = nx
                ny = y + dy[i] # 이동한 y = ny

                if 0 > nx or nx >= n or 0 > ny or ny >= m: # nx, ny가 범위를 벗어나면
                    continue # 다시
                if maps[nx][ny] == 0: # 지나갈 수 없는 곳이라면
                    continue # 다시
                if not visited[nx][ny]: # 방문하지 않은곳이라면
                    visited[nx][ny] = visited[x][y] + 1 # 방문 체크 +1(즉 이동거리)
                    q.append([nx,ny]) # q에 추가
        return visited # 이동거리가 담긴 리스트 반환

    answer = bfs() # 리스트를 받음
    # 도달할 수 있다면 처음좌표(1) 을 추가한 것을 반환 도달 못하면 -1 반환
    return answer[n-1][m-1]+1 if answer[n-1][m-1] != 0 else -1 

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
