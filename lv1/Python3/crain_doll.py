# My turn
def solution(board, moves):
    basket = []
    answer=0
    for m in moves:
        for b in range(len(board[1])):
            if board[b][m-1] != 0:
                basket.append(board[b][m-1])
                board[b][m-1] = 0
                break
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                answer +=2
                basket.pop()
                basket.pop()
    
    return answer

# Good explanation
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
