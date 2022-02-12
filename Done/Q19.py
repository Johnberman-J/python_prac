def solution(n):
    answer = ""
    odd = "박"
    even = "수"

    for i in range(n):
        if(i%2==0):
            answer = answer + even
        else:
            answer = answer + odd

    return answer