def solution(n):
    answer = []
    n = str(n)
    length = len(n)
    
    for i in range(length):
        answer.append(int(n[i]))
    
    answer.reverse()

    return answer