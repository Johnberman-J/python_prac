def solution(x):
    answer = True
    x_arr = list(str(x))
    dividend_sum = 0
    
    for num in x_arr:
        dividend_sum = dividend_sum + int(num)
    
    if x%dividend_sum != 0:
        answer = False
    
    return answer