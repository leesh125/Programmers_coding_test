def solution(emails):
    answer = 0

    for email in emails:
        ans = 0
        flag = True
        stack = []
        
        if email[-4:] not in ['.com', '.net', '.org'] or 'a'>email[-5] and email[-5]>'z':
            continue
        
        for e in email[:-4]:
            if e == '@':
                ans += 1
            if ans == 0:
                if 'a' <= e <= 'z' or e == '.':
                    stack.append(e)
                else:
                    flag = False
                    break
            elif ans == 1:
                if 'a' <= e <= 'z':
                    continue
            else:
                flag = False
                break
            
        if flag and ans == 1 and len(stack) != 0:
            answer+=1
    return answer
print(solution(['.@.com']))