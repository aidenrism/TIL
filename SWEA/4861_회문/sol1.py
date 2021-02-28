import sys
sys.stdin = open('input.txt')

def my_palindrome(word, num):
    # print(word, num, len(word))
    n = len(word)
    m = num
    for j in range(n-m+1):
        reverse_word = ''
        for k in range(m-1+j, j-1, -1):
            reverse_word += word[k]
        # print(reverse_word, 1)
        if word[j:j+m] == reverse_word:
            # print(1)
            return word[j:j+m]
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    sentences = [input() for _ in range(n)]
    # print(sentences)
    output = ''
    for i in range(n):
        result = my_palindrome(sentences[i], m)
        if result:
            output += result


    for i in range(n):
        col_sentence = ''
        for j in range(n):
            col_sentence += sentences[j][i]
        result2 = my_palindrome(col_sentence, m)
        if result2:
            output += result2
    print('#{} {}'.format(tc, output))

