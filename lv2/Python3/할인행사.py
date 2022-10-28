def solution(want, number, discount):
    answer = 0
    dic = {}
    total = sum(number)
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    print(dic)
#     temp_total = total
#     for i in range(total):
#         if discount[i] in dic:
#             if dic[discount[i]] > 0:
#                 dic[discount[i]] -= 1
#                 temp_total -= 1
#     if temp_total == 0: answer +=1
    
#     left_idx = 1; right_idx = total
#     while right_idx < len(discount):
#         if discount[left_idx-1] in dic:
#             temp_total += 1
#             discount[left_idx-1] += 1
#         if discount[left_idx] in dic:
#             temp_total -= 1
#             discount[left_idx] -= 1
#         if discount[right_idx] in dic:
#             temp_total -= 1
#             discount[right_idx] -= 1
#         if temp_total == 0: answer +=1
    
    return answer