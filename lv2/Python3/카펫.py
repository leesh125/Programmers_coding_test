def solution(brown, yellow):
    total = brown + yellow
    candidate = set()
    for i in range(3,int(total**0.5)+1):
        if total % i == 0:
            candidate.add((total//i, i))
    
    for c in candidate:
        width, height = c
        if (width + height) * 2 - 4 == brown:
            return [width, height]