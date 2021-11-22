# My turn
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[(len(s)/2)-1] + s[(len(s)/2)]
    else:
        answer = s[(len(s)/2)]
    return answer

# Good explanation
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]

a= ['a','b','c','d','e']
print(a[2:3])
print(string_middle(a))