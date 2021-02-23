import sys
sys.stdin = open('input.txt')

tc, n = map(int, input().split())

print(tc, n)

graph = [[] for _ in range(n+1)]
load = list(map(int, input().split()))
start = []
end = []
for i in range(len(load)):
    if i%2 == 0:
        start += [load[i]]
    else:
        end += [load[i]]

for i in range(n):
    graph[start[i]].append(end[i])

print(load)
print(start)
print(end)
print(graph)
print(graph[0])

