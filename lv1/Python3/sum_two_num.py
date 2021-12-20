# My turn
def solution(a, b):
    answer = 0

    if a > b:                
        while a+1!=b:     # 원래 a의 숫자까지 더하기 위해 +1
            answer += b   # answer에 b를 합해준다
            b += 1        # b를 하나씩 증가 
    elif b > a:
        while a!=b+1:
            answer += a
            a += 1
    else:
        answer = a

    return answer

# Good explanation 1
def adder(a, b):
    if a > b: a, b = b, a      # a가 b보다 크면 두 수를 교환
    return sum(range(a,b+1))   # a ~ b 까지 합을 반환

# Good explanation 1
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2   # 등차수열 
                                   # 항의 개수 n개, 첫째값 a, 마지막 값 l
                                   # sum = n(a+l) / 2