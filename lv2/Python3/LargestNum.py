def solution(numbers):
    answer = ''
    tmp = [] # 문자를 4자리로 만들어서 담을 리스트
    sum = 0
    for number in numbers:
        c = (str(number)*4)[:4] # 문자열 비교를위해 4자리로 맞춰줌
        length = len(str(number)) # 문자열의 길이(나중에 결과값시에 이 길이만큼 인덱싱)
        tmp.append((c,length)) # (4자리로 맞춘 문자열, 원래 해당 문자열의 길이)

    tmp.sort(reverse=True) # 역순 정렬(가장 큰 수 표현위해)
    if int(tmp[0][0]) == 0: # 가장 큰수의 시작이 0이면
        return '0' # 답은 0임

    for c, length in tmp: # 4자리 문자열, 원래 문자열의 길이
        answer += c[:length]

    return answer

# Good Explanation
def solution(numbers):
    numbers = list(map(str, numbers)) # 해당 숫자를 문자열 형태로 변환
    # 원소마다 문자열 길이를 *3(원소는 1000 이하이기에 1000 이하까지만 비교하기), 역순 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers))) # [0,0,0,0] 같은 리스트 처리를 위해 int형으로 바꿨다가 문자열로

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([97,978]))
print(solution([0,0,0,0]))

