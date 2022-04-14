import re

def make_set(str): # 문자열을 두 문자씩 분리
    str_set = []
    for i in range(len(str)-1):
        str_set.append(str[i]+str[i+1])
    return str_set

def to_regex(regex,str): # 문자열에 정규표현식 적용
    only_str= []
    for s in str:
        if regex.search(s):
            only_str.append(s.upper())
    return only_str

def solution(str1, str2):
    regex = re.compile('^[a-zA-Z][a-zA-Z]$') # 정규표현식
    # 문자열을 두 문자씩 끊어 리스트로
    str1_set = make_set(str1) 
    str2_set = make_set(str2)
    # 위 리스트 각 문자에 정규표현식 적용(알파벳만 포함)
    only_str1 = to_regex(regex,str1_set)
    only_str2 = to_regex(regex,str2_set)
    # 2번째 알파벳 문자열 모음을 기록할 dict
    str2_dic = {} 
    for s in only_str2: # 2번째 알파벳 문자열
        if s not in str2_dic: # 해당 문자열이 dict에 없다면
            str2_dic[s] = 1 # 1
        else: # 해당 문자열이 dict에 있다면
            str2_dic[s] += 1 # 그 갯수 증가

    intersection = 0 # 교집합

    for s1 in only_str1: # 1번째 알파벳 문자열 모음 중
        if s1 in only_str2 and str2_dic[s1] != 0: # 해당 문자열이 2번째 문자열에 속하면서 dict에 값이 0이 아니면
            intersection += 1 # 교집합 추가
            str2_dic[s1] -= 1 # 겹친 부분 dict에서 제거
    # 교집합 or 합집합이 0이 아니면 :(교집합 / 합집합) * 65536, 둘 중 하나가 0이면 65536 qksghks
    return int((intersection / (len(only_str1) + len(only_str2) - intersection)) * 65536) if len(only_str1) != 0 or len(only_str2) != 0 else 65536

# Good Explanation
import re
import math

def solution(str1, str2):
    # 정규 표현식에 해당되는 문자연속 2개를 리스트 형태로
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    # 파이썬 교집합 : set & set, 합집합 : set | set
    gyo = set(str1) & set(str2) 
    hap = set(str1) | set(str2)

    if len(hap) == 0 : # 합집합이 0 이면 
        return 65536 # 65536 반환

    print(gyo)
    print(hap)
    # 교/합집합의 합 : 교집합 요소 중 해당 요소가 첫,두번째 문장에서 적게 불리면 교집합, 많이 불리면 합집합
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo]) 
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])
    
    return math.floor((gyo_sum/hap_sum)*65536)

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', '	e=m*c^2'))

# [^문자들] : [문자들]의 반대로 피해야할 문자들의 집합을 정의함.	
# ex) [^aeiou] : 소문자 모음이 아닌 문자들

# + : 앞 패턴이 하나 이상이어야 함	
# ex) \d+ : 숫자가 하나 이상이어야 함

# ^ : 이 패턴으로 시작해야 함	
# ex) ^abc : abc로 시작해야 함 (abcd, abc12 등)
