def solution(s):
    answer = ''

    new_s = list(map(int,s.split(' ')))
    answer += str(min(new_s))
    answer += ' '
    answer += str(max(new_s))
    return answer

print(solution("1 2 3 4"))