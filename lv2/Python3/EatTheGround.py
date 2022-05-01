# My turn
def solution(land):
    len_land = len(land) # 행의 길이
    # dp
    for i in range(1, len_land): # 1 ~ 행의 길이 까지
        for j in range(4): # 모든 열 순회
            # 현재 값은 max(현재 값 or 현재 값 + 이전 행의 각 열의 값)
            land[i][j] = max(land[i][j], land[i][j] + land[i-1][(j+1)%4],land[i][j] + land[i-1][(j+2)%4],land[i][j] + land[i-1][(j+3)%4])

    return max(land[-1]) # 마지막의 최댓값 구함

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])

# Good Explanation
def solution(land):

    for i in range(1, len(land)): # 1 ~ 마지막 행
        for j in range(len(land[0])): # 모든 열 순회
            # 현재 값 = 이전 행에서의 열의 값중 최댓값 + 현재 값
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
