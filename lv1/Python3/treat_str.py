#My turn
def solution(s):
    c = 0
    for i in s:
        # 0 ~ 9를 아스키 코드로 받아 그 안에 해당하는지
        if ord(i) >= 48 and ord(i) <= 57: 
            c+=1
    return len(s) in (4,6) and c == len(s)

# Good explanation 1 
def alpha_string46(s):
    # isdigit() = 문자열이 숫자로만 되어있는지 확인
    return s.isdigit() and len(s) in (4, 6)

# Good explanation 2
def alpha_string46(s): 
    # 예외처리
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 