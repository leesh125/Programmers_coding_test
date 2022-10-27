def solution(elements):
    answer = set()
    q = elements + elements[:-1]
    len_elements = len(elements)
    for i in range(1,len_elements+1):
        start = 0
        for j in range(len_elements):
            answer.add(sum(q[start:start+i]))
            start += 1
    
    return len(answer)