# My turn (정답 but 효율성 0)
# def solution(info, query):
#     answer = []
#     len_info = len(info)
#     len_query = len(query)
#     info_list = [[] for _ in range(len_info)]
#     query_list = [[] for _ in range(len_query)]

#     for i in range(len_info):
#         info_list[i] = info[i].split(' ')
#     for i in range(len_query):
#         query_list[i] = query[i].split(' and ')
#         food,score = query_list[i].pop().split(' ')
#         query_list[i].append(food)
#         query_list[i].append(int(score))
    
#     for q in query_list:
#         index = [i for i in range(len_info)]
#         for i in range(5): # info의 열
#             tmp = []
#             for j in index: # info의 행
#                 if i == 4:
#                     if int(info_list[j][i]) >= q[i]:
#                         tmp.append(j)
#                     continue
#                 else:
#                     if q[i] == '-' or info_list[j][i] == q[i]:
#                         tmp.append(j)
#             if len(tmp) == 0:
#                 index = []
#                 break
#             index = tmp
#         answer.append(len(index))
#     return answer
from bisect import bisect_left
def solution(infos, query):
    answer = []
    info_dict = {}

    # '-'의 경우의 수를 같이 추가해주는 이유: query에서 검색할 때 조건이 없는 경우에 같이 조회되기위해
    for info in infos: # 지원자의 정보
        info = info.split(" ") # 분리
        for lan in [info[0], "-"]: # 언어
            for job in [info[1], "-"]: # 직업
                for career in [info[2], "-"]: # 직급
                    for food in [info[3], "-"]: # 음식
                        if lan+job+career+food not in info_dict: # 해당
                            info_dict[lan+job+career+food] = []
                        info_dict[lan+job+career+food].append(int(info[4]))
    
    for key in info_dict.keys(): # 이분탐색으로 조건에 충족하는 점수의 수를 빠르게 뽑기위해
        info_dict[key].sort() # key에 있는 value 리스트를 오름차순 정렬
    
    for q in query: # 해당 쿼리를 하나씩 탐색
        lan,_,job,_,career,_,food,score = q.split() # and는 _처리(건너뛰기)
        score = int(score)
        key = ''.join(lan+job+career+food)
        if key not in info_dict: # key 값이 dict에 없으면
            answer.append(0) # 0 추가, 다음 쿼리로
            continue
        # 이분 탐색 1
        score_list = info_dict[key] # 해당 쿼리가 가지는 점수 리스트들
        len_score_list = len(score_list)
        start,end = 0, len_score_list-1 # 시작인덱스:0, 마지막 인덱스
        tmp = len_score_list # dict[key] 리스트에 점수가 없으면 0을 리턴하기 위해 tmp를 score_list의 길이만큼

        while start <= end: # 시작점이 끝점보다 작거나 같을 동안
            mid = (start + end) // 2 # 중간값 구하기

            if score <= score_list[mid]: # 해당 쿼리의 점수가 해당 쿼리가 가지는 점수리스트의 중간값보다 작거나 같으면
                end = mid - 1 # 절반 나눔(앞쪽에서 비교,끝점을 중간값-1로)
                tmp = mid # 현재 중간값을 임시 답 변수로
            else: # 해당 쿼리의 점수가 해당 쿼리가 가지는 점수리스트의 중간값보다 크면
                start = mid + 1 # 절반 나눔(뒤쪽에서 비교,시작점을 중간값+1로) 
        answer.append(len(score_list) - tmp)

        # 이분 탐색 2
        # score_list = info_dict[key] # 해당 쿼리가 가지는 점수 리스트들
        # index = bisect_left(score_list, score) # 쿼리의 점수가 점수 리스트에 들어갈 위치(bisect_left: 같은 점수 있을때 왼쪽 정렬)
        # answer.append(len(score_list) - index) # 전체 점수 리스트 길이에서 해당 점수가 들어갈 위치의 index 빼기(해당 점수보다 큰 수만 가져옴)
    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


