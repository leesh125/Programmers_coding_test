# My turn
def solution(word):
    all_case = sum(list(map(lambda x: 5 ** x, range(1,6)))) # 모든 경우의 수(3920)
    # 문자를 숫자형태로 바꿔줌
    num = list(map(lambda x: 1 if x == 'A' else (2 if x == 'E' else (3 if x == 'I' else (4 if x == 'O' else 5))), word))
    # 첫번째 자릿수의 차이는 3920 // 5의 1승, 두번째 자릿수 차이 3920 // 5의 2승 이런식으로 식이 나오는데 여기에 aeiou 차이만큼 곱해주면 된다, A 일때는 1
    return sum(list(map(lambda x : (x[1]-1)*(all_case//5**(x[0]))+1 if x[1] != 1 else 1, enumerate(num,start=1))))


solution("AAAE")
solution("I")
solution("EIO")

# Good Explanation
from itertools import product

# product(리스트 or 문자열 등, repeat = 뽑고자 하는 원소의 길이) 중복 순열
# 1 ~ 5까지 뽑고 이를 정렬한 후 index를 구한다
solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
