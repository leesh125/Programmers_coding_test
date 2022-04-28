def solution(arr):
    global answer # 전역 변수 선언
    answer = [0,0] # [0의 count, 1의 count]
    quad(arr, answer, len(arr)) # 처음 배열, 처음 x와 y의 좌표, 현재 배열의 길이
    return answer

def quad(arr, s, n): # 쿼드 분할
    x, y, tg = s[0],s[1],arr[s[0]][s[1]] # x 좌표, y 좌표, 현재 arr[x][y] 안에 값

    for i in range(n): # 매개변수 n(분할 길이) 만큼 돌기, n이 1이라면 if문 수행하지 않고 넘어감
        for j in range(n):
            if arr[x+i][y+j] != tg: # 처음값과 다르다면
                # 배열, 분할된 사각형 x,y 좌표만큼 재귀, 길이 // 2
                quad(arr, [x,y], n//2) 
                quad(arr, [x,y+n//2], n//2)
                quad(arr, [x+n//2,y], n//2)
                quad(arr, [x+n//2,y+n//2], n//2)
                return # 분할이 안되었다면 해당 사각형 순회를 멈춤
    answer[tg] += 1 # if 문을 무사히 넘겼다면(현재 사각형이 모두 같은 값) 현재 사각형의 처음 좌표값 비교후 답 배열에 +1
#solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
