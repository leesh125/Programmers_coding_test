# My Turn
import re

def solution(new_id):
    
    answer = ''
    answer = new_id.lower()
    answer = re.findall('\w|\-|\_|\.',answer)
    answer = ''.join(answer)
    answer = re.sub('(([\.])\\2{1,})','.',answer)
    answer = re.sub('^\.|\.$','',answer)
    if answer == "":
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub('\.$','',answer)    
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer

print(solution("abcdefghijklmn.p"))

# Good Turn
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

# Good Turn2
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer