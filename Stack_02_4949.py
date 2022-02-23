# 스택 > 균형잡힌 세상

import sys


input_data = sys.stdin.readline

while True:
    temp_stack = []
    input_string = input_data().rstrip()
    # 이부분 주의. 마지막(7번)케이스때문에 strip()이 아닌 rstrip()써야함.
    if input_string == ".":
        break

    for word in input_string:
        if word=="(" or word=="[":
            temp_stack.append(word)
        elif word==")":
            if len(temp_stack)!=0 and temp_stack[-1] == "(":
                temp_stack.pop()
            else:
                temp_stack.append(word)
                break
        elif word=="]":
            if len(temp_stack)!=0 and temp_stack[-1] == "[":
                temp_stack.pop()
            else:
                temp_stack.append(word)
                break
                
    
    if len(temp_stack)==0:
        print("yes")
    else:
        print("no")

            
                

