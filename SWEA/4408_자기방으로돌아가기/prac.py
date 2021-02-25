# test = [0] * 100
# print(test)
#
# st = [[1,5],[2,3],[4,5],[1,10]]
# for i in range(len(st)):
#     for j in range(st[i][0],st[i][1]):
#         test[j] += 1
#
# print(test)
# print(st[0])
# print(st[1][1])
# print(st)
# print(len(st))

import sys
sys.stdin = open('input.txt')


def q_sort(nums):
    if len(nums) <= 1:
        return nums

    left, right = [], []
    pibut = nums[0]

    # 1부터 시작해야 한다!
    for i in range(1, len(nums)):
        if nums[i] < pibut:
            left.append(nums[i])
        else:
            right.append(nums[i])

    sorted_left = q_sort(left)
    sorted_right = q_sort(right)

    return [*sorted_left, pibut, *sorted_right]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    students = []
    cnt_list = [0]*400

    for idx in range(N):
        # start, end = map(int, input().split())
        students.append(list(map(int, input().split())))
    # print(students)

    # print(q_sort(students))
    students = q_sort(students)
    # for i in range(N):
    #     for j in range(i+1, N):
    #         # if students[i][1] < students[j][1] and students[i][1] > students[j][0]:
    #         if students[i][1] > students[j][0]:
    #             for
    #             cnt_list[i] += 1
    # if cnt > 2:
    #     cnt -= 1

    for i in range(N):
        for j in range(students[i][0], students[i][1]):
            cnt_list[j] += 1
    # print(cnt_list)
    # print(len(students))
    # print(students[0])
    # print(students)
    print(q_sort(cnt_list)[-1])
    # print('#{} {}'.format(tc, cnt))