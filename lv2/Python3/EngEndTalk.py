# My turn
def solution(n, words):
    dic = {words[0]:1} # dictionary 형식으로 값의 중복 체크를 위해
    len_words = len(words) # 단어의 갯수들
    idx = 1 # 1 인덱스부터 시작
    
    while idx != len_words: # 인덱스가 끝까지 도달하지 않았다면
        if words[idx] not in dic: # 해당 단어가 사전에 없으면
            dic[words[idx]] = 1 # 사전에 추가
        else: # 있으면 빠져나오기
            break
        if words[idx][0] != words[idx-1][-1]:  # 끝말잇기가 아니라면
            break # 빠져나오기
        idx += 1 # 인덱스 1 추가
    
    if idx == len_words: # 단어의 길이 끝까지 도달했다면
        return [0,0] # 0,0 리턴
    else: # 중간에 틀린부분이 있다면
        return[idx % n +1,idx // n + 1] # 몇번째 사람인지, 몇번의 순회 도중인지

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])

# Good Exaplanation
def solution(n, words):
    for p in range(1, len(words)): # 1인덱스 부터 끝까지
        # 끝말잇기가 아니거나 현재까지 나온 단어중에 포함이 되어 있다면
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: 
            return [(p%n)+1, (p//n)+1] # 몇번째 사람인지, 몇번의 순회인지 체크
        print(p)
    else: # for 문을 다 돌아도 해당 되는것이 없다면
        return [0,0] # 0,0 출력

solution(2,["hello", "one", "even", "never", "now", "world", "draw"])