# N =5
# emp = [[0] * N for _ in range(N)]
# visited = [(4, 3), (3, 3), (4, 2), (2, 3), (4, 1), (1, 3), (3, 1), (0, 3), (2, 1), (1, 1), (0, 1)]
# # for i in range(1):
# #     emp[1,1].append(1)
# # emp[1][1] = 9
# for i in range(1,len(visited)):
#     # print(visited[i][0], visited[i][1])
#     emp[visited[i][0]][visited[i][1]] = 1
# emp[visited[0][0]][visited[0][1]] = 2
# emp[visited[-1][0]][visited[-1][-1]] = 3
#
# for i in emp:
#     print(*i)
#
# cnt = 0
# for i in range(5):
#     for j in range(5):
#         if emp[i][j] == 1:
#             cnt += 1
# print(cnt)
# print(len(visited))
#
# # for dir in range(3):
# #     print(dir)

q = [(1,2)]
p = [[1,2]]
r = [[1,2]]
a,b = q.pop()
print(a)
print(b)
aa, bb = p.pop()
cc = r.pop()

print(aa)
print(bb)
print(cc)

o, i = [5,6]
print(o)
print(i)