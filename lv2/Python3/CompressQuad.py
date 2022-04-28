from collections import deque
def solution(arr):
    answer = []
    len_arr = len(arr)
    len_tmp = len_arr
    zero_cnt, one_cnt = 0,0

    def check(start_row,end_row,start_col,end_col):
        if end_row-start_row == end_col-start_col == 1:
            return True
        for i in range(start_row,end_row):
            if sum(arr[i][start_col:end_col]) not in [0,end_col-start_col]:
                return False
        return True

    q = deque([(0,len_arr,0,len_arr)])
    
    while q:
        start_row,end_row,start_col,end_col = q.popleft()
        if check(start_row,end_row,start_col,end_col):
            
            if arr[start_row][start_col] in [0,1]:
                print(start_row,end_row,start_col,end_col)
                if arr[start_row][start_col] == 0:
                    zero_cnt += 1
                elif arr[start_row][start_col] == 1:
                    one_cnt += 1
            for i in range(start_row,end_row):
                for j in range(start_col,end_col):
                    arr[i][j] = -10000
        else:
            len_tmp //= 2
            if len_tmp != 0:
                for i in range(start_row,len_arr,len_tmp):
                    for j in range(start_col,len_arr,len_tmp):
                        q.append((i,i+len_tmp,j,j+len_tmp))
        
    print(zero_cnt,one_cnt)
    
    
    return answer

#solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])

solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
