from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(place,i,j):
    q = deque()
    q.append((i,j,2,False))
    visited = [[False] * 5 for _ in range(5)]
    visited[i][j] = True

    while q:
        x,y,cnt,p = q.popleft()

        if cnt == 0: continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                if place[nx][ny] == 'X': # 파티션
                    q.append((nx,ny,cnt-1,True))
                elif place[nx][ny] == 'P': # 사람
                    if not p:
                        return False
                elif place[nx][ny] == 'O': # 책상
                    q.append((nx,ny,cnt-1,p))
    return True

def solution(places):
    answer = []

    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place,i,j):
                        flag = False
                        break
            if not flag:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer