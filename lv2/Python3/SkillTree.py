# My turn
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees: # 스킬트리들
        index = [] # 인덱스를 저장할 배열
        flag = True # 조건을 만족하는지 안하는지

        for s in skill_tree: # 스킬트리의 한 문자씩 비교
            if s in skill: # 해당 스킬이 스킬리스트에 있으면
                if not index: # index 배열이 비어있다면
                    if skill.index(s) == 0: # skill의 인덱스가 첫번째 스킬리스트 원소이면
                        index.append(skill.index(s)) # index 추가하기
                    else: # 우선적으로 배워야 할 스킬이 아니면
                        flag = False # 거짓
                        break # 빠져나오기
                else: # # index 배열이 차있다면
                    if index[-1]-skill.index(s) != -1: # 마지막 인덱스원소와 현재 스킬의 인덱스의 차이가 -1이 아니라면
                        flag = False # 거짓
                        break # 빠져나오기
                    else: # 현재 스킬리스트 인덱스가 인덱스 배열에 있는 스킬리스트의 인덱스의 다음이라면
                        index.append(skill.index(s)) # index 추가

        
        if flag: # 참이라면
            answer += 1 # 답 되는 것 +=1

    return answer

print(solution("CBD", ["CED"]))


# Good Explanation
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees: # 스킬트리들
        skill_list = list(skill) # 현재 스킬트리를 리스트로

        for s in skills: # 한 문자씩 비교
            if s in skill: # 현재 스킬이 스킬리스트에 있을때
                if s != skill_list.pop(0): # 첫번째로 배워야 할 것이 아니라면
                    break # 빠져나오기
        else: # 다 빠져나오면
            answer += 1 # 답 += 1

    return answer