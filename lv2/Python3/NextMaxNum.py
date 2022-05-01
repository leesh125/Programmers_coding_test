def solution(n):
    cnt = bin(n).count('1') # 처음 숫자를 이진 수로 변환한 것에서 1의 갯수 count
    while True: # 반복
        n += 1 # n += 1
        if cnt == bin(n).count('1'): # 증가한 수의 이진수에서 1의 갯수의 count가 본래 cnt와 같다면
            return n # return
print(solution(21))

