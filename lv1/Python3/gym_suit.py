def solution(n, lost, reserve):
    answer = 0
    borrow = 0
    
    for l in lost:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    lost.sort()
    reserve.sort()
    for l in lost:
        for r in range(len(reserve)):
            if abs(l-reserve[r]) == 1 or abs(l-reserve[r]) == 0:
                borrow += 1
                reserve[r] = -1000
                break
            
    return n-(len(lost)-borrow)

print(solution(3,[1,2],[2,3])) # == 2  
print(solution(5,[2,4],[1,3,5])) # == 5
print(solution(5,[2,3,4],[1,2,3]))

# Good explanation
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)