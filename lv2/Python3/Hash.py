# My turn
def solution(phone_book):
    phone_book = sorted(phone_book) # 접두사로 정렬(1 ~ 9 순서)

    for i in range(len(phone_book)-1): # 현재 & 뒤에 문자만 비교해줘도 됨(접두사로 이미 정렬되어 있기때문)
        if phone_book[i+1].startswith(phone_book[i]): # 다음 문자의 시작이 현재문자이면
            return False # False
    return True # 접두사 없으면 True

# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123"]))
#print('123' in '456')

# Good Explanation
def solution(phoneBook):
    phoneBook = sorted(phoneBook) # 접두사로 정렬
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]): # 모든 전화부(p2), 첫째를 제외한 전화부(p2) 순차 반복
        if p2.startswith(p1): # 현재 전화가 다음 전화에 접두사면
            return False # False
    return True
print(solution(["123","456","789","321","432"]))

# Good Explanation
def solution(phone_book):
    answer = True
    hash_map = {} # dict
    for phone_number in phone_book: # key:전화번호, value: 갯수(1)
        hash_map[phone_number] = 1
    for phone_number in phone_book: # 각 전화번호
        temp = "" # 분석한 문자를 하나씩 담을 temp
        for number in phone_number: # 전화번호에 한글자씩
            temp += number # temp에 누적
            if temp in hash_map and temp != phone_number: # 누적된 문자열이 hash_map에 있고 다른 전화번호 이면
                answer = False # False
    return answer