from collections import deque

def bfs3(place,startX,startY):
    # 현재 좌표에서 비교 대상이 되는 모든 좌표의 x,y
    dx = [-1,1,0,0,-2,0,2,0,1,1,-1,-1] 
    dy = [0,0,-1,1,0,-2,0,2,1,-1,1,-1]
    visited = [[0] * 5 for _ in range(5)] # 방문 여부 체크
    
    q = deque()
    q.append((startX, startY)) # 0,0 부터 시작

    while q: # q가 차있을 동안
        x, y = q.popleft() # 시작점 뽑기
            
        for i in range(12): # 대상이 되는 좌표 모두 비교
            nx = x + dx[i] # 이동한 x좌표
            ny = y + dy[i] # 이동한 y좌표

            if nx <= -1 or nx >=5 or  ny <= -1 or ny >=5: # 범위 초과면 continue
                continue
            
            if not visited[nx][ny]: # 방문하지 않은 곳이라면
                if abs(dx[i]) + abs(dy[i]) < 2: # 이동한 좌표가 상하좌우 일때
                    if place[x][y] == 'P' and place[nx][ny] == 'P': # 상,하,좌,우가 둘 다 P이면
                        return 0 # 종료
                    else: # 상하좌우에 학생혼자 앉아 있ㄷ다면
                        q.append((nx,ny)) # q에 다음 비교할 좌표 추가
                        visited[x][y] = 1 # 현재 좌표를 방문 표시

                else: # 이동한 좌표가 대각선 일때(맨해튼 거리일 때)
                    if place[x][y] == 'P' and place[nx][ny] == 'P': # 대각선에 사람이 있을 시
                        if dx[i] == 0: # 가로로 2칸 떨어졌을때
                            if place[x][((ny+y)//2)] == 'O': # 그 사이에 칸막이가 아니라면
                                return 0 # 종료
                        elif dy[i] == 0: # 세로로 2칸 떨어졌을때
                            if place[((nx+x)//2)][y] == 'O': # 그 사이에 칸막이가 아니라면
                                return 0 # 종료
                        else: # 대각선 일 때
                            if place[x][ny] == 'O' or place[nx][y] == 'O': # 나머지 대각선이 모두 칸막이가 아니라면
                                return 0 # 종료
                    
    return 1 # 모든 제약이 통과되면 1 반환

def solution(places):
    answer = []

    for place in places: # 강의실 반복
        answer.append(bfs3(place,0,0)) # 해당 강의실 bfs 탐색

    return answer # 결과값 도출
# P = 응시자, O = 빈 테이블, X = 파티션
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]))

# Good Explanation
def check(place):
    for irow, row in enumerate(place): # 행 번호와 행의 쌍 
        for icol, cell in enumerate(row): # 열 번호와 열의 쌍
            # 해당 좌표가 'P'가 아니면
            if cell != 'P': 
                continue # pass

            # 현재 좌표가 'P' 일때 상,하,좌,우 비교
            if irow != 4 and place[irow + 1][icol] == 'P': # 마지막 행이 아니고 밑에 행이 'P'이면
                return 0 # 종료
            if icol != 4 and place[irow][icol + 1] == 'P': # 마지막 열이 아니고 오른쪽 열이 'P'이면
                return 0 # 종료
            if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X': # 행이 0,1,2 이고 두칸 아래가 'P'이면서 그 사이에 칸막이가 없을 때
                return 0 # 종료
            if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X': # 열이 0,1,2 이고 두칸 오른쪽이 'P'이면서 그 사이에 칸막이가 없을 때
                return 0 # 종료

            # 대각선 비교
            # 마지막 행,열이 아니면서 오른쪽 아래가 P이고, 오른쪽 칸과 밑에 칸 중 칸막이가 하나라도 없을 시
            if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
                return 0 # 종료
            # 마지막 행,열이 아니면서 왼쪽 아래가 P이고, 왼쪽 칸과 밑에 칸 중 칸막이가 하나라도 없을 시
            if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
                return 0 # 종료
    return 1 # 조건 모두 통과시 1 반환

def solution(places):
    return [check(place) for place in places]

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))