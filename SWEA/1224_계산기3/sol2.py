import sys
sys.stdin = open('input.txt')


isp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
    ')': None
}

icp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 3,
    ')': None
}


# 후위 표기식으로 변환하는 함수
def backsol(numbers):
    for idx in range(len(numbers)):
        number = '0123456789'

        # print(idx)
        # print(numbers[idx])
        if numbers[idx] in number:
            back.append(numbers[idx])
            # print(back)
        else:
            if len(stack) == 0:
                stack.append(numbers[idx])

            elif numbers[idx] == '(':
                stack.append(numbers[idx])

            elif numbers[idx] == '+':
                while stack[-1] != '(' and len(stack) != 0:
                    back.append(stack.pop())
                stack.append(numbers[idx])

            elif numbers[idx] == '*':
                while stack[-1] != '+' and stack[-1] != '(':
                    back.append(stack.pop())
                stack.append(numbers[idx])

            elif numbers[idx] == ')':
                while stack[-1] != '(':
                    if stack[-1] != '(':
                        back.append(stack.pop())
                    else:
                        pass
                else:
                    stack.pop()
            if idx > N-2 and stack:
                while stack:
                    back.append(stack.pop())
        # for 다 돌고 스택에 남은 것을 결과에 담는다
    while stack:
        back.append(stack.pop())
        # string 으로 변환해 반환
    return ''.join(back)


# 후위 표기식을 계산하는 함수
def cal(result):
    stack = []
    for idx in range(len(result)):
        # 만약 숫자면 스택에 push
        if result[idx] not in isp.keys():
            stack.append(int(result[idx]))
        # 만약 기호면, 스택에 있는 두 숫자를 연산한 후 스택에 push
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if result[idx] == '+':
                stack.append(num2 + num1)
            elif result[idx] == '-':
                stack.append(num2 - num1)
            elif result[idx] == '*':
                stack.append(num2 * num1)
            elif result[idx] == '/':
                stack.append(num2 / num1)

    # 스택의 0번 인덱스 항목을 반환한다.
    return stack[0]


T = 1

for tc in range(1,11):
    N = int(input())
    numbers = input()
    back = []
    stack = []
    print('#{} {}'.format(tc, cal(backsol(numbers))))