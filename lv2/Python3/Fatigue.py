# My turn
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    all_combi = list(permutations(dungeons,len(dungeons))) # 모든 던전 루트 경우의 수

    for combi in all_combi: # 각 경우의 수마다
        real_k = k # k 초기화
        cnt = 0 # 가능횟수 0 초기화
        for need_f, use_f in combi: # 필요 피로도, 소모 피로도
            if real_k >= need_f: # k가 필요 피로도 이상이면
                cnt += 1 # 던전 클리어 가능 +1
                real_k -= use_f # 피로도 빼주기
        answer = max(answer,cnt) # 가장 큰 cnt 추출
    
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))

# Good Explanation 1
# for: (인덱스 - 최소 필요, 소모 피로) 형식의 반복자에서
# if k >= m: 가 최소 필요보다 클 경우
# max(): (k - 소모 피로, 클리어 던전을 뺀 던전 배열)을 재귀 형태로 진행해서 가장 큰값을 추출
# or[0]: 빈값([])은 [0]
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])

# Good Explanation 2
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer: # 던전 클리어 카운트가 가장 큰 누적 던전 클리어 카운트 보다 크면
        answer = cnt # 갱신

    for j in range(N): # 던전 루트 갯수 만큼
        if k >= dungeons[j][0] and not visited[j]: # k가 현재 던전의 최소 필요 이상이고, 방문하지 않은곳이라면
            visited[j] = 1 # 방문한 곳으로 처리
            # (소모 피로 빼준 k, 클리어 +1, 던전 배열), 즉 모든 루트를 방문처리 할 수 있다/
            dfs(k - dungeons[j][1], cnt + 1, dungeons) 
            visited[j] = 0 # 백트랙: 다음 던전을 시작점으로 할 때 비교했던 던전을 0으로 초기화해서 들리게끔

def solution(k, dungeons):
    global N, visited
    N = len(dungeons) # N: 던전 루트 갯수
    visited = [0] * N # 방문 표시
    dfs(k, 0, dungeons) # 현재 피로도, 던전 클리어 카운트, 던전 배열
    return answer