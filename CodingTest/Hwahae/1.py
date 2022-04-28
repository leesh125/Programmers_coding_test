import re

def solution(emails):
    answer = 0
    
    for email in emails:
        ans = 0
        flag = True

        if email[-4:] not in ['.com', '.net', '.org'] or 'a'>email[-5] or 'z'<email[-5]:
            continue
        
        for e in email[:-4]:
            if e == '@':
                ans += 1

            if ans == 0:
                if 'a' <= e <= 'z' or e =='.':
                    flag = True
                else:
                    flag = False
            elif ans == 1:
                if 'a' <= e <= 'z':
                    flag = True
                else:
                    flag = False
                
            if flag == False:
                break

        if flag and ans == 1:
            answer += 1

    return answer

print(solution(["a@d.com"]))
print(solution(["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]))