# My turn
def solution(nums):
    s_nums = set(nums)
    dic_nums = dict.fromkeys(s_nums, 0)

    for i in dic_nums:
        dic_nums[i] = nums.count(i)

    if len(dic_nums) >= len(nums)/2:
        answer = int(len(nums)/2)
    elif len(dic_nums) == 1:
        answer = 1
    elif len(dic_nums) < len(nums)/2:
        answer = int(len(dic_nums))
    
    return answer

print(solution([3,3,3,2,2,4]))

# Good explanation 1
def solution(ls):
    return min(len(ls)/2, len(set(ls)))

# Good explanation 2
def solution(nums):
    answer = 0
    myList = set(nums)
    if len(nums)/2 > len(myList):
        answer = len(myList)
    else:
        answer = len(nums)/2
    return answer