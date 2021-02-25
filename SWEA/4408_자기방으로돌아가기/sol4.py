import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     rooms = []
#     for _ in range(n):
#         a, b = map(int, input().split())
#         if a > b:
#             a, b = b, a
#         rooms.append((a, b))
#
#     result = 0
#     while rooms:
#         a, b = rooms.pop(0)
#         done = []
#         for idx in range(len(rooms)):
#             c, d = rooms[idx]
#             if a > d or b < c:
#                 done.append(idx)
#         for i in done[::-1]:
#             rooms.pop(i)
#         result += 1
#
#     print('#{} {}'.format(tc, result))
#
#     T = int(input())
#     for tc in range(1, T + 1):
#         n = int(input())
#         rooms = []
#         for _ in range(n):
#             a, b = map(int, input().split())
#             if a > b:
#                 a, b = b, a
#             rooms.append((a, b))
#
#         result = 0
#         while rooms:
#             a, b = rooms.pop(0)
#             done = []
#             for idx in range(len(rooms)):
#                 c, d = rooms[idx]
#                 if a > d + 1 or b + 1 < c:
#                     done.append(idx)
#             for i in done[::-1]:
#                 rooms.pop(i)
#             result += 1
#
#         print('#{} {}'.format(tc, result))