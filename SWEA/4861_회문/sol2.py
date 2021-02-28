
word = 'GOFFAKWFSM'

n = len(word)
m = 7
for j in range(n - m + 1):
    reverse_word = ''
    for k in range(m - 1 + j, j - 1,-1):
        reverse_word += word[k]
    print(reverse_word, 1)
    if word[j:j + m] == reverse_word:
        print(word[j:j + m])