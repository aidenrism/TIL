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
    # return back

def solution(numbers):

    number = '0123456789'
    cal = []

    for idx in range(len(numbers)):
        if numbers[idx] in number:
            cal.append(int(numbers[idx]))
        else:
            if len(cal) >= 3:
                if numbers[idx] == '*':
                    if numbers[idx] == '*':
                        cal.append(cal.pop(-2) * cal.pop())
                    elif numbers[idx] == '+':
                        cal.append(cal.pop(-2) + cal.pop())
            else:
                if numbers[idx] == '*':
                    cal.append(cal.pop(-2) * cal.pop())
                elif numbers[idx] == '+':
                    cal.append(cal.pop(-2) + cal.pop())
    return cal

for tc in range(1, 11):
    N = int(input())
    numbers = list(input())
    # print(numbers)
    # print(numbers[0]+numbers[2])
    # print(type(numbers[0]),type(int(numbers[0])))

    print(backsol(numbers))
    # print(eval(backsol(numbers)))

    print('#{} {}'.format(tc, *solution(backsol(numbers))))