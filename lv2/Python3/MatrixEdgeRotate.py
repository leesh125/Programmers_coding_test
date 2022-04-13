def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * (columns) for _ in range(rows)] # 값이 표현된 행렬

    cnt = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = cnt # 1부터 순차적으로 행렬값 채워나가기
            cnt += 1

    for a,b,c,d in queries: # (x1,y1), (x2,y2)
        top,left,bottom,right = a-1,b-1,c-1,d-1
        
        first = matrix[top][left] # 첫번째꺼 미리 빼놓기
        ans = first # 임의의 최솟값을 첫번째 행렬값으로

        for i in range(top, bottom): # 맨 왼쪽 위에서 밑에까지
            matrix[i][left] = matrix[i+1][left] # 한칸씩 올리기
            ans = min(ans,matrix[i][left]) # 변경한 값과 최솟값 비교
        for i in range(left, right): # 맨 아래 왼쪽에서 오른쪽까지
            matrix[bottom][i] = matrix[bottom][i+1] # 한칸씩 왼쪽으로 이동
            ans = min(ans,matrix[bottom][i]) # 변경한 값과 최솟값 비교
        for i in range(bottom, top,-1): # 맨 오른쪽 밑에서 위에까지
            matrix[i][right] = matrix[i-1][right] # 한칸씩 내리기
            ans = min(ans,matrix[i][right]) # 변경한 값과 최솟값 비교
        for i in range(right, left,-1): # 맨 위 오른쪽에서 왼쪽에까지
            matrix[top][i] = matrix[top][i-1] # 한칸씩 오른쪽으로 이동
            ans = min(ans,matrix[top][i]) # 변경한 값과 최솟값 비교
        matrix[top][left+1] = first # 값이 하나씩 밀려 첫번째 값을 그 다음 열로 이동
        
        answer.append(ans) # 최솟값 추가
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))
