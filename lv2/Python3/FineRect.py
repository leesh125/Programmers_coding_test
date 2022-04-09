# My turn

''' 최대 공약수를 쓰는 이유
    :   교점 수 = 반복되는 횟수 = 최대공약수
     -> 교점이 없을 때 대각선이 뚫는 사각형 개수=(가로'+세로'-1)
     -> (가로'+세로'-1)*(최대공약수)=(가로+세로-최대공약수)
    
    답: 전체사각형 개수-(가로+세로-최대공약수)
'''
def solution(w,h):
    if w == h: # 가로 세로 같으면
       return w * h - w # 전체에서 가로 or 세로 길이의 칸만 빼주면 됨
    else:
        if h > w:
            w,h = h,w 
        gcd = uclid(w,h) # 최대공약수 구하기
        return (w*h) - (w+h-gcd) # 공식: (가로*세로) - (가로+세로-가로세로 gcd)

# 유클리드 호제법
def uclid(x,y): # x >= y
    while x % y != 0: # x,y가 나눠지지 않으면
        z = x % y # x에서 y를 나눈 나머지를 가지고 비교 할것임
        x, y = y,z # y와 위의 나머지로 비교
    return y # 나눠떨어질 때에 y가 최대 공약수


print(solution(8,12))

# Good Explanation
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)

# Good Explanation2
from math import gcd
def solution(w,h):
    return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)