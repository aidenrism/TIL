import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x == parent[x]:
        return x
    else:
        return parent[find_set(x)]


def combine(go, to):
    parent[find_set(to)] = find_set(go)
T = int(input())
n, m = map(int, input().split())
pair = list(map(int, input().split()))

parent = [0] * (n+1)
for i in range(n):
    parent[i] = i

for i in range(m):
    go = pair[i*2]
    to = pair[i*2+1]
    combine(go, to)


print(parent)

print(len(parent))
sp = set(parent)
print(sp)
print(len(sp)-1)


# print(pair)
#
# graph = {}
# idx = 0
# graph[idx] = 1
#
# for i in range(n):
#     if i in pair:
#         graph[idx] += i
#         idx += 1
#         graph[idx] = 0
#
# print(graph)
