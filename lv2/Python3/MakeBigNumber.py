# from itertools import combinations
# def solution(number, k):
#     number = list(map(int,number))
#     return ''.join(map(str,max(list(combinations(number,len(number)-k)))))


def solution(number, k):
    answer = ''
    
    len_number = len(number) # 숫자의 길이
    length = len_number - k # 만들 자릿수
    index = 0 # 처음 인덱스 0 시작
    while length > 1: # 만들 자릿수가 1보다 작으면 멈춤
        tmp_index = 0 # 출발 인덱스를 변동하기 위한 후에 더할 인덱스
        tmp = number[index:len_number-length+1] # 첫번째 자릿수가 가질 인덱스 범위는 처음부터 (전체 길이 - 만들 자릿수 +1)
        big = '0' # 가장 큰값을 대입하기 위한 변수
        for i in range(len(tmp)): # 첫번째 자릿수가 가질 인덱스 범위에서 최댓값 추출
            if tmp[i] == '9': # 그게 9면 제일 크기때문에
                big = '9' # 가장 큰값 = 9
                tmp_index = i # 해당 (더할)인덱스를 담기
                break # 빠져나오기
            elif tmp[i] > big: # 9가 이나면 비교를 해봐야함, 현재 인덱스 수가 가장 큰값이면
                big = tmp[i] # 갱신
                tmp_index = i # 해당 (더할)인덱스를 담기
        index += tmp_index+1 # 다음 비교 인덱스는 현재 인덱스 +1부터임
        answer += big # 해당 인덱스 범위내에서 가지는 큰값을 추가
        length -= 1 # 만들 자릿수 -1
    # 아직 비교할 뒷자리가 하나 남았다면 그중에서 큰 값을 더한 문자열을 반환
    return answer + max(number[index:]) if index < len_number else answer




# Good Explanation
def solution(number, k):
    stack = [number[0]] # 첫번째 수를 스택에
    for num in number[1:]: # 두번째 문자부터 비교
        # 스택이 차있고, 스택 최상단이 현재 숫자보다 작고 k가 0이상일 때
        while len(stack) > 0 and stack[-1] < num and k > 0: 
            k -= 1 # 만들 자릿수 -1
            stack.pop() # 스택 최상단을 빼낸다(갱신하기 위해)
        stack.append(num) # 이전 최상단 값보다 더 큰값을 추가
    if k != 0: # 제거 횟수가 다 사용 안되었을 경우(숫자가 내림차순 식으로 나타났을때 pop을 안하기에)
        stack = stack[:-k] # 현재 스택에서 뒤에 인덱스를 현재 k 만큼 뺀값
    return ''.join(stack) # join
#print(solution("1924", 2))
#print(solution("1231234", 3))
print(solution("54321", 2))