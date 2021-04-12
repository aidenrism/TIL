import sys
sys.stdin = open('input.txt')


def find_max(idx, score, k):
    global max_score

    # 제한 칼로리를 넘어서면 멈춘다
    if k > L:
        return
    # 점수가 기존값보다 커지면 최대점수로 바꾼다
    if score >= max_score:
        max_score = score

    # 정해놓은 재료만큼 오면 멈춤다
    if idx == N:
        return

    # 해당재료를 포함시키지 않을 때
    find_max(idx+1, score, k)
    # 해당재료를 포함시켜줄 때
    find_max(idx+1, score + burger[idx][0], k+burger[idx][1])


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    burger = []
    for _ in range(N):
        t, k = map(int, input().split())
        burger.append([t, k])
    # print(burger)
    max_score = 0
    find_max(0, 0, 0)
    print(f'#{tc} {max_score}')