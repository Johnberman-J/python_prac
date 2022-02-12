def solution(n):
    answer = 0
    ans_arr=list(str(n))

    for num in ans_arr:
        answer = answer + int(num)    

    return answer