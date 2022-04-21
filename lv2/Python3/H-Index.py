# My turn
def solution(citations):
    citations.sort() # 인용수 오름차순으로 정렬
    index = citations[-1] # 가장 많이 인용된 것을 index로
    total_cite = 0 # 누적 인용 수(자기 보다 많이 인용된 인용논문의 수)

    while True: # 순환
        # 현재 논문의 인용 횟수(초기값: 가장 많은 인용횟수)가 발표된 논문들에서의 인용횟수 중 몇개 있는지를 누적
        total_cite += citations.count(index) 
        if citations.count(index) + total_cite >= index: # (현재 인용수의 갯수 + 누적 인용논문 수)가 현재 인덱스 이상이면
            return index # 현재 인덱스(인용수 or 인용수의 count)
        index -= 1 # index

# Good Explanation 1
def solution(citations):
    citations.sort(reverse=True) # 인용의 수 내림차순 정렬
    # enumerate로 (index, 발표된 논문들 인용수,ex.1-6, 2-5, 3-3, 4-1, 5-0) == 해당 인용수 이상의 논문 갯수(ex. 6이상 1개, 5이상 2개, 4이상 1개)
    # 1-6, 2-5, 3-3, 4-1, 5-0 => (해당 인용수 이상의 논문 갯수, 해당 논문의 인용수)
    # min(index,value) => 가능할 수 있는 모든 h-index의 값들
    # 1.h번 이상 인용된 논문이 h편 이상, 2.나머지 논문이 h번 이하 인용 의 조건 
    # => 해당 인용수 이상의 논문 갯수 < 해당 논문의 인용수: 해당 인용수 이상의 논문 갯수 이상 인용된 논문 해당 인용수 이상의 논문 갯수이상 1번 조건 충족
    # => 해당 인용수 이상의 논문 갯수 >= 해당 논문의 인용수: 1번 조건을 충족하지 못하므로 해당 논문의 인용수가 h값
    # max => 그중 가장 큰값을 뽑아냄
    answer = max(map(min, enumerate(citations, start=1))) 
    return answer

print(solution([3,0,6,1,5,3]))
print(solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20]))
# Good Explanation 2
def solution(citations):
    citations = sorted(citations) # 오름 차순 정렬
    l = len(citations) 
    for i in range(l): # 논문 갯수 만큼
        # [지금 몇 편이 남았는가? -> 모든 인용횟수가 이 값보다 큰가?
        # (가장 작은 값이 이 값보다 큰가?)]
        if citations[i] >= l-i: # 0 >= 5-0, 1 >= 5-1, 3 >= 5-2, 5 >= 5-3, 6 >= 5-4
            return l-i # l-i : i인덱스 값과 같거나 큰 수의 개수
    return 0
    # 0 1 3 5 6