# 스택 > 스택

length = int(input())
temp_stack = []

for i in range(length):
    input_data = input().split(" ")
    
    if len(input_data) == 1:
        if input_data[0] == "top":
            if len(temp_stack) <= 0:
                print(-1)
            else:
                print(temp_stack[-1])
        elif input_data[0] == "size":
            print(len(temp_stack))
        elif input_data[0] == "empty":
            if temp_stack:
                print(0)
            else:
                print(1)
        elif input_data[0] == "pop":
            if temp_stack:
                value = temp_stack.pop()
                print(value)
            else:
                print(-1)
    elif len(input_data) == 2:
        temp_stack.append(int(input_data[1]))
