N, M = 3, 5
pizzas = [7, 2, 6, 5, 3]

oven = []
cnt = 0
for _ in range(N):
    oven.append(pizzas.pop(0))
cnt += N
# print(oven)
# print(pizzas)

while pizzas:
    for i in range(N):
        print(oven)
        oven[i] = oven[i]//2

        if oven[i] == 0:
            if pizzas:
                oven[i] = pizzas.pop(0)
                cnt = oven[i]
                print(cnt)
    print(oven, 'end')
for i in range(N):
    print(oven, 'new')
    oven[i] = oven[i] //2
print(oven, 'new_end')

# print(cnt)