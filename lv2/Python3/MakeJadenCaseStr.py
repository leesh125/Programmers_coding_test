def solution(s):
    # 공백으로 분리 후, 각 분리된 문자열 마다 ''이 아니면 앞글자를 대문자로 ''이면 그대로, 이것들을 리스트로 만든다음 붙혀준다.
    return " ".join(list(map(lambda x:x.capitalize() if x != '' else '', s.split(' '))))
