# 분모가 0일때도 생각해야한다
def solution(N, stages):
    answer = []
    fail_arr = []
    temp_stages = stages
    total_success = len(stages)

    for i in range(1,N+1):
        fail_count = 0
        temp_arr = []
        for j in range(len(temp_stages)):
            if temp_stages[j] <= i:
                fail_count += 1
            else:
                temp_arr.append(temp_stages[j])

        fail_prob = fail_count/total_success
        fail_arr.append(fail_prob)

        total_success = total_success - fail_count
        temp_stages = temp_arr

    a = sorted(fail_arr, reverse=True)
    print(fail_arr)
    
    for i in range(len(a)):
        answer.append(fail_arr.index(a[i])+1)
        fail_arr[fail_arr.index(a[i])]=2

    return answer