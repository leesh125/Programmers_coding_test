def solution(n):
    ans = 0
    digit = 1
    nine = 9
    
    while n > digit*nine:
        n = n-(digit * nine)
        ans = ans + nine
        digit+=1
        nine = nine*10

    ans = (ans+1) + (n-1) // digit
    
    return int(str(ans)[(n-1)%digit])
