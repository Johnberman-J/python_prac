def solution(arr):
    answer = []
    temp_num = arr[0]
    answer.append(temp_num)

    for num in arr:
        if num != temp_num:
            answer.append(num)
            temp_num = num
     
    return answer