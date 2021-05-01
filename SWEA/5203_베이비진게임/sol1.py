import sys
sys.stdin = open('input.txt')


# 2. 체크하는 함수
def check(lst):
    global runs, triplet
    for i in range(len(lst)):
        # 세게면 트리플렛
        if lst[i] == 3:
            triplet += 1
        # 인덱스가 마지막 두개가 아니라면 run 체크
        if i < len(lst)-2:
            if (lst[i] and lst[i+1] and lst[i+2]) >= 1:
                runs += 1
    # run이나 triplet이 있다면 승리
    if runs or triplet:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    runs = 0
    triplet = 0
    player1 = [0]*10
    player2 = [0]*10
    ans = 0

    # 1. 플레이어1과 2에게 돌아가면서 카드주기
    for i in range(12):
        if i%2 == 0:
            player1[card[i]] += 1
            # 한장 줄 때 마다 체크, 만약 run이나 triplet이 있다면 멈춘다
            if check(player1):
                ans = 1
                break
        else:
            player2[card[i]] += 1
            # 한장 줄 때 마다 체크, 만약 run이나 triplet이 있다면 멈춘다
            if check(player2):
                ans = 2
                break
    # 3. 결과출력
    print(f'#{tc} {ans}')

