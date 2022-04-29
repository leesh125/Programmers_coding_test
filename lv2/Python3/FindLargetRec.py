def solution(board):
    answer = 0
    len_board_row = len(board) # 행의 길이
    len_board_col = len(board[0]) # 열의 길이

    for i in range(1,len_board_row): # 1 ~ 행길이까지
        for j in range(1,len_board_col): # 1 ~ 열길이까지
            if board[i][j] != 0: # 0이 아니라면
                board[i][j] = min(board[i-1][j-1],board[i][j-1],board[i-1][j]) + 1 # dp 이용
                # 최대 사각형 길이를 구하기 위해선 본인 이전의 사각형이 최대이어야 한다.
    
    for b in board: # 최댓값 추출
        answer = max(answer,max(b))

    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))