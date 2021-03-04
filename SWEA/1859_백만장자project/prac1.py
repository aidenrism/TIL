prices = [1,2,7,4,2,6]

print(max(prices))

cnt = [0] * len(prices)
print(cnt)

# cnt[max(prices)] += 1
print(cnt)
# print(prices[max(prices)])

n = len(prices)
cnt = 0
items = []
for i in range(n):
    if prices[i] != max(prices[i:n]):
        items.append(prices[i])
    elif prices[i] == max(prices[i:n]):
        idx_cnt = 0
        for idx in items:
            idx_cnt += idx
        print(i*, prices[i]*i)
