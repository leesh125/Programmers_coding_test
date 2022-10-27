def solution(topping):
    answer = 0
    my_dic, bro_dic = {topping[0]:1}, {}
    me,bro = 1, 0
    len_topping = len(topping)
    
    for i in range(1,len_topping):
        if topping[i] not in bro_dic:
            bro_dic[topping[i]] = 1
            bro += 1
        else:
            bro_dic[topping[i]] += 1
    
    if me == bro: answer += 1
    
    for i in range(1,len_topping-1):
        
        if topping[i] not in my_dic:
            my_dic[topping[i]] = 1
            me += 1
        
        bro_dic[topping[i]] -= 1
        if bro_dic[topping[i]] == 0:
            bro -= 1
            
        if me == bro: answer += 1

    return answer