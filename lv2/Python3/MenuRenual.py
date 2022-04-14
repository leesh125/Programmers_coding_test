from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course: # 메뉴 구성 수
        new_menu = {} # 
        for menu in orders: # 한 사람이 주문한 메뉴들
            menu_li = list(''.join(menu)) # 단품메뉴로 리스트형 변환
            for li in combinations(menu_li, c): # 메뉴 구성수 만큼 모든 조합 가능한 메뉴
                res = ''.join(sorted(li)) # 조합한 메뉴
                if res not in new_menu.keys(): # 조합한 메뉴가 처음이라면
                    new_menu[res] = 1 # 메뉴 : 메뉴갯수(1)
                else:
                    new_menu[res] += 1 # 기존 메뉴 : 메뉴갯수(+1)
        # 메뉴 갯수 만큼 정렬 그것을 리스트로
        sort_menu = sorted(new_menu.items(), key=lambda x:[x[1]])
        
        print(sort_menu)
        if len(sort_menu) > 0: # 추출한 메뉴 조합이 있다면
            top_menu, top_cnt = sort_menu.pop() # 가장 메뉴 갯수가 많은 것 추출
            if top_cnt >= 2: # 최소 2번이상 주문된 메뉴조합이라면
                answer.append(top_menu) # answer에 추가하기

        if len(sort_menu) > 0: # 추출하고도 아직 메뉴 조합이 있을 때
            while sort_menu: # 메뉴가 전부 추출되기전 동안
                menu, cnt = sort_menu.pop() # 그 다음 메뉴 갯수가 많은 것 메뉴와 메뉴 갯수 추출
                if cnt == top_cnt and cnt >= 2: # 추출한 메뉴 갯수가 가장 많은 메뉴 갯수와 같고 그것이 2 이상이면 
                    answer.append(menu) # answer에 추가
                else:
                    break
    
    return sorted(answer) # 정렬


# Good Explanation
import collections
import itertools

def solution2(orders, course):
    result = []

    for course_size in course: # 조합된 메뉴의 갯수: [2,3,4]
        order_combinations = []
        for order in orders: # 주문 하나당
            # combinations(list, size): 하나의 리스트에서 size 갯수만큼의 모든 조합 계산(메뉴 구성수 만큼 모든 조합 가능한 메뉴)
            # 정렬된 모든 주문 조합,조합된 메뉴의 갯수를 모두 담기
            order_combinations += itertools.combinations(sorted(order), course_size)
        # most_common(): 데이터의 개수가 많은 순으로 정렬된 배열을 리턴    
        most_ordered = collections.Counter(order_combinations).most_common()
        
        # 가장 많이 주문된 메뉴에서 그 갯수가 2개 이상이고 가장 많이 주문된 것들을 result에 누적
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
        
    return [ ''.join(v) for v in sorted(result) ] #정렬된 문자열로 반환

print(solution2(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))