from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])

    # 가능한 모든 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col),i)) # [0,1,2,3]으로 가지는 모든 조합
    
    # 유일성과 최소성이 모두 충족되는 unique 리스트
    unique = [] 
    for c in combi: # 모든 조합을 한번씩 돌면서
        # relation을 돌면서 해당 column 조합에 포함되는 모든 원소를 tuple형태로 list에 추가한다
        tmp = [tuple(item[key] for key in c) for item in relation]

        if len(set(tmp)) == row: # 유일성
            flag = True

            for u in unique: # 최소성
                if set(u).issubset(set(c)): # 이미 있는 후보키 리스트의 원소가 해당 조합의 부분집합이면
                    flag = False # 추가를 안할거
                    break
        
            if flag: unique.append(c) # 유일성, 최소성 모두 만족되는 것들만 리스트에 추가

    return len(unique)


# Good Explanation
def solution(relation):
    answer_list = list()
    # 가능한 모든 조합 수 마다(비트 연산으로 팩토리얼 효과를 봄, 속성의 수 만큼 표현할 수 있는 조합의 경우의수)
    for i in range(1, 1 << len(relation[0])): 
        tmp_set = set()
        for j in range(len(relation)): # 행의 길이만큼
            tmp = ''
            for k in range(len(relation[0])): # 속성의 수 만큼
                if i & (1 << k): # 비트를 속성의 수만큼 순차적으로 이동시켰을때
                    tmp += str(relation[j][k]) # 해당 행의 현재 속성을 포함하는 것들을 문자열로 누적
            tmp_set.add(tmp) # 중복을 제거
        
        if len(tmp_set) == len(relation): # 유일성을 만족하는 것이 있다면
            not_duplicate = True # 최소성 확인을 위한 bool 변수
            for num in answer_list: # 현재 유일성 체크하는 리스트를 살펴볼 때
                if (num & i) == num: # & 비트 연산으로 중복되는 비트 자리가 있을 때
                    not_duplicate = False # 최소성 만족 X
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])