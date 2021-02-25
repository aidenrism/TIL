런타임에러 코드
import sys
sys.stdin = open('input.txt')


# def q_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     left, right = [], []
#     pibut = nums[0]
#     for i in range(1, len(nums)):
#         if nums[i] < pibut:
#             left.append(nums[i])
#         else:
#             right.append(nums[i])
#     sorted_left = q_sort(left)
#     sorted_right = q_sort(right)
#     return [*sorted_left, pibut, *sorted_right]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = []
    cnt_list = [0]*400

    for idx in range(N):
        students.append(list(map(int, input().split())))

    students = sorted(students)


    for i in range(N):
        # print(students[i][1], students[i][0])
        if students[i][1] > students[i][0]:
            if students[i][1]%2==1:
                for j in range(students[i][0], students[i][1] + 2):
                    cnt_list[j] += 1
            else:
                for j in range(students[i][0]-1, students[i][1]+1):
                    cnt_list[j] += 1
                # print(j)
        elif students[i][0] > students[i][1]:
            # print(students[i][0])
            for j in range(students[i][0], students[i][1]-1, -1):
                cnt_list[j] += 1
                # print(j)
    # print(cnt_list)
    print('#{} {}'.format(tc, max(cnt_list)))
