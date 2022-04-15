# My turn
import re,copy
from collections import deque
from itertools import permutations

def solution(expression):
    answer = 0

    regex_operand = re.compile('\d+') # 피연산자들만 추출하는 정규표현식
    regex_operator = re.compile('[^\d]') # 연산자들만 추출하는 정규표현식
    operand = regex_operand.findall(expression) # 피연산자들 추출
    operator = regex_operator.findall(expression) # 연산자들 추출
    # 연산자들의 가능한 조합(permutation:중복 포함, combination: 중복 미포함)
    combination_operator = list(permutations(list(set(operator)), len(list(set(operator)))))
    q= deque() # 큐

    for i in range(len(operator)): # 피연산자와 연산자를 한줄로
        q.append(int(operand[i]))
        q.append(operator[i])
        if i == len(operator)-1: # 마지막 피연산자 추가
            q.append(operand[i+1])
    
    
    for combination in combination_operator: # 연산 우선순위
        q2 = copy.deepcopy(q) # q를 깊은복사한 q2(연산 우선순위 결과가 한바퀴 돌면 다시 계산을 해서 원래 식을 가져다 쓰기위해)
        
        for i in range(len(combination)): # 연산자 조합에서 첫번째
            k = 0 # 중간중간 빠져나가는 원소들때문에 고정된 인덱스 증가량 추가
            tmp_q2_len = len(q2) # q2 길이(총 인덱스 수)

            while True: # 반복 수ㅐㅇ
                n = q2.popleft() # 수식 가장 왼쪽에서 뽑아내기
                if n != combination[i]: # 우선순위 연산자가 아니라면
                    q2.append(n) # 큐 마지막 끝에 추가
                    k += 1 # 하나만큼 빠진 인덱스 체크
                else: # 우선순위 연산자면
                    before_num = q2.pop() # 가장 최근에 추가되었던 마지막 원소 추출(숫자일 수 밖에 없음)
                    next_num = q2.popleft() # 현재 큐에서 가장 왼쪽에 있는 원소 추출(숫숫자일 수 밖에 없음)
                    
                    # eval 쓸 수 있지만 안쓰는게 좋음
                    if combination[i] == '-': # 우선순위 연산이 -면
                        q2.append(int(before_num)-int(next_num)) # - 연산
                    elif combination[i] == '+': # 우선순위 연산이 +면
                        q2.append(int(before_num)+int(next_num))  #  +연산
                    else: # 우선순위 연산이 *면
                        q2.append(int(before_num)*int(next_num))  # *연산
                    k += 2 # 두개만큼 빠진 인덱스 체크(이전 것을 꺼내와서, 총 두개를 추출했기에)
                if k == tmp_q2_len: # 증가되는 인덱스가 총 길이만큼 왔을 때
                    break # 한 줄의 연산 끝내기

        answer = max(answer,abs(q2[0])) # 최댓값 갱신
        
    return answer

# print(solution("100-200*300-500+20"))
# print(solution("1+2+3"))
# print(solution("2-990-5+2"))
# print(solution("50*6-3*2"))
# print(solution("2-3"))

# 문자열 리스트 역순 우선순위로 계산
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations: # 연산자 에서
        a = op[0] # 첫번쨰 연산자
        b = op[1] # 두번째 연산자
        temp_list = []
        for e in expression.split(a): # 첫번째 연산자를 기준으로 문장을 나눔(가장 마지막에 계산하기 위해)
            temp = [f"({i})" for i in e.split(b)] # 두번째 연산자를 기준으로 괄호를 씌운채 문장을 나눔(마지막 이후에 계산하기 위해)
            temp_list.append(f'({b.join(temp)})')  # 괄호를 추가해 두번째 연산자로 다시 모음(이미 괄호가 씌어져서 연산 우선순위는 나눠짐)
        answer.append(abs(eval(a.join(temp_list)))) # 계산
    return max(answer)
print(solution("100-200*300-500+20"))