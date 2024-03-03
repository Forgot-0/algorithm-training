DW_NUM = 7
MO_NUM = 12
DY_NUM = 365

dw = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mo = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dmo = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_dmo = [0] * MO_NUM

MAXN = 400

N = 0
days = [0] * MAXN
months = ["" for _ in range(MAXN)]
j1dw = ""

hol = [False] * MAXN
ct = [0] * DW_NUM

N = int(input())
year = int(input())

for i in range(N):
    days[i], months[i] = input().split()
    days[i] = int(days[i])
j1dw = input()

is_leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
if is_leap:
    dmo[1] += 1

for i in range(MO_NUM):
    sum_dmo[i] = 0
for i in range(1, MO_NUM):
    sum_dmo[i] = sum_dmo[i - 1] + dmo[i - 1]

for i in range(N):
    num_of_month = 0
    while num_of_month < MO_NUM:
        if months[i] == mo[num_of_month]:
            break
        num_of_month += 1

    hol[days[i] + sum_dmo[num_of_month]] = True

startdw = 0
while startdw < DW_NUM:
    if dw[startdw] == j1dw:
        break
    startdw += 1

best = 0
best_ct = 0
worst = 0
worst_ct = MAXN
for curd in range(1, DY_NUM + is_leap + 1):
    curdw = (startdw + (curd - 1)) % DW_NUM
    ct[curdw] += not hol[curd]

for i in range(DW_NUM):
    if ct[i] > best_ct:
        best = i
        best_ct = ct[i]

    if ct[i] < worst_ct:
        worst = i
        worst_ct = ct[i]

print(dw[best], dw[worst])
