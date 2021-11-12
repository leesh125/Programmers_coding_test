def solution(numbers, hand):
    answer = ''
    l_hand=10
    r_hand=10
    dis_l=0
    dis_r=0
    i = 0
    for n in numbers:
        
        if n == 0:
            n = 11
        if n in [1,4,7]:
            answer += 'L'
            l_hand = n
        elif n in [3,6,9]:
            answer += 'R'
            r_hand = n
        elif n in [2,5,8,11]:
            if abs(l_hand - n) == 1 or abs(l_hand-n) ==3:
                dis_l = 1
            if abs(r_hand - n) == 1 or abs(r_hand-n) ==3:
                dis_r = 1
            if abs(l_hand - n) == 2 or abs(l_hand-n) ==4 or abs(l_hand-n) ==6:
                dis_l = 2
            if abs(r_hand - n) == 2 or abs(r_hand-n) ==4 or abs(r_hand-n) ==6:
                dis_r = 2    
            if abs(l_hand - n) == 7 or abs(l_hand-n) ==5 or abs(l_hand-n) ==9:
                dis_l = 3
            if abs(r_hand - n) == 7 or abs(r_hand-n) ==5 or abs(r_hand-n) ==9:
                dis_r = 3
            if abs(l_hand - n) == 10:
                dis_l = 4
            if abs(r_hand - n) == 8:
                dis_r = 4
            if abs(l_hand - n) == 0:
                dis_l = 0
            if abs(r_hand - n) == 0:
                dis_r = 0

            if i == 0:
                if n in [2,5,8,11]:
                    if hand == "left":
                        answer += 'L'
                        l_hand = n
                    elif hand == "right":
                        answer += 'R'
                        r_hand = n
            elif i>=1:
                if dis_l < dis_r:
                    answer += 'L'
                    l_hand = n
                elif dis_r < dis_l:
                    answer += 'R'
                    r_hand = n
                elif dis_l == dis_r:
                    if hand == "left":
                        answer += 'L'
                        l_hand = n
                    elif hand == "right":
                        answer += 'R'
                        r_hand = n
        i+=1                
            

    return answer

print(solution([0,2,4,6,8,1,7,5,3,0,3,0],"right"))

# Good explanation
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer