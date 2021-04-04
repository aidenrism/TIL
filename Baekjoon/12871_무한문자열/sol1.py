# s = 'ab'
# t = 'abab'
import sys
sys.stdin = open('input.txt')

# 길이가 짧은 문자열 확인
T = 2
for tc in range(T):
    s = input()
    t = input()
    words_len = len(s) * len(t)
    ls = int(words_len / len(s))
    if s * len(t) == t * len(s):
        print(1)
    else:
        print(0)


