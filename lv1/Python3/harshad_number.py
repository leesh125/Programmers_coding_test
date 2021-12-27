# My turn
def solution(x):
    answer = True
    sum = 0
    real_x = x

    if x < 10: # 1~9 는 하샤드 수
        return True

    while x >= 10: # x가 10보다 크면
        sum += x % 10 # 일의 자리를 계속 더함
        x //= 10 # 1의 자리를 버림

    return True if real_x % (sum+x) == 0 else False # 하샤드면 true

# Good explanation
def Harshad(n):
    # n을 string으로 하고 각 자리마다 다시 int형 반환으로 합을 구함
    return n % sum([int(c) for c in str(n)]) == 0
