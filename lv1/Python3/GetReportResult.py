# My turn
def solution(id_list, report, k):
    answer = []

    user_list = [] # 신고자 리스트
    black_list = {} # {신고당한 사람: 몇 번 신고 당했는지}
    k_black_list = {} # 2번 이상 신고당한 사람 담은 dict(연산을 간단하게 하기 위해 따로 생성)
    reporter_list = {} # {신고 한 사람: 신고를 당한 사람}

    for i in range(len(report)):
        start,end = report[i].split() # 신고자, 피신고자
        user_list.append((start,end)) # (신고자, 피신고자)를 신고자 리스트에 담으ㅁ
    user_set = list(set(user_list)) # 중복 신고 제거
    
    for user in user_set: # 신고자, 피신고자
        if user[1] not in black_list: # 피신고자가 블랙리스트에 없으면
            black_list[user[1]] = 1 # 신고 건수 => 1
        else: # 이미 블랙리스트에 있으면
            black_list[user[1]] = black_list[user[1]] + 1 # 신고 건수 += 1
    
    for black_user in black_list: # 피신고자
        # 피신고자의 신고 건수가 K보다 크거나 같고 2번 이상 신고당한 사람을 담은 dict에 포함되어 있지 않으면
        if black_list[black_user] >= k and black_user not in k_black_list: 
                k_black_list[black_user] = black_list[black_user] # 추가
    
    for user in user_set: # 신고자, 피신고자
        if user[1] in k_black_list: # 2번이상 신고받은 피신고자
            if user[0] not in reporter_list: # 신고자가 {신고 한 사람: k번이상 신고한사람의 신고건수} dict에 없으면
                reporter_list[user[0]] = 1 # 1
            else:
                reporter_list[user[0]] += 1 # 이미 있으면 += 1
 
    for id in id_list: # id를 하나씩 확인하면서
        # 해당 유저가 k번이상 신고한사람 dict에 있으면 그 건수를 출력 없으면 0 출력
        answer.append(reporter_list[id]) if id in reporter_list else answer.append(0)
        
    return answer

# Good explanation
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list} # {유저: 신고당한 건수}

    for r in set(report): # 신고자, 피신고자(=r.split()[1])
        reports[r.split()[1]] += 1 # 유저의 신고건수 갱신

    for r in set(report): # 신고자(=r.split()[0]), 피신고자(=r.split()[1])
        if reports[r.split()[1]] >= k: # 신고당한 건수가 k개 이상인 유저
            # 신고 건수가 k개 이상인 사람을 신고한 신고자의 인덱스 값에 += 1
            answer[id_list.index(r.split()[0])] += 1

    return answer