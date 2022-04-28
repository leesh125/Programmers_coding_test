def solution(waiting):
    answer = []

    dic = {}

    for wait in waiting:
        if wait in dic:
            continue
        else:
            dic[wait] = 1
            answer.append(wait)


    return answer