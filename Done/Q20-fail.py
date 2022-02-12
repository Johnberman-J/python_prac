def solution(participant, completion):
    remain_arr = participant

    for i in range(len(completion)):
        remain_arr.remove(completion[i])
    
    return remain_arr[0]