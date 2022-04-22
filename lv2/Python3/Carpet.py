# My turn
def solution(brown, yellow):
    answer = []

    # 중앙 노란색 카펫의 경우의 수 모두 구하기(조건 1. 노란카펫은 무조건 직사각형 형태 타일, 조건 2. 가로가 세로보다 김)
    set_yellow = [[yellow//i,i] for i in range(1,int(yellow**0.5)+1) if yellow%i == 0] # 제곱근까지 한 이유는 세로가 가로를 넘지 않기 위해
    
    for width, height in set_yellow: # 가로, 세로
        if width+height + 2 == brown//2: # 가로 + 세로 + 2 == 갈색 타일의 절반이면
            return [width+2,height+2] # 바깥 직사각형 가로 세로를 구하기
    
    return answer

# Good Explanation
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1): # 1 ~ 제곱근까지
        if red % i == 0: # 노란 타일 수가 i로 나눠떨이저면(가로,세로 쌍)
            if 2*(i + red//i) == brown-4: # 2*(가로 + 세로) == 갈색 타일 수와 같다면
                return [red//i+2, i+2] # 해당 가로 세로 추출

# Good Explanation 2
import math
def solution(brown, yellow):
    # 근의 공식 (x == 가로, y == 세로)
    # x*y = brown + yellow, (x-2) * (y-2) == yellow # 격자를 생각해보자
    # 위 식을 x기준으로 풀면 2x**2 - (brown+4)x + 2yellow + 2brown = 0
    # 근의 공식으로 x를 구한 후, y를 구한다(더 큰값을 x로)
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]