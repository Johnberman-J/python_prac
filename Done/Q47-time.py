import math


def solution(n):
    answer = 0
    chk_list = [True] * (n+1)
    max_num = int(math.sqrt(n)) + 1
    
    for i in range(2, max_num):
        if chk_list[i] == False:
            continue

        for j in range(i, n+1):
            if i*j <= n:
                chk_list[i*j] = False
        
    for i in range(2, n+1):
        if chk_list[i] != False:
            answer += 1
     
    return answer