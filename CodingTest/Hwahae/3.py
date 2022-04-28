def solution(card,word):
    answer = []
    len_card = len(card)

    for i in range(len_card):
        card[i] = list(card[i])

    for w in word:
        tmp_card = [[] for _ in range(len_card)]
        cnt = 0
        for i in range(len_card):
            tmp_card[i] = list(card[i])

        visit = [1,1,1]
        for i in range(len(w)):
            for j in range(3):
                if w[i] in tmp_card[j]:
                    tmp_card[j][tmp_card[j].index(w[i])] = -1
                    cnt += 1
                    visit[j] = 0
        print(visit, cnt)
        
        if sum(visit) == 0 and cnt == len(w):
            answer.append(w)

    
    return answer

solution(["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], ["GPQM", "GPMZ", "EFU", "MMNA"])
solution(["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"], ["AAAKKKKKMMMMM","ABCDKJ"])