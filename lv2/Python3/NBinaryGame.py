def solution(n, t, m, p):
    answer = '0' # 모든 진수의 첫번쨰 수는 0
    all_count = t*m # 총 나올 숫자의 길이
    res = ''

    num = 1 # 1부터 시작(0은 이미 answer에 담음)
    while len(answer) <= all_count: # 나올 수 있는 길이의 수가 총 count보다 크면 break
        tmp = '' # 임시 문자열
        tmp_num = num # 임시 숫자 = num

        while tmp_num > 0: # 현재 임시 숫자가 0보다 클 동안
            tmp_num, mod = divmod(tmp_num, n) # divmod로 몫과 나머지 구하기
            if mod >= 10: # 만약 11진수 이상의 수에서의 나머지 값이 10이상이면
                tmp += chr(mod+55) # 'A'~'F'로 철
            else: # 나머지가 10 아래라면
                tmp += str(mod) # 나머지 그대로 추가
        answer += tmp[::-1] # 역순 정렬한 것을 answer에 누적시키기
        num += 1 # 다음 숫자로 비교
    
    for i in range(p-1,all_count,m): # 처음 튜브에 순서부터, 총 표현되는 숫자의 길이만큼, 인원수만큼 증가하여
        res += answer[i] # res에 현재 answer 인덱스 원소값 누적
    
    return res
solution(2,4,2,1)
solution(16,16,2,1)
solution(16,16,2,2)


