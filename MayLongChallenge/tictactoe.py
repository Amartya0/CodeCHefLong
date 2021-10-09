for _ in range(int(input())):
    a = []
    x = 0
    y = 0
    b = 0
    w = 0
    for _ in range(3):
        t = input().upper()
        if t in ['XXX', 'OOO']:
            w += 1
        x += t.count("X")
        y += t.count("O")
        b += t.count("_")
        a.append(t)
    for i in range(3):
        if f'{a[0][i]}{a[1][i]}{a[2][i]}' in ['XXX', 'OOO']:
            w += 1
    if f'{a[0][0]}{a[1][1]}{a[2][2]}' in ['XXX','OOO']:
        w += 1
    if f'{a[0][2]}{a[1][1]}{a[2][0]}' in ['XXX','OOO']:
        w += 1
    if w > 1 or (x > y + 1 or y > x):
        print("3")
    else:
        if b > 0:            
            if w==1:
                print("1")
            elif w==0:
                print("2")
        else:
            print("1")