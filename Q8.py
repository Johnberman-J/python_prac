def solution(arr):
    answer = 0
    sum = 0
    length = len(arr)

    for i in range(0,length):
        sum = sum + arr[i]

    answer = sum/length

    return answer