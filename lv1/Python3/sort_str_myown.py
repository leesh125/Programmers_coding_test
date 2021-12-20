# My turn
def solution(strings, n):
    answer = []
    arrDic = {}
    i = 0
    k = 0

    # dictionary에 값 넣기(보기 편하게 하려고)
    for s in strings:  
        arrDic[i] = s
        i += 1

    # 순차정렬
    for i in range(len(arrDic)-1):
        j = i+1
        while j < len(arrDic):   
            if arrDic[i][n] > arrDic[j][n]:  # 뒤에 것이 해당 값이 더 크면 교환하기
                temp = arrDic[i]
                arrDic[i] = arrDic[j]
                arrDic[j] = temp
            elif arrDic[i][n] == arrDic[j][n]:  # 값이 같은게 나왔을 때
                if arrDic[i][k] > arrDic[j][k]: # 사전순 비교
                    temp = arrDic[i]
                    arrDic[i] = arrDic[j]
                    arrDic[j] = temp
                elif arrDic[i][k] == arrDic[j][k]:  # 처음부터 끝까지 계속 같다면 continur를 통해 다음 값 비교
                    k += 1
                    continue
            k = 0
            j +=1

    return list(arrDic.values())

solution(["aea", "ba", "ce", "aee"], 1)
solution(["abzcd","cdzab","abzfg","abzaa","abzbb","bbzaa"], 2)

# Good explanation 
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])  # sorted(key) == 정렬을 목적으로 하는 key를 넣어준다

strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))