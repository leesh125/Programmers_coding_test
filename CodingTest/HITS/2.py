import heapq

def solution(n, quests):
    deq = []
    answer = []

    dp = [[0]*(n+1) for _ in range(n+1)]

    for quest in quests:
        dp[quest[0]][quest[1]] = 1
    
    for i in range(1, n+1):
        cnt = 0
        before_list = []
        for j in range(1, n+1):
            if dp[j][i] == 1:
                before_list.append((j,i)) 

        if len(before_list) == 0:
            answer.append(i)
        else:
            for before,after in before_list:
                if before in answer:
                    cnt += 1
                    dp[before][after] = 0
            if cnt == len(before_list):
                answer.append(i)
            else:
                heapq.heappush(deq, i)
    
    while deq:
        num = heapq.heappop(deq)
        cnt = 0
        for i in range(1,n+1):
            if dp[i][num] == 1:
                if i in answer:
                    answer.append(num)
                    dp[i][num] = 0
                else:
                    heapq.heappush(deq, i)

    return answer


print(solution(5, [[1,3],[1,4],[3,5],[5,4]]))