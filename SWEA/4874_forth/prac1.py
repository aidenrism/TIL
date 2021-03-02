def backsolve(testlist):
    stack = []
    for i in range(len(test_list)):
        if test_list[i] == '+':
            try:
                stack.append(stack.pop() + stack.pop())
            except:
                return 'error'
        elif test_list[i] == '-':
            try:
                stack.append(stack.pop() - stack.pop())
            except:
                return 'error'
        elif test_list[i] == '*':
            try:
                stack.append(stack.pop() * stack.pop())
            except:
                return 'error'
        elif test_list[i] == '/':
            try:
                stack.append(stack.pop() / stack.pop())
            except:
                return 'error'
        else:
            stack.append(test_list[i])

        if test_list[i] == '.':
           return stack[0]



test_list = [10,'*', 2, '+', 3, 4, '+', '*', '.']

print(backsolve(test_list))