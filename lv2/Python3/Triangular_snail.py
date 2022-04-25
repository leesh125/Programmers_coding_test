# My turn
def solution(n):
    answer = [[0]*i for i in range(1,n+1)] # 답이 들어갈 자리 미리 만들어둠
    
    num = 1 # cnt
    n_count = 0 # 왼, 밑, 오 순환을 카운트

    l_col,l_start,l_end = 0, 0, 0 # 왼쪽 순환 시 필요한 변수
    b_row, b_start, b_end = 1, 0, 0 # 밑쪽 순환 시 필요한 변수
    r_start, r_end,r_col = 1,0, 1 # 오른쪽 순환 시 필요한 변수

    while True: # 순환
        for i in range(l_start,n-l_end): # 왼쪽 순환
            answer[i][l_col] = num
            num += 1
        l_start += 2 # 모든 순환이 돌면 다음 왼쪽 순환은 2행 밑에서
        l_end += 1
        l_col += 1
    
        n_count += 1 # 순환 횟수 +1
        if n_count == n: # 숫자만큼 순환이 된다면(순환은 숫자만큼함)
            break
        
        num-=1 # 중복 숫자 자리 -1
        for j in range(b_start,n-b_end): #밑 순환
            answer[n-b_row][j] = num 
            num += 1
        b_start += 1 # 다음 순환의 시작 열은 +1 지점에서부터
        b_end += 2 # 다음 순환의 끝 열은 현재 끝 -2 지점 까지
        b_row += 1 # 행은 -1
        

        n_count +=1
        if n_count == n:
            break

        num-=1 # 중복 숫자 자리 -1
        for k in range(n-r_start,r_end,-1): # 오른쪽 순환
            answer[k][-r_col] = num
            num += 1
        r_start += 1 # 다음 시작 행은 현재 행 -1
        r_end += 2 # 다음 끝 행은 현재 끝행 -2
        r_col += 1 # 열은 -1 지점

        n_count += 1
        if n_count == n:
            break
    result = []
    for ans in answer:
        result.extend(ans) # extend를 통해 1차원 배열에 그대로 추가하기
    
    return result

# Good Explanation
def solution(n):
    dx=[0,1,-1];dy=[1,0,-1] # x,y로 이동할 수 있는 경로
    b=[[0]*i for i in range(1,n+1)] # 답이 들어갈 자리 미리 만듦
    x,y=0,0;num=1;d=0 # 
    while num<=(n+1)*n//2: # n이 취할 수 있는 가장 큰 수 까지(그 이상 숫자는 안나옴)
        b[y][x]=num # 해당 y,x에 현재 num 값 입력(처음은 [0][0] = 1)
        ny=y+dy[d];    nx=x+dx[d];    num+=1 #  # 그 다음 갈 수 있는 위치만큼을 더해줌,num도 +=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0: # 행이 n보다 작고 열이 행 인덱스보다 작고 아직 채워지지 않은 값이라면
            y,x=ny,nx # ny,nx 대입
        else: # 범위를 초과했다면
            d=(d+1)%3 # 다음 y,x 이동 값으로(ex.왼쪽 채우다가 끝 행을 만나면 밑에 행의 열을 쭉 채우는 것)
            y+=dy[d];    x+=dx[d] # 이동할 위치 만큼 더해줌
    
    # sum(덧셈할 것, 처음에 더할 것)
    # [] 을통해 리스트 덧셈임을 알림(ex. [] + [1,2] + [1,2,3])
    return sum(b,[])
solution(4)