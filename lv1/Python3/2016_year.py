# My turn
import datetime

def solution(a, b):
    answer = ''
    days = ['MON','TUE', 'WED','THU','FRI','SAT','SUN']
    answer = days[datetime.date(2016, a, b).weekday()]    
    return answer

print(solution(5,24))

# Good explanation
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

print(getDayName(5,24))
