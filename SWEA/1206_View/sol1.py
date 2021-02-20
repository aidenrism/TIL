import sys

sys.stdin = open('input.txt')


# T = int(input())
#
def my_max(x):
    max_num = x[0]
    for i in range(1, len(x)):
        if max_num < x[i]:
            max_num = x[i]
    return max_num


# numbers = [1, 2, 10, 3, 5, 12, 3, 0, 0]

# my_max()

# print(len(numbers))


# print(my_max(numbers))


for j in range(1, 11):
    count = 0
    length = int(input())
    numbers = list(map(int, input().split()))
    for i in range(len(numbers)):
        if i > 1 and i < len(numbers) - 2:
            # print(i)
            # 만약 양 옆에 두개가 존재한다면
            side_num = [numbers[i - 2], numbers[i - 1], numbers[i + 1], numbers[i + 2]]
            if numbers[i] >= my_max(side_num):
                # print(i)
                if numbers[i - 2] >= my_max([numbers[i - 1], numbers[i + 1], numbers[i + 2]]):
                    count += numbers[i] - numbers[i - 2]

                elif numbers[i - 1] >= my_max([numbers[i - 2], numbers[i + 1], numbers[i + 2]]):
                    count += numbers[i] - numbers[i - 1]

                elif numbers[i + 1] >= my_max([numbers[i - 2], numbers[i - 1], numbers[i + 2]]):
                    count += numbers[i] - numbers[i + 1]

                elif numbers[i + 2] >= my_max([numbers[i - 2], numbers[i - 1], numbers[i + 1]]):
                    count += numbers[i] - numbers[i + 2]

            else:
                pass

        else:
            continue

    print('#{} {}'.format(j, count))

# count = 0
# #
# # emp2 = []
#
# def my_max(x):
#     max_num = x[0]
#     for i in range(1, len(x)):
#         if max_num < x[i]:
#             max_num = x[i]
#     return max_num
#
# for i in range(10):
#     numbers = list(map(int, input().split()))
#     # print(len(numbers+1))
#     # emp = []
#     for i in range(1,len(numbers)):
#         if numbers[i] > (numbers[i-2] and numbers[i-1] and numbers[i+1] and numbers[i+2]):
#             if numbers[i-2] > (numbers[i-1] and numbers[i+1] and numbers[i+2]):
#                 count += numbers[i] - numbers[i-2]
#
#             elif numbers[i-1] > (numbers[i-2] and numbers[i+1] and numbers[i+2]):
#                 count += numbers[i] - numbers[i-1]
#
#             elif numbers[i+1] > (numbers[i-2] and numbers[i-1] and numbers[i+2]):
#                 count += numbers[i] - numbers[i+1]
#
#             elif numbers[i+2] > (numbers[i-2] and numbers[i-1] and numbers[i+1]):
#                 count += numbers[i] - numbers[i+2]
#     print(count)
#


# if numbers[i-2] > numbers[i-1] and numbers[i] - numbers[i-2] > 0:
#     number[i+2] > numbers[i+1] and numbers[i] - numbers[]


# count += 1
#     emp += [i]
#     emp2 += [i]
# print(len(emp), type,(emp))
# print(len(emp2), type, (emp2))

# print(numbers, type(numbers), len(numbers))


# 입력값이 100 이고 테스트케이스는 10개임
# 그냥 숫자로 T 받고 100 range동안 출력하면 '0 0 225 ..' 숫자로 쌓인 문자열 나옴
# list 변환하면 ['0', ' ', '0', ...] 과 같이 문자열을 쪼갠 리스트로 출력됨 >> ''공백단위로 숫자로 mapping 해줘야 함
# map 안하고 .split() 만해서 리스트로하면 그래도 문자열로 된 숫자들이 리스트로 감싸짐
