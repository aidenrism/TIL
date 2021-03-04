import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))

    max_idx = -1
    items = []
    revenue = 0

    # for i in range(n):
    #     #     if prices[i] == max(prices[max_idx+1:n]):
    #     #         max_idx = i
    #     #         idx_cnt = 0
    #     #         for idx in items:
    #     #             idx_cnt += idx
    #     #         # print(idx_cnt, len(items))
    #     #         revenue += len(items)*prices[i] - idx_cnt
    #     #         items = []
    #     #     elif prices[i] != max(prices[max_idx+1:n]):
    #     #         items.append(prices[i])
    #     #         # print(items)
    #     #
    #     # # print(max_idx)
    #     # print(revenue)
    for i in range(n-1, -1, -1):
        if prices[i] == max(prices):
           max_list = (i, prices[i])
    # print(tc, max(prices))
    print(tc, max_list)
