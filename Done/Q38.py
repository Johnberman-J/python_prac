def solution(s):
    answer = 0
    chk_arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(chk_arr)):
        s = s.replace(chk_arr[i], str(i))
    
    answer = int(s)

    return answer