# import sys

n, m = map(int, input().split())
g = input()
s = input()
glit =[0]*52
slit =[0]*52

for i in range(n): #glit에 알파벳에 맞게 숫자 카운팅
    if ord("a") <= ord(g[i]) and ord(g[i]) <= ord("z"):
        glit[ord(g[i])-ord('a')] += 1
    else:
        glit[ord(g[i])-ord('A')+26] += 1

for i in range(n):#s중에서 n개만큼만 선택
    if ord("a") <= ord(s[i]) and ord(s[i]) <= ord("z"):
        slit[ord(s[i])-ord('a')] += 1
    else:
        slit[ord(s[i])-ord('A')+26] += 1
cnt = 0
for i in range(m-n+1):
    fail = False
    for j in range(52):
        if glit[j] != slit[j]:
            fail = True
            break
    if fail == False:
        cnt += 1
    if i == m-n:
        break

    pos =0
    if ord('a') <= ord(s[i]) and ord(s[i]) <= ord('z'):
        pos = ord(s[i])-ord('a')
    else:
        pos = ord(s[i])-ord("A")+26
    slit[pos] -= 1

    if ord('a') <= ord(s[i+n]) and ord(s[i+n]) <= ord('z'):
        pos = ord(s[i+n])-ord('a')
    else:
        pos = ord(s[i+n])-ord("A")+26
    slit[pos] += 1

print(cnt, end="")