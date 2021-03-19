import sys
sys.stdin = open('input.txt')
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # N: 동시에 구울 수 있는 피자의 수
                                     # M: 피자의 수
    Ci = list(map(int, input().split())) # 각 피자에서 치즈의 양

    Oven = Ci[:N] # 초기 화덕에 넣은 피자
    # print(Ci)
    # print(Oven)
    Oven_idx = list(range(1, N+1)) # 초기 화덕에 넣은 피자의 인덱스
    # print(Oven_idx)
    mod = Ci[N:] # 완료되는대로 넣을 피자
    mod_idx = list(range(N+1, M+1)) # 완료되는대로 넣을 피자의 인덱스

    while len(Oven) > 1: # 화덕 안에 피자 수가 1개가 남을 때까지 반복
        circle = Oven.pop(0)//2 # 오픈의 첫번째 피자를 꺼냈을 때 남은 치즈의 양
        circle_idx = Oven_idx.pop(0) # 위 피자에 해당하는 인덱스
        if circle == 0: # 남은 치즈의 양이 0이라면
            if len(mod) > 0: # 이 때 화덕에 넣을 수 있는 피자의 양이 0보다 크다면
                Oven.append(mod.pop(0)) # 하나를 빼서 화덕에 넣고
                Oven_idx.append(mod_idx.pop(0)) # 해당 익덱스도 넣는다.
            else: # 그렇지 않다면, 즉 남은 피자의 양이 없다면 뺀걸로 끝났으니 continue
                continue
        else: # 남은 치즈의 양이 0이 아니라면, 다시 넣자.
            Oven.append(circle)  #  다시 화덕에 넣자
            Oven_idx.append(circle_idx) # 인덱스도 다시 넣자

    print('#{} {}'.format(t, *Oven_idx))