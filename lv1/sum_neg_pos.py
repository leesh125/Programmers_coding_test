# My turn
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] is False:
            absolutes[i] *= -1

    answer = sum(absolutes)

    return answer

print(solution([4,7,12],[True,False,True]))

# Good explanation

2
3
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))