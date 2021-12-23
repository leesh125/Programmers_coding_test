# My turn
#에라토스테네스의 체
def solution(n):
    num = [True] * (n+1)

    m = int(n**0.5)

    for i in range(2, m+1):
        if num[i] == True:
            for j in range(i+i, n+1, i):
                num[j] = False
    print(num)
    arr =  [i for i in range(2, n+1) if num[i] == True]
    
    return  len(arr)

print(solution(11))

# Good Explanation
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

num=set(range(2,15+1))
print(num)