# if ['c', 'A', 'd', 'a'] == 'cAda':
#     print(1)
# else:
#     print(2)
# ww = list(input())
# print(ww)
# if ['c', 'A', 'd', 'a'] in ww:
#     print(33)

def check():
    global cnt

    for i in range(m-n+1):
        print(''.join(s[i:i+n]))
        if ''.join(s[i:i+n]) in w_list:
            cnt += 1

def perm(idx, length):
    global w_list, word
    if idx == length:
        # print(word)
        w_list.append(''.join(word))
        # w_list.extend(list([','.join(word)]))
        fake_list.append(word)

    else:
        for change in range(idx, length):
            word[change], word[idx] = word[idx], word[change]
            perm(idx+1, length)
            word[idx], word[change] = word[change], word[idx]

n, m = map(int, input().split())
word = list(input())
s = list(input())
arr = [i for i in range(n)]
cnt = 0
w_list = []
fake_list = []
perm(0, n)
check()
print(w_list)
print(fake_list)
print(cnt)
# print(arr)
if ['c', 'd', 'A', 'a'] in w_list:
    print(11)
else:
    print(00)
# for i in w_list:
#     print(i)


