def solution(price, money, count):
    answer = -1
    change = money

    for i in range(1,count+1):
        change = change - price * i
        
    if change >= 0:
        answer = 0
    else:
        answer = abs(change)

    return answer