def solution(participant, completion):
    answer = ''

    p_dict = dict()
    for p in participant:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1
    
    for c in completion:
        if c in p_dict:
            p_dict[c] -= 1
    
    for name, num in p_dict.items():
        if num != 0:
            answer+= name
    
            
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))

#Good Explanation 1
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]



#Good Explanation 2
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer)[0]
print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))

