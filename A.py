p, v = map(int, input().split())
q, m = map(int, input().split())
print(2 * (v + m + 1) - max(0, min(p+v, q+m) - max(p - v, q - m) + 1))