import sys
sys.stdin = open('input.txt')


T = int(input())
V, E, n1, n2 = map(int, input().split())
# print(n1)
tree = [[0 for _ in range(2)] for _ in range(V+1)]
# print(tree)
# print(len(tree))
node = list(map(int, input().split()))
# print(node)
# print(len(node))
# print(tree[node[1]][0])
for i in range(E*2):
    if i%2 == 0:
        if tree[node[i]] == [0, 0]:
            tree[node[i]] = [node[i+1]]
        else:
            tree[node[i]] += [node[i+1]]
print(tree)
#
# print(tree[5])
# if n1 in tree[5]:
    # print(1)
for i in range(len(tree)):
    if n1 in tree[i]:
        anc = i
# print(anc)
anc_node1 = []
while True:
    for i in range(len(tree)):
        if n1 in tree[i]:
            anc_node1 += [i]
            n1 = i
    if n1 == 1:
        break
# print(anc_node1) # [5, 3, 1]

anc_node2 = []
while True:
    for i in range(len(tree)):
        if n2 in tree[i]:
            anc_node2 += [i]
            n2 = i
    if n2 == 1:
        break
# print(anc_node2) # [11, 6, 3, 1]

same_anc = []
if len(anc_node1) >= len(anc_node2):
    for i in anc_node2:
        if i in anc_node1:
            same_anc.append(i)
else:
    for i in anc_node1:
        if i in anc_node2:
            same_anc.append(i)
# print(same_anc)  # [3, 1]
# print(same_anc[0]) # 3
# print(tree[3]) # [5, 6]
cnt_list = []
# for i in range(len(tree)):
#     cnt_list.append(tree[same_anc[0]])
# print(cnt_list)

n = same_anc[0]
print(n)

# for i in tree[9]:
#     cnt_list.append(i)

# print(cnt_list)
# while cnt_list:
#     n = cnt_list.pop()
#
# cnt_list.append(tree[n][0])
cnt = 1
def count(n):
    global cnt
    for i in tree[n]:
        # print(i)
        cnt += 1
        cnt_list.append(i)

    while cnt_list:
        n = cnt_list.pop()
        # print(tree[n])
        if tree[n][0]:
            count(n)
    return cnt

print(count(3))
