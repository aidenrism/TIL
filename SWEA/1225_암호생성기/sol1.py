import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    passwords = list(map(int, input().split()))

    new_words = passwords[0]
    while new_words > 0:
        for num in range(1,6):
            words = passwords.pop(0)
            new_words = words - num
            if new_words <= 0:
                new_words = 0
                passwords.append(new_words)
                break
            passwords.append(new_words)

    print('#{}'.format(T) , end = ' ')
    print(*passwords)