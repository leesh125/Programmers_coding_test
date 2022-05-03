# My turn
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))] # 미리 답 규격 정하기
    row_arr2 = [[] for _ in range(len(arr2[0]))] # arr2를 행과 열을 바꾼다
    for i in range(len(arr2)): # 행
        for j in range(len(arr2[0])): # 열
            row_arr2[j].append(arr2[i][j]) # 해당 행,열에 값을 row_arr2 에다가 집어넣기
    
    for i in range(len(answer)): # 행
        for j in range(len(answer[0])): # 열
            answer[i][j] = sum(map(lambda a,b : a*b, arr1[i], row_arr2[j])) # arr1의 열값과 arr2의 행값을 더함
    print(answer)
    return answer

solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]])
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],	[[5, 4, 3], [2, 4, 1], [3, 1, 1]])


# Good Explanation
def productMatrix(A, B):
    # A 행렬의 행과 B 행렬의 열을 zip 형식으로 분리하여 따로따로 곱한후 list원소에 행단위로 저장
    # (*args) : - 파라미터를 몇개 받을지 모르는 경우에 사용한다. - 튜플 형태로 전달된다.
    # zip(*args) : 행 단위로 쪼갠후 거기에서 순차적으로 하나씩(열 순서로) 리스트를 만듦
    # 결론: *를 붙여서 입력하면 col끼리 서로 엮어준다
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# Good Explanation2
import numpy as np
def productMatrix(A, B):
    # numpy 사용
    return (np.matrix(A)*np.matrix(B)).tolist()