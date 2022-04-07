def count(board,n):
    temp = 0

    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                if cnt == 3:
                    temp += 1
            else:
                cnt = 1
        if temp > 0:
            break

        cnt = 1
        for j in range(1,n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                if cnt == 3:
                    temp += 1
            else:
                cnt = 1
        
    return temp

def solution(board):
    answer = 0
    n = len(board)

    for i in range(n):
        for j in range(n):
            if j+1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                temp = count(board,n)
                answer += temp
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            if i+1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                temp = count(board,n)
                answer += temp
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

    return answer if answer != 0 else -1

