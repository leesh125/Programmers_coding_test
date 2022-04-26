# My turn
def solution(s):
    total,rotate = 0,0 # 0을 제거한 총 갯수, 순환 수
    while True: # 순환
        rotate += 1 # 순환횟수 +1
        z_count = 0 # 0을 count하는 변수
        
        for i in range(len(s)): # s의 문자 하나씩 탐색
            if s[i] == '0': # 0세기
                z_count += 1
        total += z_count # 총 0 count수 누적
        if len(s) - z_count != 1: # 남은 길이가 1이 아니라면
            s = bin(len(s) - z_count).lstrip('0b') # 남은 길이를 이진수로 변환
        else: # 남은 길이가 1이라면
            return [rotate,total] # 순환 수, 총 0 count 반환
    

solution("110010101001")
solution("01110")

# Good Explanation
def solution(s):
    a, b = 0, 0 # 순환 수, 총 0 count
    while s != '1': # s가 1이 아닐동안(길이가 1이 아닐동안)
        a += 1 # 순환 +=1
        num = s.count('1') # 1의 횟수 count
        b += len(s) - num # 총 0count는 총 길이 - 1의 count 수
        s = bin(num)[2:] # 1의 count를 이진수로 변환하여 s
    return [a, b]