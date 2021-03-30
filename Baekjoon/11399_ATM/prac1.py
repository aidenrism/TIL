import sys
sys.stdin = open('input.txt')

N = int(input())
atm = list(map(int,input().split()))
print(atm)

for i in range(N-1):
    for j in range(N-1):
        if atm[j+1] > atm[j]:
            atm[j+1], atm[j] = atm[j], atm[j+1]
print(atm)

for i in range(N-1):
    for j in range(N-1):
        if atm[j+1] < atm[j]:
            atm[j+1], atm[j] = atm[j], atm[j+1]
print(atm)
print(sum(atm))

total = 0
for i in range(N):
    for j in range(i+1):
        total += atm[j]
print(total)