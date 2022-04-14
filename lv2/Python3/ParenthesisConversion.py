def is_correct(strings):
    if strings[0] == ')' or strings[-1] == '(': # 처음과 맨끝 둘 중 짝이 안맞으면
        return False # 불가능
    left, right = 0,0

    for s in strings:
        if s == '(': 
            left += 1 # 왼쪽 cnt 추가
        else:
            right += 1 # 오른쪽 cnt 추가
        if right > left: # 이미 망가짐(오른쪽이 더 많으면 균형을 만들 수 없음)
            return False
    if left != right:
        return False # 좌우 균형이 안맞으면 False
    return True # 균형이 맞으면 True
    

def solution(p):
    if p == "": # 최종적인 v가 비어있기 까지(괄호 쌍은 맞기에 에러 X)
        return ""

    def fix_state(p):
        if len(p) == 0:
            return p
        u, v = "", ""
        left, right = 0,0

        for i in p: # 2. u,v 분리
            u += i
            if i == '(':
                left += 1
            else:
                right += 1
            if left == right:
                break
        v = p[len(u):]

        if is_correct(u): # 3.u가 올바른 괄호 문자열이면
            return u + fix_state(v) # 3.1수행한 결과 문자열을 u에 이어 붙인 후 반환
        else: # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
            tmp = "(" # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙이기
            tmp += fix_state(v) # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙이기
            tmp += ")" # 4-3. ')'를 다시 붙이기 
            for i in u[1:len(u)-1]: # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙이기
                if i == '(':
                    tmp += ')'
                else:
                    tmp += '('
            return tmp # 4-5. 생성된 문자열을 반환
  


    status = is_correct(p) # 첫번째 주어진 문자열로 test

    if status: # 올바른 괄호라면
        return p # 그대로 출력
    else: # 올바르지 않으면
        return fix_state(p) # 2단계로(u,v 분리)


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

# Good Explanation
def solution(p):
    if p=='': return p # 빈 문자열 그대로 반환
    r=True; c=0
    for i in range(len(p)): # 문자열 길이만큼 반복
        if p[i]=='(': c-=1 # 앞 문자가 '('이면  c-=1
        else: c+=1 # 앞 문자가 ')' 이면 c+=1
        if c>0: r=False # ')'가 더 많으면 r= False(쌍이 맞을 수 없음) 
        if c==0: # 균형 잡힙 괄호 일때
            if r: # 올바른 괄호라면
                return p[:i+1]+solution(p[i+1:]) # 3단계 수행 (u+재귀(v))
            else: # 올바르지 않은 괄호라면
                # 4단계 수행 '(' + 재귀(v) + ')' + 첫번쨰와 마지막을 제외한 u에대해 문자를 모두 바꾸고 => 이를 반환
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))