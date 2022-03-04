# 스택 > 괄호
# strip()은 앞,뒤에 있는 공백문자들을 제거해주는 메소드

length = int(input())

for i in range(length):
    temp_stack = []
    input_data = input()

    for check in input_data:
        if check == "(":
            temp_stack.append(check)
        elif check == ")" :
            if len(temp_stack) <= 0:
                temp_stack.append(check)
                break
            else:
                temp_stack.pop()
            
    if len(temp_stack) == 0:
        print("YES")
    else:
        print("NO")