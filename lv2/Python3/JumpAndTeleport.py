# My turn
def solution(n):
    ans = 0
    while n != 0: # n이 0이 아닐동안
        if n % 2 == 0: # n 이 짝수면
            n //= 2 # 나누기
        else: # 홀수면
            n -= 1 # n -= 1
            ans += 1 # 효율 += 1
    return ans
# 1001
# 1010
# 10101
solution(5) # 0101
solution(6) # 0110
solution(7) # 0111
solution(5000)

# Good Explanation
def solution(n):
    # 점프(Shift 연산), 이동 (1의 자리수의 0 -> 1 변환) => 2진표현( 점프 및 이동의 기록 )
    return bin(n).count('1') # 해당 수를 2로 나눴을 떄 홀수면 비트상 1 짝수면 0이기에
