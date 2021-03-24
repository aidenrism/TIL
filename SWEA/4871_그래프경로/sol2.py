# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# v, e = map(int, input().split())
#
# emp1 = []
# emp2 = []
#
# for _ in range(e):
#     s, g = map(int, input().split())
#     sg_list = [s,g]
#     # print(sg_list)
#     if s == 1:
#         emp1.append(sg_list)
#     else:
#         emp2.append(s)
#
#     for i in range(len(emp1)):
#         if s in emp1[i]:
#             emp1.append([g])
# #
# print(emp1)
# print(emp2)

test_list = [1]
test_list.append(2)
test_list += [3]
print(test_list)