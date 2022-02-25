# 스택 > 스택

length = int(input())
temp_stack = []
answer = ""

for i in range(length):
    input_data = input().split(" ")
    
    if len(input_data) == 1:
        if input_data[0] == "top":
            if len(temp_stack) <= 0:
                # print(-1)
                answer = answer + "-1" + "\n"
            else:
                # print()
                data = str(temp_stack[-1])
                answer = answer + data + "\n"
        elif input_data[0] == "size":
            # print(len(temp_stack))
            data = str(len(temp_stack))
            answer = answer + data + "\n"
        elif input_data[0] == "empty":
            if temp_stack:
                # print(0)
                answer = answer + "0" + "\n"
            else:
                # print(1)
                answer = answer + "1" + "\n"
        elif input_data[0] == "pop":
            if temp_stack:
                value = str(temp_stack.pop())
                answer = answer + value + "\n"
            else:
                # print(-1)
                answer = answer + "-1" + "\n"
    elif len(input_data) == 2:
        temp_stack.append(int(input_data[1]))

print(answer)