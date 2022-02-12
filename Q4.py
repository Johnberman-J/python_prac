def solution(a, b):
    answer = 0
    if a>b :
        length = range(b,a+1)
        for i in length:
            answer = answer + i
    elif b>a :
        length = range(a,b+1)
        for i in length:
            answer = answer + i
    else:
        answer = a        
    return answer