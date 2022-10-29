def solution(want, number, discount):
    answer = 0
    dic = {}
    total = sum(number)
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    temp_total = total
    for i in range(total):
        if discount[i] in dic:
            if dic[discount[i]] > 0:
                dic[discount[i]] -= 1
                temp_total -= 1
            else:
                dic[discount[i]] -= 1
    if temp_total == 0: answer +=1
    
    left_idx = 1; right_idx = total
    while right_idx < len(discount):
        if discount[left_idx-1] in dic:
            if dic[discount[left_idx-1]] < 0:
                pass
            else:
                temp_total += 1
            dic[discount[left_idx-1]] += 1
        if discount[right_idx] in dic:
            if dic[discount[right_idx]] > 0:
                temp_total -= 1
            else:
                pass
            dic[discount[right_idx]] -= 1
        if temp_total == 0: answer +=1
        
        left_idx += 1; right_idx += 1
        
    return answer