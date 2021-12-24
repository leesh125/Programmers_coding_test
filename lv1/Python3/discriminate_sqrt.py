# My turn
def solution(n):
    sn = int(n ** 0.5)  # 입력받은 숫자에 제곱근을 구함 
    if sn * sn == n:    # 그 두개를 다시 곱했을때 입력받은 숫자라면 (정확히 .0으로 나누어진 것이였다면)
        return (sn+1)**2  # (n+1)**2 출력
    else:
        return -1

print((131 ** 0.5) % 1 == 0 )

# Good explanation
def nextSqure(n):
    sqrt = n ** (1/2)  # 제곱근 구하기

    if sqrt % 1 == 0:  # 제곱근을 1로 나웠을 때 나머지가 0이면(제곱근이 아니면 나머지가 0이 아님)
        return (sqrt + 1) ** 2
    return 'no'