# My turn
def solution(arr):
    if len(arr) == 1:  # 배열 길이가 1이면
        return [-1]    # -1 리턴
    else:
        arr.remove(min(arr))   # 가장 작은 값 제거
        return arr             