import sys
sys.stdin = open("input.txt")


def solution(string):
    lasers = []
    sticks = []

    for idx in range(len(string)):
        if string[idx] == '(':
            # laser?
            if string[idx+1] == ')':
                lasers.append((idx, idx+1))
            else:
                n = 0
                for j in range(idx, len(string)):
                    n = n + 1 if string[j] == '(' else n - 1
                    if n == 0:
                        sticks.append((idx, j))
                        break

    result = len(sticks)
    for stick in sticks:
        for laser in lasers:
            if stick[0] < laser[0] and stick[1] > laser[1]:
                result += 1

    # print(laser, sticks)
    return result
T = int(input())

for tc in range(1, T+1):
    print("#{} {}".format(tc, solution(input())))