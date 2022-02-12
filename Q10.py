def solution(arr1, arr2):
    answer = arr1

    for i in range(len(arr1)):
        for k in range(len(arr1[i])):
            arr1[i][k] = arr1[i][k] + arr2[i][k]

    return answer