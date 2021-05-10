import sys
from collections import deque
sys.stdin = open('input.txt')


T = int(input())
# a, b = map(int, input().split())
a = 2
b = 8
cnt = 0
dir = [1, -1, 2, -10]
# ans = []
# ans.append(a)
# while True:
#     q = ans.pop(0)
#     cnt += 1
#     for i in range(4):
#         if i != 2:
#             ans.append(q + dir[i])
#         else:
#             ans.append(q * dir[i])
#     if b in ans:
#         print('ok')
#         print(ans)
#         break
# print(cnt)
#######
result = {}
ans = []
idx = 0
result[idx] = 1
ans.append(a)
while True:
    q = ans.pop(0)
    result[idx] += 1
    for i in range(4):
        if i != 2:
            ans.append(q + dir[i])
        else:
            ans.append(q * dir[i])
    idx += 1
    if b in ans:
        print('ok')
        print(ans)
        break
print(cnt)
print(result)

