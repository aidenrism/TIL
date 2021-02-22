# 오미정오늘 오전 2:06
# a = 'bananabana'
# bo = 'bana'
# a = 'cccccca'
# bo = 'ccc'
a = 'asakusa'
bo = 'sa'

# T =int(input())
long = len(a)
short = len(bo)
# print(n%m)
cnt = 0
emp = []

st = -1
en = -1

for i in range(long - short + 1):
    if st< i < en:
        continue
    # cccccc ccc인 경우
    if long%short == 0 and bo == a[i:i+short]:
        cnt = int(long / short)
        break
    else:
        if bo in a[i:i+short]:
            cnt+=1
            st =i
            en = i+short
            continue
        cnt += 1

print(cnt)