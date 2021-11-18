# My turn
def solution(array, commands):
    answer = []
    res = []
    for c in commands:
        answer = array[(c[0]-1):(c[1])]
        answer.sort()
        res.append(answer[c[-1]-1])
    return res

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# Good explanation 1
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# Good explanation 2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer