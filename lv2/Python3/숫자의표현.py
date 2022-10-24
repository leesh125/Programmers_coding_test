def solution(n):
    answer = 1

    for i in range(1, n//2+1):
        total = 0
        while True:
            total += i
            i+=1
            if total == n: answer += 1
            if total > n: break

    return answer