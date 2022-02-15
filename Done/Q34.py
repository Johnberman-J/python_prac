def solution(answers):
    answer = [0,0,0]
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if supo1[i%5]==answers[i]:
            answer[0] = answer[0] + 1
        if supo2[i%8]==answers[i]:
            answer[1] = answer[1] + 1
        if supo3[i%10]==answers[i]:
            answer[2] = answer[2] + 1

    max_num = max(answer)
    
    rank_arr=[]

    for i in range(len(answer)):
        if answer[i]==max_num:
            rank_arr.append(i+1)

    rank_arr.sort()

    return rank_arr