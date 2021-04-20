import sys
sys.stdin = open('input.txt')



def minimun_cost(idx, total):
    global result
    if total > result:
        return
    if idx == n:
        result = total
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            minimun_cost(idx+1, total+cost[idx][i])
            visited[i] = 0

T = int(input())
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
print(cost)
visited = [0 for _ in range(n)]
result = 9999
minimun_cost(0, 0)
print(visited)
print(result)