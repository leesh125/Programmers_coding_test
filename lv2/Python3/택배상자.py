def solution(order):
    answer = 0
    sub = []
    idx = 0
    
    for i in range(len(order)):
        if i+1 == order[idx]:
            answer += 1
            idx += 1
            while sub:
                if sub[-1] == order[idx]:
                    answer += 1
                    idx += 1
                    sub.pop()
                else: break
        else:
            sub.append(i+1)
            
    return answer