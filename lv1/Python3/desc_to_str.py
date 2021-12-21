# My turn
def solution(s):
    # 아스키 코드를 반환해주는 ord에 -를 적용하여 역순으로 정렬되게끔
    return print("".join(sorted(s, key=lambda x: -ord(x)))) 

# Good explanation
def solution(s):
    # 문자열을 역순으로 정렬 (sorted는 list로 변환 후 정렬한다)
    return ''.join(sorted(s, reverse=True))
