# My turn
def solution(n):
    answer = 0

    n_list = list(str(n))  # 정수를 문자열로 그리고 배열로 변환
    n_list.sort(reverse=True)  # 역순으로 정렬
    strn = "".join(n_list)  # join하여 다시 문자열로
    
    return int(strn) # 정수로 변환
    
print(solution(118372))

# Good explanation
def solution(n): # 내 풀이와 같음
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))