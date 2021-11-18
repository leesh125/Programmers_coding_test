from itertools import combinations
def solution(nums):
    answer = 0
    
    s_numarr = []
    numarr = list(combinations(nums, 3))
    
    for i in numarr:
        s_numarr.append(sum(i))
    
    n_sum = 0
    for s in s_numarr:
        for i in range(2,s):
            if s % i == 0:
                n_sum += 1
        
        if n_sum == 0:
            answer += 1
        
        n_sum = 0
    

    return answer

print(solution([1,2,3,4]))

# Good explanation 1
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer;

# Good explanation 2
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer