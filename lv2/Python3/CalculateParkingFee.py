import math
def time_check(start, end): # 주차 시간을 체크
    return (int(end[:2]) - int(start[:2]))* 60 - (int(start[3:]) - int(end[3:]))

def solution(fees, records):
    answer = []
    car_dic,acc_park = {}, {} # 차의 출차 정보를 담을 car_dic, 차의 누적 주차 시간을 담을 acc_park(dict)
    basic_time, basic_fee, part_time, part_fee = fees[0], fees[1], fees[2], fees[3] # 주어진 정보들

    for record in records: # 기록을 하나씩 순회
        time, car_num, in_out = record.split(' ') # 시간, 차 번호, 출차 정보
        if car_num not in acc_park: # 한번도 들어오지 않았던 차면
            acc_park[car_num] = 0 # 누적 주차 시간에 현재 차 정보를 담음

        if in_out == 'IN': # 주차면
            car_dic[car_num] = time # 차번호 : 주차 시간 기록
        else: # 출차면
            acc_park[car_num] += time_check(car_dic[car_num], time) # 누적 주차 시간에 주차 시간을 누적
            car_dic[car_num] = False # 일종의 Flag(이 차가 끝까지 안나갔나를 체크하려고)

    for car in car_dic: # 출차 정보중에
        if car_dic[car]: # 아직 남아있는 차가 있으면
            acc_park[car] += time_check(car_dic[car], '23:59') # 00시 되기전에 밀어버려!
    # 조건: 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 
    acc_park = sorted(acc_park.items(), key = lambda x : int(x[0])) 
    
    for acc in acc_park: # 누적 차량 주차시간
        _, total_time = acc 
        answer.append(basic_fee) if total_time <= basic_time else answer.append(basic_fee + math.ceil((total_time-basic_time)/part_time) * part_fee)
            
    return answer
# 주차 요금(기본시간(분), 기본 요금, 단위 시간(분)) 
solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
#solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT"])
#dic = {'10':'2', '3': '2', '5':'3', '2':'4'}
#print(sorted(dic, key= lambda x: int(x)))