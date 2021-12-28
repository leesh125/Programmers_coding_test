# My turn
def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)): 
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j] # 원소 하나씩 더하기
           
    return answer

solution([[1,2], [2,3]],[[3,4], [5,6]])
arr = [[1,2], [2,3]]
arr2 = [[3,4], [5,6]]

print(list(zip(arr,arr2)))
# Good explanation
def sumMatrix(A,B):
    # 첫째 행 끼리 묶고, 또 그안에서 요소들끼리 묶음 그리고 더한 값을 리스트로 반환
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer