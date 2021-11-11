# My turn
def solution(s):
    numbers = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',	
        'three' : '3',	
        'four' : '4',	
        'five' : '5',	
        'six' : '6',	
        'seven' : '7',	
        'eight' : '8',	
        'nine' : '9'	
    }
    answer = ''
    num =''

    for i in s:
        if i in numbers.values():
            answer += i
        else:
            num+=i
            if num in numbers.keys():
                answer += numbers[num]
                num = ''
    return int(answer)


# print(solution("2three45sixseven"))


# Good explanation
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution1(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


print(solution1("2three45sixseven"))



# Good explanation2
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
