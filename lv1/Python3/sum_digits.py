# My turn
def solution(n):
    answer = 0
    stn = str(n)  # 숫자를 문자로 변환
    
    for i in range(len(stn)):  # 문자 하나하나
        answer += int(stn[i])  # 숫자로 변환
    return answer

print(solution(619))

# Good explanation 1
def sum_digit(number):   # 재귀함수
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

# Good explanation 2
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    # map(f, iterable) : 각 요소가 함수 f에 희해 수행된 결과를 묶어서 리턴
    return sum(map(int,str(number))) 
    