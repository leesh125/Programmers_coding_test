# My turn
def solution(a, b):
    sum = 0
    for n in range(len(a)):
        sum += a[n]*b[n]
    return sum

# Good explanation
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

    
print(solution([1,2,3,4],[-3,-1,0,2]))
