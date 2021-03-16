import sys
sys.stdin = open('input.txt')


def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 ==0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


def check(imp):
    # print(len(wei))
    answer = 0

    for i in range(len(imp)):
        weight = 0
        point = False
        # print(wei[i])
        for j in range(len(imp[i])):

            weight += imp[i][j]
            weight -= 4
            # print(weight)
            if weight < 0:
                point = False
                break
            else:
                point = True
        if point:
            answer += 1
    return answer


n, k = map(int, input().split())

imp = list(map(int, input().split()))

wei = []
for i in range(1, n+1):
    if not wei:
        wei.append(500 - k + imp[i-1])
    else:
        wei.append(wei[-1] + 500 - k + imp[i - 1])
# print(wei)
print(check(permute(imp)))
# print(permute(imp))


