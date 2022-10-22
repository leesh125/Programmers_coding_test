def solution(s):
    return ' '.join(list(map(lambda x: x.capitalize() if x != '' else '', s.split(' '))))
    
print(solution("3people unFollowed me"))