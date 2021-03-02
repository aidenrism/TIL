import sys
sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     maze = [list(input().split()) for _ in range(n)]
#     # for _ in range(n):
#     #     maze.append(list(map(int, input().split())))
#         # maze.append(list(input().split()))
#     print(maze)
#     print(maze[4][0][3])
#     # print(maze[1])
#
#     for i in range(n):
#         for j in range(1):
#             for k in range(n):
#                 if maze[i][j][k] == 2:
#                     print('yes')


#
test_numb = int(input())
for i in range(test_numb):
    arr_size = int(input())
    arr = list()
    start_location = list()
    end_location = list()
    for j in range(arr_size):
        one_arr_str = input()
        one_arr = list()
        for ind, k in enumerate(one_arr_str):
            # print(ind, k)
            if k == '2':
                start_location.append(j)
                start_location.append(ind)

            elif k == '3':
                end_location.append(j)
                end_location.append(ind)
            one_arr.append(k)
        arr.append(one_arr)
    print(arr,type(one_arr))
#     # print(start_location)
#     # print(end_location)
#     print(one_arr_str,type(one_arr_str))
#     # ans = solution(start_location, end_location, arr)
#     #
#     # print("#{} {}".format(i+1, ans))