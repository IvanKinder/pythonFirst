def decode(i):
    if i % 10 == 2:
        print()
    if i == 127:
        print(chr(i))
    else:
        print(f'{i} - {chr(i)}', end=' ')
        decode(i + 1)


decode(32)
