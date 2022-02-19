def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        if i == j:
            answer.append(array[i-1])
            continue

        sum_arr = array[i-1:j]
        sum_arr.sort()

        result = sum_arr[k-1]
        answer.append(result)

    return answer
