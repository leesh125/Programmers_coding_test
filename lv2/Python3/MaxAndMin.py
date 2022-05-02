def solution(s): # 한줄충
    # int 형으로 변환후 정렬 한 것에서 가장 작은거 + " " + int 형으로 변환후 정렬 한 것에서 가장 큰거
    return sorted(s.split(' '), key= lambda x: int(x))[0] + ' ' + sorted(s.split(' '), key= lambda x: int(x))[-1]


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))

# Good Explanation
def solution(s):
    s = list(map(int,s.split())) # split된 걸 int로 바꾸고 리스트로
    return str(min(s)) + " " + str(max(s)) # 최솟값 + " " + 최댓값