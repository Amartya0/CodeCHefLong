for _ in range(int(input())):
    N,A,B = map(int,input().split())
    l = input()
    zeroes = l.count('0')
    ones = l.count('1')
    print(zeroes * A + ones * B)