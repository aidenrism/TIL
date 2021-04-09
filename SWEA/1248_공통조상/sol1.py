import sys
sys.stdin = open('input.txt')


# 5. 서브 트리의 크기를 구하는 함수
def count(n):
    global cnt
    cnt += 1
    # 자식노드의 값이 있다면 재귀를 통해서 서브트리 카운트
    if tree[n][0]:
        for child in tree[n]:
            count(child)

    # 아래 코드는 재귀에러 발생
    # for i in tree[n]:
    #     # 자식노드의 개수만큼 카운팅해준다.
    #     cnt += 1
    #     # cnt_list.append(i)
    # # 카운트 리스트에 자식 노드들을 넣어주고 하나씩 빼면서 그 노드의 자식노드들을 append 한다.
    # while cnt_list:
    #     # n = cnt_list.pop()
    #     # 자식노드에 연결된 노드들이 없다면 종료한다.
    #     if tree[n][0]:
    #         count(n)
    return cnt


T = int(input())
for tc in range(1, 11):
    V, E, n1, n2 = map(int, input().split())
    # 0 두개로 채워주는 트리
    tree = [[0 for _ in range(2)] for _ in range(V+1)]
    node = list(map(int, input().split()))

    # 1. 트리가 비어있으면 부모 자식 정점을 이어주고 있다면 값을 추가해줌
    for i in range(E*2):
        if i%2 == 0:
            if tree[node[i]] == [0, 0]:
                tree[node[i]] = [node[i+1]]
            else:
                tree[node[i]] += [node[i+1]]

    # 2-1. 빈 리스트에 첫번째 정점의 조상들을 넣어준다.
    anc_node1 = []
    while True:
        for i in range(len(tree)):
            if n1 in tree[i]:
                anc_node1 += [i]
                n1 = i
        if n1 == 1:
            break
    # print(anc_node1) # [5, 3, 1]

    # 2-2. 빈 리스트에 두번째 정점의 조상들을 넣어준다.
    anc_node2 = []
    while True:
        for i in range(len(tree)):
            if n2 in tree[i]:
                anc_node2 += [i]
                n2 = i
        if n2 == 1:
            break
    # print(anc_node2) # [11, 6, 3, 1]


    # 3. 두 정점의 공통조상을 찾아준다.
    same_anc = []
    for i in anc_node2:
        if i in anc_node1:
            same_anc.append(i)


    cnt_list = []
    # 처음으로 만나는 공통조상은 가장 앞의 값이다.
    n = same_anc[0]
    cnt = 0
    # 4. 가장 앞에 있는 공통조상의 서브트리의 크기를 구하는 함수를 실행한다.
    total = count(same_anc[0])
    # print(tree)

    # print(count(0))
    # 6. 결과값을 출력한다.
    print(f'#{tc} {same_anc[0]} {total}')
