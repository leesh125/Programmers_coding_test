# My turn
max_score = 0 # 제일 점수 차 많이 나는 화살루틴
answer = [] # 답이 되는 모든 것들을 담을 배열

def solution(n, info):
    visited = [False for _ in range(11)] # 방문체크(어느 점수의 화살을 방문했는지)
    ryan = [0 for _ in range(11)] # 라이언의 화실 루틴
    dfs(ryan,info,n,visited) # dfs 탐색(라이언 화살, 어피치 화살, 화살 갯수, 방문 체크)
    # 답이 되는 점수판을 정렬(낮은 것을 많이 쏜것이 뒤에 나오는 오름차순)
    return sorted(answer)[-1][::-1] if answer else [-1]

def dfs(ryan,appeach,n,visited): # dfs
    global answer,max_score # 최고 점수와 답 배열 가져오기
    
    if n == 0: # 화살을 다 쐈을 때
        score = get_score(ryan, appeach) # 라이언과 어피치의 점수차
        if score <= 0: # 0 이하면 비교 할 필요 X
            return # 끝내기
        elif score == max_score: # 만약 최고점수와 같다면 답 배열에 추가
            answer.append(ryan[::-1]) # 가장 낮은 점수 많이 쏜거 비교하려고
        elif score > max_score: # 최고 점수보다 높은 점수차 라면
            max_score = score # 현재 점수를 최고점수로
            answer.clear() # 답 배열 초기화
            answer.append(ryan[::-1]) # 현재 점수상태인 화살루틴을 답 배열에 추가
    elif n > 0: # 화살이 남았다면
        for i in range(len(ryan)): # 라이언 화살루틴
            if not visited[i]: # 방문 하지 않은 점수라면
                visited[i] = True # 방문처리
                # 점수가 0점대라면(마지막 도달) 라이언이 남은 화살을 다 쏘게끔, 아니면 어피치보다 1 더 크게한다(그래야 이기니까)
                ryan[i] = n if i == len(ryan)-1 else appeach[i] + 1 
                dfs(ryan,appeach,n-ryan[i],visited) # 현재 (라이언 화살루틴, 어피치 화살루틴, 빠진 화살 갯수 갱신, 방문처리) dfs
                ryan[i] = 0 # dfs 끝났다면 다시 초기화
                visited[i] = False # 방문도 초기화

def get_score(ryan,appeach): # 점수를 얻는 함수
    score = 0 # 0 초기화
    for i in range(-1,-12,-1): # -1 ~ 처음 인덱스
        if appeach[i] == 0 and ryan[i] == 0: # 둘 다 0이면 둘 다 0점
            continue
        elif appeach[i] >= ryan[i]: # 어피치가 높다면
            score -= ((i * -1) -1) # 누적 score 해당 점수만큼 -=
        else: # 라이언이 높다면
            score += ((i * -1) -1) # 누적 score 해당 점수만큼 +=
    return score # 점수 반환
#print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
#solution(1,[1,0,0,0,0,0,0,0,0,0,0])
#print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
#print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))

# Good Explanation 1
from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]

# Good Explanation2
from itertools import combinations_with_replacement
from collections import Counter

def solution2(n, info):
    max_diff, max_comb_cnt = 0, {}

    # 0 ~ 11 까지 숫자 중 반복을 허용하여 가질 수 있는 5 가지 수 모두 리턴
    for comb in combinations_with_replacement([range(11)], n): 
        cnt = Counter(comb) # 주어진 5개의 숫자 count 사전 형태로
        score1, score2 = 0, 0 # 라이언 점수, 어피치 점수
        for i in range(1, 11):
            if info[10-i] < cnt[i]: # 라이언 점수가 더 크면(어피치 현재 점수 화살보다 라이언의 현재 점수 화살이 더 크면)
                score1 += i # 라이언 점수 누적
            elif info[10-i] > 0: # 어피치 점수가 더 크면
                score2 += i # 어피치 점수 누적
                
        diff = score1 - score2 # 라이언 점수 - 어피치 점수
        if diff > max_diff: # 최고값보다 크면
            max_comb_cnt = cnt # 현재 라이언 점수 배열을 그대로
            max_diff = diff # 최고값 갱신
            
    if max_diff > 0: # 최고값이 1 이상이라면
        answer = [0]*11 # 화살 배열 만들고
        print(max_comb_cnt)
        for n in max_comb_cnt: # 화살 쏜 점수 : 몇 개
            answer[10-n] = max_comb_cnt[n] # 해당 점수에 해당되는 곳에 화살 갯수 넣어주기
        return answer # 어차피 낮은 점수부터 순회했기때문에 가장 첫번째 최고값 나왔던것이 가장 낮은 점수를 많이쏜 화살 루틴
    else:
        return [-1]
print(solution2(5,[2,1,1,1,0,0,0,0,0,0,0]))