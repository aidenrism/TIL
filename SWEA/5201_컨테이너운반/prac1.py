import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight = sorted(weight)[::-1]
    truck = sorted(truck)[::-1]
    load = []
    # print(weight)
    for i in range(n):
        # weight[i]
        for j in range(len(truck)):
            if weight[i] <= truck[j]:
                load.append(weight[i])
                # print(truck[j])
                truck.remove(truck[j])
                break
    # print(load)
    # print(truck)
    print(sum(load))