n = int(input())
spisok = list(map(lambda x : bool(int(x) & 1), input().split()))
i = 0
while i < n:
    if spisok[i]:
        break
    elif i > 0:
        print('x', end='')
    i += 1
if i > 0:
    print('+', end='')
i += 1
while i < n:
    if spisok[i]:
        print('x', end='')
    else:
        break
    i += 1
if i < n:
    print('+', end='')
while i + 1 < n:
    print('x', end='')
    i += 1