# My turn
def solution(numbers):
    answer = []

    for number in numbers: # 하나씩 비교
        if number % 2 == 0: # 짝수이면 마지막 비트 0 이기에 이것을 1로만 바꿔주면 최소 숫자임
            answer.append(number+1) # 그말은 즉 현재 숫자 + 1 이라는 소리
        else: # 홀수면
            bit = list(bin(number).lstrip('0b')) # 이진수로 바꾼 후 '0b' 제거
            flag=False # 01 -> 10 으로 바꾸는 게 제일 작은 수임
            for i in range(len(bit)-1,0,-1): # 비트 끝 자리에서부터
                if bit[i] == '1' and bit[i-1] == '0': # '01' 형태면
                    bit[i],bit[i-1] = bit[i-1],bit[i] # 둘을 바꿔줌
                    flag = True # 깃발
                    break 
            if flag: # 깃발 체크면
                answer.append(int(''.join(bit),2)) # 01 -> 10 으로 바꾼 수를 10진수로 변환
            else: # 깃발 체크 X면
                answer.append(int('10'+''.join(bit[1:]),2)) # 앞자리 비트를 '10'으로 바꿔준 후 10진수 변환
    return answer


# Good Explanation
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers): # 0-index 형식, 숫자 (enumerate 할 필요 X)
        # 1. 현재 숫자와 최소 만족조건인 현재 숫자 +1을 XOR 연산을 함
        # 1.1 짝수인 경우 끝 비트만 차이가 나므로 >> 2 해도 0임
        # 1.2 홀수인 경우 끝부터 최고점 비트까지 이어가다 '0'이 나오는 지점 부터 끝 비트 까지 1로 채워진 결과가 나옴
        # 2. 홀수: 홀수의 답은 현재 숫자의 비트 중 '01' 부분을 '10'으로 바꿔주면 됨
        # 2.1 현재 숫자 + 1의 비트는 일단 '01'이 부분이 '10'으로 무조건 바뀜
        # 2.2 그럼 이제 그 뒤에 비트숫자를 처리해야하는데, 이는 XOR한 비트('0'이 나오는 시점부터 1이 쭉이어짐)에서 '10'처리를 위한 2자리 비트만 오른쪽으로 이동시켜준다
        # 2.3 그 값을 현재 숫자 +1 에 더해준다.
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer
solution([2,9])