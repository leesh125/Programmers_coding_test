# My turn
def solution(seoul):
    # 배열.index("값") = 해당 배열안에 있는 값의 인덱스를 리턴
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다" 

# Good exlpanation
def findKim(seoul):
    # .format 사용
    return "김서방은 {}에 있다".format(seoul.index('Kim'))