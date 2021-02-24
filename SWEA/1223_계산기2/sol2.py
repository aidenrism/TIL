import sys
sys.stdin = open('input.txt')


def backsol(numbers):

    stack = []
    back = []
    for idx in range(N):
        if idx%2 == 0:
            back.append(numbers[idx])
        else:
            if len(stack) == 0:
                stack.append(numbers[idx])
            elif numbers[idx] == '+':
                while stack:
                    back.append(stack.pop())
                stack.append(numbers[idx])
            elif numbers[idx] == '*':
                if stack[-1] == '+':
                    stack.append(numbers[idx])
                else:
                    if stack[-1] != '+':
                        back.append(stack.pop())
                    stack.append(numbers[idx])
        if idx > N-2:
            while stack:
                back.append(stack.pop())
    return ''.join(back)

def solution(back):
    stack = []
    for char in back:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            y = stack.pop()
            x = stack.pop()
            stack.append(x + y)
        elif char == '*':
            y = stack.pop()
            x = stack.pop()
            stack.append(x * y)

    return stack

for tc in range(1, 11):
    N = int(input())
    numbers = list(input())
    # print(backsol(numbers))
    print('#{} {}'.format(tc, *solution(backsol(numbers))))