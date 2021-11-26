# My turn
def solution(n, arr1, arr2):
    answer = [''] * n
    newArr1 = []
    newArr2 = []
    for i in range(0,n):
        newArr1.append(bin(arr1[i])[2:].zfill(n))
        newArr2.append(bin(arr2[i])[2:].zfill(n))
        
        for j in range(0,n):
            if newArr1[i][j] + newArr2[i][j] == '00' :
                answer[i] += ' '
            else:
                answer[i] += '#'
            
    return answer


print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))

n = 5
a=bin(5)[2:].zfill(n)
print(a)


# Good explanation
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer