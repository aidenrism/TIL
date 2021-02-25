# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     customers = list(map(int, input().split()))
#
#     max_time = 0
#     for customer in customers:
#         if customer > max_time:
#             max_time = customer
#
#     bread = -K
#     for i in range(max_time + 1):
#         if not i % M:
#             bread += K
#         if i in customers:
#             bread -= customers.count(i)
#             if bread < 0:
#                 result = 'Impossible'
#                 break
#     else:
#         result = 'Possible'
#
#     print('#{} {}'.format(tc, result))

################################################


# def solution(n, m, k, order):
#     order.sort()
#     for idx in range(n):
#         food = (order[idx] // m) * k
#         sold = idx
#         if food - (sold + 1) < 0:
#             return 'Impossible'
#     return 'Possible'
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n, m, k = map(int, input().split())
#     order = list(map(int, input().split()))
#     print('#{} {}'.format(tc, solution(n, m, k, order)))