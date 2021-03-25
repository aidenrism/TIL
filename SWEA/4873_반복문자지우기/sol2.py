words = ['C','A','A','A','B','A']

i = 1

while len(words) > 1:
    current = words.pop(-i)
    if words[-i] == current:
        words.pop(-i)
        if i > 1:
            i += 1
        # else:
        #     print(2)
    else:
        if i == 1:
            words.insert(len(words), current)
        else:
            words.insert(-i+1,current)
        i -= 1
print(words)