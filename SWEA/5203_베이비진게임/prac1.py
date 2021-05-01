import sys
sys.stdin = open('input.txt')


def check(lst):
    global run, triplet
    for i in range(len(lst)):
        if lst[i] == 3:
            triplet += 1
        if i < len(lst)-2:
            # if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:
            if (lst[i] and lst[i+1] and lst[i+2]) >= 1:

                run += 1
    # print(run, 'run')
    # print(triplet, 'tri')
    if run or triplet:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):

    card = list(map(int, input().split()))
    run = 0
    triplet = 0
    player1 = [0]*10
    player2 = [0]*10
    ans = 0
    for i in range(12):
        if i%2 == 0:
            player1[card[i]] += 1
            if check(player1):
                ans = 1
                break
        else:
            player2[card[i]] += 1
            if check(player2):
                ans = 2
                # print('플레이어2', card[i])
                break
    print(player1)
    print(player2)
    print(ans)
    # arr = [1,1,1,2,3]
    # print(check(arr))


