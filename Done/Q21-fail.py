def solution(s):
    answer = ''
    words_arr = s.split(" ")
    ans_arr = []
    for word in words_arr :
        for i in range(len(word)):
            if i%2==0:
                answer = answer + word[i].upper()
            else:
                answer = answer + word[i]
        ans_arr.append(answer)
        answer = ""
    
    answer = " ".join(ans_arr)
    return answer