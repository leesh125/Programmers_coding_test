# My turn
def solution(s):
    # 빠른 처리를 위해 문자 시작이 ')' 이거나 문자 끝이 '(' 이면 진행할 필요 없음
    if s[0] == ')' or s[-1] == '(': 
        return False

    stack = [s[0]] # 처음 문자 집어 넣기
    for i in range(1,len(s)): # 1 인덱스 부터 문자열 끝까지
        if stack: # 스택이 차있다면
            if stack[-1] == '(' and s[i] == ')': # 맨마지막 들어온 것이 '(' 이고 현재 원소값이 ')' 이면
                stack.pop() # 스택 최상단 값 꺼내기
            else: # 아니면
                stack.append(s[i]) # 그냥 추가
        else: # 스택이 비어있을 땐
            stack.append(s[i]) # 그냥 추가
    
    return False if stack else True # 스택이 차있으면 False 비어있음 True

solution("(())()")

# Good Explanation
def is_pair(s):
    x = 0
    for w in s:
        if x < 0: # ')'이 더 많다면 비교 의미 없이 불가능함
            break
        # 문자가 '(' 이면 x += 1, 문자가 ')' 이면 x-=1, 이도저도 아니면 그냥 x
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0 # x가 0이면 조건 충족