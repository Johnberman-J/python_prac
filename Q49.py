def solution(n, lost, reserve):
    answer = 0
    chk_list = [True] * n+1

    for i in range(len(lost)):
        chk_list[lost[i]] = False
    
    print(chk_list)
    
    # for i in range(len(reserve)):
    #     if reserve[i] - 2 < 0:
    #         chk_list[reserve[i]] = True
    #     else:
    #         chk_list[reserve[i]-2] = True      
    #         chk_list[reserve[i]] = True
        
    
    # for chk in chk_list:
    #     if chk == True:
    #         answer += 1

    return answer