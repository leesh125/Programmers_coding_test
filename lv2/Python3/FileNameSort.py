# My turn
def check_head(s): # head 부분 검증
    if 'a' <= s <= 'z' or 'A' <= s <= 'Z' or s == " " or s == "." or s == "-":
        return True
    return False

def check_num(n): # number 부분 검증
    if '0' <= n <= '9':
        return True
    return False

def solution(files):
    answer = [[""] * 3 for _ in range(len(files))] # head, number, tail을 각각 따로 담을 리스트
    res = [] 
    index = 0 # 인덱스 0부터 시작

    for file in files: # 파일 순회
        flag = True # flag 기본값 True
        for i in range(len(file)): # file 길이만큼
            if check_head(file[i]): # head 부분 검증
                if flag: 
                    answer[index][0] += file[i] # 해당 인덱스의 0(head) 부분에 문자열 추가
                else: # head -> num 부분을 검증한 후면
                    break # 더이상 검증할 필요없음
            elif check_num(file[i]): # number 부분 검증
                answer[index][1] += file[i] # 해당 인덱스의 1(number) 부분에 문자열 추가
                flag = False # flag를 False로 하여 그 뒤로 문자열 검증은 건너 뜀
        if i < len(file)-1: # 숫자 부분에서 검증이 끝난 것을 위한 처리
            answer[index][2] += file[i:] # tail 부분 추가
        index += 1 # 인덱스 1 증가

    # head 부분을 대문자로 변경 후 비교 -> number 부분을 정수로 변환 후 비교
    answer = sorted(answer, key= lambda x: (x[0].upper(),int(x[1]))) 
    for a in answer: 
        res.append(''.join(a)) # res에 추가해주기
    return res

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
#["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

# Good Explanation
import re

def solution(files):
    # 숫자에 대한 정렬 먼저 진행(배열 형태로 나오기에 [0] 원소에 해당되는 숫자형태의 문자를 int로 치환후 이를 비교)
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    # 그 다음 head(문자열)에 대한 정렬 진행([0]인덱스에는 head 부분에 대한 정보)
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
# ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# "F-5 Freedom Fighter", "A-10 Thunderbolt II", "F-14 Tomcat", "B-50 Superfortress"
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]