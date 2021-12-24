# My turn
def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <= 'Z':    # 대문자이면
            if ord(s[i])+n > 90:           # 만약 아스키코드값이 90(Z)를 넘으면
                answer += chr((ord(s[i])+n)%90+64)   # 다시 65부터 순회
            else:
                answer += chr(ord(s[i])+n)
        elif s[i] >= 'a' and s[i] <= 'z':
            if ord(s[i])+n > 122:
                answer += chr((ord(s[i])+n)%122+96)
            else:
                answer += chr(ord(s[i])+n)
        else:
            answer += " "
    return answer
print(solution("a B z",4))


# Good Explanation
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():   # 대문자이면
            # 아스키 90(Z) - 65(A) + n(들어온 수) % 26(대문자 갯수) + 아스키65(A)
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))  
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)