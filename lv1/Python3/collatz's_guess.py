# My turn
def solution(num):
    answer = 0
    
    while answer <= 500: #500번 반복
        if num == 1: # 1이면 
            break    # 0 리턴
        answer += 1  # 하나씩 증가
        if num % 2 == 0: # 짝수이면
            num /= 2     
        else:
            num = num * 3 + 1

    return answer if answer <= 500 else -1 # 반환

# Good explanation
def collatz(num):
    if num == 1: # 1이면 
        return 0    # 0 리턴
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1 # 짝수이면 앞에거 
        if num == 1: # 1이면 바로 반복 횟수를 반환
            return i + 1
    return -1 # 500번 시도해도 안나오면 -1