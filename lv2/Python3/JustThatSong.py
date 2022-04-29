# My turn
def solution(m, musicinfos):
    answer = '' # 답에 해당되는 노래제목
    check_time = 0 # 흘러나온 시간이 긴 것을 저장하기 위한 변수
    m = list(m) # 음계를 리스트로
    len_m = 0 # 음계 길이

    for i in range(len(m)):
        if m[i] != '#': # '#'은 건너뛰고 음계 거리 계산
            len_m += 1

    for musicinfo in musicinfos: # 노래 정보
        start_time, end_time, music, score = musicinfo.split(',') # 시작, 끝, 노래, 악보
        len_score = len(score) # 악보 길이
        total_time = ((int(end_time[:2])-int(start_time[:2])) * 60) - (int(start_time[3:])-int(end_time[3:])) # 시간 계산
        
        tmp = [] # 임시 배열
        idx,leng = 0,0 # 인덱스와 악보 길이
        while leng != total_time: # 악보 길이 동안
            tmp.append(score[idx%len_score]) # 음계 추가
            if score[(idx+1)%len_score] == '#': # 다음 음계가 '#'이라면
                tmp.append(score[(idx+1)%len_score]) # '#'도 배열에 추가
                idx += 1 # 인덱스 추가(길이는 안늘리고)
            leng += 1 # 총 길이 +=1
            idx += 1 # 인덱스 +=1
        
        
        index,length,len_tmp = 0,0, len(tmp) # 인덱스, 길이, 임시 변수 총 길이
        info_tmp = [] # 본인이 기억한 음계 길이만큼 저장될 배열

        while index < len_tmp: # 인덱스가 임시변수 길이보다 작을동안
            info_tmp.append(tmp[index]) # 추가
            if tmp[index] != '#': # '#'이 아니라면 
                length += 1 # 길이 += 1
            if index + 1 < len_tmp and tmp[index+1] == '#': # 마지막 인덱스 전이고 다음 인덱스에 해당하는 것이 '#' 이라면
                info_tmp.append(tmp[index+1]) # 임시변수에 '#' 추가
                index += 1 # 인덱스 다음거로

            if length == len_m: # 해당 길이가 내가 기억한 길이와 맞을때
                print(length, info_tmp)
                if m == info_tmp: # 답과 일치하면
                    if check_time < total_time: # 총 나온 시간이 긴 것은
                        check_time = total_time # 그 시간을 기록하고
                        answer = music # 해당 노래를 답으로
                    break # 빠져나오기
                info_tmp.pop(0)  # 답과 일치하지 않으면 첫번째 배열것 빼기
                if len(info_tmp) != 0 and info_tmp[0] == '#': # 만약 임시 배열 길이가 1 이상이고 첫번째 원소가 '#' 이라면
                    info_tmp.pop(0) # 그냥 빼내기
                length -= 1 # 길이 -= 1
                        
            index += 1 # 인덱스 다음거로            

    return answer if answer else '(None)' # 답이 있으면 답을 없으면 '(None)' 출력

#print(solution("C", ["13:00,13:01,WORLD,F"]))
#print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
#print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
#print(solution("CC#BCC#BCC#",["03:00,03:08,FOO,CC#B"]))
#print(solution("CCB",["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))

# Good Explanation
def shap_to_lower(s): # '#'이 붙은 음계를 소문자로(다른 문자로 대체)
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m) # '#'음계 변경
    for info in musicinfos: # 노래 정보
        split_info = info.split(',') # ',' 기준으로 나누고
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:]) # 시간 구하기
        title = split_info[2] # 노래 제목
        part_notes = shap_to_lower(split_info[-1]) # 흘러나온 음계들 '#'을 변경
        # 흘러나온동안의 음계들(몫과 나머지로 계산)
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]: # 해당 노래가 흘러나온동안 음계에 포함되고 흘러나온 음계가 가장 큰것을
            answer=[time_length,title] # 답에 추가
    return answer[-1] 

solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])