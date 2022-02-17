def solution(d, budget):
    answer = 0
    sum_money = budget
    d.sort()
    
    for money in d:
        if sum_money < money:
            break
        sum_money -= money
        answer += 1

    return answer