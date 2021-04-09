# # KEY > 단계별로 나눠서 생각하기
#
# import sys
# sys.stdin = open('input.txt')
#
#
# # 3. 공통 조상 찾는 함수 생성
# def find_ancestor(a, b):
#
#     # 3-1. a의 모든 조상 기록 anc_a
#     anc_a = []
#     # 3-2. 가까운 공통 조상 기록 common_anc
#     common_anc = []
#
#     # 3-3. 첫 번째 인자의 모든 조상 구하기
#     def find(node):
#         if not baby_tree[node]:
#             return
#         anc_a.append(baby_tree[node])
#         find(baby_tree[node])
#
#     # 3-4. 두 번째 인자의 조상 중 가까운 공통 조상
#     def refind(node):
#         if not baby_tree[node]:
#             return
#         if baby_tree[node] in anc_a:
#             common_anc.append(baby_tree[node])
#             return
#         refind(baby_tree[node])
#
#     find(a)
#     refind(b)
#     return common_anc
#
#
# # 4. 서브트리 구하기
# def subtree(n):
#     des.append(n)
#
#     if not tree[n]:
#         return
#
#     for next in tree[n]:
#         subtree(next)
#
#
# T = int(input())
# for tc in range(1,2):
#     # 1. input 받기
#     v, e, a, b = map(int, input().split())
#     edges = list(map(int, input().split()))
#
#     # 2-1. 부모 인덱스를 기준으로 자식 기록 tree
#     tree = [[] for _ in range(v+1)]
#     # 2-2. 자식 인덱스를 기준으로 부모 기록 tree
#     baby_tree = [0] * (v+1)
#
#     for i in range(e):
#         p, c = edges[2*i], edges[2*i+1]
#         tree[p].append(c)
#         baby_tree[c] = p
#
#     anc = find_ancestor(a, b)[0]
#     des = []
#     subtree(anc)
#     print(tree)
#     print('#{} {} {}'.format(tc, anc, len(des)))

import random

a = random.sample(range(1, 100), 10)
print(a)# 정렬 전 리스트
print('')
for i in range(len(a)-1): # 리스트의 크기-1만큼 반복
    for j in range(i+1, len(a)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
        if a[i] > a[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
            a[i] , a[j]  = a[j], a[i] # swap 해주기
print('')
print(a) # 정렬 후 리스트

#출력
[8, 4, 7, 2, 3]

[2, 3, 4, 7, 8]