def solution(lottos, win_nums):
    answer = [0, 0]
    correct = 0
    zero_count = 0
    
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }

    for num in lottos:
        for win_num in win_nums:
            if num==win_num:
                correct = correct + 1
        if num==0:
            zero_count = zero_count + 1

    answer[1] = rank[correct]

    correct = correct + zero_count

    answer[0] = rank[correct]
    
    return answer