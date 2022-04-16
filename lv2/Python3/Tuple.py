# My turn
import re
def solution(s):
    answer = []
    dic = {}
    # 정규표현식을 통해 숫자드만 리스트에 담기
    test = ''.join(re.compile('[^{}]').findall(s)).split(',') 
    
    for t in set(test): # 리스트에 담긴 숫자들 순회(중복 제거)
        dic[t] = test.count(t) # key: 숫자, value: 갯수
    sort_dic = sorted(dic.items(), key=lambda x:-x[1]) # 갯수가 가장 많은 것대로 정렬
    
    answer = [int(d[0]) for d in sort_dic] # 정렬된 숫자를 순서대로 리스트에 담기

    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
solution("{{123}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")

# Good explanation
import re
from collections import Counter
def solution(s):

    s = Counter(re.findall('\d+', s)) # Counter를 사용해 key(숫자), value(갯수)를 dict 형태로
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)])) # value(갯수)가 많은 순대로 정렬
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))