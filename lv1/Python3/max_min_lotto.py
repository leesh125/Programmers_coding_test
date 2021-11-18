# My turn
def solution1(lottos, win_nums):
    i = 0
    count = 0
    z_count = 0
    answer = []

    for l in lottos:
        if l in win_nums:
            count += 1
        if l == 0:
            z_count += 1

    while i<2:
        if i == 0:
            total = count + z_count
        elif i == 1:
            total = count

        if total == 6:
            answer.append(1)
        elif total == 5:
            answer.append(2)
        elif total == 4:
            answer.append(3)
        elif total == 3:
            answer.append(4)
        elif total == 2:
            answer.append(5)
        else:
            answer.append(6)    
        i += 1

    return answer

print(solution1([44,1,0,0,31,25], [31,10,45,1,6,19]))

# Good turn
def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

print(solution2([44,1,0,0,31,25], [31,10,45,1,6,19]))

