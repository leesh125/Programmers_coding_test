# My turn
def solution(record):
    answer = [] # 아이디마다 들어옴과 나감을 알 수 있는 배열
    result= [] # 최종 관리자에게 보여질 문자열 배열
    dic = {} # 아이디: 이름

    for r in record: # 채팅방 흐름
        r = r.split(' ')
        
        if r[0] == 'Enter': # 만약 들어온거라면
            dic[r[1]] = r[2] # 해당 아이디: 이름 dic에 저장
            answer.append((True,r[1])) # 흐름을 알려주기
        elif r[0] == 'Leave': # 나간거라면
            answer.append((False,r[1])) # 흐름을 알려주기
        else: # 이름을 변경한거면
            dic[r[1]] = r[2] # 변경된 아이디: 이름
                
    for ans in answer: # 흐름
        if ans[0]: # True면
            result.append((dic[ans[1]]+"님이 들어왔습니다."))  # 들어옴
        else: # False면
            result.append((dic[ans[1]]+"님이 나갔습니다.")) # 나감

    return result

print(solution(["Enter uid1234 Muzi", "Change uid1234 Muzi", "Leave uid1234", "Enter uid1234 Prodo"]))

# Good explanation
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer