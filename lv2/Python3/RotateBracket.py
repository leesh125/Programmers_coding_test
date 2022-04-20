def solution(s):
    answer = 0
    len_s = len(s) # 문자열의 길이

    for i in range(len_s): # 문자열의 길이만큼 
        tmp = s[i:] + s[:i] # 임시 리스트 = s를 왼쪽으로 회전한 것
        stack = [tmp[0]] # stack 첫번째에 임시 리스트 [0] 인덱스 추가
        for j in range(1,len_s): # 추가된 첫번째 제외한 나머지 문자들의 길이만큼
            if len(stack) == 0: # 스택에 암것도 없으면
                stack.append(tmp[j]) # 스택에 문자 추가
                continue # 반복문 다시 돌음
            # 짝이 맞는 괄호가 연달아 있다면 stack에서 짝이 맞는것을 추가하고 현재 문자를 추가 X
            if (stack[-1] == '(' and tmp[j] == ')') or (stack[-1] == '{' and tmp[j] == '}') or (stack[-1] == '[' and tmp[j] == ']'):
                stack.pop()
            else: # 짝이 안맞으면 
                stack.append(tmp[j]) # stack에 추가
        if len(stack) == 0: # 짝이 다 맞으면
            answer += 1 # 가능한 것 + 1
    
    return answer
print(solution("[](){}"))
print(solution("}]()[{"))

def is_valid(s): 
    stack = []
    for ch in s: # 해당 문자열에서 문자 하나씩
        if not stack: # stack이 비어있으면
            stack.append(ch) # 스택에 문자 추가
        # 스택이 비어있지 않을때,스택에 최상단과 현재 괄호가 짝이맞다면 꺼내기
        elif stack[-1] == '(':  
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True # 스택이 차있으면 False 짝이 다 맞아 떨어지면 True

def solution(s):
    answer = 0
    for i in range(len(s)): # 문자열 길이 만큼
        answer += is_valid(s[i:]+s[:i]) # 짝이 맞는지 수행을 해봄
    return answer