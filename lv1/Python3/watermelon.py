# My turn
def solution(n):
    wat = ["수", "박"]
    answer = ""
    for i in range(n):      # n까지
        answer += wat[i%2]  # 수,박을 계속 더함  
    return answer

# Good explanation
# (효율성 2n)
def water_melon(n):
    s = "수박" * n       
    return s[:n]       # 적혀진 수 까지의 인덱스 리턴