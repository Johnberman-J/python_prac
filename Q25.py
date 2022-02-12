from math import sqrt


def solution(n):
    answer = -1
    chk_num = sqrt(n)

    for num in range(int(chk_num)+1):
        if pow(chk_num,2) == pow(num,2):
            answer = pow(num+1,2)
            break


    return answer