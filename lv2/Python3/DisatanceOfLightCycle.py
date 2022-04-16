def solution(grid):
    answer = []
    
    x_len = len(grid) # 행 길이
    y_len = len(grid[0]) # 열 길이
    # (행,열,방향) => x행 y열 ?방향으로 이동했음
    visited = [[[0 for _ in range(4)] for _ in range(y_len)] for _ in range(x_len)]

    for x in range(x_len):
        for y in range(y_len):
            for dir in range(4): # 0: 위, 1: 아래, 2: 오른쪽, 3: 왼쪽
                # 순회를 했을 때 현재 x,y,방향과 비교를 위해 따로 분리함
                cur_x = x 
                cur_y = y
                cur_dir = dir
                cnt = 0 # 이동 횟수
                while True: # 사이클 돌기
                    visited[cur_x][cur_y][cur_dir] += 1
                    cnt += 1 
                    if cur_dir == 0:
                        cur_x -= 1
                    elif cur_dir == 1:
                        cur_x += 1
                    elif cur_dir == 2:
                        cur_y += 1
                    elif cur_dir == 3:
                        cur_y -= 1
                    
                    # 범위 초과 처리
                    if cur_x < 0:
                        cur_x = x_len-1
                    elif cur_x >= x_len:
                        cur_x = 0
                    if cur_y < 0:
                        cur_y = y_len-1
                    elif cur_y >= y_len:
                        cur_y = 0
                    
                    # 이동 처리('S'면 현재 방향 그대로 유지)
                    if cur_dir==0: # 현재 위로 가는 방향
                        if grid[cur_x][cur_y] == 'L': # 'L'을 만났을 때
                            cur_dir = 3
                        elif grid[cur_x][cur_y] == 'R': # 'R'을 만났을 때
                            cur_dir = 2
                    elif cur_dir==1: # 현재 아래로 가는 방향
                        if grid[cur_x][cur_y] == 'L': # 'L'을 만났을 때
                            cur_dir = 2
                        elif grid[cur_x][cur_y] == 'R': # 'R'을 만났을 때
                            cur_dir = 3
                    elif cur_dir==2: # 현재 오른쪽으로 가는 방향
                        if grid[cur_x][cur_y] == 'L': # 'L'을 만났을 때
                            cur_dir = 0
                        elif grid[cur_x][cur_y] == 'R': # 'R'을 만났을 때
                            cur_dir = 1
                    elif cur_dir==3: # 현재 왼쪽으로 가는 방향
                        if grid[cur_x][cur_y] == 'L': # 'L'을 만났을 때
                            cur_dir = 1
                        elif grid[cur_x][cur_y] == 'R': # 'R'을 만났을 때
                            cur_dir = 0

                    if visited[cur_x][cur_y][cur_dir] >= 2: # 이미 방문했던 코스라면(중복된 코스 밟음) 
                        break # 빠져나오기

                    # 처음 돌아왔던 사이클이면
                    if x == cur_x and y == cur_y and dir == cur_dir:
                        answer.append(cnt) # 이동 경로 수 추가
                        break # 빠져나오기
    
    return sorted(answer)

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))