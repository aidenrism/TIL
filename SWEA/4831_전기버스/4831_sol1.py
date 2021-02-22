import sys

sys.stdin = open('sample_input.txt')

T = int(input())
# K, N, M = input()
# print(K, N, M)
for tc in range(1, T + 1):
    elec_bus = list(map(int, input().split()))
    K, N, M = [i for i in elec_bus]
    #
    bus_stops = list(map(int, input().split()))
    #
    togo = N
    count = 0
    start = 0  # 계속 초기화 해줘야 해서 하위로 가야함
    # k가 남은거리보다 작을 때까지
    while K < togo:
        # 출발지점
        # start = 0 -t
        # k보다 작은 빈리스트
        low_than_k = []
        # 만약 K만큼 가기전에 충전소가 없다면 0
        for stops in bus_stops:
            # k 보다 작은 값들
            if 0 < stops - start <= K:
                low_than_k += [stops]
                continue
            else:
                pass
        # 만약 low than k가 있다면 진행
        if low_than_k:
            highest = low_than_k[0]
            for stop in low_than_k:
                if stop > highest:
                    highest = stop
                    continue
            # 남은거리 togo에서 k가 갈 수 있는 범위중 높음값을 출발점에서 빼줌
            togo -= highest - start
            # 간거리 +1
            count += 1
            # 출발점은 마지막 갔던 정류소부터
            start = highest
            continue
        # low than k 가 없다면 0을 반환
        else:
            # 기존 센거만큼 다시 빼줌
            count -= count
            break
    print('#{} {}'.format(tc, count))
