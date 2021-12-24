# My turn
def solution(s):
    return int(s)

# Good explanation
def strToInt(str):
    result = 0

    # enumerate() : 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
    #               인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result