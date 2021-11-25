# My turn
def solution(price, money, count):
    for c in range(1,count+1):
        money -=  price * c

    if money >= 0:
        return 0
    else:
        return -money

# Good explanation
def solution(price, money, count): 
    return max(0,price*(count+1)*count//2-money) # 등차수열 합공식