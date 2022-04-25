def solution(prices):
    len_prices = len(prices) 
    answer = []
    
    for i in range(len_prices): # 길이만큼
        cnt = 0 # 자기보다 크거나 같은 수를 셀 변수
        for j in range(i,len_prices-1): # 현재 지점부터 마지막 전까지
            if prices[i] <= prices[j]: # 자기 이상 숫자면
                cnt +=1 # cnt += 1
            else: # 작으면 
                break # 빠져나오기
        answer.append(cnt) # 센 갯수만큼 리스트에 추가
    
    return answer

solution([1,2,3,2,3])