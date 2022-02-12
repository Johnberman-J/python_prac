def solution(x, n):
    answer = []
    count = 0
    append_number = 0

    while(count<n):
        if count<1:
            append_number = x
            answer.append(append_number)
        else:
            append_number = append_number + x
            answer.append(append_number)
        
        count = count+1

    return answer