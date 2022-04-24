def solution(m, n, board):
    answer = 0
    graph = [list(board[i]) for i in range(m)] # 리스트 형태로 변환
    same = {} # dic 형태로 팡 터질 블록들 담을 것임(중복 제거도 됨)
    while True: # 반복
        for d in range(n): # 열을 기준으로 dic을 담을거임(빈 공간 내릴 때 편하게 하려고)
            same[d] = []
        
        tmp = 0 # 팡 터질 블록들의 갯수
        for a in range(m-1): # 행(-1 까지만 해도 계산이 됨)
            for b in range(n-1): # 열
                now = graph[a][b] # 현재블록
                # 현재 블록에 값이 있고 조건에 맞다면
                if now and now == graph[a][b+1] and now == graph[a+1][b] and now == graph[a+1][b+1] and 'A'<=now<='Z':
                    for x1 in range(2): # 0,1 행
                        for y1 in range(2): # 0,1 열
                            if [a+x1,b+y1] not in same[b+y1]: # dic에 해당 열 리스트에 값이 없다면(중복 체크)
                                same[b+y1].append([a+x1,b+y1]) # 팡 터질 블록 추가
                                tmp += 1 # 갯수 추가
        answer += tmp # 누적 시키기
        
        if tmp == 0: # 더 이상 터질게 없다면 
            return answer # 답을 출력
        
        for i in range(n): # 열 dic 순회
            if same[i]: # 해당 열에 터지는 블록이 있다면
                #same[i].sort() # 일단 정렬(안해도 됨, 순차적으로 저장했기 때문에)

                for x,y in same[i]: # 터진 블록
                    graph[x][y] = False # false 처리
                
                while True: # 반복
                    move = 0 # 이동횟수
                    for c in range(m-2,-1,-1): # 마지막 행 -1 지점부터 0까지
                        if graph[c][i] and not graph[c+1][i]: # 해당 지점에 값이 있고 밑에 행이 False(터짐)이라면
                            graph[c][i], graph[c+1][i] = graph[c+1][i], graph[c][i] # 바꿔주기
                            move += 1 # 이동 횟수 +1
                    if move == 0: # 이동 한게 없다면 
                        break # 빠져나오기


#solution(8,5,["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"])
print(solution(6,6,["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ]))
#solution(3,8,["AAAAAAAA", "BBAAAACC", "BBAAAACC"])
#solution(2,2,["aa","aa"])
#print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
#print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
#print(solution(6,5,["CCZXZ","CCZXZ","XXZXZ","AAZAA","AAAAA","ZAAXX"]))
#solution(6,6,["OXXOXX", "OXXXXX", 'OOXXXX', 'OXXOXX', 'OXXXXX', 'OOXXXX'])
#solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"])


