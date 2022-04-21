# My turn
from itertools import combinations
def solution(clothes):
    answer = 0
    dic = {} # 옷을 담는 해쉬
    combi = []
    all_combi = []

    for cloth in clothes: # 모든 옷마다
        if cloth[1] not in dic: # 옷 종류가 dic에 없으면
            dic[cloth[1]] = 1 # 1추가
        else: # 이미 있는 종류면
            dic[cloth[1]]+=1 # +=1
        answer += 1 # 1개짜리는 이미 계산하기 위해
    for d in dic: 
        combi.append(dic[d]) # 각 옷의 종류별 옷의 갯수를 담음
    
    len_combi = len(combi) 
    if len_combi == 30: # 만약 30 종류라면
        return 2 ** 30 -1 # 입냐, 안입냐 - 1(무조건 하나는 입어야 함)
    for i in range(2,len_combi+1): # 2 ~ 옷의 종류만큼
        all_combi.extend(list(combinations(combi,i))) # 모든 조합을 구함
    
    for all in all_combi: # 모든 조합에서
        tmp = 1
        for i in range(len(all)): # 각 조합에 담긴 수들을
            tmp *= all[i] # 모두 곱한다
        answer += tmp # 그리고 누적
    
    return answer

solution([["crowmask", "face"]])

# Good explnation
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes]) # 옷의 종류들이 몇개 있는지 Count
    # reduce(집계 함수(첫번째 인자: 누적자(accumulator), 두번째 인자: 현재값(current value)), 순회 가능한 데이터, 초기값)
    # 초깃값 1, 옷의 종류의 count 리스트를 순회, x=누적자 y=현재값, 누적값에 현재값 +1 을 누적곱해준다 그리고 -1
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 
    return answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])

# Good explnation2
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1

# Good explnation3
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1