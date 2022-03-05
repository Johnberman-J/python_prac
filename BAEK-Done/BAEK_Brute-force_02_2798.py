# 브루트포스 > 블랙잭

m,n = map(int, input().split())
number_arr = list(map(int, input().split()))
sum_arr = []
number_arr.sort(reverse=True)

for i in range(len(number_arr)-2):
    for j in range(i+1,len(number_arr)-1):
        if number_arr[i]+number_arr[j] > n:
            continue
        for k in range(j+1, len(number_arr)):
            if number_arr[i]+number_arr[j]+number_arr[k] > n:
                continue
            sum_number = number_arr[i]+number_arr[j]+number_arr[k]
            sum_arr.append(sum_number)

print(max(sum_arr))