# 그리디 알고리즘 > 잃어버린 괄호

input_arr = input().split("-")

sum = 0

for i in range(len(input_arr)):
    temp_sum = 0
    temp_arr = input_arr[i].split("+")

    for j in range(len(temp_arr)):
        temp_sum += int(temp_arr[j])
    
    if i==0:
        sum += temp_sum
    else:
        sum -= temp_sum

print(sum)
