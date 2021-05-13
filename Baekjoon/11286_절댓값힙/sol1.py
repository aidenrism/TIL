import heapq
from sys import stdin
# sys.stdin = open('input.txt')


# T = int(input())
# q = []
# for _ in range(T):
#     num = int(input())
#     if num != 0:
#         heapq.heappush(q, (abs(num), num))
#     else:
#         if q:
#             print(heapq.heappop(q)[1])
#         else:
#             print(0)

T = int(stdin.readline().rstrip())
q = []
for _ in range(T):
    num = int(stdin.readline().rstrip())
    if not num:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(num), num))


