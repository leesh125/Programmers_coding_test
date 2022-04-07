def solution(n):
    ans = 0
    digit = 1
    nine = 9
    
    while n > digit*nine: # n이 (자릿수 * 건너뛴 수) 보다 작을때까지
        n = n-(digit * nine) # 건너 뛰기(해당 자릿수에 포함안되면)
        ans = ans + nine # 건너뛴만큼의 숫자들 더하기(얼마만큼 건너 뛰었는지)
        digit+=1 # 자릿수 1 증가
        nine = nine*10 # 9, 90, 900.. 증가(건너뛸것)

    # (ans+1) = (9 or 99..) + 1 // 자릿수 -> 다음 자리 넘어가려면 +1 부터
    # (n-1) // digit = 다음 자리 넘어간 수로 인해 k-1 하고 자릿수만큼 나눈다
    # 그 값들을 더하면 현재 무슨 숫자에 속해있는지 알 수 있다.
    ans = (ans+1) + (n-1) // digit 
    
    # 현재 속한 수에서 자릿수 만큼 나눈 나머지 인덱스 = n번째 자릿수
    return int(str(ans)[(n-1)%digit]) 
