# My turn
def solution(answers):
    answer = []
    s_1 = []
    s_2 = []
    s_3 = []
    s_4 = [3,3,1,1,2,2,4,4,5,5]
    s_5 = [2,1,2,3,2,4,2,5]
    a_1 = 0
    a_2 = 0
    a_3 = 0
    for i in range(0,len(answers)):
        s_1.append(i%5+1)
        s_2.append(s_5[i%8])
        s_3.append(s_4[i%10])

        if s_1[i] == answers[i]:
            a_1 += 1
        if s_2[i] == answers[i]:
            a_2 += 1
        if s_3[i] == answers[i]:
            a_3 += 1

    dict = {1:a_1, 2:a_2, 3:a_3}
    a_list = list(dict.values())
    max_list = max(a_list)
    
    for i in range(1,4):
        if dict[i] == max_list:
            answer.append(i)

    return answer

print(solution([1,3,2,4,2]))

# Good explanation
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result