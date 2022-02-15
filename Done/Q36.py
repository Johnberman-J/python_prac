def solution(s):
    answer = ''
    ans_arr = list(s)
    ans_arr.sort(reverse=True)
    answer = "".join(ans_arr)
    return answer