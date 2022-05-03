# My turn
def solution(n):
    dp = [False for _ in range(n+1)] # dp 이용
    dp[0],dp[1] = 0, 1 # 0 = 0 , 1 = 1

    for i in range(2,n+1): # 2부터 n까지
        dp[i] = dp[i-1] + dp[i-2] # 이전 것과 그 이전 것 더한 것이 현재값

    return dp[n] % 1234567

print(solution(13))
print(solution(5))

# Good Explanation
def fibonacci(num):
    a,b = 0,1 # 0,1 로 초기값
    for i in range(num):
        a,b = b,a+b # b = a, b = a+b 누적
    return a