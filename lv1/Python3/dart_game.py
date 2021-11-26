# My turn
def solution(dartResult):
    dart_list = []
    score = []
    
    dartResult = dartResult.replace('10','N')

    for d in dartResult:
        dart_list.append(d)
    
    for i in range(len(dart_list)):
        if dart_list[i] == 'N':
            dart_list[i] = '10'
    
    for i in range(len(dart_list)):
        try:
            dart_list[i] = int(dart_list[i])
        except ValueError:
            pass
    
    if type(dart_list[1]) == str and type(dart_list[2]) == int:
        dart_list.insert(2,"@")
    if type(dart_list[4]) == str and type(dart_list[5]) == int:
        dart_list.insert(5,"@")
    if len(dart_list) == 8:
        dart_list.append("@")
    
    for i in range(1,len(dart_list)):
        if dart_list[i] == "S":
            dart_list[i] = 1
        if dart_list[i] == "D":
            dart_list[i] = 2
        if dart_list[i] == "T":
            dart_list[i] = 3    

    for i in range(3):
        score.append(dart_list[i*3]**dart_list[i*3+1])

    if dart_list[2] == "*":
        score[0] *= 2
    elif dart_list[2] == "#":
        score[0] *= -1

    if dart_list[5] == "*":
        score[0] *= 2
        score[1] *= 2
    elif dart_list[5] == "#":
        score[1] *= -1

    if dart_list[8] == "*":
        score[1] *= 2
        score[2] *= 2
    elif dart_list[8] == "#":
        score[2] *= -1


    return sum(score)



# Good explanation 1
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
        
    answer = sum(dart)
    return answer

# Good explanation 2
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
        print(answer)
    return sum(answer)

print(solution('1S2D*3T'))