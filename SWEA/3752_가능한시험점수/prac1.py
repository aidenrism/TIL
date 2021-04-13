import sys
sys.stdin = open('input.txt')


def findset(idx, score):
    global total

    total.append(score)
    if idx == n:
        return
    findset(idx+1, score)
    findset(idx+1, score+ score_list[idx])


T = int(input())
n = int(input())
score_list = list(map(int, input().split()))
total = []
print(score_list)
findset(0, 0)
print(total)
# 여러개의 조합 중 중복된 값을 제외
print(set(total))
# 중복 제외 조합의 개수
print(len(set(total)))

print([1]+[0]*12)