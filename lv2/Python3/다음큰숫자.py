def solution(n):
    cnt = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == cnt:
            return n

    