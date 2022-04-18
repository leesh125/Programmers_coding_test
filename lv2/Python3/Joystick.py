# My turn
import copy
from collections import deque
def solution(name):
    moves = [-1,1] # 왼쪽 오른쪽 이동
    nameList = list(name) # 리스트로 변경

    def bfs(start): # bfs 탐색
        q = deque([start]) # (array,index,count)
        while q: # q에 값이 있을동안
            array, index, cnt = q.popleft() # 배열,인덱스,조이스틱 움직인 수
            cnt += min(ord(array[index]) - 65, 91 - ord(array[index])) # 현재 인덱스의 문자를 'A'로 만드는데 필요한 조이스틱 이동
            array[index] = 'A' # 'A'로 변경
            if array.count('A') == len(array): # 해당 배열이 전부 'A'면
                return cnt # 여태 움직인 조이스틱 수 반환
            for move in moves: # 왼쪽, 오른쪽 이동
                new_array = copy.deepcopy(array) # 배열에 해당 인덱스를 'A' 바꾼 새로운 배열을 복사
                new_idx = index + move # 왼쪽, 오른쪽 이동
                new_cnt = cnt + 1 # 조이스틱 +1
                q.append((new_array,new_idx,new_cnt)) # 새로운 배열, 새로운 인덱스, 새로운 cnt 추가

    return bfs((nameList,0,0)) # 처음부터 시작해서 나온 cnt 반환

print(solution("JBAABBB")) # 18
print(solution("JAZ")) # 문자열 길이 하나랑 2개도 테스트하기
print(solution("JEROEN"))
print(solution("JAN"))
print(solution("BBBBAAAABA"))

# Good Explanation
def solution(name):
    answer = 0
    n = len(name) # 문자열 길이

    # 기본적으로 해당 문자열의 모든 문자를 'A'로 바꾸기 위한 비용과 처음부터 끝까지 가기위한 이동 수를 기반으로 답을 구하는 과정을 추가

    def alphabet_to_num(char): # 알파벳을 숫자로 변환하는데 드는 조이스틱 이동 수
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name: # 모든 문자열의 문자를
        answer += alphabet_to_num(ch) # 'A'로 바꾸기위한 비용을 누적

    move = n - 1 # 처음부터 끝까지 가기위한 비용을 move에 담아두기
    for idx in range(n): # 0~마지막 인덱스까지
        next_idx = idx + 1 # 다음 인덱스를 next_idx에 담기
        while (next_idx < n) and (name[next_idx] == 'A'): # 다음 인덱스가 마지막 보다 작고, 다음 인덱스의 문자가 'A'면
            next_idx += 1 # 다음 인덱스 + 1('A'가 연달아 있는것을 찾기위해)
        distance = min(idx, n - next_idx) # (현재 인덱스, 전체길이-(마지막 'A'인덱스 +1)) 의 최솟값 구하기
        # (총 누적 거리, 현재 인덱스 + (전체길이-마지막 'A'의 인덱스 + 1) + 여태 이동했던 거리)의 최솟값 구하기
        move = min(move, idx + n - next_idx + distance) 

    answer += move # 모든 문자열 'A'로 바꾸기위한 총 비용 누적('A'로 만들기위한 비용 + 이동비용)
    return answer