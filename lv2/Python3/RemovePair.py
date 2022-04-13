def solution(s):
    stk = [s[0]] # 스택에 첫 원소 문자 대입
    
    for i in range(1, len(s)): # 첫번째 문자부터 끝까지
        stk.append(s[i])  # 스택에 추가

        if len(stk) >= 2: # 스택 길이가 2 이상일 때
            if stk[-1] == stk[-2]: # 가징 마지막, 그 전 문자가 같으면
                stk.pop() # 꺼내기 * 2
                stk.pop()

    return 1 if len(stk) == 0 else 0 # 다 꺼내졌으면 1 아님 0

print(solution('baabaa'))