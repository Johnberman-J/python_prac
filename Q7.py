def solution(absolutes, signs):
    answer = 0
    length = len(absolutes)
    count = 0
    
    while(count<length):
        if(signs[count]==True) :
            answer = answer + absolutes[count]
        else:
            answer = answer + absolutes[count] * -1
        count = count+1
    return answer