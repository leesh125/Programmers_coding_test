def solution(numbers, target):
    answer = 0
    
    def dfs(num, level): # dfs(합, 숫자의 단계)
        nonlocal answer # 해당 함수가 아닌 상위 함수의 변수

        if level == len(numbers): # 숫자의 단계가 마지막일때
            if num == target: # 합이 target과 같으면
                answer += 1 # cnt 누적
            return # 종료
        
        dfs(num + numbers[level], level + 1) # dfs 탐색 (다음 수를 +로) , 단계+1
        dfs(num - numbers[level], level + 1) # dfs 탐색 (다음 수를 -로) , 단계+1
        
    dfs(numbers[0], 1) # 처음 dfs 탐색 (첫번쨰 수까지 누적, 단계)
    dfs(-numbers[0], 1) # 처음 dfs 탐색 (첫번쨰 수(음수)까지 누적, 단계)

    return answer

print(solution([1, 1, 1, 1, 1],3 ))

# bfs 풀이

from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0,0)) # (sum, level)

    while q:
        total, level = q.popleft() # (현재 단계까지 합계, 현재 단계==인덱스)
        
        if level > len(numbers): # 현재 단계가 numbers의 길이를 초과했다면(인덱스 벗어남)
            break # 빠져나오기
        if level == len(numbers) and total == target: # 현재단계가 마지막이고 합계가 target과 같으면
            answer += 1 # cnt 누적
        
        if level < len(numbers): # 4단계 아래만(인덱스 떄문에)
            q.append((total+numbers[level], level+1)) # q에 추가
            q.append((total-numbers[level], level+1))

    return answer

print(solution([1, 1, 1, 1,1],3 ))

# Good Explanation
def solution(numbers, target):
    if not numbers and target == 0 : # 배열이 비어있고 target이 0이되면
        return 1 # 1 반환(경우의 수 1 추가)
    elif not numbers: # 배열이 비어있고 target이 0이 아니면
        return 0 # 0 반환(경우의 수 X)
    else:
        # 재귀 함수 인자로(현재 이후부터의 수 list, target에서 현재 수 빼기) : 최종적으로 target이 0이 될때까지
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
