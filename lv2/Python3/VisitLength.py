# My turn
def solution(dirs):
    answer = 0 # 답
    # 방문 배열([시작행,시작열,끝행,끝열])
    visited = [[[[False for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]
    start_row,start_col,end_row,end_col = 5,5,5,5 # 가운데에서 시작
    visited[5][5][5][5] = True # 방문 처리(굳이 안해도됨)

    for dir in dirs: # 방향
        flag = False # 조건에 충족하는지 안하는지
        if dir == 'U' and start_row != 0: # U이고 시작행이 0이 아니면
            end_row -= 1 # 다음 이동할 행 -= 1
            flag = True # 조건 참
        elif dir == 'D' and end_row != 10: # D이고 시작행이 10(끝)이 아니면
            end_row += 1 # 다음 이동할 행 += 1
            flag = True # 조건 참
        elif dir == 'L' and start_col != 0: # L이고 시작열이 0이 아니면
            end_col -= 1 # 다음 이동할 열 -= 1
            flag = True # 조건 참
        elif dir == 'R' and end_col != 10: # R이고 끝행이 10(끝)이 아니면
            end_col += 1 # 다음 이동할 열 += 1
            flag = True # 조건 참
         
        if flag and not visited[start_row][start_col][end_row][end_col]: # 조건 충족하고 들린 루트가 아니라면
            answer += 1 # 답 += 1 
            visited[start_row][start_col][end_row][end_col] = True # 양방향 루트 추가
            visited[end_row][end_col][start_row][start_col] = True
        start_row, start_col = end_row, end_col # 끝행과 끝열을 다음 시작행과 시작열로 교체
    
    return answer

#solution("ULURRDLLU")

# Good Explanation
def solution(dirs):
    s = set() # 중복 제거 집합
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)} # dict 형식
    x, y = 0, 0 # x좌표 y좌표 0,0
    for i in dirs: # 방향
        nx, ny = x + d[i][0], y + d[i][1] # 이동할 좌표 = 현재 좌표에서 이동할 문자에 해당되는 인덱스 +
        if -5 <= nx <= 5 and -5 <= ny <= 5: # x,y 좌표가 범위내에 있다면
            s.add((x,y,nx,ny)) # 양방향 추가
            s.add((nx,ny,x,y))
            x, y = nx, ny # 이동한 좌표를 현재 좌표로
    return len(s)//2 # 양방향 간선이라 //2 해줌

solution("LULLLLLLU")