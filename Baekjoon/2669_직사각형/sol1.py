import sys
sys.stdin = open('input.txt')


hundred = [[0] * 101 for _ in range(101)]
cnt1 = 0

for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for j in range(y1+1, y2+1):
        for i in range(x1+1, x2+1):
            if hundred[j][i] == 0:
                hundred[j][i] = 1
                cnt1 += 1
print(cnt1)

    # print(x1)
    # print(hundred)

# point = [[0] * 101 for _ in range(101)]
# cnt = 0
#
# for _ in range(4):
#     x1, y1, x2, y2 = list(map(int, input().split()))
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             if point[j][i] == 0:
#                 point[j][i] = 1
#                 cnt += 1
# print(cnt)