def solution(s):
    zeroCnt,time = 0,0
    while True:
        time += 1
        oneCnt = 0
        for i in range(len(s)):
            if s[i] == '1': oneCnt+=1
            else:  zeroCnt +=1
        s = ''.join(bin(oneCnt)[2:])
        if s == '1': return [time, zeroCnt]