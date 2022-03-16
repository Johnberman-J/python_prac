# 동적 계획법 > RGB 거리
# 세가지의 누적합을 전부 dp에 넣어두고 최소값을 마지막에 찾아낸다!


length = int(input())
price = []

for i in range(length):
    price.append(list(map(int, input().split())))

for i in range(1, len(price)):
    price[i][0] = min(price[i-1][1], price[i-1][2]) + price[i][0]
    price[i][1] = min(price[i-1][0], price[i-1][2]) + price[i][1]
    price[i][2] = min(price[i-1][0], price[i-1][1]) + price[i][2]

print(min(price[length-1][0], price[length-1][1], price[length-1][2]))
