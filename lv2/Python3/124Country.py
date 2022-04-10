def solution(n):
    answer = []
    while n:
        t = n % 3
        if t == 0: # 3으로 나눠떨어질 때 4를 추가해야함
            t = 4 
            n -= 1 # 0,1,2 -> 1,2,4 로 미뤄야 한다 따라서 1을 빼준다
        answer.append(str(t)) # 3진법에 의한 나머지를 종합
        n //= 3
    
    return ''.join(answer[::-1]) # 3진법 역순으로 표현하면 정답
    


print(solution(40))

# Good Explanation
def change124(n):
    num = ['1','2','4'] # 1, 2, 4
    answer = ""


    while n > 0: # 계속 나누기
        n -= 1 # 배열원소 인덱스를 표현하기위해 -1
        answer = num[n % 3] + answer # 누적하여 표현
        n //= 3 # n을 3으로 나눈 몫으로

    return answer