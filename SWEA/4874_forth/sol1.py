import sys
sys.stdin = open('input.txt')


def backsolve(test_list):
    stack = []
    operater = ['+', '-', '*', '/', '.']
    try:
        for i in range(len(test_list)):
            if test_list[i] not in operater:
                stack.append(test_list[i])
            else:
                if test_list[i] == '.':
                    ans = stack.pop()

                if test_list[i] == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif test_list[i] == '-':
                    stack.append(int(stack.pop()) - int(stack.pop()))
                elif test_list[i] == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif test_list[i] == '/':
                    stack.append(int(stack.pop()) // int(stack.pop()))
    except:
        ans = 'error'
    if len(stack) >= 1:
        ans = 'error'

        # if test_list[i] == '.':
        #     if len(stack) == 2:
        #         return stack[0]
        #     else:
        #         return 'error'
        # if len(test_list) <= 3:
        #     return 'error'
    return ans
T = int(input())
for tc in range(1, T+1):


    test_list = list(input().split())
    print('#{} {}'.format(tc, backsolve(test_list)))