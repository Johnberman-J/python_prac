def solution(seoul):
    length = len(seoul)
    i = 0

    while(i<length):
        if seoul[i]=="Kim":
            break
        i = i + 1
    
    answer = "김서방은 " + str(i) + "에" + " 있다"

    return answer