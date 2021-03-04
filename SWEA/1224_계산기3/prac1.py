import sys
sys.stdin = open('input.txt')
#
# # def backsol(numbers):
# #
# #     for idx in numbers:
# #         number = '012345679'
# #
# #         print(idx)
# #         print(numbers[idx])
#
# # for tc in range(10):
# N = int(input())
# numbers = input()
# back = []
# stack = []
# number = '012345679'
# # for idx in range(N):
# for idx in range(len(numbers)):
#     # print(idx,type(idx))
#     print(numbers[idx], idx)
#     if numbers[idx] in number:
#
#         #         # print( type(int(numbers[idx])))
#
#         back.append(numbers[idx])
#
# print(back)
# # print(backsol(numbers))
#     # print(solution(backsol(numbers))

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


def cal(numbers):

    number = '0123456789'
    cal = []

    for idx in range(len(numbers)):
        if numbers[idx] in number:
            cal.append(int(numbers[idx]))
        else:
            # if len(cal) >= 3:
            #     # if numbers[idx] == '*':
            #     if numbers[idx] == '*':
            #         cal.append(cal.pop(-2) * cal.pop())
            #     elif numbers[idx] == '+':
            #         cal.append(cal.pop(-2) + cal.pop())
            # else:
            if numbers[idx] == '*':
                cal.append(cal.pop(-2) * cal.pop())
            elif numbers[idx] == '+':
                cal.append(cal.pop(-2) + cal.pop())
    return cal

for tc in range(1,11):
    N = int(input())
    numbers = input()
    back = []
    stack = []
    print('#{} {}'.format(tc, *cal(backsol(numbers))))