def solution(progresses, speeds):
    answer = []
    cnt = 0

    progresses_stack = list(reversed(progresses)) # 스택 구현을 위해 역순 정렬
    speeds = list(reversed(speeds)) # 위와 동일

    while len(progresses_stack) != 0: # 스택이 차있을 동안
        if progresses_stack[-1] >= 100: # 최상단 원소가 100% 이상 돌입 시
            cnt += 1 # 일 수 증가
            progresses_stack.pop() # 빼내기
            continue # 바로 아래도 100퍼가 되었는지 확인
        else: # 아직 100퍼가 안됐고
            if cnt != 0: # 일 수 증가가 있다면
                answer.append(cnt) # 이전까지의 일 수 증가
                cnt = 0 # 일 수 변수 초기화
        
        for i in range(len(progresses_stack)):
            progresses_stack[i] += speeds[i] # 일 수마다 증가한 퍼센트 누적 시키기
    answer.append(cnt) # 마지막 continue로 인해 출력안된 일 수 추가
    
    return answer

#print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))

# Good Explanation 1
def solution1(progresses, speeds):
    Q=[] # 현재 작업 100프로 완료되는 시점, 그 시점에 해결되는 기능 수 리스트
    for p, s in zip(progresses, speeds): # 작업 퍼센트들, 작업 속도들
        # 해당 작업이 100프로 완료되는 시점이 이전 작업보다 오래걸리면
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): 
            Q.append([-((p-100)//s),1]) # 현재 작업 100프로 완료되는 시점, 그 시점에 해결되는 기능 수
        else: # 이전 작업보다 일찍 끝나면 (=> 대기)
            Q[-1][1]+=1 # 이전 작업이 끝나는 시점에 해결되는 기능 수 추가(대기 상태로 인해)
        print(Q)
    return [q[1] for q in Q] # 가능한 기능 수 출력
print(solution1([93, 30, 55],[1, 30, 5]))

# Good Explanation 2
def solution2(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0: # 스택이 차 있을 동안
        if (progresses[0] + time*speeds[0]) >= 100: # 지나온 일 수 동안 진행한 퍼센트가 100이 넘으면
            progresses.pop(0) # 최상단 작업 빼기
            speeds.pop(0)
            count += 1 # 일 수 증가
        else: # 100 퍼가 안넘었을 때
            if count > 0: # 여태까지 100퍼가 넘은 작업이 하나 이상이라도 있으면
                answer.append(count) # 해당 일 수 결과 리스트에 추가
                count = 0 # 일 수 변수 초기화
            time += 1 # 날짜 증가
    answer.append(count) # 마지막 계산 안된 일 수 추가
    return answer