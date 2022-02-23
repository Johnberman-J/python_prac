def solution(board, moves):
    answer = 0
    board.reverse()
    stack_arr = get_stack(board)
    answer = get_delete_count(stack_arr, moves)

    return answer

def get_stack(input_arr):
    stack_arr = []
    
    i=0
    while i < len(input_arr):
        temp_arr = []
        for line in input_arr:
            chk_number = line[i]
            if chk_number !=0:
                temp_arr.append(chk_number)
        
        stack_arr.append(temp_arr)
        i += 1
    
    return stack_arr

def get_delete_count(stacks_arr, moves_arr):
    count = 0
    break_stack = []
    
    for selector in moves_arr:
        print(count)
        modify_selector = selector - 1
        if len(stacks_arr[modify_selector]) > 0:
            pop_from_stack_arr = stacks_arr[modify_selector].pop()

            if len(break_stack) == 0:
                break_stack.append(pop_from_stack_arr)
            else:
                last_break_stack = break_stack[len(break_stack)-1]
                if last_break_stack == pop_from_stack_arr:
                    break_stack.pop()
                    count += 2
                else:
                    break_stack.append(pop_from_stack_arr)
        else:
            continue
            
    return count