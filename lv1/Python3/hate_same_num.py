# My turn
def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] = -1
    
    for a in arr:
        if a != -1:
            answer.append(a)
    return answer

print(solution([1,1,3,3,0,1,1]))

# Good explanation
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

a = [1,2,3,4,5,6,7,8]
