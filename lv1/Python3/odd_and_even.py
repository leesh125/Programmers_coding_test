# My turn
def solution(num):
    return "Odd" if num % 2 == 1 else "Even" # 말 그대로..

# Good explanation
def evenOrOdd(num):
    # 2진 비트가 1번째 비트자리에 의해 홀짝이 결정됨
    # & 연산자로 0과 1을 구하고 인덱스로 활용
    return ["Even", "Odd"][num & 1]