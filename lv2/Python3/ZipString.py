# My turn
def solution(s):
    answer = []

    if len(s) == 1: # 문자열 하나 입력되면 1 리턴
        return(1)
    
    s_list = list(s) # 리스트로 만들기
    
    # 1~문자열 길이만큼(절반 이상 나눠봤자 같은 쌍이 없음)
    for k in range(1,len(s)//2+1): 
        cnt = 1 # 다음 문자와 같을 때 증가할 변수
        arr=[] # 2개 이상 문자열을 나눌때 그 쌍을 담을 배열
        string = '' # 최종 압축 문자열(누적해서 결과까지)

        if k == 1: # k==1 (문자열 하나씩만 비교)
            for i in range(len(s_list)-1): # 이전 원소까지
                if s_list[i] == s_list[i+1]: # 현재 문자가 다음 문자와 같으면
                    cnt += 1 # cnt 증가
                else: # 현재 문자가 다음 문자와 다를때
                    if cnt != 1: # cnt가 세어졌다면
                        string += str(cnt) + s_list[i] # cnt와 현재 문자를 합친 문자열을 누적
                        cnt = 1 # cnt 초기화
                    else: # cnt가 안 세어졌다면
                        string += s_list[i] # 현재 문자 그대로 문자열 누적

                if i == len(s_list)-2: # 마지막 이전 문자
                    if cnt == 1: # cnt가 세어지지 않았다면
                        string += s_list[i+1] # 맨 마지막 문자 누적
                    else: # cnt가 세어져다면
                        string += str(cnt) + s_list[i] # cnt와 마지막 이전 문자 출력
            answer.append(len(string)) # 해당 문자열의 길이를 정답 배열에 추가
        else: # k != 1
            for i in range(len(s_list)): # 마지막 원소까지
                if i == 0: # 첫번째 문자면
                    string += s_list[i] # 문자 누적
                    continue
                
                if i % k == 0: # 만약 현재 인덱스가 k로 나눠떨어지면
                    arr.append(string) # 이전까지 누적되었던 문자를 arr 배열에 추가
                    string = '' # 문자 초기화
                    string += s_list[i] # 현재문자 다시 string에 기록
                else: # 그렇지 않으면(k로 안나눠지면)
                    string += s_list[i] # 현재 문자 누적

                if i == len(s_list)-1 and len(s_list) % i != 0: # 맨 마지막 원소 그리고 나머지 문자가 있을때
                    arr.append(string) # 누적된 문자를 arr 배열 추가

            
            test = '' # 최종 압축 문자열
            for i in range(len(arr)-1): # 마지막 이전까지
                if arr[i] == arr[i+1]:# 현재 문자가 다음 문자와 같으면
                    cnt += 1 # cnt 증가
                else:# 현재 문자가 다음 문자와 다를때
                    if cnt != 1:# cnt가 세어졌다면
                        test += str(cnt) + arr[i]# cnt와 현재 문자를 합친 문자열을 누적
                        cnt = 1# cnt 초기화
                    else:# cnt가 안 세어졌다면
                        test += arr[i] # 현재 문자 그대로 문자열 누적
            
                if i == len(arr)-2:# 마지막 이전 문자
                    if cnt == 1:# cnt가 세어지지 않았다면
                        test += arr[i+1]# 맨 마지막 문자 누적
                    else: # cnt가 세어져다면
                        test += str(cnt) + arr[i]# cnt와 마지막 이전 문자 출력
            answer.append(len(test))# 해당 문자열의 길이를 정답 배열에 추가

    return min(answer)

print(solution("acacacacacacbacacacacacac"))

# Good explanation
def compress(text, tok_len):
    # 토큰만큼 나눠 문자열 분리 저장
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = [] # 현재 단어와, cnt 저장할 배열
    cur_word = words[0] # 현제 딘어: 0번째 
    cur_cnt = 1 # 현재 cnt = 1
    for a, b in zip(words, words[1:] + ['']): # zip을 사용하여 현재원소와 다음원소 비교
        if a == b: # 같으면  
            cur_cnt += 1 # cnt 증가
        else: # 다르면
            res.append([cur_word, cur_cnt]) # 현재 저장된 단어와 현재 저장된 cnt 추가
            cur_word = b # 현재 단어를 갱신
            cur_cnt = 1 # cnt 1로 갱신
    # 갯수가 한개인건 그대로 계산 , 2이상 cnt가 있는 문자와 그 카운트 숫자(1카운트)의 합
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text): 
    # 1~문자열 길이 절반만큼의 토큰을 부여하고 이들중 최소 문자열 길이 출력
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))