import sys
import time
start = time.time()
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))

    idx = h_idx = n-1
    total = 0

    while idx >= 0:
        h_price = prices[h_idx]
        c_price = prices[idx]
        if h_price > c_price:
            total += h_price - c_price
        else:
            h_idx = idx
        idx -= 1

    print('#{} {}'.format(tc, total))
# print(time.time()-start)


#     idx = h_idx = 0
#     total = 0
#     while h_idx < n-1:
#         high_price = prices[h_idx]
#         current_price = prices[idx]
#         if high_price < current_price:
#             total += high_price + current_price
#         else:
#             idx = h_idx
#         h_idx += 1
#
#     print(tc, total)
# print(time.time() - start)

