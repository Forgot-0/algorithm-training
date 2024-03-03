FirstGame = input()
SecondGame = input()
x = int(input())
sumFirst = int(FirstGame[0]) + int(SecondGame[0])
sumSecond = int(FirstGame[2]) + int(SecondGame[2])
res = 0
i = 0

while True:
    if sumFirst > sumSecond:
        print(i)
        break
    elif x == 1:
        if sumFirst == sumSecond and int(FirstGame[2]) < int(SecondGame[0]) + i:
            print(i)
            break
    elif x == 2:
        if sumFirst == sumSecond and int(FirstGame[0]) > int(SecondGame[2]):
            print(i)
            break
    sumFirst += 1
    i += 1