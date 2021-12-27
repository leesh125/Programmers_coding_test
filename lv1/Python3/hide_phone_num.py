# My turn
def solution(phone_number):
    # p_n 마지막 4자리를 따와서 p_n 길이만큼 오른쪽 정렬, 나머지는 *처리
    return phone_number[-4:].rjust(len(phone_number), '*')

# Good explanation
def hide_numbers(s):
    # p_n 길이 - 4 만큼 *표 + 나머지 뒤 4자리
    return "*"*(len(s)-4) + s[-4:]