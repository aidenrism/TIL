prices = [1,2,7,4,2,6]
n = 6

max_idx = -1
# idx_cnt = 0
items = []
revenue = 0

for i in range(n):
    if prices[i] == max(prices[max_idx+1:n]):
        max_idx = i
        idx_cnt = 0
        for idx in items:
            idx_cnt += idx
        print(idx_cnt, len(items))
        revenue += len(items)*prices[i] - idx_cnt
        items = []
    elif prices[i] != max(prices[max_idx+1:n]):
        items.append(prices[i])
        # print(items)

# print(max_idx)
print(revenue)

