def solution(line):
    answer = []
    INF = int(1e15) # max와 min 비교를 위한 무한대 값
    max_x, min_x, max_y, min_y = -INF,INF,-INF,INF # 초기값 세팅
    for i in range(len(line)): # 직선
        for j in range(i, len(line)): # 자기 자신을 제외한 직선
            if (line[i][0] * line[j][1] - line[i][1] * line[j][0]) != 0: # 분모가 0 이 아니면
                x = (line[i][1] * line[j][2] - line[i][2] * line[j][1]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0]) # 교점 x좌표
                y = (line[i][2] * line[j][0] - line[i][0] * line[j][2]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0]) # 교점 y좌표
                int_x,int_y = int(x), int(y) # int 형으로 변환
                if x == int_x and y == int_y: # 정수라면
                    answer.append([int_y,int_x]) # 좌표 형식의 x,y 는 반대이므로 바꿔서 삽입
                    max_x, min_x, max_y, min_y = max(max_x,int_x), min(min_x,int_x), max(max_y,int_y), min(min_y,int_y) # 전체 그래프의 행, 열 길이를 위한 최대,최소 구하기
    star = [['.'] * (max_x-min_x+1) for i in range(max_y-min_y+1)] # 전체 행,열 만큼 '.'으로 채우기
    for x,y in answer: # 교점 x,y 좌표
        star[max_y-x][y-min_x] = '*' # 가장 높은 지점에서 해당 좌표 만큼 뺀 x, 현재 좌표에서 최소 열(왼쪽값)을 뺀 y
    print(answer)
    result = []
    for i in range(len(star)):
        result.append(''.join(star[i]))
        #star[i] = ''.join(star[i])
    
    return result

#solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
# Good Explanation
solution = lambda line: (lambda rx, ry, s: ["".join("*" if (x, y) in s else "." for x in rx) for y in ry])(*((lambda i, j, s: (range(min(i), max(i) + 1), range(max(j), min(j) - 1, -1), s))(*(lambda s: ([v for v, _ in s], [v for _, v in s], s))(set((x // z, y // z) for x, y, z in [(b * f - e * d, e * c - a * f, a * d - b * c) for (a, b, e) in line for (c, d, f) in line] if z and not (x % z or y % z))))))