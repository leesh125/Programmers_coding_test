# My turn
def solution(N, stages):
    answer = []
    failure = {}

    for i in range(1,N+1):
        if i in stages:
            cnt = stages.count(i)
            failure[i] = cnt/len(stages)
            stages = [j for j in stages if j != i]
        else:
            failure[i] = 0

    fail_values = list(failure.values())
    fail_values.sort(reverse=True)
    
    
    for f in fail_values:
        for i in range(1,len(failure)+1):
            if failure[i] == f:
                answer.append(i)
                failure[i] = -1
                break
        
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))


# Good explanation 1
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)


# Good explanation 2
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer