def solution(phone_number):
    answer = ''
    ans_list = list(phone_number)

    for word in range(0,len(ans_list)-4):
        answer = answer + "*"
    for num in range(len(ans_list)-4,len(ans_list)):
        answer = answer + ans_list[num]
                
    return answer