s = 'ab'
t = 'abab'


# 길이가 짧은 문자열 확인

if len(s) <= len(t):
    x = int(len(t)/len(s))
    word = s * x
print(x)
print(word)
if word == t:
    print(1)
else:
    print(0)
