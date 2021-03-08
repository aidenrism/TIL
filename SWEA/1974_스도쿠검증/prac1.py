# a = 1
# b = 3

# if (a, b == 3):
#     print(a, b)
# if a == 3 and b == 3:
#     print('aa')
# if (a and b) ==3:
#     print(a)
# if False:
#     print(0)
# if True:
#     print(10)
if False and False:
    print(0)
if True and False:
    print(1)
if False and True:
    print(2)
if True and True:
    print(3)
# import sys
# sys.stdin = open('input.txt')

# def Isreal(sudoku):
#     # cnt1 = 0
#     # cnt2 = 0
#     result = 0
#     cnt1 = 0
#     cnt2 = 0
#     cnt3 = 0
#     cnt4 = 0
#     for i in range(9):
#
#
#         for j in range(9):
#             cnt1 += sudoku[i][j]
#             cnt2 += sudoku[j][i]
#
#             if i % 3 == 0 and j % 3 == 0:
#                 for k in range(3):
#                     for l in range(3):
#                         cnt4 += 1
#                         cnt3 += sudoku[i + k][j + l]
#                 if cnt3 != 45:
#                     result += 100
#                 # print(cnt3)
#         if cnt1 != 45 and cnt2 != 45:
#             # if (cnt1 and cnt2) != 45:
#             # if cnt1 != 45 and cnt2 != 45:
#             result += 10
#     print(cnt1)
#     print(cnt2)
#     print(cnt3)
#     # print(cnt4)
#
#     print(result)
#     # if result == 0:
#     #     return 1
#     # else:
#     #     return 0
#
#     # print(cnt1)
#     # print(cnt2)
#     # print(cnt3)
#
# T = int(input())
# for tc in range(1, T+1):
#     sudoku = [list(map(int, input().split())) for _ in range(9)]
#
#     print('#{} {}'.format(tc, Isreal(sudoku)))
