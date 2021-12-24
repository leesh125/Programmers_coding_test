# My turn
def solution(s):
    answer = ''
    ans = s.split(' ')  # 공백을 나누고
    
    for j in range(len(ans)):
        for i in range(len(ans[j])):
            if i % 2 == 0:           # 단어의 짝수번째 문자는
                answer += ans[j][i].upper()  # 대문자로
            else:
                answer += ans[j][i].lower()
        ans[j] = answer
        answer = ''

    return " ".join(ans)

print(solution("ab  ab ab ab"))
ans = "Abc qwe zxc    rty"
print(ans.split(' '))
print("".join(ans))

# Good explanation
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))