import sys
sys.stdin = open('input.txt')
#
# def last_idx(x):
#     for i in range(len(x)-1, -1, -1):
#         if x[i] == max(x):
#             return i
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     pizzas = list(map(int, input().split()))
#     pizza_idx = list(range(1, M+1))
#     oven = pizzas[:N]
#     oven_idx = pizza_idx[:N]
#     pizza_pop = 0
#     table = pizzas[N:]
#     table_idx = pizza_idx[N:]
#
#     while len(oven) > 1:
#         # oven (pizzas[:N])
#         # oven_idx.append(pizza_idx[:N])
#         if len(oven) < N:
#             if len(table) > 0:
#                 oven.append(table.pop(0))
#                 oven_idx.append(table_idx.pop(0))
#             else:
#                 i = last_idx(oven)
#                 last_pizza = oven_idx[i]
#                 break
#         elif len(oven) == N:
#             for i in range(N):
#                 oven[i] = oven[i] // 2
#                 if oven[i] == 0:
#                     oven.pop(i)
#                     oven_idx.pop(i)
#                     pizza_pop += 1
#                     break
#         # print(pizzas)
#         # print(oven)
#     print('#{} {}'.format(tc, last_pizza))


# oven = []
# cnt = 0
# for _ in range(N):
#     oven.append(pizzas.pop(0))
# cnt += N
#
# while pizzas:
#
#         print(oven)
#
#             if pizzas:
#                 oven[i] = pizzas.pop(0)
#                 cnt = oven[i]
#                 print(cnt)
#     print(oven, 'end')
# for i in range(N):
#     print(oven, 'new')
#     oven[i] = oven[i] //2
# print(oven, 'new_end')



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    pizza_idx = list(range(1, M + 1))
    oven = pizzas[:N]
    oven_idx = pizza_idx[:N]
    table = pizzas[N:]
    table_idx = pizza_idx[N:]

    while len(oven) > 1:

        if len(oven) < N:
            if len(table) > 0:
                oven.append(table.pop(0))
                oven_idx.append(table_idx.pop(0))
            else:
                if len(table) == 0:
                    for _ in range(len(oven)):
                        if len(oven) == 1:
                            last_pizza = oven_idx[0]
                        oven[0] //= 2
                        if oven[0] == 0:
                            oven.pop(0)
                            oven_idx.pop(0)
                        else:
                            oven.append(oven.pop(0))
                            oven_idx.append(oven_idx.pop(0))
                    if len(oven) == 1:
                        last_pizza = oven_idx[0]
                        break

        elif len(oven) == N:
            for _ in range(N):
                oven[0] //= 2
                if oven[0] == 0:
                    oven.pop(0)
                    oven_idx.pop(0)
                    break
                else:
                    oven.append(oven.pop(0))
                    oven_idx.append(oven_idx.pop(0))

    print('#{} {}'.format(tc, last_pizza))