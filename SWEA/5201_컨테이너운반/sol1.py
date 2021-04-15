import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 1. 크기순으로 화물무게와 트럭 적재용량을 세운다 (내림차순)
    weight = sorted(weight)[::-1]
    truck = sorted(truck)[::-1]
    # 2. 실리는 화물 리스트
    load = []

    for i in range(n):

        for j in range(len(truck)):
            # 운반 가능한 무게면 append
            if weight[i] <= truck[j]:
                load.append(weight[i])
                # 운반후에 그 트럭은 remove
                truck.remove(truck[j])
                break
    # 3. 결과 값 출력
    print(f'#{tc} {sum(load)}')
