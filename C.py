sum_s = 0
for _ in range(int(input())):
    a = int(input())
    if a%4 == 3:
        sum_s += 2
    else:
        sum_s += a%4
    sum_s += a//4

print(sum_s)