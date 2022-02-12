# 파이썬은 나누기하면 실수형으로 바뀐다. 이점을 주의

def solution(s):
    answer = ''
    length=len(s)
    
    if length%2==0:
        a = int(length/2 -1)
        b = int(length/2)
        answer=s[a]+s[b]
    else:
        a = int(length/2)
        answer=s[a]
    return answer