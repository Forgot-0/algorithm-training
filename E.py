n, k, d = map(int, input().split())

for _ in range(1):
    n *= 10
    if k - n%k < 10:
        n = n + k - n%k
    elif n%k == 0:
        n = n
    else:
        print(-1)
        break

else:
    print(f"{n}" + '0'*(d-1))