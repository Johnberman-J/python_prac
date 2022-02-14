def solution(lottos, win_nums):
    answer = [0, 0]
    correct = 0
    zero_count = 0
    
    for num in lottos:
        for win_num in win_nums:
            if num==win_num:
                correct = correct + 1
        if num==0:
            zero_count = zero_count + 1

    if correct == 1 or correct == 0:
        answer[1] = 6
    elif correct == 2:
        answer[1] = 5
    elif correct == 3:
        answer[1] = 4
    elif correct == 4:
        answer[1] = 3
    elif correct == 5:
        answer[1] = 2
    elif correct >=6:
        answer[1] = 1

    correct = correct + zero_count

    if correct == 1 or correct == 0:
        answer[0] = 6
    elif correct == 2:
        answer[0] = 5
    elif correct == 3:
        answer[0] = 4
    elif correct == 4:
        answer[0] = 3
    elif correct == 5:
        answer[0] = 2
    elif correct >=6:
        answer[0] = 1

    return answer