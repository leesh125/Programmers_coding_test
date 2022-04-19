# My turn
def solution(n,a,b):
    cnt = 1 # 라운드 수
    while True: # 반복
        # a가 홀수일 때 b가 a+1 이거나, a가 짝수일 때 b가 a-1 이면
        if (a % 2 == 1 and b == a+1) or (a % 2 == 0 and b == a-1): 
            return cnt # a와b는 해당 라운드에서 붙음(라운드 반환)
        a = a//2 + a%2 # a/2 (ex. 3번째일때 이기면 순번이 2가 됨)
        b = b//2 + b%2 # b/2 (ex. 4번째일때 이기면 순번이 2가 됨)
        cnt += 1 # 라운드 증가
    
print(solution(8,7,4))

# Good Explanation
def solution(n,a,b):
    # 1을 빼서 두 선수의 위치를 0 - index 형식으로
    # a,b 사이의 거리가 멀면 최상단 비트가 차이가 남(2진수 이기 때문)
    # xor을 통해 최상단 비트가 찍힌 만큼의 비트 길이를 반환
    return ((a-1)^(b-1)).bit_length()

# Good Explanation2
def solution(n,a,b):
    answer = 0
    while a != b: # a와 b가 같기까지
        answer += 1 # 라운드 수 추가
        a, b = (a+1)//2, (b+1)//2 # (본인 위치 + 1) /2 를 한 몫이 다음 라운드 자기의 순번

    return answer