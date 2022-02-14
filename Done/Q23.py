# sort()는 기준에 따라 오름차순 또는 내림차순 정렬을 하는 것 
# reverse()는 단순히 리스트의 순서를 뒤집는 것

def solution(n):
    answer = []
    n = str(n)
    length = len(n)
    
    for i in range(length):
        answer.append(int(n[i]))
    
    answer.reverse()

    return answer