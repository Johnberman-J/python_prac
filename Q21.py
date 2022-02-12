def solution(s):
    s = s.split(" ")
    ans_arr = []
    for word in s:
        answer = ''
        for i in range(len(word)):
            if i%2 == 0:
                answer = answer + word[i].upper()
            else:
                answer = answer + word[i]

    return answer