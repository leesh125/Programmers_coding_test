# My turn
def solution(msg):
    answer = []
    len_msg = len(msg) # 문자열의 길이
    index = 1 # 인덱스 1부터 시작
    dic_index = 27 # dic에 추가될 인덱스는 27부터 시작
    dic = {} # 단어를 담을 dict

    if len_msg > 1: # 1이상 긴 문자열일떄
        dic[msg[0]+msg[1]] = dic_index # 0,1 인덱스 원소를 더한 것을 사전에 담기
        dic_index += 1 # dic index 추가하기
        answer.append(ord(msg[0])-64) # 0번째 원소는 무조건 답 배열에 추가됨

    
    while index < len_msg: # 인덱스가 문자열 길이보다 작을동안
        now = msg[index] # 현재 인덱스 원소값을 now에
        if index+1 == len_msg: # 다음 인덱스 원소가 끝이라면
            next = '' # 아무것도 추가하지 않기
        else: # 다음 인덱스 원소가 있으면
            next = msg[index+1] # 기억해놨다가
        tmp = now + next # 현재 입력에 추가

        if tmp not in dic: # 사전에 없는 것이라면
            dic[tmp] = dic_index # tmp를 dic에
            dic_index += 1 # dic index += 1
            answer.append(ord(msg[index])-64) # 현재 입력을 answer 배열에 담기
            tmp = '' # tmp 초기화
        else: # 사전에 이미 있는 것이라면
            tmp_index = index + 2 # 임시 인덱스를 현재 인덱스 +2 로 설정
            
            while tmp_index < len_msg: # 임시 인덱스가 문자열 끝까지 가지 않을동안
                remember = tmp # 현재 tmp 문자열을 기억해놓기
                tmp += msg[tmp_index] # tmp에 다음 인덱스 원소값 추가
                if tmp not in dic: # 사전에 없는 것이라면
                    dic[tmp] = dic_index # tmp를 dicd에
                    dic_index += 1 # dic index +=1
                    answer.append(dic[remember]) # 기억해놨던 것의 사전 값을 answer 배열에 담기
                    break # 빠져나오기
                tmp_index += 1 # 사전에 있다면 다음것도 추가해서 비교

            if tmp_index >= len_msg: # tmp 인덱스가 끝에 도달했다면 바깥 while문을 더이상 수행하지않기에
                answer.append(dic[tmp]) # 남아있느 tmp 배열에 있는 문자열을 마지막으로 추가
            index = tmp_index -1 # 2만큼 더해준 tmp_index -1
        
        index += 1 # 바깥 while문 한번 돌면 인덱스 1증가
    
    return answer if answer else [1] # 답이 있으면 답 출력 없으면 1

print(solution("A"))
#print(solution("TOBEORNOTTOBEORTOBEORNOT"))
#print(solution("ABABABABABABABAB"))

# Good Explanation

def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)} # 1 ~ 26 인덱스에 A ~ Z 까지 삽입
    num = 27 # 다음 dic에 추가될 문자열 인덱스 27 부터 시작
    while msg: # 문자열
        tt = 1 # 1 인덱스
        # 해당 인덱스 전까지 문자가 tmp에 있고 문자열 길이보다 작거나 같을때(해당 문자열이 없으면 while문 빠져나옴)
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1 # tt를 1 증가시켜서 다음 문자열까지 확인
        tt -= 1 # 확인이 끝났으면 tt-1(dic에 있는 문자열 까지만 처리하려고)
        if msg[:tt] in tmp.keys(): # 위에서 확인한 이미 존재하는 문자열이면
            answer.append(tmp[msg[:tt]]) # tt까지의 문자열 value를 answer에 추가
            tmp[msg[:tt + 1]] = num # 사전에 현재 입력 + 다음 글자 를 추가
            num += 1 # dic의 key값 1 증가
        msg = msg[tt:] # 비교했던 길이만큼은 제외
    return answer

# Good Explanation 2
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 알파벳
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))} # zip을 사용하여 알파벳의 value 삽입
    answer = []

    while True:
        if msg in d: # 헤딩 문자열이 이미 dic에 있다면
            answer.append(d[msg]) # 그것의 value를 담기
            break # while문 빠져나오기
        for i in range(1, len(msg)+1): # 1 ~ 문자열 길이 까지
            if msg[0:i] not in d: # 해당 문자열이 dict 에 없다면
                answer.append(d[msg[0:i-1]]) # 이전까지의 문자열의 value를 answer에 담기
                d[msg[0:i]] = len(d)+1 # 현재까지의 문자열을 새로이 dic에 담기(dic에 길이 +1을 해주면 됨)
                msg = msg[i-1:] # i 이전 문자열 부터 새로이 비교
                break

    return answer